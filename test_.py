import unittest
from io import StringIO
import sys
import runpy

class TestSolution(unittest.TestCase):
    def setUp(self):
        # 여러 테스트 케이스를 리스트로 정의
        self.test_cases = [
            {
                "input": """100 2
90 1
70 2""",
                "expected": """170"""
            },
        ]

    def run_test_case(self, input_data, expected_output):
        original_stdin = sys.stdin
        original_stdout = sys.stdout
        
        try:
            sys.stdin = StringIO(input_data)
            sys.stdout = StringIO()
            
            runpy.run_path('safe_sft_lv2.py')
            
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