import unittest
from checkout import CheckOut
from rules import RULES

class TestPrice < Test::Unit::TestCase

  def price(goods):
    co = CheckOut.new(RULES)
    for item in goods.split(//):
        co.scan(item)
    return co.total()

  def test_totals
    self.assertEqual(  0, price(""))
    self.assertEqual( 50, price("A"))
    self.assertEqual( 80, price("AB"))
    self.assertEqual(115, price("CDBA"))

    self.assertEqual(100, price("AA"))
    self.assertEqual(130, price("AAA"))
    self.assertEqual(180, price("AAAA"))
    self.assertEqual(230, price("AAAAA"))
    self.assertEqual(260, price("AAAAAA"))

    self.assertEqual(160, price("AAAB"))
    self.assertEqual(175, price("AAABB"))
    self.assertEqual(190, price("AAABBD"))
    self.assertEqual(190, price("DABABA"))

  def test_incremental
    co = CheckOut.new(RULES)
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
