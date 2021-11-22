#<grif>
# #Class is to discuss nested loops. while-true, while
'''
name = ""
while (name.lower() != "quit"):
  name = input("Enter your name (press quit when you're done):")
  if(name.lower() != "quit"):
    print ("Good Morning " + name)
print("Other codes to bomb your pc..............:P")
'''
#while loop for printing 1-10
'''
startNum = 100
endNum = 1
while (startNum >= endNum):
  print(startNum)
  startNum = startNum - 1
'''
#Lists help to store the same information for different records. [ uses square brackets ]
'''
myFriends = ["Arya", "Jon", "Ned",]
for i in myFriends:
  print(i)
print("After Jon made the mistake of going with the Dragon Mother, I do not like him again, Also Bran became the Greenseer so here is another list of my friends:")
myFriends[1] = "Bran"
for i in myFriends:
  print(i)
print ("They have begged me so I will name him fourth")
myFriends.append("Jon")
for i in myFriends:
  print(i)
'''

plus = 0
n=0
empAge = []
#for i in empAge:
while n<=2:
  a = int(input("Enter the ages of one after the other:"))
  empAge.append(a)
  plus = plus + a
  n=n+1
print(plus)
print (empAge)
#</therin>