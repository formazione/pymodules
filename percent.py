class Percent:
    def __init__(self, operation="500*22%"):
        self.operation = operation
        if "%" == self.operation[-1] and "*" in self.operation:
            getnum = self.operation[:-1]
            ops = getnum.split("*")
            base = int(ops[0])
            percentage = int(ops[1])
            self.result = base * percentage / 100
            self.description = "The {}% of {} is {}".format(*ops, self.result)
        else:
            print("The argument must be a string like '500*22%'")


x = Percent("1200*30%")
print(x.result)
print(x.description)
