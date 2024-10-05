# python program to create a dictionary for country names in alphabetical order
countries = {}

country_names = input('Enter country names (with space separation) : ').split()

country_names.sort()

print(country_names)

for country in country_names:
    if country[0].upper() not in countries:
        countries[country[0].upper()] = [country.title()]
    else:
        countries[country[0].upper()].append(country.title())

print(countries)