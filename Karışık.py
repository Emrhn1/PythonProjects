sifre = input("şifreyi giriniz:")
def kontrol():
    ı = 0
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0
    g = 0
    h = 0
    toplam = 0
    if len(sifre) < 4:
        print("şifre kısadır")
    elif len(sifre) > 8:
        print("şifre büyüktür")
        
    else:
        for i in sifre:
            if 0< ord(i) <40:
                ı = 1
            elif 46 < ord(i) < 48:
                ı = 1
            elif 57 < ord(i) < 65:
                ı = 1
            elif 90 < ord(i) < 97:
                ı = 1
            elif ord(i) > 122:
                ı = 1
        if ı == 1:
           print("ŞİFRE YALNIZCA SAYI, HARF VE İZİN VERİLEN ÖZEL KARAKTERLERDEN OLUŞMALI")
        else:
            for i in sifre:
                if 64 < ord(i) < 91:
                    a+=1
                    f  = 1 
                if 47 < ord(i) < 58:
                    b+=1
                    g = 1
                if 96 < ord(i) < 123:
                    c+=1
                    h = 1
                if 39 < ord(i) < 47:
                    d+=1
            if f == 0:
                print("büyük harf içermelidir")
            if g == 0:
                print("rakam içermelidir") 
            if h == 0:
                print("küçük harf içermelidir")
            if a*b*c==0:
                print("geçersiz şifre girilmiştir")
            else:
                print("şifreniz geçerlidir")
                a+=1
                b+=1
                c+=1
                d+=1
                toplam=(120*a*b*c*d) - 120
            if toplam < 2000:
              print("şifreniz çok zayıftır")
            elif 2000 <= toplam < 4000:
                print("zayıf şifre")
            elif 4000 <= toplam < 6000:
                print("ortalama şifre")
            elif 6000 <= toplam < 9000:
                print("güçlü şifre")
            else:
                print("çok güçlü şifre")
    
        
kontrol()