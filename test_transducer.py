import json
import unittest


class TestTransducer(unittest.TestCase):
    def setUp(self) -> None:
        with open('fixtures/case1_input.json') as f:
            self.case1_input = json.load(f)
        with open('fixtures/case1_output.json') as f:
            self.case1_output = json.load(f)

    def test_useless(self):
        pass
