class Person:
    def __init__(self, name: str, phone: int, email: str, country: str ):
        self.name = name
        self.phone = phone
        self.email = email
        self.country = country
    def contact_info(self):
        print(f'''
Email: {self.email}.'
Phone number: {self.phone}.''')
    def personal_info(self):
        print(f''''
Name: {self.name}
Country: {self.country}''')

class Worker(Person):
    def __init__(self,name: str, phone: int, email: str, country: str, hourly_rate: float, amount_worked: int ):
        super().__init__(name, phone, email, country)
        self.hourly_rate = hourly_rate
        self.amount_worked = amount_worked
    def check_rate(self):
        print(f'Current hourly rate of {super().self.name} is {self.hourly_rate}')
    def check_amount_worked(self):
        print(f'Current  {super().self.name} worked {self.amount_worked} hours.')
    def total_salary(self, total):
        total = self.hourly_rate * self.amount_worked
        print(f'Current salary is: {total}')

