
def sum_int_or_str(a, b):
    return int(a) + int(b)


assert(sum_int_or_str(1, '2')) == 3
assert(sum_int_or_str(2, 2)) == 4


def get_second_character(a):
    "get second character, if only 1 character return 0"
    if len(a) > 1:
        return a[1]

    return 0


assert(get_second_character("ab")) == "b"
assert(get_second_character("a")) == 0


car = {
    'brand': 'Toyota',
    'year': 2022
}


assert(car['brand']) == 'Toyota'

cars = [
    {
        'brand': 'Toyota'
    },
    {
        'brand': "Honda",
        'products': [
            'civic'
        ]
    }
]

assert(cars[1]['products'][0]) == 'civic'

raw_cars = 'toyota,honda,indiacar'

assert(raw_cars.split(',')) == [
    'toyota', 'honda', 'indiacar']  # turn raw_cars into a list


raw_cars = raw_cars.upper()

assert(raw_cars.split(',')) == ['TOYOTA', 'HONDA', 'INDIACAR']

raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'
# Step 1 Split
# Step 2 Casting to set, return {''}
# Step 3 Casting back to list, ['']

raw_cars = ['toyota', 'honda', 'indiacar']


def function_a(a):
    a = a.copy()
    a.append('abc')


function_a(raw_cars)
print(raw_cars)

a = 3

if (a + 2) == 2 or (a + 1) == 3:
    print("True")
elif a == 3:
    print("3")

if (a + 3) == 6:
    print(True)
else:
    print(False)

a = True if (a + 3) == 6 else False
print(a)

raw_cars = 'toyota,honda,indiacar,indiacar,indiacar'
raw_cars = raw_cars.split(',')
raw_cars = set(raw_cars)
raw_cars = len(raw_cars)
assert(raw_cars) == 3

"GIT"
