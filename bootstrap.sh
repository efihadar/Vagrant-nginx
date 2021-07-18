# install python3
sudo yum install -y python3
sudo yum -y install python3-pip
sudo python3 -m pip install requests

# nginx
sudo yum install epel-release -y
sudo yum -y install nginx
sudo systemctl start nginx
sudo systemctl enable nginx

# set up certificate and TLS
openssl req -new -newkey rsa -days 365 -nodes -x509 -subj "/C=IL/ST=efi/L=efi/O=efi/CN=efihadar.com" -keyout /etc/nginx/key.pem -out /etc/nginx/cert.pem

# set up nginx server
sudo mv /home/vagrant/nginx.conf /etc/nginx/nginx.conf
sudo chown root:root /etc/nginx/nginx.conf
sudo setenforce 0
sudo systemctl restart nginx

# run server.py and add it to boot startup
sudo python3 /home/vagrant/server.py
echo "@reboot sudo python3 /home/vagrant/server.py" > ~/servercron
sudo crontab ~/servercron
sudo rm ~/servercron

#Installing snap
# sudo yum install snapd
# sudo systemctl enable --now snapd.socket
# sudo ln -s /var/lib/snapd/snap /snap

#Install Certbot
# sudo snap install --classic certbot
# sudo yum install certbot-nginx
# certbot --nginx