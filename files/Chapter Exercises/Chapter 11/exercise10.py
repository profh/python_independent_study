# Chapter:		11
# Exercise:		10
# Start:		07:05:56 PM 07/06/2007
# End:			07:07:07 PM 07/06/2007
# Rating:		1
# Note:			Annoying to find out the algorithm

class PrimeNumberProvider(object):

    def __init__(self, sieve=None):
        if sieve is None:
            self.__make_sieve()
        else:
            self.sieve = sieve

    def __make_sieve(self):
        #the sieve is all primes less than 100
        seed = [3, 5, 7]
        rng = range(11,98,2) #step=2, ie. just odd numbers
        for p in seed:
            rng = [x for x in rng if x % p]
        self.sieve = [2] + seed + rng
        
    def get_primes(self, upperbound):
        p_high = self.sieve[-1]  #largest element in sieve
        if upperbound > p_high**2:
            #sieve is too small
            raise Exception('Upper Bound is too high.')
        if upperbound <= p_high:
            primes = [p for p in self.sieve if p < upperbound]
        else:
            from math import sqrt
            N = sqrt(upperbound)
            rng = range( p_high+2, upperbound, 2 )
            for p in self.sieve[1:]:  #first element in sieve is 2, don't need it
                if p > N:
                    break
                rng = [x for x in rng if x % p]
            primes = self.sieve + rng
        return primes 
def main():
	upperbound = input("Number to generate primes up to: ")
	p = PrimeNumberProvider()
	print p.get_primes(upperbound)
	
main()
