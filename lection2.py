# # # # lists = []
# # # # for i in range(1,1000):
# # # #     if i % 3 == 0:
# # # #         lists.append(i)
# # # #
# # # # print(lists)
# # #
# # #
# # # lists = [x for x in range(1,100) if x % 3 == 0]
# # # print(lists)
# #
# #
# # lists = []
# # for i in range(-100, 50):
# #     if i % 3 == 0 and i % 5 == 0:
# #         ## pow(i, 3)
# #         number = abs(i**3)
# #         lists.append(number)
# # print(lists)
#
#
#
# # lists = [abs(pow(x, 3)) for x in range(-100, 50) if x % 3 == 0 and x % 5 == 0]
# # print(lists)
#
# # def filter_list(range1, range2):
# #     lists = [abs(pow(x, 3)) for x in range(range1,range2) if x % 3 == 0 and x % 5 == 0]
# #     return lists
# # list1 = filter_list(-100, 100)
# # print(list1)
#
#
# kyal = {
#     'home': '2floor',
#     'car': 'BMW x7'
# }
# saikal = {
#     'home': '3floor',
#     'car': 'Land Crouser'
# }
# eldar = {
#     'home': '6floor',
#     'car': '570 Lx'
# }
#
#
# python_boot = [eldar, saikal, kyal]
# car = [x.get('car') for x in python_boot]
# print(car)
#
#
# # python_boot = [eldar, saikal, kyal]
# # home = []
# # for i in python_boot:
# #     home.append(i.get('home'))
# #print(home)


from datetime import datetime
def function1():
    start = datetime.now()
    lists = []
    for i in range(1,10000):
        lists.append(i)
    end = datetime.now() - start
    print('Время для цикла for', end)
    return lists

def function2():
    start = datetime.now()
    lists = [x for x in range(1,10000)]
    end = datetime.now() - start
    print('Время list comprehentions', end)
    return lists

function1()
function2()
# print(datetime.now())