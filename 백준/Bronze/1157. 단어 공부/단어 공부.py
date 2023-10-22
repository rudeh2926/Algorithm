a = input().upper()
al = list(set(a))
c = []
for i in al:
  b = a.count
  c.append(b(i))
if c.count(max(c)) > 1:
  print("?")
else:
  print(al[(c.index(max(c)))])