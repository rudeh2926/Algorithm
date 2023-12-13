import sys
import re

p = re.compile('(100+1+|01)+')
for i in range(int(sys.stdin.readline())):
   s = input()
   if p.fullmatch(s):
       print("YES")
   else:
       print("NO")