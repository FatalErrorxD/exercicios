import random

import caracteres

min=[]

for n in range (20):
    min.append(n+5)

num=int(random.choice(min))
listlet=[]
for k in range((num)):
    listlet.append(k)
numlet=int(random.choice(listlet))
senhaslet=random.choices(caracteres.alfabeto, k=numlet)
senhasnum=num-numlet

w=0
listnum=[]
while w<senhasnum:
    u=random.choice([0,1,2,3,4,5,6,7,8,9])
    listnum.append(str(u))
    w=w+1
senhaord= (senhaslet + listnum)
senha=random.sample(senhaord, k=len(senhaord))

string=''.join(senha)
print(string)