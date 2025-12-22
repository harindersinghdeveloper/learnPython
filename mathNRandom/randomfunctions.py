import random

#using below everytime we get different random numbers
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

#if we want a fix sequence of random number, then we need to use seed
random.seed(101)
print(random.randint(1,100))
print(random.randint(1,100))
print(random.randint(1,100))

# to make sure we get same set of random number sequence when we seed, let put assertions
random.seed(101)
print(random.randint(1,100).__eq__(75))
print(random.randint(1,100).__eq__(25))
print(random.randint(1,100).__eq__(70))
#reset seed
random.seed()


# choose a random element from a given list
my_list = list(range(100))
print(random.choice(my_list))

# for float random
print(random.uniform(a=0,b=100))