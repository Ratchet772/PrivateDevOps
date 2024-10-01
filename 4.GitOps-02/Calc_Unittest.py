import unittest
from Calc import Calc

class UnitTest(unittest.TestCase):
  def setUp(self):
    self.calc = Calc()
  def test_divide(self):
    self.assertEqual(self.calc.divide(100,4), 5)
  def test_multiply(self):
    self.assertEqual(self.calc.multiply(100,4), 400)
  def test_sum(self):
    self.assertEqual(self.calc.sum(100,4), 104)
  def test_subtract(self):
    self.assertEqual(self.calc.subtract(100,4), 96)

if __name__ == "__main__":
  unittest.main()
