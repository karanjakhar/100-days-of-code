class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay  = pay
        self.email = first + '.' + last + '@company.com'

        self.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self):
        return 'hey'

    def __str__(self):
        return 'hi'

    def __add__(self,other):
        return self.pay + other.pay


emp1 = Employee('a','b',20)
emp2 = Employee('c','d',40)
print(emp1)
print(emp2)
print(emp1 + emp2)

    

        
