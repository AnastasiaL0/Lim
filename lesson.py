N = int (input("Длинна первого бортика: "))
M = int (input("Длинна второго бортика: "))
x = int (input("Расстояние до 1 бортика: "))
y = int (input (" Расстояние до 2 бортика: "))
a = N - x
b = M - y
if x>=(N/2) :
    print ("Коту осталось проплыть " , a )
elif y>=(M/2):
    print ("Коту осталось проплыть " , b )
elif (N/2)>x:
    print ("Осталось плыть " , x)
else:
    print ("Осталось плыть " , y)