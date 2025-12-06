
from unittest import case
from soupsieve import match


i=0
el=[]

with open('input.txt', 'r') as f:
    while True:
        line = f.readline().strip()
        if not line:
            break
        elements = line.split(' ')
        # print(elements)
        if str(elements[0]).isnumeric():
            el.append(list(filter(lambda x: x.isnumeric(), elements)))
            i += 1
        else:
            actions=list(filter(lambda x: x in {'+','-','*','/'}, elements))

sum = [0]*len(actions)

for j in range(len(actions)):
    for i in range(len(el)):
        match actions[j] :
            case '+':
                sum[j] += int(el[i][j]) 
            case '-':
                sum[j] -= int(el[i][j])
            case '*':
                if i == 0:
                    sum[j] = 1
                sum[j] *= int(el[i][j])
            case '/':
                if i == 0:
                    sum[j] = int(el[i][j])
                else:
                    sum[j] /= int(el[i][j])
            case _:
                raise ValueError('Unknown operation')
            
total = 0
for s in sum:
    total += s
print(f"Final sum is: {total}")