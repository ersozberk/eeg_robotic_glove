import mindwave
import serial
import time

# NeuroSky MindWave bağlantısı
headset = mindwave.Headset('/dev/tty.MindWaveMobile-DevA')
time.sleep(2)

# Arduino bağlantısı
arduino = serial.Serial('COM3', 9600)  # Arduino'nun bağlı olduğu COM portunu kontrol edin
time.sleep(2)

def analyze_data(attention):
    if attention > 50:
        return '1'  # Hava pompala
    else:
        return '0'  # Hava pompalamayı durdur

try:
    print("Bağlantı kuruluyor...")
    headset.connect()
    time.sleep(5)
    
    if headset.status == 'connected':
        print("Bağlantı kuruldu.")
    else:
        print("Bağlantı başarısız.")
    
    while True:
        attention = headset.attention
        command = analyze_data(attention)
        arduino.write(command.encode())
        time.sleep(1)

except KeyboardInterrupt:
    print("Program durduruldu.")
    headset.disconnect()
    arduino.close()
