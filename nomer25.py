for n in range(1, 1000000):
  if (5*8*2**(3*n-2)+27*3**(3*n-1))%19==0:
    print("YES")
  else:
    print("NO")