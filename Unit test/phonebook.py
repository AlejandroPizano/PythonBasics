class PhoneBook:
    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for name, number in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name == name2:
                    continue
                if number.startswith(number2):
                    return False
        return True
#solo por agregar