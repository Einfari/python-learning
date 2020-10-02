#!/usr/bin/python3
# -*- coding:utf-8 -*-

# File Name: Animal.py
# Author: Lipsum
# Mail: niuleipeng@gmail.com
# Created Time: 2016-05-12 15:24:47

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')


class Cat(Animal):
    def __init__(self,name):
        self.__name = name

    def run(self, speed):
        print('%s is running %s...' %(self.__name,speed))

    def run(self):
        print('Cat is running...')

    # def run(self):
        # print('Cat is running...')

def run_twice(animal):
    for i in range(2):
        animal.run()


if __name__ == '__main__':
    animal = Animal()
    dog = Dog()
    cat = Cat('momo')

    animal.run()
    dog.run()
    cat.run()

    run_twice(animal)
    run_twice(dog)
    run_twice(cat)

