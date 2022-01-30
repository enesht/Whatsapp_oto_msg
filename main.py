import pywhatkit as py
print("Zamanlı Mesaj göndericiye hoş geldiniz ")
countrycode = input("+90 Örneğindeki gibi + işaretide olucak şekilde ülke kodunu yazınız: ")
#Numarayı birleşik yazabilirsiniz
telno = input("Telefon numarasını yazın: ")
mesaj = input("Mesajda ne yazılmasını istiyorsunuz?: ")
#zamanlamayı kodun içerisinden değiştirin başka şekilde modül izin vermiyor.
py.sendwhatmsg(f"{countrycode}{telno}",mesaj,18,39,tab_close=True)
