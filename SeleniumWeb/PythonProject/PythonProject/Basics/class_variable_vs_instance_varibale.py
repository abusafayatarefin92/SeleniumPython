class RateOfInterest:

    interest = 0.2
    def __init__(self,
                 name,
                 loan):
        self.name = name
        self.loan = loan

    def calculate_interest(self):
        print('Total interest: ', self.loan * self.interest)

person1 = RateOfInterest('Rabiul', 60000)
person1.calculate_interest()

person2 = RateOfInterest('Karim', 80000)
person1.calculate_interest()
