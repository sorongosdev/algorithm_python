import unittest
from io import StringIO
import sys
import runpy

class TestSolution(unittest.TestCase):
    def setUp(self):
        # 여러 테스트 케이스를 리스트로 정의
        self.test_cases = [
            {
                "input": """4 6
101111
101010
101011
111011""",
                "expected": """15"""
            },
            {
                "input": """4 6
110110
110110
111111
111101""",
                "expected": """9"""
            },
            {
                "input": """2 25
1011101110111011101110111
1110111011101110111011101""",
                "expected": """38"""
            },
            {
                "input": """7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111""",
                "expected": """13"""
            },
        ]

    def run_test_case(self, input_data, expected_output):
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            runpy.run_path('maze_bj_2178.py')
            
            output = sys.stdout.getvalue().strip()
            self.assertEqual(output, expected_output)
            
        finally:
            sys.stdin = original_stdin
            sys.stdout = original_stdout

    def test_all_cases(self):
        for test_case in self.test_cases:
            with self.subTest(input=test_case["input"]):  # subTest를 사용하면 하나가 실패해도 다른 테스트 계속 실행
                self.run_test_case(test_case["input"], test_case["expected"])

if __name__ == '__main__':
    unittest.main()