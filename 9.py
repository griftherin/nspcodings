#dictionaries
#key-value data pair
'''
dict1 = {"key1": "value1"}
print(dict1["key1"])
custData = []
customer1 = {'name':'Mubaarak','cardNum':'5399647896332153','pin':'2904','phoneNum':'08163861179'}
print(customer1['cardNum'])
custData.append(customer1)
print(custData)
'''
custData = {}
customer1 = {'name':'Mubaarak','cardNum':'5399647896332153','pin':'2904','phoneNum':'08163861179'}
custData['name'] = customer1

print(custData['name']['name'])