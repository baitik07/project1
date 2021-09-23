# # # # # # # #ДЕКОРАТОРЫ
# # # # # # #
# # # # # # # from datetime import datetime
# # # # # # #
# # # # # # # def time(function):
# # # # # # #     def wrapper():
# # # # # # #         start = datetime.now()
# # # # # # #         function()
# # # # # # #         end = datetime.now() - start
# # # # # # #         print(end)
# # # # # # #     return wrapper
# # # # # # #
# # # # # # # @time
# # # # # # # def function1():
# # # # # # #
# # # # # # #     lists = []
# # # # # # #     for i in range(1,10000):
# # # # # # #         lists.append(i)
# # # # # # #     return lists
# # # # # # #
# # # # # # # @time
# # # # # # # def function2():
# # # # # # #     lists = [x for x in range(1,10000)]
# # # # # # #     return lists
# # # # # # #
# # # # # # # function1()
# # # # # # # function2()
# # # # # #
# # # # # #
# # # # # #
# # # # # def humburger(cotlet):
# # # # #     def wrapper(*args, **kwargs):
# # # # #         print("Upper bread")
# # # # #         cotlet(*args, **kwargs)
# # # # #         print("Down bread")
# # # # #     return wrapper
# # # # # #
# # # # # @humburger
# # # # # def cotlet(ingridient):
# # # # #     print(f'Cotleta by {ingridient}' )
# # # # #
# # # # # cotlet("chicken")
# # # #
# # # #
# # # # lists = ['Kyal', 'Saikal', 'Meerim', 'Isko']
# # # # print(f'S-{lists[1]} M-{lists[2]}')
# # # # print("{0} {2} {1} {3}".format(lists[1], lists[3], lists[0], lists[2]))
# # #
# # #
# # # name = {
# # #         'name': 'Vika',
# # #         'age': 18+4,
# # #        }
# # # a = name.pop('name')
# # # name.update({'name': "Eldar"})
# # # print(name)
# # # #print(a)
# # import math
# #
# # print(pow(3, 2)) #возвидение в корни
# # print(math.sqrt(4))
#
#
# number = int(input("Any number for factorial function: "))
#
# def fact(s):
#     count = 1
#     for i in range(1, s+1):
#         count *= i
#     return count
# print(fact(number))



a = int(input('A side of bisictrisa: '))
b = int(input('B side of bisictrisa: '))


