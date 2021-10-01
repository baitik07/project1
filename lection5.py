#   SET    МНОЖЕСТВА


# a = set()
# print(type(a))
# a = {'a', '4', 6, 9, 9, 6}
# print(a)


# a = [12, 23, 34, 45, 56, 67, 78, 89, 56, 45]
# print(a)
# s = set(a)
# a = list(s)
# print(s)



# a = set()
# a.add(4)
# print(dir(a))

#       UNION

# set1 = {1, 3, 5, 6, 6}
# set2 = {'a', 'df', 'c'}
# a = set1.union(set2)
# set1.update(set2)
# print(set1)
# print(set2)
# print(a)
# a = set1.pop()
# print(set1)
# print(a)





# set1 = {1, 3, 5, 6, 6}
# set2 = {'a', 'df', 'c', 6}
# set1.remove(1)
# set1.remove(3)
# set2.remove('a')
# print(set1, set2)
# # print(set1.intersection_update(set2))
# set1.intersection_update(set2)
# print(set1)
# print(set1.intersection(set2))

# set1 = {1, 3, 5, 6, 6}
# set2 = {'a', 'df', 'c', 6}
# print(set1.symmetric_difference(set2))

# set1 = {1, 2, 3, 6}
# set2 = {2, 3, 5}
# set2.symmetric_difference_update(set1)
# print(set2)
# print(set1.difference(set2))

# a = frozenset{1,3,5,7}


a = [[12, 3], ['a', True]]
# print(a[1][1])
for i in a:
    # print(i)
    for j in i:
        print(j)

