from itertools import permutations

def solve():
    houses = range(5)
    # We create a generator and permutate inside the 5 range, because there are 5 houses.
    # So we'll be using the 0,1,2,3,4 as the positions for the houses, enabling us to code the rules very simply with equalities and distances.
    # We simply write the variable names and iterate over the permutations, while establishing ifs for every rule.
    # By the end, the next element of the generator SHOULD be the solution. 
    # We extract every variable to use in dictionaries later on.
    englishman, spaniard, ukranian, japanese, norwegian, water, milk, orange, coffee, tea, zebra, horse, snail, dog, fox = next(
            (englishman, spaniard, ukranian, japanese, norwegian, water, milk, orange, coffee, tea, zebra, horse, snail, dog, fox ) 
                    for ( red, blue, ivory, yellow, green) in permutations(houses) 
                    if abs(ivory - green) == 1 
                    for (englishman, spaniard, ukranian, japanese, norwegian) in permutations(houses) 
                    if norwegian == 0
                    if abs(norwegian - blue) == 0
                    if red == englishman
                    for (water, milk, orange, coffee, tea) in permutations(houses) 
                    if milk == 3
                    if coffee == green
                    if ukranian == tea
                    for (lucky, chester, kool, old, parliament) in permutations(houses) 
                    if japanese == parliament
                    if kool == yellow
                    if lucky == orange
                    for (zebra, horse, snail, dog, fox) in permutations(houses) 
                     if spaniard == dog
                     if snail == old
                     if chester - fox == 1
                     if abs(kool - horse) == 1)
    # Here, we simply create dictionaries to allow our return to be textual and clear to the user, assigning the variable to its name.
    people = {'Englishman': englishman, 'Spaniard': spaniard, 'Ukranian': ukranian, 'Japanese': japanese, 'Norwegian': norwegian}
    drinks = {'Water': water, 'Orange Juice': orange, 'Milk': milk, 'Coffee': coffee, 'Tea': tea}
    pets = {'Zebra': zebra, 'Snail': snail, 'Dog': dog,  'Horse': horse, 'Fox': fox}

    return people, drinks, pets
   
def drinks_water():
    people, drinks, pets = solve() # Extract the dictionaries
    water_drinker = drinks.get('Water') # Get the desired item
    return {v: k for k, v in people.items()}.get(water_drinker) # Reverse the people dictionary to use the position of the house with the item and get the person.

def owns_zebra():
    people, drinks, pets = solve() # Extract the dictionaries
    zebra_owner = pets.get('Zebra') # Get the desired item
    return {v: k for k, v in people.items()}.get(zebra_owner) # Reverse the people dictionary to use the position of the house with the item and get the person.
