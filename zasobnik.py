class Zasobnik:   #IntegerStack TO DO Node
    def __init__(self,size): #може бути безкінечною, але можна додати і розмір
        self.size = size
        self.zasobnik = []

    def is_empty(self):
        return len(self.zasobnik) == 0

    def is_full(self):
        return len(self.zasobnik) == self.size


    def push (self, item):  # дозволяє додати yf horu останнього до zasobnik
        if len(self.zasobnik)< self.size:
            self.zasobnik.append(item)
            return True
        return False
    def peek(self):
        if not self.is_empty():
            return self.zasobnik[-1]
        return None

    def is_empty(self):
        return len(self.zasobnik) == 0

    def is_full(self):
        return len(self.zasobnik) == self.size

    def clear(self):
        self.zasobnik.clear()

    def count(self):
        return len(self.zasobnik)