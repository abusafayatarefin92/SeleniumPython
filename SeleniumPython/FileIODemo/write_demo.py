# file = open('C:\\Users\\abu.arefin\\Desktop\\git\\FileIO\\writedemo.txt', 'w')
# file.write('This is the first line')
# file.close()

# file = open('C:\\Users\\abu.arefin\\Desktop\\git\\FileIO\\write_demo_list.txt', 'w')
# list = [67,73,908,8127534,87264,405976,2654]
#
# for items in list:
#     file.write(str(items) + '\n')
#
# file.close()

file = open('C:\\Users\\abu.arefin\\Desktop\\git\\FileIO\\write_demo_list.txt', 'a')
list = [67,73,908,8127534,87264,405976,2654]

for items in list:
    file.write(str(items) + '\n')

file.close()