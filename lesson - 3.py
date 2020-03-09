import time


def decorator_func(orig_func):
    import time
    """passing *args and **kwargs to our function, allows us to get arguments from our main function"""

    def wrapper_func(*args, **kwargs):  # args and kwargs allow us to accept an arbitary number of positional or
        # keyword arguments
        print('********')
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        print('********')
        t2 = time.time() - t1
        print('{} run in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper_func


# * args - unpack our values (as default) - def info('New York', 'City')
# ** kwargs - unpack our key values - def info(city = 'New York', country = 'Belgium')
import time


@decorator_func
def display(car, year):  # we pass 2 arguments - car`s model and its year
    for i in range(5):
        print('Our car ', car, ' was made in ', year)


display('BMW', 1995)



""""Stack Class"""
stack = []  # we start with an empty stack list for our numbers


class Stack:
    def __init__(self, stack):
        self.stack = stack

    # definitions of adding a new element to our list 'stack' for numbers
    def add(self, number):
        print("Add a new item", number)
        if len(self.stack) != 0:
            self.stack.append(0)
            for i in range(len(self.stack) - 1, 0, -1):
                self.stack[i] = self.stack[i - 1]
            self.stack[0] = number

        else:
            self.stack.append(number)

    # here we will remove an element from out stack
    def pop(self):
        print("Pop the last number", self.stack[0])
        # here we check a condition of length of our list.
        # If it`s equal to 0 we get an error that we cant pop an element from empty stack
        if len(self.stack) != 0:
            self.stack.pop(0)  # pop the first number in our list
        else:
            raise ValueError('Our stack is empty, you can`t pop a number from it!!!!')


stac = Stack(stack)
stac.add(12)
print(stac)
stac.add(1)
print(stac)
stac.add(9)
print(stac)
stac.add(33)
stac.pop()
print(stac)



"""Now we will create a Queue Class"""
queue = []


class Queue:
    def __init__(self, queue):
        self.queue = queue

    def add(self, number):
        print('Add', number)
        if len(self.queue) != 0:
            self.queue.append(0)
            for i in range(len(self.queue) - 1, 0, -1):
                self.queue[i] = self.queue[i - 1]
            self.queue[0] = number
        else:
            self.queue.append(number)

    def pop(self):
        print('Pop number', self.queue[-1])
        if len(self.queue) != 0:  # pop the last number of our list
            self.queue.pop()
        else:
            raise ValueError('Our queue is empty, you can`t pop a number from it!!!!')


queue = Queue(queue)

queue.add(23)
print(queue)
queue.add(12)
print(queue)
queue.add(4)
print(queue)
queue.pop()
print(queue)
