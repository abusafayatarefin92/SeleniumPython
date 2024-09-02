# file_write = open('demofile.txt', 'a')
# file_write.write( '\n' + '2nd line')
# file_write.close()
#
# file_read = open('demofile.txt', 'r')
# print(file_read.read())
# file_read.close()

with open('demofile.txt', 'a') as file_write:
    file_write.write('\n' + 'This line is from with operation')

with open('demofile.txt', 'r') as file_read:
    print(file_read.read())