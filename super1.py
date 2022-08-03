# class A:
#     def __init__(self):
#         print('Initializing: class A')
#     def sub_method(self, b):
#         print('Printing from class A:', b)
# class B(A):
#     def __init__(self):
#         print('Initializing: class B')
#         super().__init__()
#     def sub_method(self, b):
#         print('Printing from class B:', b)
#         super().sub_method(b + 1)
# class C(B):
#     def __init__(self):
#         print('Initializing: class C')
#         super().__init__()
#     def sub_method(self, b):
#         print('Printing from class C:', b)
#         super().sub_method(b + 1)
#
# c = C()
# c.sub_method(1)

for numb in range(1,5):
    if numb==2:
        pass
    else:
        print ("Present Number =  {} ".format(numb))
