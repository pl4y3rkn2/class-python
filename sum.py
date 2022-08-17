class Sumatoria(num1, num2, num3):
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3

    def total(self):
        #print(self.num1 + self.num2 + self.num3)
        return self.num1 + self.num2 + self.num3

if __name__ == '__main__':
    print(Sumatoria(num1 = 50000, num2 = 46000, num3 = 34566))
