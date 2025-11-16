my_price_dic = {'apple' : 2.99, 'banana' : 6.99, 'oranges' : 3.94}
print(my_price_dic)
print(my_price_dic['apple'])
my_location_dic = {'apple' : 'L1', 'banana' : 'L2', 'oranges' : 'L3'}
my_master_dic = {'prices': my_price_dic, 'locations': my_location_dic}

#get apple price and location
print(f'price of banana is {my_master_dic['prices']['banana']}')
print(f'location of banana is {my_master_dic['locations']['banana']}')

#update price and location of banana
my_master_dic['prices']['banana'] = 7.99
my_master_dic['locations']['banana'] = 'L44'

print(f'price of banana is {my_master_dic['prices']['banana']}')
print(f'location of banana is {my_master_dic['locations']['banana']}')
