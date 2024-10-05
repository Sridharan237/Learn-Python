# python program to find the longest and shortest meanings in a dictionary

dict1 = {
    'piece':'a portion of and object or material, produced by cutting',
    'patch':'a piece of cloth or other material used to mend or strengthen a torn or weak point',
    'area':'a region or part of a town, a country, or the world',
    'visit':'go to see and spend time with (someone)',
    'with':'having or possessing',
    'small':'less than normal'
}

print(type(dict1.keys()))
print(type(dict1.values()))

keys = list(dict1.keys())
values = list(dict1.values())
lens = [len(x) for x in values]

min_meaning = min(lens)
max_meaning = max(lens)

min_index = lens.index(min_meaning)
max_index = lens.index(max_meaning)

print('Shortest Meaning => {}:{}'.format(keys[min_index], values[min_index]))
print('Longest Meaning => {}:{}'.format(keys[max_index], values[max_index]))

