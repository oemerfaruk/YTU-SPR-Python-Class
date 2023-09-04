denklem = dict()
yeniDenklem = dict()

def setDenklem():
    while True:
        katsayi = int(input("Katsayıyı giriniz: "))
        us = int(input("ÜS giriniz: "))
        
        if katsayi == 0 and us == 0: break
        else: denklem[katsayi] = us

    return denklem

def turev(a):
    for j,k in a.items(): yeniDenklem[j*k] = k - 1

    return yeniDenklem

def sonuc():
    z, result = int(input("Bilinmeyen: ")), 0

    for j,k in yeniDenklem.items(): result += j * pow(z,k)

    return result


turev(setDenklem())

print("Denklem: {}\nTürevi alınmış denklem {}\nSonuç: {}".format(denklem, yeniDenklem,sonuc()))