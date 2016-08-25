'''
based on spec a CheckOut object
takes Rule objects on creation
scans goods one at at ime
has a method for evaluatiing total.
since rule objects can specify group pricing as well, maybe we keep two hashes
one for mapping SKU's to pricing rules and one for mapping SKU's to tally so far.
if we kept a latest scanned we could have a #update_total() function that increments total appropriately, minimizing work that #total() does
fuck it, SKU is obtuse, just call it item_id
'''

class CheckOut():
    def __init__(self, rules =[]):
        self.rules = {}
        self.scan_totals = {}
        self.last_scan = None
        self.total = 0
        for rule in rules:
            self.rules[rule.item_id] = rule
            self.scan_totals[rule.item_id] = 0

    def scan(self, item_id):
        self.last_scan = item_id
        self.scan_totals[item_id]+=1
        self._update_total()
        return True

    def total(self):
        return self.total

    def _update_total(self):
        return True
