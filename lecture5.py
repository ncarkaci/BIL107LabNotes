#!/usr/bin/env python
#-*-coding: utf-8-*-


print "*** DOSYA OKUMA YAZMA ***"

# Dosyay� a�
file = open("deneme.txt","a+")

string1 = "metin 1 "
string2 = "metin 2 "
string3 = "metin 3 ve di�erleri "+string1+string2

# Dosyaya yaz
file.write(string1)
file.write(string2)
file.write(string3)
file.close() # Dosyay� kapat

# Dposyay� a�
file = open("deneme.txt","r")
print file # Size dosyan�n i�eri�ini vermez, dosyan�n durumunu verir : "<open file 'deneme.txt', mode 'r' at 0x00000000021B4150>" sonucu verir.

# Dosyan�n i�eri�ini iki �ekilde okuyabilirsiniz 
# 1. Durum
f = file.read() # Dosyay� read fonksiyonuyla oku ve bir de�i�kenen ata daha sonra o de�i�keni print et
print f+"\n"

# 2. Durum dosyay� for d�ng�s�yle oku ve her sat�r� ekrana bas
for satir in file: # Sat�r sat�r dosyay� oku
    print satir

# Dosyan�n i�indeki metinleri harf harf okumak i�in bu ikisini birle�tirelim

for satir in f:
    print satir
    
# Konsoldan veri okuyup dosyay yazal�m

data =  raw_input("L�tfen dosyay yaz�lacak metni giriniz : ")

file = open("deneme.txt","a+")

file.writelines(data)
for satir in file:
    print satir
