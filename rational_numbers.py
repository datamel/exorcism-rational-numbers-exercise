from __future__ import division
import math
class Rational(object):
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.__reduce__()

        if (self.numer and self.denom) < 0:
            self.numer = self.numer*-1
            self.denom = self.denom*-1
        elif (self.numer and not self.denom) or (not self.numer and self.denom)<0:
            abs(self.numer) and abs(self.denom)
            self.numer = self.numer*-1 

    def __reduce__(self):    
        
        factor = math.gcd(self.numer, self.denom) 
        self.numer = int(self.numer/factor) 
        self.denom = int(self.denom/factor)
       

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
 
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        
        addnumer = ((self.numer *other.denom) + (other.numer*self.denom))
        adddenom = (self.denom*other.denom) 
        factor = math.gcd(adddenom, addnumer)
        self.numer = int(addnumer/factor) 
        self.denom = int(adddenom/factor)
        
        return Rational(self.numer, self.denom)

    def __sub__(self, other):
        
        subtrnumer = ((self.numer *other.denom) - (other.numer*self.denom))
        subtrdenom = (self.denom*other.denom) 
        factor = math.gcd(subtrdenom, subtrnumer)
        self.numer = int(subtrnumer/factor) 
        self.denom = int(subtrdenom/factor)
        
        return Rational(self.numer, self.denom)
   

    def __mul__(self, other):
        
        multnumer = (self.numer *other.numer)
        multdenom = (self.denom*other.denom) 
        factor = math.gcd(multdenom, multnumer)
        self.numer = int(multnumer/factor) 
        self.denom = int(multdenom/factor)
        
        return Rational(self.numer, self.denom)

    def __truediv__(self, other):

        holdingnumer = other.numer
        holdingdenom = other.denom
        other.numer = holdingdenom
        other.denom = holdingnumer
        divnumer = (self.numer *other.numer)
        divdenom = (self.denom*other.denom) 
        factor = math.gcd(divdenom, divnumer)
        self.numer = int(divnumer/factor) 
        self.denom = int(divdenom/factor)
        
        return Rational(self.numer, self.denom)      

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
