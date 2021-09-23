def len_count(data):
    print(type(data))
    count = 0
    for item in data:
        count = count+1
    return count
name = 'amit singh'
return_data = len_count(name)
print('The length of passed value is',return_data)