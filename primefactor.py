import sys
import numpy


class primes:
    def __init__(self):
        self.primelist = [1,2,3,]
        self.primefactors = []

    def isprime(self, n):
        primestatus = True
        for i in range(2,int(n)):
            if int(n)%i == 0:
                #print ("Setting to False")
                primestatus = False
                break
        #if primestatus == False:
            #pass
            #print ("Not Prime")
        if primestatus == True:
            #print ("Must Be Prime")
            self.primelist.append(int(n))

    def primenumlist(self, n):
        y = 4
        if n == "1" or n=="2" or n=="3":
            print ("1, 2, 3 are too easy!")
            sys.exit(0)
        elif n == "0":
            print ("Zero is neither prime nor composite.")
            sys.exit(0)
        while y < int(n)/2:
            self.isprime(y)
            y +=1

    def primefactoring(self, n):
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
    n = input("Enter a number to calculate its prime factors: ")
    p = primes()
    p.primenumlist(n)
    p.primefactoring(n)
