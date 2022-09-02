import random
import math
num = random.randint(1, 50)
raiz = num ** (1/2)
print ('seu numero é {}, e a raiz é{}'.format(num, math.ceil(raiz)))