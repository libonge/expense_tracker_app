class Expense:
    def __init__(self, name, category, amount)  -> None :
        self.name = name 
        self.category = category
        self.amount = float(amount)

    def __repr__(self): 
        return f"<Expense: {self.name}, {self.category}, R{self.amount:.2f}>"