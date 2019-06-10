l=[[0,0,0,0,0,0],[0,"s1s",0,0,"s2s","l2"],[0,0,"l1",0,0,0],[0,0,0,0,"l2","s2t"],["l1",0,0,0,"s1t",0],["$",0,0,0,0,0]]
def display(l):
  for i in range(0,len(l)):
    for j in range(0,len(l)):
      print(l[i][j],end=" ")
    print()
i,j=5,0
p,q=i,j
steps=36
count=1
while(1):
  if(i==0 and j==0):
      print("winner winner")
      break
  n=int(input("Enter the number"))
  if(i==0 and n>j):
    print("enter the value again")
    continue
  if(n>6):
    print("enter the value again")
    continue
  else:
    for k in range(0,n):
      if(count<=5):
        if(i%2!=0):
          j=j+1
          count=count+1
        else:
          j=j-1
          count=count+1
      else:
        i=i-1
        count=1
  l[i][j]="$"
  l[p][q]=0
  if(p==4 and q==0):
      l[p][q]="l1"
  if(p==2 and q==2):
      l[p][q]="l1"
  if(p==4 and q==4):
      l[p][q]="slt"
  if(p==3 and q==5):
      l[p][q]="s2t"
  if(p==3 and q==4):
      l[p][q]="l2"
  if(p==1 and q==5):
      l[p][q]="l2"
  if(i==4 and j==0):
      l[i][j]="l1"
      l[2][2]="l1$"
      i,j=2,2
      count=4
  if(i==4 and j==4):
      l[i][j]="s1t$"
  if(i==3 and j==4):
      l[i][j]="l2"
      l[1][5]="l2$"
      i,j=1,5
      count=5
  if(i==1 and j==1):
    l[i][j]="s1s"
    l[4][4]="slt$"
    i,j=4,4
    count=2
  if(i==1 and j==4):
    l[i][j]="s2s"
    l[3][5]="s2t$"
    i,j=3,5
    count=6  
  if(i==3 and j==5):
      l[i][j]="s2t$"
  if(i==1 and j==5):
      l[i][j]="l2$"
  p,q=i,j
  display(l)
