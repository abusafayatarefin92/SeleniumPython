file = open('writedemo.txt', 'a')
file.write('\n' + 'Some content')

file = open('writedemo.txt', 'r')
print(file.read())
file.close()
