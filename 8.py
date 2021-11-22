#Class 8
#revision with lists
'''
newList = []
newList[0] = "rain"
newList.append ("snow")
'''
'''
em = []
#append all the odd numbers between 10 and 50 into em
for i in range (10,50):
  if (i%2 != 0) and (i%5 == 0):
    em.append(i)
print (em)

state = ["abia", "Adamawa", "Akwa-ibom", "anambra", ["Bayelsa", "Bauchi", "Benue"], "Borno", "Cross-Rivers"]
state[4][1]
'''
'''
fiveLetter = []
states_1 = ["kwara", "ondo", ["ogun", "delta", "abia", "anambra", "bayelsa", "katsina", "fct", "imo", "enugu"], "rivers", ["abia", "Adamawa", "Akwa-ibom", "anambra", "Bayelsa", "Bauchi", "Benue", "Borno", "Cross-Rivers"], "plateau", "benue", "nasarawa"]
for state in states_1:
  if len(state) == 5:
    fiveLetter.append(state)
for i in states_1:
  if type(i) == list:
    for a in i:
      if len(a) == 5:
        fiveLetter.append(a)
print (fiveLetter)
'''

fiveLetter = []
states_1 = ["kwara", "ondo", ["ogun", "delta", "abia", "anambra", "bayelsa", "katsina", "fct", "imo", "enugu"], "rivers", ["abia", "Adamawa", "Akwa-ibom", "anambra", "Bayelsa", "Bauchi", "Benue", "Borno", "Cross-Rivers"], "plateau", "benue", "nasarawa"]
if states_1[1] == "kwara":
  print("yes")
for state in states_1:
  if type(state) == str and len(state) == 5:
    fiveLetter.append(state)
  elif type(state) == list:
    for a in state:
      if len(a) == 5:
        fiveLetter.append(a)
    if state[1] == "ogun":
        print (state)
print (fiveLetter)