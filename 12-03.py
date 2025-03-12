
# # half list reverse when it is odd count considering mid value
# def half_reverse(list):
#     low = len(list)//2
#     high = len(list)-1
#     while low < high:
#         list[low] , list[high] = list[high], list[low]
#         low+=1
#         high-=1
#     print(list)
# half_reverse([1,2,3,5,23,8,9,65,44])


# # half list reverse when it is odd count not considering mid value
# def half_reverse_1(list):
#     low = (len(list)//2) + 1
#     high = len(list)-1
#     while low < high:
#         list[low] , list[high] = list[high], list[low]
#         low+=1
#         high-=1
#     print(list)
# half_reverse_1([1,2,3,5,23,8,9,65,44])


# # searching using if
# def searching(list, value):
#     if value in list:
#         return "Yes"
#     return "No"
# print(searching([1,2,4,6,6,4790],7))


# # searching using for
# def searching(list, value):
#     for i in list:
#         if i == value:
#             return "Yes" 
#     return "No"
# print(searching([1,2,4,6,6,4790],1))