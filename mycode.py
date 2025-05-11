
my_lst = [1,2,3,4,5,6,7,8]

my_lst2 = [ x if x%2 else x +1 for x in my_lst] 

print(my_lst2)