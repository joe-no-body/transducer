import json
import unittest

import transducer


class TestTransducer(unittest.TestCase):
    def setUp(self) -> None:
        with open('fixtures/case1_input.json') as f:
            self.case1_input = json.load(f)
        with open('fixtures/case1_output.json') as f:
            self.case1_output = json.load(f)

    def test_transducer(self):
        self.assertEqual(transducer.run(self.case1_input), self.case1_output)
