from __future__ import division

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
        import math
        ## TypeError: 'float' object cannot be interpreted as an integer
        
        factor = math.gcd(self.numer, self.denom) 
        ## broke (works if I just say = 1)
        self.numer = int(self.numer/factor) 
        self.denom = int(self.denom/factor)
        #### commented this out as it blew up ith recursive loop!!
        #return Rational(self.numer, self.denom)

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
 
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        import math
        addnumer = ((self.numer *other.denom) + (other.numer*self.denom))
        adddenom = (self.denom*other.denom) 
        factor = math.gcd(adddenom, addnumer)
        self.numer = int(addnumer/factor) 
        self.denom = int(adddenom/factor)
        
        return Rational(self.numer, self.denom)
       # return '{}/{}'.format(self.numer, self.denom)

    def __sub__(self, other):
        import math
        subtrnumer = ((self.numer *other.denom) - (other.numer*self.denom))
        subtrdenom = (self.denom*other.denom) 
        factor = math.gcd(subtrdenom, subtrnumer)
        self.numer = int(subtrnumer/factor) 
        self.denom = int(subtrdenom/factor)
        
        return Rational(self.numer, self.denom)
       # return '{}/{}'.format(self.numer, self.denom)

    def __mul__(self, other):
        import math
        multnumer = (self.numer *other.numer)
        multdenom = (self.denom*other.denom) 
        factor = math.gcd(multdenom, multnumer)
        self.numer = int(multnumer/factor) 
        self.denom = int(multdenom/factor)
        
        return Rational(self.numer, self.denom)
       # return '{}/{}'.format(self.numer, self.denom)

    def __truediv__(self, other):
        pass

    def __abs__(self):
        pass

    def __pow__(self, power):
        pass

    def __rpow__(self, base):
        pass
