dish={
    'rice':100,
    'curry':200,
    'soup':150,
    200:'zAID'
}
print(dish.values())
print(dish.keys())
dish['salad']=300
dish['soup']=250
dish.pop('rice')
del dish[200]
print(dish.items())
