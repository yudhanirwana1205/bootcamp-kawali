# import datetime
# import math
import json

# # dt_now = datetime.datetime.now()

# # print(dt_now)

# # print(dt_now.strftime('%d-%m-%Y'))


# # arr_1 = [5, 78, 2, 0]

# # assert(min(arr_1)) == 0

# # assert(max(arr_1)) == 78

# # # function 5 pangkat 5

# # assert(math.pow(5, 5)) == 3125

# x = {
#     "name": "John",
#     "age": 30
# }

# print('DICT: ', x)
# print(type(x))

# y = json.dumps(x)

# print('JSON:', y)
# print(type(y))

# """
# Send data

# dict -> convert to json(dumps) -> done

# get data

# json -> convert to dict(loads) -> done

# baru bisa manupulasi data
# """

# y = '{"name": "John", "age": 30}'  # json
# x = json.loads(y)
# print(x['age'])
# print(type(x))

# 1. Open file & Read

f = open('./json_read.txt')

json_string = f.read()

print(json_string)

# 2. loads

json_dict = json.loads(json_string)
print(json_dict)
print(type(json_dict))
print(json_dict['name'])


def dump_and_write(filename, data):
    json_string = json.dumps(data)
    f = open(filename, 'w')
    f.write(json_string)
    f.close()


users = [
    {
        'email': "smkn1kawali@sch.id",
        'password': '1234'
    },
    {
        'email': "smkn1kawaliuser@sch.id",
        'password': '1234'
    }

]

# 1. Dumps

dump_and_write('./json_write.txt', users)

users.append({
    'email': "",
    'password': ''
})

dump_and_write('./json_write.txt', users)
