#Inputs

SenderName = input("What is your name?:")
Typeofitem = input("what type is your item?:")
is_Fragile = input("Is it fragile (yes/no)?:")
weight = float(input("How heavy is it in kg?"))
distance = float(input("How far is it in km?:"))
is_Express = input("Is it in hurry (yes/no)?:")
is_International = input("It is from another country(yes/no)?:")

#Calculation steps
 
base_cost = (weight * 2.50) + (distance * 0.15)
 
if weight <= 2.0 and distance <= 100 and not is_Express and not is_International:
	total = 0
elif is_International == 'yes' and is_Express == 'yes' :
	total = (base_cost * 1.40) + 50
elif weight > 30 and is_International == 'yes' and is_Express == 'yes' :
	total = (base_cost * 1.20) + 25
elif weight > 30 and distance > 1000 :
	total = base_cost + 30
else:
	total = base_cost

print()
print("MAMARKK EXPRESS")
print('Sender:', SenderName)
print('Order:', Typeofitem)
print('Fragile:', is_Fragile)
print('Weight:', weight, 'kg')
print('Distance:', distance, 'km')
print('Express:', is_Express)
print('International:', is_International)
print('Base Cost: PHP', base_cost)
print('Total: PHP', total)

