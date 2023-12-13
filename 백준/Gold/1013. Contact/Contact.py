import sys
import re

a = re.compile('(100+1+|01)+')
for i in range(int(sys.stdin.readline())):
   b = input()
   if a.fullmatch(b):
       print("YES")
   else:
       print("NO")