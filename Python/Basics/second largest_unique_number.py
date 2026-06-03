#second largest unique number

def unique(l):
  d = {}

  for i in l:
    if i not in d:
      d[i] = 1

  l1 = list(d.keys())
  l1.sort()

  if len(l1) < 2:      # we are writing this condition because if there is a list [9,9,9,9] in dic it stores only one 9 so when u write l1[-2] it fails.
    print("no second largest element")
  else:
    print(f"second largest unique element is : {l1[-2]} ")


l = list(map(int,input("enter list ").split()))
unique(l)
