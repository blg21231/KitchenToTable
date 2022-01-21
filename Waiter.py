delivery = []

#pull user data from user_id
#order.append(user data)

requests = []
for order in orders.csv:
  if distance(order.address, waiter.address, waiter.transportation) <= waiter.maxDistance:
    requests = requests.append(order)

#show all requests to user

#get user selections
delivery = []
for dish in userselection:
  #delivery.append(selection)
  orders[orders.id == dish.id].status = matched
 
 #User review
 #if user chooses foodie:
 #foodies.stars.append(user input)
 #foodies.reviews.append(user input)
 
  #if user chooses chef:
 #chefs.stars.append(user input)
 #chefs.reviews.append(user input)
