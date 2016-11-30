#!/usr/bin/env python
#-*-coding: utf-8-*-



# FONKS�YON TANIMLAMA
print "*** FONKS�YON TANIMLAMA ***"
def fonkA():
    print "Ben A fonksiyonum"

fonkA() # fonksiyonu �a��ral�m

def fonkB():
    print "Ben B fonksiyonum. �imdi A fonksiyonunu �a��raca��m"

fonkB()


# parametre alan fonksiyon ald��� paramtreyi ekrana yaz�yor
def fonk2(param):
	print param

# fonksiyonu �a��ralim
fonk2("deneme parametresi bakal�m ne olacak ")

#birden fazla paramtre alan fonksiyon
def fonk3(param, param2):
	print param
	print param2
	print param+param2
        
        
#fonksiyonu �a��ral�m
fonk3("parametre 1 ","parametre 2 ")


# ekrandan metin al�p ald��� metni tekrar ekrana yazan fonksiyon
def ekranaYamaFonksiyonu():
    data =  raw_input("Ekran yaz�lacak metni girin. ��k�� i�i q yaz�n : ")
    
    if data == "q":
        print "��k�yorum ..."
        exit
    else:
        print data
        ekranaYamaFonksiyonu()

# fonksiyonu �al��t�ral�m
ekranaYamaFonksiyonu()
    
def dort_islem(param1, param2, islemkod):
	
        if islemkod=="+":
            return param1+param2
        elif islemkod == "*":
            return param1*param2
        elif islemkod == "/":
            return param1/param2
        elif islemkod == "%":
            return param1%param2
        elif islemkod == "-":
            return param1-param2
        else:
            print "��lem Kod Tan�namad� : "+islemkod

dort_islem(3, 5, "%")

# Biz ��kana kadar ekrandan i�lem yapan bir program 
def dort_islem_ekrandan():
    sayi1 = raw_input("Say� Giriniz : ")
    sayi2 = raw_input("Sayi Giriniz : ")
    islemkod = raw_input("Yap�lacak ��lem T�r�n� Giriniz (��k�� ��lemi i�in q yaz�n�z ): ")
    
    if islemkod == "q":
        print "��k�yorum ..."
        exit
    else: 
        print dort_islem(int(sayi1), int(sayi2), islemkod)
        dort_islem_ekrandan()
    

dort_islem_ekrandan()

def asalmi(asal_sayi):
    for sayi in range(2,asal_sayi):
        if(asal_sayi%sayi) == 0:
            return False
    return True

print asalmi(4)

    
def asal_sayilar(limit):
    for sayi in range(1,limit):
        if asalmi(sayi):
            print sayi


asal_sayilar(20)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
 

var1 = factorial(4)
var2 = factorial(100)

print var1
print var2

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-2)+fibonacci(n-1)

print fibonacci(5)

def pritnAllFibonacciNum(n):
    print "Fibonacci Say�lar�n� S�ral�yorum : "
    print "S�ra : "+"   De�er : "
    for sayi in range (0,n):
        print sayi,fibonacci(sayi)
        
pritnAllFibonacciNum(6)
