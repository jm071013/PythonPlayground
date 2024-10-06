print("Hello, Euler number!")

#n = 100000000
#m = 1.0
#m = (1 + 1/n)
#print(m)
#e = pow(m,n)

for x in range(10):
  n = x+1
  m = (1 + 1/n)
  e = pow(m,n)  
  print('For iteration %d Euler number is %f ' % (x+1, e))
