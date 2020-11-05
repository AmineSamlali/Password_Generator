f = open('My_Password_log.txt','w+')
list = ['amine','ali','ali','moha']
for word in list:
    f.write(f'{word}\n')

f.close()