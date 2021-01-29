# raspberry-scripts

## Installation du service pour le bouton shutdown. 


```
cd ~
git clone https://github.com/amouchere/raspberry-scripts.git

# Dépendance nécessaire pour l'utilisation des ports GPIO
sudo apt-get install -y python3-gpiozero
sudo cp ~/raspberry-scripts/shutdown-button.service /etc/systemd/system/shutdown-button.service
sudo systemctl enable shutdown-button.service
sudo systemctl start shutdown-button.service

```
