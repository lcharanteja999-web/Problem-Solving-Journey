#----common elements using sets----

def unique(l1,l2):
  s1 = set(l1)
  s2 = set(l2)

  print(s1 & s2)  #here & means intersection in sets

  #for union elements in set we write
  print(s1 | s2)


l1 = list(map(int,input("enter list one \n").split()))
l2 = list(map(int,input("ente list two \n").split()))
unique(l1,l2)
