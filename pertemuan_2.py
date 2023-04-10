# thislist = ['apple', 'banana', 'mango']

# thislist.pop(1)

# assert(thislist) == ['apple', 'mango']  # use pop or remove

# thislist.append('kiwi')

# assert(thislist) == [
#     'apple', 'mango', 'kiwi']  # use insert or append

# new_list = ['apple', 'apple', 'apple', 'apple',
#             'mango', 'kiwi', 'apple', 'apple',
#             'apple', 'apple']  # use loop, membership 'in', and append or use range

# assert(new_list[4:6]) == ['mango', 'kiwi']

# new_list = ['apple', 'apple', 'apple', 'apple',
#             'mango', 'kiwi', 'apple', 'apple',
#             'mango', 'kiwi',
#             'apple', 'apple']  # use loop, membership 'in', and append

# new_list2 = []

# for x in new_list:
#     if x != 'apple':
#         new_list2.append(x)

# assert([x for x in new_list if x != 'apple']) == [
#     'mango', 'kiwi', 'mango', 'kiwi']

# list1 = ['mango']
# list2 = ['apple']

# list1.extend(list2)
# list1 = list1 + list2
# list1 += list2  # equal to list = list1 + list2
# print(list1)

# list1 = [1, 4, 5, 6, 2, 4]
# list1.sort(reverse=True)
# print(list1)

# list1 = [1, 4, 5, 6, 2, 4]
# list1.reverse()  #
# print(list1)

# list1 = ['apple', 'banana', 'mango']
# list1.reverse()
# print(list1)

# list1 = [1, 4, 5, 6, 2, 4]

# # [x for x in new_list if x != 'apple']
# assert([x for x in list1 if x != 4]) == [1, 5, 6, 2]

# assert([x for x in list1 if x == 4]) == [4, 4]

# list1 = [1, 4, 5, 6, 2, 4]
# list2 = list1.copy()
# list2.pop()

# print(list1, list2)

# list1 = [1, 4, 5, 7]

# list3 = list1.copy()
# list3.pop()

# assert(list3) == [1, 4, 5]
# assert(list1) == list1

# cars = {
#     'brand': 'honda',
#     'product': 'civic'
# }

# print(cars['brand'])

# print(cars.keys())

# for key in cars.keys():
#     print(cars[key])

# cars = {
#     'brand': 'honda',
#     'product': 'civic'
# }


# assert(list(cars.keys())[1]) == 'product'

# print(cars.values())

# print(cars.get('year', None))
# print('Tidak akan dijalankan')

# if 'year' in cars:
#     print(cars['year'])  # cars.get('year', None)

# cars.update(
#     {
#         'year': 2020,
#         'key2': 2121
#     }
# )
# cars['year'] = 2020
# print(cars)

# cars['brand'] = 'Toyota'
# print(cars)


# def my_function(*kids):
#     print(kids)
#     for kid in kids:
#         print(kid)


# my_function("Emil", "Tobias")


# def full_name(first_name, last_name):
#     print(first_name + " " + last_name)


# full_name(last_name="Tobias", first_name="Emil")


# def detail_people(**data):
#     print(data)


# detail_people(nama_depan="Emil",
#               nama_belakang="Tobias",
#               status="Bekerja")

# detail_people(nama_depan="Emil",
#               nama_belakang="Tobias",
#               umur=20)


# def upper_case_country(country="Norway"):
#     print(country.upper())


# upper_case_country("Swiss")


# def multiply_by_two(a):
#     return a * 2


# assert(multiply_by_two(3)) == 6


# def multiply_by_x(a, x=2):
#     "If x not passed, then define the default value to 2"
#     return a * x


# assert(multiply_by_x(3)) == 6
# assert(multiply_by_x(3, 1)) == 3

# user_input = input('input dikali dengan 2: ')
# print(multiply_by_two(int(user_input)))

# how_many_input = input("Berapa kali ingin input data? ")
# i = 0
# while i < int(how_many_input):
#     user_input = input('input dikali dengan 2: ')
#     print(multiply_by_two(int(user_input)))
#     i += 1

# how_many_input = input("Berapa kali ingin input data? ")
# i = 0
# while True:

#     if i == 0:
#         break

#     user_input = input('input dikali dengan 2: ')
#     print(multiply_by_two(int(user_input)))
#     i += 1

# """
# Enter the number of students in your class: 3
# Enter the name of student : Emil
# Enter the grades of student  (comma-separated): 85,90,92
# Enter the name of student : Tobiaz
# Enter the grades of student  (comma-separated): 78,80,84
# Enter the name of student : Refsnes
# Enter the grades of student (comma-separated): 92,95,98

# Average grades:
# Emil: 89.0
# Tobiaz: 80.67
# Refsnes: 95.0
# """


how_many_input = input("Enter the number of students in your class: ")

students = []

for i in range(int(how_many_input)):
    name = input('Enter the name of student: ')
    grade = input('Enter the grades of student  (comma-separated): ')
    students.append(
        {
            'nama': name,
            'grade': grade,
            'average_grade': totalGrades(grades)
        }
    )

print(students)
