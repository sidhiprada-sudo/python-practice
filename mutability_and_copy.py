#mutable
def change(lst):
    lst.append(100)
a=[1,2,3]
change(a)
print(a)
#immutable
def num(x):
    x=x+10
n=5
num(n)
print(n)
#copy
import copy
a=[[1,2],[3,4]]
b=a.copy()
c=copy.deepcopy(a)
b[0].append(99)
print(a)
print(c)
