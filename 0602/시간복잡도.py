n = input()
 
def fun1(n):
    for i in range(n):
        list=[]
        if i // 3 == 0 or i // 5 ==0:
            list.append(i)
        print(sum(list))
