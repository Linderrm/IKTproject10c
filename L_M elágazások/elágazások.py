
from cgitb import text
import random
from re import I

#1------------------------------------

"""
State=input("jó napod van")
if State=="igen":
    ihprint("igen")
elif State=="igen" :
    print("nem")
else:
    print("ilyen válsz nincs")        
"""      

#2-------------------------------
"""
Number=int(input("kérek egy számpot"))
if(Number%2==0):
    print("szám páros")
else:
    print("páratlan")    
    """

    #3--------------------------------------
"""

szám =random.randint(1,6)
szám1=int(input("kérek egy számot"))
print(szám)

if(szám1<szám):
    print("kisebb")
elif(szám1>szám):
    print("kisebb")
else:
    print("egyenlő")        
"""

#4-----------------------
"""
for x in range (1,11):
    print(x)
"""    

#5-----------------
"""
tm=range(1,11)


for x in  reversed(tm):
    print(x)
"""
#6-----------------
"""
szam=int(input("kérek egy számot"))
text = input("kérem a szöveget")
i=0
while(i<szam):
    print(text)
    i=i+1
    """

#7----------------------------

maradek=1
while maradek!=0 :
    szam=int(input("kérek egy számot"))
    maradek=szam%2


