def calculate_profit(income):
    profit = income - 124000
 
    if profit <= 0:
        return 0
 
    elif profit <= 560000:
        return profit * 0.05
 
    elif profit <= 1260000:
        return (profit - 560000) * 0.12 + 28000
 
    elif profit <= 2520000:
        return (profit - 1260000) * 0.2 + 90400
 
    elif profit <= 4720000:
        return (profit - 2520000) * 0.3 + 222400
 
    else:
        return (profit - 4720000) * 0.4 + 716400
 
def test_profit_zero():
    assert calculate_profit(100000) == 0
 
def test_profit_5_percent():
    assert calculate_profit(300000) == 8800
 
def test_profit_12_percent():
    assert calculate_profit(700000) == 29920
 
def test_profit_negative():
    assert calculate_profit(50000) == 0
 
def test_profit_edge_case():
    assert calculate_profit(124000) == 0





