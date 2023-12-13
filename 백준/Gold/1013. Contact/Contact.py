import sys
import re

a = re.compile('(100+1+|01)+')
for i in range(int(sys.stdin.readline())):
   b = input()
   if a.fullmatch(b):
       print("YES")
   else:
       print("NO")


// 한줄
import re, sys; print('\n'.join(['YES' if re.fullmatch('(100+1+|01)+', input()) else 'NO' for _ in range(int(sys.stdin.readline()))]))
