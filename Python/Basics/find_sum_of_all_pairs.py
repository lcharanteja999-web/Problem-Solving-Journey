#--find all the pairs of given sum---

def array(l,target):

  l1 = []

  for i in range(len(l)):
    for j in range(i +1 ,len(l)):
      if l[i] + l[j] == target:
          l1.append((l[i],l[j]))

  print(l1)


l = list(map(int,input("enter list ").split()))
target = int(input("enter target value "))
array(l,target)
