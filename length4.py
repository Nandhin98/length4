  a=list(input())
  b=permutations(a)
  c=[]
 for i in list(b):
     k=''
     for j in i:
         k+=j
     if k not in c:
         c.append(k)
         print(k)
