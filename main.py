from fronta import Fronta


from zasobnik import Zasobnik


def main():
    queue_size = int(input("Enter the size of the queue: "))
    char_queue = Fronta(queue_size)

    while True:
        print("\nMenu:")
        print("1. Check if the queue is empty")
        print("2. Check if the queue is full")
        print("3. Add an element to the queue (Enqueue)")
        print("4. Delete an element from the queue (Dequeue)")
        print("5. Display all queue elements")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("Queue is empty." if char_queue.is_empty() else "Queue is not empty.")

        elif choice == '2':
            print("Queue is full." if char_queue.is_full() else "Queue is not full.")

        elif choice == '3':
            if char_queue.is_full():
                print("Queue is full. Cannot add new element.")
            else:
                element = input("Enter the character to enqueue: ")
                char_queue.enqueue(element)
                print("Element enqueued.")

        elif choice == '4':
            item = char_queue.dequeue()
            if item is not None:
                print(f"Dequeued element: {item}")
            else:
                print("Queue is empty. Cannot dequeue.")

        elif choice == '5':
            char_queue.show()

        elif choice == '6':
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
def main_stack():
    stack_size = int(input("Enter the size of the stack: "))
    stack = Fronta(stack_size)

    while True:
        print("\nMenu:")
        print("1. Push an integer onto the stack")
        print("2. Pop an integer from the stack")
        print("3. Count integers in the stack")
        print("4. Check if the stack is empty")
        print("5. Check if the stack is full")
        print("6. Clear the stack")
        print("7. Peek at the top integer")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            item = int(input("Enter an integer to push: "))
            if zasobnik.push(item):
                print("Integer pushed onto the stack.")
            else:
                print("Stack is full. Cannot push.")

        elif choice == '2':
            item = zasobnik.pop()
            if item is not None:
                print(f"Popped integer: {item}")
            else:
                print("Stack is empty. Cannot pop.")

        elif choice == '3':
            print(f"Number of integers in stack: {zasobnik.count()}")

        elif choice == '4':
            print("Stack is empty." if zasobnik.is_empty() else "Stack is not empty.")

        elif choice == '5':
            print("Stack is full." if zasobnik.is_full() else "Stack is not full.")

        elif choice == '6':
            zasobnik.clear()
            print("Stack cleared.")

        elif choice == '7':
            item = zasobnik.peek()
            if item is not None:
                print(f"Top integer: {item}")
            else:
                print("Stack is empty.")

        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_stack()