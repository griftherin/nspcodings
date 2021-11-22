#date = 29 October 2021
#Dr Ajayi Supo starting with how was our assignment
#to conclude data types today (hopefully)
'''
side1 = float(input("Enter the length of side 1 of the triangle:"))
side2 = float(input("Enter the length of side 2 of the triangle:"))
side3 = float(input("Enter the length of side 3 of the triangle:"))
sq1 = side1**2
sq2 = side2**2
sq3 = side3**2
if (sq1 == (sq2 +sq3) or sq2 ==(sq3+sq1) or sq3==(sq1+sq2)):
  print ("The triangle is right angled")
else:
  print ("The triangle is not right angled")
  '''
'''
for x in range (10):
    print (x)
'''
startNum = int(input("Enter the start number:"))
endNum = int(input("Enter the stopping number:"))
for n in range (startNum,endNum,1):
  if (n%2 != 0):
    print(n)