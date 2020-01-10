# Debian / Ubuntu (Prerequisitos)
```
apt-get install python libnss3 libgconf-2-4 libx11-6
apt-get install composer git unzip
```

## Instalar chrome
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

## Descargar chromedriver compatible con el chrome instalado
Para Chrome 78 
https://chromedriver.storage.googleapis.com/78.0.3904.105/chromedriver_linux64.zip

### Instalar pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Instalar Selenium y Request
```
pip install selenium requests
```

# Ejecutar
```
python reyno.py
```
