database = 'Ron:black tea,Luna:peppermint,Neville:green tea,Neville:black tea,Hermione:lemon & ginger,Neville:espresso,Ron:peppermint,Neville:peppermint,Luna:espresso,Luna:espresso,Luna:mocha,Ron:black tea,Ron:mocha,Harry:long black,Neville:green tea,Hermione:green tea,Ron:hot water,Harry:espresso,Luna:lemon & ginger,Ron:green tea,Neville:hot water,Harry:lemon & ginger,Ron:mocha,Hermione:lemon & ginger,Luna:hot water,Luna:lemon & ginger,Harry:peppermint,Hermione:lemon & ginger,Neville:peppermint,Ron:lemon & ginger,Neville:flat white,Ron:peppermint,Neville:flat white,Ron:black tea,Neville:black tea,Neville:lemon & ginger,Luna:mocha,Harry:peppermint,Hermione:hot water,Harry:espresso,Ron:long black,Ron:lemon & ginger,Ron:long black,Neville:green tea,Ron:peppermint,Neville:mocha,Hermione:mocha,Neville:espresso,Harry:mocha,Ron:espresso,Luna:espresso,Luna:hot water,Harry:espresso,Harry:hot water,Ron:green tea,Neville:green tea,Luna:flat white,Harry:lemon & ginger,Luna:lemon & ginger,Luna:espresso,Neville:lemon & ginger,Hermione:black tea,Luna:espresso,Hermione:green tea,Harry:peppermint,Ron:peppermint,Luna:green tea,Harry:lemon & ginger,Hermione:lemon & ginger,Harry:hot water,Harry:green tea,Harry:hot water,Harry:espresso,Hermione:espresso,Luna:black tea,Neville:long black,Hermione:green tea,Neville:black tea,Hermione:long black,Ron:mocha,Luna:green tea,Hermione:espresso,Neville:mocha,Neville:mocha,Luna:peppermint,Luna:flat white,Neville:mocha,Neville:long black,Luna:black tea,Neville:green tea,Harry:peppermint,Harry:hot water,Ron:mocha,Hermione:long black,Neville:black tea,Harry:peppermint,Luna:mocha,Hermione:black tea,Luna:lemon & ginger,Luna:flat white,Neville:green tea,Luna:flat white,Luna:hot water,Harry:mocha,Ron:hot water,Luna:espresso,Harry:mocha,Harry:flat white,Hermione:flat white,Neville:green tea,Harry:flat white,Luna:green tea,Neville:long black,Harry:hot water,Hermione:flat white,Harry:flat white,Ron:espresso,Ron:flat white,Luna:green tea,Luna:flat white,Harry:green tea,Neville:peppermint,Harry:long black,Harry:green tea,Hermione:espresso'.split(',')

# initialise people & drinks dicts
people = {}
drinks = {}

# run through the database and track count of people & drinks
for i in database:
    person, drink = i.split(':', 1)
    if person not in people:
        people[person] = 1
    else:
        people[person] += 1
    if drink not in drinks:
        drinks[drink] = 1
    else:
        drinks[drink] += 1

# print results
print("The most popular drink is", (max(drinks, key=drinks.get)), "with a count of", max(drinks.values()))
print("The person who drank the most is", (max(people, key=people.get)), "with a count of", max(people.values()))

# Bonus round !
# initialise drink_type dict
drink_type = {'coffee': 0, 'tea': 0, 'other': 0}

# run through drinks dict and count as coffee, tea or other
for j in drinks.items():
    if j[0] in ['long black', 'flat white', 'espresso', 'mocha']:
        drink_type['coffee'] += j[1]
    elif j[0] in ['peppermint', 'lemon & ginger', 'green tea', 'black tea']:
        drink_type['tea'] += j[1]
    else:
        drink_type['other'] += j[1]

# print result
print("The most popular drink type is", max(drink_type), "with a count of", max(drink_type.values()))
