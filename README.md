# EEG Kontrollü El Hareket Sistemi

Bu proje, sağ eli felçli hastaların EEG (Elektroensefalografi) beyin dinleme cihazı yardımıyla beyin sinyallerini okuyarak ellerini kontrol etmelerine olanak tanıyan yenilikçi bir sistemdir. 

## Sistem Bileşenleri

- **NeuroSky MindWave**: Beyin sinyallerini toplar.
- **Arduino Uno**: Hava pompalama mekanizmasını kontrol eder.
- **Bluetooth Modülü (HC-05 veya HC-06)**: EEG verilerini Arduino'ya iletir.
- **Hava Pompalama Mekanizması**: Parmak hareketlerini sağlar.
- **Hava Kabloları ve Eldiven**: Hava pompalama sisteminin bir parçası.

## Kurulum

### Donanım Kurulumu

1. NeuroSky MindWave cihazını başınıza yerleştirin ve bilgisayarınızla Bluetooth aracılığıyla eşleştirin.
2. Arduino'yu bilgisayarınıza bağlayın.
3. Bluetooth modülünü Arduino'ya bağlayın.
4. Pompa mekanizmasını ve solenoid valfleri Arduino'nun uygun pinlerine bağlayın.

### Yazılım Kurulumu

#### Arduino Kodu

Arduino kodunu `Arduino/eeg_control.ino` dosyasından kopyalayın ve Arduino IDE kullanarak yükleyin.

#### Python Kodu

Python kodunu `Python/eeg_control.py` dosyasından kopyalayın ve çalıştırın:

```bash
pip install -r requirements.txt
python Python/eeg_control.py
