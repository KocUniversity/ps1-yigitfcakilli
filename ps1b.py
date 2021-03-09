n, B = list(map(int, input().strip().split()))
T = 0

upper_bound=10000
lower_bound=0
T=5000
temp_value=0
counter=0
flag=0
while temp_value!=T:
 series_sum=0
 counter +=1
 for i in range(1,n+1):
   if i%2==0:
    series_element=((2**i+1)**(n-i))*T
   else:
    series_element=((3**i+1)**(n-i))*T
   series_sum += series_element
 temp_value=T
 if series_sum>B:
   upper_bound=T
 else: 
   lower_bound=T
 T=(upper_bound+lower_bound)/2
 if counter==200:
    break
T=temp_value
if T%1!=0: 
  T=int((T-T%1)+1)
elif counter==200 or T==10000:
  T=-1

print(int(T))