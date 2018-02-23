# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 15:51:09 2017

@author: Jinsu Elhance
"""
#TWO WAYS TO RETURN A STRING OF NUMBERS (ALPHABET POSITION) RELATED TO A STRING
Dict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26} 

def alphabet_position2(text):
    """
    Input: a string
    Output: Same as above
    """
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
    #This function is much cleaner, joins each letter's alphabetical position using join function if c.isalpha())

def get_sum(a,b):
    return sum(range(min(a,b), max(a,b)+1))
    #Simple and clean (USE THE SUM FUNCTION)
    
class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)

clock = Clock('5:30')
clock.print_time()

def narcissistic(value):
    result = 0
    strvalue = str(value)
    power = len(strvalue)
    for i in strvalue:
        result += int(i)**power
    return result == value

def genPrimes():
    candidate = 1
    primes = []
    while True:
        candidate += 1
        if all(candidate%i for i in primes):
            primes += [candidate]
            yield candidate
            
def camel_case(string):
    return "".join(i.capitalize() for i in string.split())

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newsearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

def modSwapSort(L): 
    """ L is a list on integers """
    print("Original L: ", L)
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                L[j], L[i] = L[i], L[j] 
                print(L)
    print("Final L: ", L)
    
def genPrim(n):
    candidate = 1
    primes = [2]
    for i in range(2,n+1):
        candidate += 1
        if all(candidate%i for i in primes):
            primes += [candidate]
    return (primes)

def dict_interdiff(d1,d2):
    inter = {}
    diff = {}
    for i in d1.keys():
        if i in d2.keys():
            inter[i] = f(d1[i],d2[i])
        elif i not in d2.keys():
            diff[i] = d1[i]
        for j in d2.keys():
            if j not in d1.keys():
                diff[j] = d2[j]
    return (inter,diff)

def song_decoder(song):
    """
    A function that takes in a string containing WUBs and decodes it
    Input = string
    Returns: a string of lyrics without the WUBs
    """
    return " ".join(song.replace('WUB', ' ').split())

def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]

def fibRecur(n):
    count = 0
    if count == n:
        return 0
    else:
        count += 1
        return fibRecur(n-1)
    
def fibExplicit(n):
    k,kth,difference = 0,0,1
    while k < n:
        kth, difference = kth + difference, kth
        k = k+1
    return kth

# =============================================================================
# The two functions below return the same values for the same inputs.
# =============================================================================

    
def highest_scoring(text):
    text = (text.lower()).split()
    highpts = 0
    for i in text:
        score = 0
        for n in i:
            if n in Dict.keys():
                score += Dict[n]
        if score > highpts:
            highpts = score
            highest = i
    return highest

def high(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))

from ucb import trace

@trace
def stairs(n):   
    
    if n==1:
        return 1
    
    elif n==2:
        return 2
    
    else:
        return stairs(n-1) + stairs(n-2)
    
def multest(x,y):
  if x == 0 or y==0:
    return 0
  elif x==1:
    return y
  else:
    return y + multest(x-1, y)

def combine(left,right):
    factor = 1
    while factor <= right:
        factor = factor*10
    return left * factor + right

def reverse(n):
    if n < 10:
        return n
    else:
        return combine(n%10, reverse(n//10))

def remove(n,digit):
    removed = 0
    while n!=0:
        n,last = n//10,n%10
        if last != digit:
            removed = combine(removed,last)
    return reverse(removed)

def kbonacci(n,k):
    if n<k-1:
        return 0
    elif n==k-1:
        return 1
    else:
        total = 0
        i= 0
        while i< n:
            total = total+k
            i += 1
        return total
    
def re(peat):
    return print(peat,peat)

def cheap(eat):
    car, seat = re, print
    seat(car(eat))
    return double(eat)

def double(double):
    if double:
        return double + double
    elif car(double)(print)(print):
        return 1000
    else:
        return seat(3)
    
seat = double
car = lambda c: lambda a: lambda r: r(5,a(c))

def sandwich(n):
    tens, ones = (n//10)%10, n%10
    n = n//100 
    while n>1:
        if ones == n%10:
            return True
        else:
            tens, ones = n%10, tens
            n= n//10
    return False

potato = {"a":12,"b":32}

def luhn_sum(n):
    """
    Return the Luhn Sum of n
    """
    def luhn_digit(digit):       
        x = digit * multiplier
        return (x//10) + x%10
    
    total, multiplier = 0,1
    
    while n:
        n, last = n//10, n%10
        total = total + luhn_digit(last)
        multiplier = 3-multiplier
        
    return total

def dashatize(n):
    last = n%10
    dashed = ""
    while n > 10:
        if last % 2 != 0:
        #if odd
            dashed =  "-" + str(last) + dashed
        else:
            dashed =  str(last) + dashed
        
        n,last = n//10,(n//10)%10
    return str(n) + dashed

def first_non_repeating_letter(string):
    """
    >>> first_non_repeating_letter("stress")
    t
    """
    index, checked= 1, ""
    for i in string:    
        if i not in string[index:].lower() and i not in checked and i not in string[index:].upper():        
            return i
        checked,index = checked + i, index + 1
    return ""
        

def reversenum(n):
    return int(str(n)[::-1])
