# our bread factory
# tests

def make_dough(ingredient_1, ingredient_2):
    ingredients = ingredient_1 + ingredient_2
    if 'wheat' in ingredients and 'water' in ingredients:
        return 'dough'
    else:
        return 'wrong ingredients'
def bake_bread(semi_product):
    if semi_product == 'dough':
        return 'bread'
    else:
        return 'not bread'

print('calling function dough with wrong ingredients, not expecting dough to be returned')
print(make_dough('cement', 'water') != 'dough')

print('calling function dough, expecting dough to be returned')
print(make_dough('wheat', 'water') == 'dough')

print('calling function dough, expecting dough to be returned')
print(make_dough('water', 'wheat') == 'dough')

print('calling function bake_bread, expecting bread to be returned')
print(bake_bread('dough') == 'bread')

print('calling function bake_bread with wrong ingredients, expecting outcome to not be bread')
print(bake_bread('cat') == 'not bread')

print('calling function bake_bread with wrong ingredients, expecting outcome not to be bread')
print(bake_bread('human bones') != 'bread')

print('---------------------------------------------------------------------------------------------')

def bread_factory(ingredient1, ingredient2):
    semi_product = make_dough(ingredient1, ingredient2)
    product = bake_bread(semi_product)
    return product

print(bread_factory('water', 'wheat') == 'bread')

print(bread_factory('cement', 'bread') != 'bread')

print(bread_factory('wheat', 'water') == 'bread')
