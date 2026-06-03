#----count word frequency----

def count(l):
  l.lower()
  d = {}

  for i in l:
    if i not in d:
      d[i] = 1
    else:
      d[i] +=1

  for keys,values in d.items():
      print(f"{keys} : {values}")


l = input("enter a string").split()

count(l)
