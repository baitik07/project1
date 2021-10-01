# k = 10/0
# print(k)


# try:
#     k = 10 / 0
# except ZeroDivisionError:
#     k = 0
# print(k)


# lists = []
# for i in range(5):
#     a = input('Type any number')
#     print(type(a))
#     lists.append(a)

# print(lists)
# print(sum(lists)/len(lists))

# def integer_list(lists):
#     result = []
#     for i in lists:
#         result.append(int(i))
#     return result
#
# lists = []
# for i in range(5):
#     a = input('Type any number: ')
#     # print(type(a))
#     lists.append(a)
# try:
#     average = sum(lists)/len(lists)
# except TypeError:
#     a = integer_list(lists)
#     average = sum(a) / len(a)
# print(average)




# try:
#     k = 10/0
# except ZeroDivisionError:
#     raise Exception("We can't divide to 0 !")


# TASK SET #4


# def diff(set1, set2, set3, request):
#     if request == 'symmetric':
#         a = set1.symmetric_difference(set2).symmetric_difference(set3)
#     elif request == 'difference':
#         a = set1.difference(set2, set3)
#     return a
# set1 = {2,3,4, 10}
# set2 = {2,5,3}
# set3 = {7,3,4}
# request = input("Type a difference or symmetric: ")
# print(diff(set1, set2, set3, request))



# set1 = {2,3,5,6,6}
# set2 = {3,4,5}
# print(set2.issuperset(set1))
