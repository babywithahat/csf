n = int(raw_input('value for n: '))
string = raw_input('action?: ')
if string == 'fibonacci':
  a,b = 0,1
  for i in range(1,n+1):
    c = a + b
    b = a
    a = c
  print c
elif string == 'sum':
  a = 0
  for i in range(1,n+1):
    a = a + 3*(i)
  print a
else:
  print 'Invalid String'
