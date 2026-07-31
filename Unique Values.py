list=['Harry',"David","Jack", "David"]
print(set(list))

list2=[12,2,3,1,3,2,12,3]
b=set(list2)
print(b)

# Another way
# a=[1,2,3,4,3,3,2,1,2,1,1,5]
# dup_items=set()
# unique_list=[]
# for x in a:
#     if x not in dup_items:
#         unique_list.append(a)
#         dup_items.add(x)
# print(dup_items)