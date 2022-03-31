#kullanıcının girdiği sayıların toplamı
#1.12.2020

#a1=int(input("1. sayıyı giriniz:"))
#a2=int(input("2. sayıyı giriniz:"))
#a3=int(input("3. sayıyı giriniz:"))
#a4=int(input("4. sayıyı giriniz:"))
#a5=int(input("5. sayıyı giriniz:"))

#toplam=a1+a2+a3+a4+a5
#ortalama= toplam/5

#kullanıcı 5 adet sayı girecek ise ;

#for döngüsü ile çözüm:

toplam=0
for i in range (5):
    print(i+1,". sayıyı giriniz:",end=' ')
    sayi=eval(input())
    toplam=toplam+sayi
    

print("girdiğiniz sayıların toplamı =", toplam)
print("girdiğiniz sayıların ortalaması=",toplam/5)
#print("girdiğiniz sayıların ortalaması=",ortalama)

#while döngüsü ile çözüm:
toplam=0
i=1
while  i<=5:  
   print(i,". sayıyı giriniz:",end=' ')
   sayi=eval(input())
   toplam=toplam+sayi
   i=i+1
print("girdiğiniz sayıların toplamı =", toplam)
print("girdiğiniz sayıların ortalaması=",toplam/5)


#kullanıcı 0 girene dek
#girmiş olduğu tüm sayıların toplam ve ortalaması
#(kullanıcının kaç tane sayı gireceği önceden bilinmiyor)

#while sayi==0:  sayı sıfıra eşit olduğu sürece demek 
#kullanıcıya sayı sor toplama ilave et 
print(" sıfır girene dek göngü çalışacak")
toplam=0
i=1
sayi= eval(input("1. sayı giriniz"))
while sayi != 0:                       #kullanıcının girdiği sayı 0 olmadığı sürece
       toplam=toplam+sayi
       i=i+1
       print(i,". sayı giriniz :",end='')
       sayi=eval(input())
            
            
print("girdiğiniz sayıların toplamı=" ,toplam)
if i>1:
    ortalama =toplam /(i-1)  # son girilen 0 ın ortalamaya katılmasını istemiyoruz
    print("girdiğiniz sayıların ortalaması=",ortalama)
else:
    print("hiç sayı girmediniz ortalama hesaplanamadı")  

 






