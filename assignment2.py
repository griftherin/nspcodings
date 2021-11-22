#<grif>
'''
#a.	Accept an amount to be borrowed from the user.
loan = float(input("Enter the amount requested by the user:"))
#b.	Accept the interest rate per annum.
interest = float(input("Enter interest rate:"))
#c.	Number of years which the user would like to repay.
#the term is converted directly into months by multiplyting by 12
term = float(input("Enter the number of years (term):"))
termMon = 12*term
#d.	Print out the repayment schedule in months (of course you should convert year(s) to months).
tInterest = (loan*interest*term)/100
tPay = loan + tInterest
unitPay = tPay/termMon
#setting the display format
print("------- Loan Scheduler -------")
print("Amount borrowed:", loan)
print("Annual Interest Rate %:", interest)
print("Term (years):",)
print("Amount borrowed:", loan)
print("Total Interest Paid: N", tInterest)
print("Amount borrowed: N", loan)
print("Pmt   Amt Pd  R Bal:")
n = 0
print(n, "  ",0.00,"  ",tPay)
while (tPay >= 0):
  n=n+1
  print(n, "  ","%.2f" %unitPay,"  ","%.2f" %(tPay-unitPay))
  tPay = tPay - unitPay
'''

x = [a for a in range(1,11)]
print("X",x)
for i in range (1,11):
  s = [i*j for j in range (1,11)]
  print (i,s)

'''
amount = float(input("Please enter the amount e.g. 4560.32 for N4560.32: N"))
N1000 =amount // 1000
remaining = amount % 1000
amount = remaining
N500 = amount // 500
remaining = amount % 500
amount = remaining
N200 = amount // 200
remaining = amount % 200
amount = remaining
N100 = amount // 100
remaining = amount % 100
amount = remaining
N50 = amount // 50
remaining = amount % 50
amount = remaining
N20 = amount // 20
remaining = amount % 20
amount = remaining
N10 = amount // 10
remaining = amount % 10
amount = remaining
N5 = amount // 5
remaining = amount % 5
print("Here’s the breakdown:")
print("N1000: " + str(N1000))
print("N500: " + str(N500))
print("N200: " + str(N200))
print("N100: " + str(N100))
print("N50: " + str(N50))
print("N20: " + str(N20))
print("N10: " + str(N10))
print("N5: " + str(N5))
print("Here’s what’s remaining in Coins: N" + str(remaining))
'''
'''
#Assign a 20000 to base pay and 20 (%) to amount of tax to be taken.
basePay, taxAmount = 20000,20
#Write two calculations which will work out tax paid and pay after tax.
taxPaid = basePay*taxAmount/100
pTaxPay = basePay-taxPaid
print("After paying ", taxPaid, "The payment after tax is now:", pTaxPay)
'''
#Use if-else statements to output the message “Good job”, for A; “Pretty good”, B; “Passed”, C; “Not so good”, D; E & F “Failed”. 
'''
grade = input("Enter your grade:")
grade = grade.capitalize()
if (grade == "A"):
  echo = "Good job"
elif (grade == "B"):
  echo = "Pretty good"
elif (grade == "C"):
  echo = "Passed"
elif (grade == "D"):
  echo ="Not so good"
elif (grade == "E" or grade == "F"):
  echo = "Failed"
print(echo)
'''