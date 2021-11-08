import random
import array

max_len = 12

salpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
balpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num = ['1','2','3','4','5','6','7','8','9']
sym = ['_','-']

combined_list = salpha + balpha + num + sym

rand_num = random.choice(num)
rand_salpha = random.choice(salpha)
rand_balpha = random.choice(balpha)
rand_sym = random.choice(sym)

temp_pass = rand_balpha + rand_num + rand_salpha + rand_sym

for i in range (max_len -  4):
    temp_pass = temp_pass + random.choice(combined_list)

    temp_pass_list = array.array('u', temp_pass)
    random.shuffle(temp_pass_list)

passwrd = ""
for x in temp_pass_list:
    passwrd = passwrd + x

print(passwrd)
