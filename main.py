import time
import winsound

sayi = int(input("Enter the number: "))

for i in range(sayi,-1,-1):
    print(i)
    time.sleep(1)

# Bu kısım döngü dışında olmalı
winsound.Beep(2500, 3000)  # 1000 Hz frekansta 1 saniye ses çalar
print("Geri sayım bitti")
















