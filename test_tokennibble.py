# test_tokennibble.py
"""
Tests for TokenNibble module.
"""

import unittest
from tokennibble import TokenNibble

class TestTokenNibble(unittest.TestCase):
    """Test cases for TokenNibble class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = TokenNibble()
        self.assertIsInstance(instance, TokenNibble)

    def test_run_method(self):
        """Test the run method."""
        instance = TokenNibble()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
