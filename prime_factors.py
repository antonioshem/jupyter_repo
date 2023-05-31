# Write a python function to find all prime factors
#input is an integer value 
#output is a list containing all prime factors
#for example get_prime_factors(630) should return [2, 3, 3, 5, 7]
#multiply them together the product is 630

def find_prime_factors(n):   #we define a function 'find_prime_factors' that takes a number n whose prime factors are to be found
    
    factors = []  # initialize empty factors that store the prime factors
    divisor = 2  # set initial value of divisor to 2 
    
    while divisor <= n:   # we start a while loop that continues until the divisor becomes greater than n. It finds all the prime numbers
        if n % divisor == 0: # checks if n is divisible by current divisor without a remainder
            factors. append(divisor)  #if the above divisor is a prime factor it is added to factors list, and n is updated reducing the value and allowing us to find next
            n = n /divisor
        else:
            divisor += 1  # if he divisor is not a factor of n, we increment it by w to continue to the next iteration loop
    return factors

n = int(input("Enter a number to find it's prime factors: "))
prime_factors = find_prime_factors(n)
print("Prime Factors are: ", prime_factors)