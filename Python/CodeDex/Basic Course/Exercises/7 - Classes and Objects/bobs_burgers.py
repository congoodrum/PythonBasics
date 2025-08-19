class Restaurant:
  name = ''
  type = ''
  rating = 0.0
  delivery = False

bobs_burgers = Restaurant()
burger_king = Restaurant()
kfc = Restaurant()

bobs_burgers.name = 'Bob\'s Burgers'
bobs_burgers.category = 'American Diner'
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

burger_king.name = 'Burger King'
burger_king.category = 'Fast Food'
burger_king.rating = 4.7
burger_king.delivery = True

kfc.name = 'KFC'
kfc.category = 'Fast Food'
kfc.rating = 4.7
kfc.delivery = True

print(bobs_burgers)
print(burger_king)
print(kfc)