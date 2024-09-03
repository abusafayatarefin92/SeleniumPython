class Employees:

    def __init__(self,
                 first_name,
                 last_name,
                 email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address

    def greet_person(self):
        print('Hello! welcome to our house ' + self.first_name + ' ' + self.last_name)

employee1 = Employees('Robiul',
                      'Islam',
                      'robiul@mail.com')
employee2 = Employees('Karim',
                      'Khan',
                      'karim@mail.com')

print(employee1.first_name)
print(employee2.first_name)

employee1.greet_person()
employee2.greet_person()