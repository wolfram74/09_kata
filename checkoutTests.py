import unittest
from checkout import CheckOut
from rules import RULES

class TestPrice(unittest.TestCase):

  def price(self, goods):
    co = CheckOut(RULES)
    for item in list(goods):
        co.scan(item)
    return co.total()

  def test_totals(self):
    self.assertEqual(  0, self.price(""))
    self.assertEqual( 50, self.price("A")) #unit price of A is 50
    self.assertEqual( 80, self.price("AB")) #unit price of B is 30
    self.assertEqual(115, self.price("CDBA")) #c+d is 35

    self.assertEqual(100, self.price("AA"))
    self.assertEqual(130, self.price("AAA")) #triple price of a is 130
    self.assertEqual(180, self.price("AAAA"))
    self.assertEqual(230, self.price("AAAAA"))
    self.assertEqual(260, self.price("AAAAAA"))

    self.assertEqual(160, self.price("AAAB"))
    self.assertEqual(175, self.price("AAABB")) # double price b is 45
    self.assertEqual(190, self.price("AAABBD")) # unit price of d is 15, therfore, c is 20
    self.assertEqual(190, self.price("DABABA"))

  def test_incremental(self):
    co = CheckOut(RULES)
    self.assertEqual(  0, co.total())
    co.scan("A")
    self.assertEqual( 50, co.total())
    co.scan("B")
    self.assertEqual( 80, co.total())
    co.scan("A")
    self.assertEqual(130, co.total())
    co.scan("A")
    self.assertEqual(160, co.total())
    co.scan("B")
    self.assertEqual(175, co.total())
