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

    def test_transducer_multiple_ops(self):
        program = {
            'a': 2,
            'b': 3,
            'c': {
                'op': 'add',
                'vars': ['a', 'b']
            },
            'd': 5,
            'e': {
                'op': 'add',
                'vars': ['c', 'd']
            }
        }
        expected_result = {
            'a': 2,
            'b': 3,
            'c': 5,
            'd': 5,
            'e': 10,
        }
        self.assertEqual(expected_result, transducer.run(program))

    def test_transducer_sub(self):
        program = {
            'a': 10,
            'b': 2,
            'c': {
                'op': 'sub',
                'vars': ['a', 'b']
            },
            'd': {
                'op': 'sub',
                'vars': ['b', 'a']
            }
        }
        expected_result = {
            'a': 10,
            'b': 2,
            'c': 8,
            'd': -8,
        }
        self.assertEqual(expected_result, transducer.run(program))
