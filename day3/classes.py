
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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount  

    @staticmethod
    def less_than(a,b):
        if a < b:
            return True
        return False
    print('hi')


#print(Employee.num_of_emps)
emp1 = Employee('a','b',10)
emp2 = Employee('c','d',20)

print(emp1.num_of_emps)
print(emp2.less_than(2,4))
