# # # #tuple1 = (1, 2, 3, 4)
# # # #tuple[1] = 10
# # #
# # #
# # # cash = [100, 200, 300, 400, 500, 600, 700]
# # # rashod = 0.2
# # # #chet = 0
# # # #for i in cash:
# # # #    chet = chet + i
# # # #print(chet)
# # # #prybl = chet - (chet * rashod)
# # # #print(prybl)
# # #
# # #
# # # #def get_cash(cash_list, rashod):
# # # #    chet = 0
# # # #    for i in cash_list:
# # # #        chet = chet + i
# # # #    prybl = chet - (chet * rashod)
# # # #    return prybl
# # #
# # # #print(get_cash(cash, rashod))
# # #
# # #
# # # #args, kwargs
# # #
# # #
# # #
# # # def get(*args, **kwargs):
# # #     if args:
# # #         print(args)
# # #     if kwargs:
# # #         print(kwargs)
# # #
# # # get(1, 'a', True, a=10, b=False)
# #
# #
# # def dgg(**kwargs):
# #     count = len(kwargs)
# #     print(count)
# #     shet = 0
# #     for x in kwargs.values():
# #         shet += x
# #
# #     return shet/count
# #
# # print(dgg(mat=100, bio=95, his=89))
#
#
# dict1 = {"k":1, "h":4, "bool": True}
#
# for x, y in dict1.items():
#     print(x,y)


def get_num(*args):
    a = 0
    for i in args:
        if type(i) == int:
            a +=i
    return a

print(get_num(1, False, 2, 3, 4, 'ABC', ['a', 'v'], 7))
