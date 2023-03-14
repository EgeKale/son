

liste= [4,1,2,5,7,3,27,123,66,899,6]

for item in liste:
    if type(item) == str:
        print('Sayilarin Oldugu Bir Liste Giriniz!!')
        break

else:
    liste.sort()
    a=(liste[0])
    b=(liste[-1])
    print(a+b)
