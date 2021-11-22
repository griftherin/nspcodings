#opening balance is 1000 for every user
#languages are 'English and French
#defining functions
#storing user details as userDet to collect and hold the the card number and password.
#sampling with a dummy mastercard
'''userDet = {
"5399335622142135":"2399"
}
#adding new entries into the dictionary
cardNum, pin = input ("Enter your card number:"), input("Enter your pin:")
userDet[cardNum] = pin
print (userDet)
'''
#using embeded list instead
#for the bank admin use only; to save the user details
#userDet = []
'''
def admin():

    a = []
    a.append(input("enter the user's account number: "))
    a.append(input("enter the user's card number: "))
    a.append(input("enter the user's card pin: "))
    a.append(input("enter the user's phone number: "))
    a.append(1000)
    userDet.append(a)
    #print (userDet)
'''
'''

        else:

            auth = "deny"
            print("Incorrect PIN please try again: ")
            count + = 1

def user():
    def balCheck():
'''

custData = {'Customer1':{'name':'Mubaarak', 'accNum':'0128377908', 'cardNum':'5399211456377139','pin':'2904','balance':1000}}
kn = 1
def newUser(): #data of new customer to be entered by the admin
    name = input("Enter Customer Name: ")
    name = {'name': name}
    name['accNum'] = (input("enter the user's account number: "))
    name['cardNum'] = (input("enter the user's card number: "))
    name['pin'] = (input("enter the user's card PIN: "))
    name['phoneNum'] = (input("enter the user's phone number: "))
    print(name)
    key = kn+1
    key1 = 'Customer'+ str(key)
    custData[key1] = name
#print (custData)

#defining language and usage english and french
english = {'pinCngSuc': 'You have successfully changed your PIN, please keep it safe','newPin2Prompt':'Confirm new PIN: ','entryError': 'You have entered a wrong entry, start again','wdraw':'Enter how much to withdraw: ','lostCard': 'Is your Card Lost? Y - Yes  N - No','action': 'Choose One, A -Withdrawal B -Check Balance & C -Change PIN','havCard':'Do you have a card? Y -Yes, N -No: ','acNum':'Enter Account Number: ','sCard': 'Card has been lost or Stolen','newPinPrompt': 'Enter New Pin: ','smalMoni':'Insufficient Balance','newUV':'New user? verify with Admin','pinError': 'Incorrect PIN! Retries Remaining: ','welcome':'Welcome','entaCardNum': 'Please enter your card Number: ','entaPin': 'Please enter your PIN: ', 'balPrint': 'Your Account Balance is: ','wdlSuccess':'Congratulations! you have withdrawn: '}
french = {'pinCngSuc': 'Vous avez réussi à changer votre code PIN, veuillez le conserver en lieu sûr','newPin2Prompt':'Confirmer le nouveau code PIN: ','entryError': 'Vous avez entré une mauvaise entrée, recommencez.','wdraw':'Entrez combien retirer: ','lostCard': 'Votre carte est perdue ? O -Oui N -Non','action': 'Choisissez-en un, A -Retrait B -Vérifiez le solde et C -Modifiez le code PIN','havCard':'Avez-vous une carte? O -Oui, N -Non: ','acNum':'Entrez le numéro de compte: ','sCard': 'La carte a été perdue ou volée','newPinPrompt': 'Entrez un nouveau code PIN: ','smalMoni':'Solde insuffisant','newUV':"Nouvel utilisateur, vérifiez auprès de l'administrateur",'pinError': 'Code PIN incorrect! Tentatives restantes: ','welcome':'Bienvenu(e)','entaCardNum': 'Veuillez entrer votre numéro de carte: ','entaPin': 'Veuillez entrer votre code PIN: ', 'balPrint': 'Le solde de votre compte est: ','wdlSuccess':'Félicitations! vous avez retiré: '}
'''
lang = input("Please select your Language: \n E for English \n F for French")
if lang.capitalize()=='E':
    lang = english
elif lang.capitalize() == 'F':
    lang = french

cardNumi = input(lang['entaCardNum'])


authcust()
'''

def authcust():
    count = 0
    cardNumi = input(lang['entaCardNum'])
    # here the card is supposed to be inserted but for the sake of this program
    #the card number will be entered instead.
    #this is for a user with card

    for a in custData.values():
        if cardNumi == a['cardNum']:
            print(lang['welcome'], a['name'])
            if count < 3:
                pini = input(lang['entaPin'])
                if pini == a['pin']:
                    stat = True
                else:
                    stat = False
                    count = count + 1
                    print(lang['pinError'], 2-count )

            else:
                stat = False
                print(lang['newUV'])
                quit()


def bal():

    if stat == True:
        for a in custData.values():
            if cardNumi == a['cardNum'] or acNumi == a['accNum']:
                print(lang['balPrint'], a['balance'])


#defining the withdrawal function
def withD():
    if stat == True:
        for a in custData.values():
            if cardNumi == a['cardNum'] or acNumi == a['accNum']:
                amtToWith = int(input(lang['wdraw']))
                if (amtToWith <= a['balance']):
                    print(lang['wdlSuccess'], amtToWith,)
                    a['balance'] = a['balance'] - amtToWith
                else:
                    print(lang['smalMoni'])
                    quit()


#defining the withdraw function without card
'''
def authnoCard():
    acNum = input(lang['acNum'])
    for a in custData.values():
        if (acNum == a['accNum']):
            print(lang['welcome'], a['name'])
            if count < 3:
                pini = input(lang['entaPin'])
                if pini == a['pin']:
                    stat = True
                else:
                    stat = False
                    count = count + 1
                    print(lang['pinError'], 2 - count)
            else:
                quit()
'''
#defining pin change function

def changePin():
    if stat == True:
        for a in custData.values():
            if cardNumi == a['cardNum'] or acNumi == a['accNum']:
                newPin = input(lang['newPinPrompt'])
                newPin2 = input(lang['newPin2Prompt'])
                if newPin == newPin2:
                    a['pin'] = newPin
                    print(lang['pinCngSuc'])
                else:
                    print(lang['entryError'])
                    quit()


acNumi = ""
cardNumi = ""
stat = False
count = 0
lang = input("Please select your Language: \n E for English:  \n F for French: ")
if lang.capitalize()=='E':
    lang = english
elif lang.capitalize() == 'F':
    lang = french
# after knowing the language, the next thing is authentication
cardGet = input(lang['havCard'])
if cardGet.capitalize() == 'N':
    lost = input(lang['lostCard'])
    if lost.capitalize() == 'Y' or lost == 'O':
        # if card is lost, we want to block the card by popping the card number
        acNumi = input(lang['acNum'])
        for a in custData.values():
            if (acNumi == a['accNum']):
                # in order to verify the owner of the account before blocking the card
                pinii = input(lang['entaPin'])
                if pinii == a['pin']:
                    del (a['cardNum'])
                    quit()
                else:
                    quit()
            else:
                print (lang['newUV'])
                quit()
    elif lost.capitalize() == 'N':
        acNumi = input(lang['acNum'])
        for a in custData.values():
            if (acNumi == a['accNum']):
                print(lang['welcome'], a['name'])
                while count < 3 and stat == False:
                    pini = input(lang['entaPin'])
                    if pini == a['pin']:
                        stat = True
                    else:
                        stat = False
                        count = count + 1
                        print(lang['pinError'], 3 - count)

elif cardGet.capitalize() == 'Y' or cardGet.capitalize() == 'O':
    cardNumi = input(lang['entaCardNum'])
    for a in custData.values():
        if cardNumi == a['cardNum']:
            print(lang['welcome'], a['name'])
            while count < 3 and stat == False:
                pini = input(lang['entaPin'])
                if pini == a['pin']:
                    stat = True
                else:
                    stat = False
                    count = count + 1
                    print(lang['pinError'], 3 - count)
else:
    print(lang['entryError'])
    quit()

if stat == True:
    action = input(lang['action'])
    if action.capitalize() == 'A':
        withD()
    elif action.capitalize() == 'B':
        bal()
    elif action.capitalize() == 'C':
        changePin()
    else:
        print('entryError')
        quit()


'''    for specUser in userDet:
        if (any cardNum in specUser)
            print ("Welcome " )
            while count < 3
                pin = input("Enter your pin: ")
                (any pin in specUser):
                auth = "allow"
'''
'''
newUser()
'''
'''
    
    a.append(1000)
    userDet.append(a)
    
customer1 = {'name': 'Mubaarak', 'cardNum': '5399647896332153', 'pin': '2904', 'phoneNum': '08163861179'}
custData['name'] = customer1
print(custData['name']['name'])
'''

