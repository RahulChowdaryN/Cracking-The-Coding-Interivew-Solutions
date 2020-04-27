from collections import deque
class AnimalShelter:
    def __init__(self):
        self.counter = 0
        self.dogs= deque()
        self.cats = deque()

    def enqueue(self,item):
        self.counter +=1
        if item == "d":
            self.dogs.append(self.counter)
            return True
        if item == "c":
            self.cats.append(self.counter)
            return True
        else:
            self.counter -=1
            return None

    def deque_dog(self):
        if self.dogs:
            return self.dogs.popleft()
        return False

    def deque_cat(self):
        if self.cats:
            return self.cats.popleft()
        return False

    def dequeAny(self):
        if not self.dogs and not self.cats:
            return None

        if not self.dogs:
            return self.cats.popleft()
        if not self.cats:
            return self.dogs.popleft()

        dog_id = self.dogs[0]
        cat_id = self.cats[0]

        if dog_id < cat_id:
            return self.dogs.popleft()
        else:
            return self.cats.popleft()

######## approach - 2

# Implement a cat and dog queue for an animal shelter.

class AnimalShelter():
    def __init__(self):
        self.cats, self.dogs = [], []

    def enqueue(self, animal):
        if animal.__class__ == Cat:
            self.cats.append(animal)
        else:
            self.dogs.append(animal)

    def dequeueAny(self):
        if len(self.cats): return self.dequeueCat()
        return self.dequeueDog()

    def dequeueCat(self):
        if len(self.cats) == 0: return None
        cat = self.cats[0]
        self.cats = self.cats[1:]
        return cat

    def dequeueDog(self):
        if len(self.dogs) == 0: return None
        dog = self.dogs[0]
        self.dogs = self.dogs[1:]
        return dog


class Animal():
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Cat(Animal): pass


class Dog(Animal): pass


import unittest


class Test(unittest.TestCase):
    def test_animal_shelter(self):
        shelter = AnimalShelter()
        shelter.enqueue(Cat("Hanzack"))
        shelter.enqueue(Dog("Pluto"))
        shelter.enqueue(Cat("Garfield"))
        shelter.enqueue(Cat("Tony"))
        shelter.enqueue(Dog("Clifford"))
        shelter.enqueue(Dog("Blue"))
        self.assertEqual(str(shelter.dequeueAny()), "Hanzack")
        self.assertEqual(str(shelter.dequeueAny()), "Garfield")
        self.assertEqual(str(shelter.dequeueDog()), "Pluto")
        self.assertEqual(str(shelter.dequeueDog()), "Clifford")
        self.assertEqual(str(shelter.dequeueCat()), "Tony")
        self.assertEqual(str(shelter.dequeueCat()), "None")
        self.assertEqual(str(shelter.dequeueAny()), "Blue")
        self.assertEqual(str(shelter.dequeueAny()), "None")


if __name__ == "__main__":
    unittest.main()

