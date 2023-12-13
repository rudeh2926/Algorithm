import sys
import re

a = re.compile('(100+1+|01)+')
for i in range(int(sys.stdin.readline())):
   b = int(input())
   if a.fullmatch(s):
       print("YES")
   else:
       print("NO")
