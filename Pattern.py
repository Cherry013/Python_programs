x = int(input("Enter the no lines:"))
H = 1
for i in range(1,x+1):
  for m in range(2):
    if H%2!=0:
      for j in range(1,i+1):
        print(j,end=" ")
      for k in range(i-1,0,-1):
        print(k,end=" ")
    if H%2==0 and H!=2*(x):
      for j in range(1,i+1):
        print(j,end=" ")
      for k in range(i,0,-1):
        print(k,end=" ")
    if H!=(2*x):
      print()
    H+=1
H = H-1
A = 2
B = 1
for i in range(x-1,0,-1):
  for j in range(1,i+1):
    print(j,end=" ")
  if i%2!=0:
    V = A**B
    for m in range(V):
      print(i,end=" ")
  if i%2==0:
    V = (A**B)+1
    for m in range(V):
      print(i,end=" ")
  for k in range(i,0,-1):
    print(k,end=" ")
  print()
  B+=1
  H+=1