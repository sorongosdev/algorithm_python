import sys
input = sys.stdin.readline

n,m = map(int, input().split())
dna = [input().strip() for _ in range(n)]

superDNA = [None] * (2**n)
superDNA[0] = ['.'] * m

def merge(dna1, dna2):
    if not dna1 or not dna2:  # 빈 리스트 체크 최적화
        return []
    dna = []
    for i in range(m):
        if dna1[i] == '.':
            dna.append(dna2[i])
        elif dna2[i] == '.':
            dna.append(dna1[i])
        elif dna1[i] == dna2[i]:
            dna.append(dna1[i])
        else:
            return []
    return dna

def gen_super_dna(index):
    loc = index & -index  # 최하위 1비트를 찾는 비트 연산
    pos = (loc).bit_length() - 1
    superDNA[index] = merge(dna[pos], superDNA[index-loc])

for i in range(1, 2**n):
    gen_super_dna(i)

def gen_answer(index):
    if answer[index] < n+1:
        return answer[index]
    
    # 비트 연산으로 최적화
    subset = index
    min_answer = n+1
    
    # 부분집합 생성 최적화
    while subset:
        # subset과 그 complement를 계산
        complement = index & ~subset
        temp = answer[subset] + answer[complement]
        min_answer = min(min_answer, temp)
        subset = (subset-1) & index
    
    answer[index] = min_answer
    return min_answer

answer = [n+1]*(2**n)
answer[0] = 0

for i in range(1,2**n):
    answer[i] = 1 if superDNA[i] else gen_answer(i)

print(answer[2**n-1])