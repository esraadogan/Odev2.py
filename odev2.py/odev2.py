import cv2
import numpy as np

def detect_red_object(frame):
    # Giriş görüntüsünü HSV renk uzayına dönüştür
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk aralığını tanımla (düşük ve yüksek değerler)
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Belirlenen renk aralığındaki pikselleri beyaz, diğerlerini siyah yap
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Görüntü üzerindeki kırmızı renkli nesneleri bul
    result = cv2.bitwise_and(frame, frame, mask=mask)

    return result

# Kamera bağlantısını başlat
cap = cv2.VideoCapture(0)

while True:
    # Kamera görüntüsünü oku
    ret, frame = cap.read()

    # Kırmızı nesneleri tespit et
    result = detect_red_object(frame)

    # Sonucu göster
    cv2.imshow('Red Object Detection', result)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kamera bağlantısını kapat
cap.release()

# Pencereleri kapat
cv2.destroyAllWindows()
