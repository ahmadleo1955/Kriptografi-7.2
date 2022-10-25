#KRIPTOGRAFI 7.2 | AHMAD LEO
k=int(input('INPUT K : '))
n=int(input('INPUT N : '))

list1=[]
i=0
if k==0:
    list1.append(1)
elif k!=0:
    while True :
      hasilpermutasi=(n-i)
      list1.append(hasilpermutasi)
      i+=1
      if ((n-i)+k)==n:
          break 

list2=[]
j=0
if k==0:
    list1.append(1)
elif k!=0:
    while True:
      hasilkombinasi=(k-j)
      list2.append(hasilkombinasi)
      j+=1
      if (k-j)==0:
          break

def hasil(data):
    r=1
    for x in data:
      r=r*x
    return r

print(f'P({n},{k})={hasil(list1)}')
print(f'C({n},{k})={hasil(list1)/hasil(list2)}')
