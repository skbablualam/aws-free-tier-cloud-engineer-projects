# Task 01: Launch EC2 and Host Apache Web Page

## 🎯 Objective
Launch a free-tier Amazon Linux EC2 instance, install Apache using `user-data`, and serve a static "Hello from Bablu" webpage.

## 🛠️ Steps Performed

1. Created t2.micro EC2 in `us-east-1`.
2. Attached security group with HTTP (80) and SSH (22) access.
3. Added this script in user-data:
```bash
#!/bin/bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
echo "Hello from Bablu - Cloud Engineer!" > /var/www/html/index.html
```
4. Accessed the public IP in browser to view the page.

📸 Screenshot
![image](https://github.com/user-attachments/assets/2e3b9cea-5ec6-48bd-9698-073e0a2c93a5)


![image](https://github.com/user-attachments/assets/4ecadc0e-4167-490c-a007-680c68b4e339)


✅ Outcome
Successfully hosted Apache page via EC2.

