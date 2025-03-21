#  python program to form a single sorted list by merging the two induvidual sorted lists

def merge_lists(list1, list2):
    res_list = []
    i,j = 0,0
    while (i < len(list1) ) and (j < len(list2)) :
        if(list1[i] < list2[j]):
            res_list.append(list1[i])
            i+=1
        else :
            res_list.append(list2[j])
            j+=1
    res_list.extend(list1[i:])
    res_list.extend(list2[j:])
    return res_list

print(merge_lists([1,3,5,7,9,9,9],[2,4,6,10]))
# output : [1, 2, 3, 4, 5, 6, 7, 9, 9, 9, 10]
    