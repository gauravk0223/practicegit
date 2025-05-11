
my_lst = [1,2,3,4,5,6,7,8]

my_lst2 = [ x if x%2 else x +1 for x in my_lst] 

print(my_lst2)

my_lst3 = list(map( lambda x : x+2 , my_lst2))
print(my_lst3)


def add (a,b) :
    return a+b