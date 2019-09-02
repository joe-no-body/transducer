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
            'x': 2,
            'y': 4,
            'z': {
                'op': 'add',
                'vars': ['x', 'y']
            }
        }
        expected_result = {
            'x': 2,
            'y': 4,
            'z': 6,
        }
        self.assertEqual(expected_result, transducer.run(program))
