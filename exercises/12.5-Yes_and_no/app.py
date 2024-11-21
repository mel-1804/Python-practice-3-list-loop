the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

def convertion_func():
    if i == 1: 
        print('wiki')
    else:
        print('woko')

new_list = list(map(convertion_func(), the_bools))
# new_list = list(map(lambda x:' wiki' if x == 1 else 'woko', the_bools))
print(new_list)


