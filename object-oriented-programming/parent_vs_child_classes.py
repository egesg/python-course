# Interihence

class Employees:
    def __init__(self, name, lastname) -> None:
        self.name = name
        self.lastname = lastname

class Supervisors(Employees):
    def __init__(self, name, lastname, password) -> None:
        super().__init__(name, lastname)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days"

adrian = Supervisors("Adrian", "A", "123456")
emily = Chefs("Emily", "E")
juno = Chefs("Juno", "J")

print(emily.leave_request(3))
# May I take a leave for 3 days
print(adrian.password)
# 123456
print(emily.name)
# Emily