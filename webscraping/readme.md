## Prerequisitos en debian 9
```
apt-get install libnss3 libgconf-2-4 libx11-6
```

## Instalar chrome
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

## Descargar chromedriver compatible con chrome instalado
Buscar en google

### Instalar pip
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Instalar Selenium
```
pip install selenium
```

### Instalar request
```
pip install request
```

# Ejecutar
```
python reyno.py
```
