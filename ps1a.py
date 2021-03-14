n, B = list(map(int, input().strip().split()))
T = 0

series_sum=0
while series_sum <=B and T<=10000:
  T += 1   
  series_sum=0
  for i in range(1,n+1):
    if i%2==0:
      series_element=((2**i+1)**(n-i))*T
    else:
      series_element=((3**i+1)**(n-i))*T
    series_sum += series_element
if T==10000:
  T=-1
  
print(T)