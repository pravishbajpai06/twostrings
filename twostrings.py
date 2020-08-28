s1=set(map(int,input().split()))
s2=set(map(int,input().split()))
if s1 & s2:
  return"YES"
else:
  return"No"
