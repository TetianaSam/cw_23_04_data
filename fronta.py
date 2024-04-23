class Fronta:
    def __init__(self,size): #може бути безкінечною, але можна додати і розмір
        self.size = size
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def is_full(self):
        return len(self.queue) == self.size


    def enqueue(self, item):  # дозволяє додати останнього до черги
        if not self.is_full():
            self.queue.append(item)
            return True
        return False

    def dequeue(self):            #дозволяє видалити першого в черзі
        if not self.is_empty():
            item = self.queue.pop(0)
            return item
        return None

    def show(self):
        if not self.is_empty():
            for i in self.queue:
                print(i, end=" ")
            print()
        else:
            print("Queue is empty.")




