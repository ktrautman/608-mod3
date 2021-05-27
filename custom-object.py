# custom-object.py
"""Custom Object: Calculatetax and calculatetip"""

# Initilization
class Purchase(object):
    def __init__(self, subtotal):
        self.subtotal = subtotal
        
    def calculatetax(self, taxpercent):
        return self.subtotal * taxpercent/100.0
    
    def calculatetip(self, tippercent):
        return self.subtotal * tippercent/100.0
    
    def calculatetotal(self, taxpercent, tippercent):
        return self.subtotal * (1 + taxpercent/100.0 + tippercent/100.0)
    
# Processing
purchase = Purchase(100.0) 
taxpercent = 7.5
tippercent = 20.0

tax = purchase.calculatetax(taxpercent)
tip = purchase.calculatetip(tippercent)

# Termination / Display
print('Subtotal: $ 100.00')
print('Tax: ',tax,'%')
print('Tip: ',tip,'%')
print('Total: $', purchase.calculatetotal(taxpercent, tippercent))