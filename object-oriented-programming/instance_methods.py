class Payslips:
    def __init__(self, name, payment, amount) -> None:
        self.name = name
        self.payment = payment
        self.amount = amount

    def pay(self):
        self.payment = "Yes"

    def status(self):
        if self.payment == "Yes":
            return self.name + " is paid " + str(self.amount)
        else:
            return self.name + " is not paid yet"

nathan = Payslips("Nathan", "No", 1000)
roger = Payslips("Roger", "No", 3000)

print(nathan.status(), "\n" ,roger.status())
# Nathan is not paid yet 
#  Roger is not paid yet

nathan.pay()
print("After payment:")
print(nathan.status(), "\n" ,roger.status())
# After payment:
# Nathan is paid 1000 
#  Roger is not paid yet
