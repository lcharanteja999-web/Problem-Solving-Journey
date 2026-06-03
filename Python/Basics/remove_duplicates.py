#----remove duplicates and keepin ght order of list same---

def remove_duplicates(l):
  s = set()
  result = []

  for i in l:
    if i not in s:
      s.add(i)
      result.append(i)
  print(result)

l = list(map(int,input("enter list \n").split()))
remove_duplicates(l)
