import sys
input = sys.stdin.readline

# n: DNA 문자열의 개수, m: 각 DNA 문자열의 길이
n,m = map(int, input().split())
dna = [input().strip() for _ in range(n)]

# 2^n 크기의 배열로, 각 비트마스크 상태에서의 병합된 DNA 저장
superDNA = [None] * (2**n)
# 초기 상태(아무것도 선택 안 됨)는 모두 '.'으로 초기화
superDNA[0] = ['.'] * m

def merge(dna1, dna2):
   # 두 DNA 문자열을 병합하는 함수
   # 빈 리스트면 병합 불가능하므로 빈 리스트 반환
   if not dna1 or not dna2:
       return []
   
   dna = []
   for i in range(m):
       if dna1[i] == '.':  # dna1이 와일드카드면 dna2 문자 사용
           dna.append(dna2[i])
       elif dna2[i] == '.':  # dna2가 와일드카드면 dna1 문자 사용
           dna.append(dna1[i])
       elif dna1[i] == dna2[i]:  # 두 문자가 같으면 그 문자 사용
           dna.append(dna1[i])
       else:  # 다른 문자면 병합 불가능
           return []
   return dna

def gen_super_dna(index):
   # 현재 비트마스크에서 가장 낮은 위치의 1비트 찾기
   # 여기서 - 연산자는 2의 보수 (not 연산 이후 1을 더한 것)
   loc = index & -index
   # 그 비트의 위치(0부터 시작)를 계산
   pos = (loc).bit_length() - 1
   # 현재 index의 superDNA를 계산해서 저장
   # dna[pos]: 현재 추가할 DNA
   # superDNA[index-loc]: 이전까지 병합된 결과
   superDNA[index] = merge(dna[pos], superDNA[index-loc])

# 모든 가능한 비트마스크에 대해 superDNA 생성
for i in range(1, 2**n):
   gen_super_dna(i)

def gen_answer(index):
   # 이미 계산된 상태면 그 값을 반환
   if answer[index] < n+1:
       return answer[index]
   
   # 현재 비트마스크의 모든 부분집합을 순회하며 최소값 찾기
   subset = index
   min_answer = n+1
   
   while subset:
       # 현재 부분집합의 여집합 계산
       complement = index & ~subset
       # 부분집합과 여집합의 답을 더한 값
       temp = answer[subset] + answer[complement]
       # 최소값 갱신
       min_answer = min(min_answer, temp)
       # 다음 부분집합 계산
       subset = (subset-1) & index
   
   # 찾은 최소값을 저장하고 반환
   answer[index] = min_answer
   return min_answer

# DP 배열 초기화: 모든 상태를 불가능한 값(n+1)로 설정
answer = [n+1]*(2**n)
# 빈 집합은 0개의 그룹 필요
answer[0] = 0

# 모든 비트마스크에 대해
# superDNA가 존재하면 1개 그룹으로 가능
# 아니면 부분문제로 나눠서 해결
for i in range(1,2**n):
   answer[i] = 1 if superDNA[i] else gen_answer(i)

# 모든 DNA를 포함하는 경우(2^n-1)의 최소 그룹 수 출력
print(answer[2**n-1])