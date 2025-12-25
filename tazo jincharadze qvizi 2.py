personage = {
     "name": 'Tony Stark',
     "age": '53',
     "city": "New-York",
     "occupation": "billionaire industrialist, CEO of Stark Industries (formerly), genius inventor, and the superhero Iron Man",
 }
print(personage)

#3
personage["hobbie"] = "engineering, building suits, and saving the world"
print(personage)

#5
def filter_dict(random_dict):
    for key, value, in random_dict.items():
        if value > 10:
            print(key, value)

filter_dict({"Python": 77, "Math": 9, })

print("pirveli cvlileba")