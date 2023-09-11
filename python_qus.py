"""
1. Iterartors and Generators ?

   Iterators: are used to provide a sequence of values one at a time

              it is used when you want to iterate over a
              large or infinite sequence of values without loading
              everything into memory

              Iterators follow a lazy evaluation approach,
              where elements are computed only when requested.

              Examples : enumerate(), zip(), range(), iter() functions
                         returns iterartor
                         map, filter, raduce
              Django : QuerySet Iterator .iterator()
                       prefetch_related iterator

   Generators: are itself a type of iterator

               Generators provide a simpler syntax and are easier
               to write compared to custom iterator classes

               generators are implemented as functions using
               the yield keyword

1b. Key diffrence between Iterator and generator ?

        Memory:
               Generators are more memory-efficient because they generate
               values on-the-fly and do not store the entire sequence
               in memory.

               Iterators can potentially consume more memory,
               especially if they need to store a large amount
               of data in memory.

        Iteration State:
               Iterators maintain their own state,
               so you can have multiple independent
               iterators over the same sequence, each with its own position

               Generators maintain their state automatically,
               and they are single-use.

               Once a generator has been
               iterated through, it cannot be reset to its initial state.
               If you need to iterate over the same sequence again,
               you need to create a new generator.

1c. What is the exact use of iterator ?

   Memory Efficiency:
    This is because iterators generate elements on-the-fly,
    whereas lists and tuples store all elements in memory.

   Lazy Evaluation:
    elements are computed or fetched only when requested.
    This can be more efficient, as it avoids unnecessary
    calculations or data loading.

   Dynamic Data Sources:
    Iterators are particularly useful when working with
    dynamic data sources, such as reading data from files
    databases, or network streams.
    They allow you to process data as it becomes available.

    Custom iterators allow you to encapsulate this complex
    logic within the iterator class
"""


# Simple Iterator
class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


obj = Iterator([2, 4, 4, 6])

# for item in obj:
#     print(item)


# File Iterator
class FileIterator:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self

    def next(self):
        if self.file is None:
            raise StopIteration
        line = self.file.readline()
        if not line:
            self.file.close()
            self.file = None
            raise StopIteration
        return line.strip()


obj = FileIterator("example.txt")

# for item in obj:
#     print(item)


def generator(array):
    for item in array:
        yield item


obj = generator([2, 6, 8])

# for item in obj:
#     print(item)

"""
2. Deep copy and shallow copy ?

    Shallow Copy stores the references of objects
    to the original memory address.

    Changes made to nested objects within
    the copy will affect the original

    A shallow copy is faster.

    ..........................................

    A deep copy, on the other hand, creates a completely
    independent copy of an object and all of its
    nested objects.

    Changes made to the copied object
    or its nested objects won't affect
    the original or any other copies.

    Deep copy is comparatively slower.
"""

import copy

obj = [[1, 2], 4, 5]
copied = copy.copy(obj)
copied[0][0] = 100

# print(copied, obj)

deepcopy = copy.deepcopy(obj)
deepcopy[0][0] = 200

# print(deepcopy, obj)


"""
3. Static Method vs Class Method

    Static method decorator : is used to define a static method within a class.
    It does not have access to the instance or its attributes,
    often used for utility functions that are related to the class


    Class method decorator : class methods are used when you want
    to define a method that can operate on or modify class-level
    attributes and data.

    while normal instance methods can access and modify class variables,
    using class methods for such operations can improve code clarity,
    consistency (establish a clear pattern in your codebase,
    which can enhanclass ParentClass:
    class_variable = 0

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1ce readability and maintainability),
    and allow for easier customization when subclassing.

    Instance Method : Instance methods in Python are methods that
                      are defined within a class and are designed
                      to operate on instances (objects) of that class
"""


# static method
class MyClass:
    @staticmethod
    def static_method(x, y):
        return x + y


result = MyClass.static_method(3, 5)  # Calling the static method
# print(result)


# Class method
class ParentClass:
    class_variable = 0

    @classmethod
    def increment_class_variable(cls):
        cls.class_variable += 1


"""
4. Diffrence between __new__ and __init__ method?

    __new__ is a special method that is responsible
    for creating a new instance of a class.

    It is called before __init__ and is responsible
    for the creation and initialization of the object.

    used when we need to customize object creation,
    such as creating a singleton or immutable object
"""


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("Creating a new object")
        return object.__new__(cls, *args, **kwargs)

    def __init__(self, name):
        print("Initializing the object")
        self.name = name


# my_object = MyClass("John Doe")

"""
6. List vs Tuples Comparison with memory ?
   List : 72 bytes
   Tuples : 56 bytes

   Tuples are immutable, which means their elements
   cannot be changed after creation.

   Lists, on the other hand, are mutable,
   allowing you to add, remove, or modify elements.

   In tuples Python doesn't need to allocate
   extra memory for potential changes.
"""

import sys

empty_list = [1, 2, 3, 4, 5, 6, "ananthu", "reshmi", [5 , 8, 0]]
size = sys.getsizeof(empty_list)


def generator(data):
    for item in data:
        yield item

gen = generator([1, 2, 3, 4, 5, 6, "ananthu", "reshmi", [5 , 8, 0]])
print(sys.getsizeof(gen))

print("Memory usage of an empty list:"+str(size)+"bytes")
