import json
import unittest

import transducer


class TestTransducer(unittest.TestCase):
    def test_transducer_add(self):
        program = {
            "a": 2,
            "b": 3,
            "c": {
                "op": "add",
                "vars": ["a", "b"]
            }
        }
        expected_result = {
            'a': 2,
            'b': 3,
            'c': 5,
        }
        self.assertEqual(expected_result, transducer.run(program))

    def test_transducer_add6(self):
        program = {
            'a': 2,
            'b': 4,
            'c': {
                'op': 'add',
                'vars': ['a', 'b']
            }
        }
        expected_result = {
            'a': 2,
            'b': 4,
            'c': 6,
        }
        self.assertEqual(expected_result, transducer.run(program))
