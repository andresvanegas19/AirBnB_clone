#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static

if ! which nginex;
then
  apt update && apt-get install -y nginx
fi

mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
rm -rf /data/web_static/current
echo "test Nginx configuration" > /data/web_static/releases/test/index.html
ln -s /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
location="\\n\tlocation \/hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"
sed -i "40i\ $location" /etc/nginx/sites-available/default
sudo /etc/init.d/nginx start
