#----average students of marks

def marks(n):
  d = {}

  for i in range(n):
    keys = input("enter names of student \n8")
    values = int(input("enter marks of student "))

    if keys in d:
      print("student name already exists")
    else:
       d[keys] = values

  sum = 0

  for i in d:
    sum += d[i]             #i means keys and d[i] is values

  avg = float(sum) / n

  for i in d:
    if d[i] > avg:
      print(f"{i} is above average")


  print(f"average of student marks is {avg}")

n = int(input("enter how many student marks u want to enter: \n"))
if n == 0:
  print("enter valid number")
else:
  marks(n)
