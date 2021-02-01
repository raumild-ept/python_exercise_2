list1=[[2,4,5],[4,6,8],[3,6,9]]

list_of_even_num = map(lambda sumlist:sum(list(filter(lambda sublist: sublist %2== 0, sumlist))),list1)
print(sum(list_of_even_num))

# print(list1)
# print(sum(list(map(sum,list1))))
