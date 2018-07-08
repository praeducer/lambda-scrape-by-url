from unittest import TestCase
from lambda_function import lambda_handler

class TestLambdaFunction(TestCase):
    def test_has_correct_return_type(self):
        result = lambda_handler({ "url": "https://blog.paulprae.com/my-statement-of-purpose/" }, None)
        self.assertTrue(isinstance(result['content'], str))

    def test_result_is_none(self):
        result = lambda_handler({}, None)
        self.assertIsNone(result['content'])
        result = lambda_handler({ "url": None }, None)
        self.assertIsNone(result['content'])
        result = lambda_handler({ "url": "" }, None)
        self.assertIsNone(result['content'])
        result = lambda_handler({ "url": "www" }, None)
        self.assertIsNone(result['content'])
        result = lambda_handler({ "url": 0 }, None)
        self.assertIsNone(result['content'])
        result = lambda_handler({ "url": 1 }, None)
        self.assertIsNone(result['content'])
