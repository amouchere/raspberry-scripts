# raspberry-scripts

## Installation du service pour le bouton shutdown. 


```shell
cd ~
git clone https://github.com/amouchere/raspberry-scripts.git

# Dépendance nécessaire pour l'utilisation des ports GPIO
sudo apt-get install -y python3-gpiozero
sudo cp ~/raspberry-scripts/shutdown-button.service /etc/systemd/system/shutdown-button.service
sudo systemctl enable shutdown-button.service
sudo systemctl start shutdown-button.service

```

## Installation d'une cron task journalière pour suivre la taille de la BDD influxdb


```shell
# Dépendances pour le shell de monitoring de la taille de la BDD
pip3 install pySerial influxdb
# installation de la cron task pour le monitoring de la taille de la BDD
crontab -l > mycron
# echo new cron into cron file
echo "* * * * * python3 /home/pi/raspberry-scripts/db-size-monitoring.py" >> mycron
# install new cron file
crontab mycron
rm mycron

```
