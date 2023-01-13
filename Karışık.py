password = input("Please enter the password")
def control():
    ı = 0
    a = 0
    b = 0
    c = 0
    d = 0
    f = 0
    g = 0
    h = 0
    total = 0
    if len(password) < 4:
        print("Password is short")
    elif len(password) > 8:
        print("Password is long")
        
    else:
        for i in password:
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
           print("Password must consist only number,letters and special characters allowed")
        else:
            for i in password:
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
                print("Must contain big letters")
            if g == 0:
                print("Must contain number") 
            if h == 0:
                print("Must contain small letters")
            if a*b*c==0:
                print("İnvalid password entered")
            else:
                print("Your password valid")
                a+=1
                b+=1
                c+=1
                d+=1
                total=(120*a*b*c*d) - 120
            if total < 2000:
              print("Your password is too weak")
            elif 2000 <= total < 4000:
                print("Weak password")
            elif 4000 <= total < 6000:
                print("Average password")
            elif 6000 <= toplam < 9000:
                print("Strong password")
            else:
                print("Too strong password")
    
        
control()
