#! /usr/bin/env python3

import re


##data = 'Nebraska'
##
##word = re.search('[abc]', data)
##
##
### How to check and print for vowels and consonants.
##data = 'cba1234567890CBAabc'
##result = re.finditer('[abc6]', data) 
##for r in result:
##    print(r.group(), end="")
##
##print()
##print()



# um maybe figure out how to append to another variable here???? len()?
state = 'Nebraska'
##consonants = re.finditer('[bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTWXZ]', state)
##for c in consonants:
##    form = c.group()
##    print(form)
##    print(c)


print()
print()
print()
consonants0 = re.findall('[bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTWXZ]', state)
##print(consonants0)
print()
##myit = iter(consonants0)
##print(next(myit),next(myit),next(myit), sep="")
print()
print()
myarray = []
myarray = consonants0
a=""
x=0
while x < len(myarray):
    print(myarray[x])
    a = str(a + myarray[x])
    x += 1

print()
print(a)
print()






####for i in consonants0:
####    print(i, end="")
##
##
##print()
##print()
##print()
##consonants1 = re.search('[bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTWXZ]', state)
##print(consonants1)
##
##
##
##
##print()
##print()
##
##
##territory = 'Nebraska'
##vowels = re.finditer('[aeiouyAEIOUY]', territory)
##for t in vowels:
##    print(t.group(), end="")
    







