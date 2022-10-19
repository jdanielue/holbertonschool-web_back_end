#!/usr/bin/env python3
""" Lorem ipsum dolor sit amets """

from parameterized import parameterized
import unittest
from unittest.mock import patch
from utils import (access_nested_map, get_json, memoize)
import requests


class TestAccessNestedMap(unittest.TestCase):
    """ Class for Lorem ipsum dolor sit amet"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test that the method returns what it is supposed to """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    