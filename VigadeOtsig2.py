import math  #другой порядок слов
print("Ruudu karakteristikud")
a=float(input('Sisesta ruudu külje pikkus => '))
S=a*3 #была лишняя звездочка
print("Ruudu pindala", round(S,2))#округляем до 2 знаков
P=4*a
print("Ruudu ümbermõõt", round(P,2))#разные ковычки 
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2)) 
print()
print("Ristküliku karakteristikud")#лишняя скобка
b=float(input("Sisesta ristküliku 1. külje pikkus => "))#тип данных
c=float(input("Sisesta ristküliku 2. külje pikkus => "))#тип данных
S=b*c
print("Ristküliku pindala", round(S,2)) #не было ковычек 
P=2*(b+c)#написала *
print("Ristküliku ümbermõõt", round(P,2))
di=math.sqrt(b**2+c**2)#не было *
print("Ristküliku diagonaal", round(di,2)) #не было скобки
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus =>'))#тип данных
d=2*r #не было *
print("Ringi läbimõõt",(d,2)) #запиатя или стр
S=math.pi*r**2 #не было *
print("Ringi pindala", round(S,2)) #не было скобки
C=2*math.pi*r
print("Ringjoone pikkus", round(C,2))#округляем до 2 знаков

