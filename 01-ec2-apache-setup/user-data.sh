#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
echo "Hello from Bablu - Cloud Engineer!" > /var/www/html/index.html
