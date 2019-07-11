from __future__ import division


class Rational(object):
    
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        import math
        factor = math.gcd(self.numer, self.denom)
        self.numer = int(self.numer/factor) 
        self.denom = int(self.denom/factor)

        return Rational(self.numer, self.denom)
        #return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        import math
        addnumer = ((self.numer *other.denom) + (other.numer*self.denom))
        adddenom = (self.denom*other.denom) 
        factor = math.gcd(adddenom, addnumer)
        self.numer = addnumer/factor 
        self.denom = adddenom/factor
        
        return Rational(self.numer, self.denom)
       # return '{}/{}'.format(self.numer, self.denom)

    def __sub__(self, other):
        import math
        subtrnumer = ((self.numer *other.denom) - (other.numer*self.denom))
        subtrdenom = (self.denom*other.denom) 
        factor = math.gcd(subtrdenom, subtrnumer)
        self.numer = subtrnumer/factor 
        self.denom = subtrdenom/factor
        
        return Rational(self.numer, self.denom)
       # return '{}/{}'.format(self.numer, self.denom)

    def __mul__(self, other):
        import math
        multnumer = (self.numer *other.numer)
        multdenom = (self.denom*other.denom) 
        factor = math.gcd(multdenom, multnumer)
        self.numer = multnumer/factor 
        self.denom = multdenom/factor
        
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
