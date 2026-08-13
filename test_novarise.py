# test_novarise.py
"""
Tests for NovaRise module.
"""

import unittest
from novarise import NovaRise

class TestNovaRise(unittest.TestCase):
    """Test cases for NovaRise class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NovaRise()
        self.assertIsInstance(instance, NovaRise)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NovaRise()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
