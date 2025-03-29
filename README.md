# Firewall Tool
Python ile yazılmış basit bir firewall aracı. `python-iptables` kullanarak Linux sistemlerinde iptables kurallarını yönetir.

## Kurulum
1. Depoyu klonlayın:
2. 
   ```bash
   git clone https://github.com/zehrakolsuz/firewall.git
   cd firewall

  2. Gerekli kütüphaneleri yükleyin:
      ```bash
      pip install -r requirements.txt

 3. Script'i çalıştırın (root yetkisi gerekebilir):
 
    ```bash
      sudo python src/firewall.py 

## Kullanım
SSH trafiğini kabul etmek için:

      
      sudo python src/firewall.py 

Daha fazla örnek için examples/ klasörüne bakın.

## Gereksinimler <br>
- Python 3.x <br>
- Linux (iptables yüklü olmalı) <br>
- python-iptables kütüphanesi  <br>


## Lisans
MIT Lisansı ile lisanslanmıştır. Detaylar için LICENSE dosyasına bakın.


