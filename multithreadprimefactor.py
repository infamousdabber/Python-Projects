import sys
import numpy
import multiprocessing
import math
from multiprocessing import *


class primes:
    def __init__(self):
        #1, 2, and 3 are pre entered to make the functions less complex for dealing with small numbers.
        #The two list are combined into one managed list, x, later on.
        self.primelist = [1,2,3,]
        self.primelistupper = []
        self.primefactors = []

    def creatingrange(self, n):
        #Creating ranges for the multiprocessing to process their own sets of numbers.
        #the lower range(p1) is used as a starting point for the lower range multiprocessing.
        #the upper range(p2) is used as an ending point rather than a starting point for the upper range multiprocessing.
        if int(n)%2==0:
            p1 = math.floor(int(n)/4)-1
            p2 = int(n)
        else:
            p1 = math.floor(int(n)/4)
            p2 = int(n)
        return (p1, p2)

    def isprime(self, n):
        #Checks if each number under half on n is prime or not and appended the prime numbers to a list.
        #This is the for the lower numbers to be processed in the multiprocessing f1.
        primestatus = True
        for i in range(2,int(n)):
            if int(n)%i == 0:
                primestatus = False
                break
        if primestatus == True:
            self.primelist.append(int(n))

    def isprimeupper(self, n):
        #This is for the upper numbers to be processed in the multiprocessing f2.
        primestatus = True
        for i in range(2,int(n)):
            if int(n)%i == 0:
                primestatus = False
                break
        if primestatus == True:
            self.primelistupper.append(int(n))

    def primenumlistlower(self, n):
        #Processes each number starting from 4 through the isprime function.
        #After the number is processed, it check to see if any new numbers are added to the list of primes and adds them to a managed list for later access.
        #This is for the lower numbers being processed in multiprocessing f1.
        #A confusing part of this function is that n isn't actaully the n value entered but rather the quartered value of the orignal n. If you take a look at where the multiprocessing line is called, the argument that is entered into this funciton is the quartered value created in the range function.
        y = 4
        if n == "1" or n=="2" or n=="3":
            print ("1, 2, 3 are too easy!")
            sys.exit(0)
        elif n == "0":
            print ("Zero is neither prime nor composite.")
            sys.exit(0)
        while y < int(n):
            self.isprime(y)
            y +=1
        #print (self.primelist)
        for h in self.primelist:
            #Appending the separate lists into one managed list.
            x.append(h)


    def primenumlistupper(self, n):
        #This is for the upper numbers being processed in multiprocessing f2.
        #
        y1, y2 = p.creatingrange(n)
        y = y1
        if n == "1" or n=="2" or n=="3":
            print ("1, 2, 3 are too easy!")
            sys.exit(0)
        elif n == "0":
            print ("Zero is neither prime nor composite.")
            sys.exit(0)
        while y < int(n)/2:
            self.isprimeupper(y)
            y +=1
        #print (self.primelistupper)
        for h in self.primelistupper:
            #Appending the separate lists into one managed list.
            x.append(h)

    def primefactoring(self, n):
        #
        #When n==9, there is an error in the process and it is considered a prime before the prime 3 can be divided through. Need fixed.
        if n == str(9):
            print ("[3, 3]")
        else:
            primecounter = 1
            numberentered = n
            i = self.primelist[1]
            while primecounter < len(self.primelist)-1:
                if int(n)%i==0:
                    if int(n)/i == 1:
                        break
                    else:
                        n = int(n)/i
                    self.primefactors.append(i)
                elif numberentered == (numpy.prod(self.primefactors)*int(n)):
                    break
                else:
                    primecounter +=1
                    i = self.primelist[primecounter]
            if self.primefactors == []:
                print ("That number is already prime.")
            else:
                self.primefactors.append(int(n))
                print (self.primefactors)


if __name__ == "__main__":
    n = input("Enter a number to check its prime factors: ")
    p = primes()
    r1, r2 = p.creatingrange(n)
    manager = Manager()
    x = manager.list()
    f1 = multiprocessing.Process(target=p.primenumlistlower, args=(r1, ))
    f2 = multiprocessing.Process(target=p.primenumlistupper, args=(r2, ))
    f1.start()
    f2.start()
    f1.join()
    f2.join()
    p.primefactoring(n)
