'''
given spec, we infer we'll need 4 products and 6 pricing rules
A = 50
3A = 130
B = 30
2B = 45
C = 20
D = 15

Rule object should have
SKU for identifying object
scratch that, item_id is actually descriptive
price for specifying what a unit price is
group_size for how big a group is
group_price for how much a group is
'''
class Rule():
    def __init__(self, item_id, price, group_size=None, group_price=None):
        self.item_id=item_id
        self.price=price
        if group_size == 1:
            group_size = None
        self.group_size=group_size
        self.group_price=group_price

RULES =[
    Rule('A', 50, group_size=3, group_price=130),
    Rule('B', 30, group_size=2, group_price=45),
    Rule('C', 20),
    Rule('D', 15)
]
