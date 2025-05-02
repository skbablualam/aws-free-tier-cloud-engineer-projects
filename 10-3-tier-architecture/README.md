# 3-Tier Web Application on AWS ☁️

This project deploys a 3-tier architecture with:
- **Frontend**: Static HTML on Amazon S3
- **Backend**: Python Flask on EC2
- **Database**: MySQL RDS

---

## 🧱 Architecture Diagram

![image](https://github.com/user-attachments/assets/072b771a-5706-4238-adc5-5240fea5f9c2)

---

## 🌐 Frontend (S3)
- Upload `index.html` to S3
- Enable Static Website Hosting
- Make bucket public (for demo)

## 🖥️ Backend (EC2)
- Flask Python App (`app.py`)
- Reads DB connection info from environment variables
- Connects to RDS to fetch current timestamp

## 🗄️ Database (RDS)
- MySQL/PostgreSQL
- Schema provided in `setup.sql`
- EC2 instance should have DB port open in SG

---

## 🔐 Security Groups

- **S3**: Public (or use CloudFront)
- **EC2**: Open HTTP (80) to the world, DB port to RDS SG
- **RDS**: Allow inbound from EC2’s SG only

## 🔁 CI/CD - GitHub Actions

- CI/CD set up using GitHub Actions
- On every `push` to `main` under `backend-ec2/`, it:
  - SSHes into EC2
  - Pulls latest code
  - Runs `deploy.sh` script

---

## 🚀 Deployment Steps

1. Launch RDS, run `setup.sql`
2. Launch EC2, configure env vars & run `app.py`
3. Upload frontend to S3
4. Test from browser

---

## 🧹 Cleanup

- Terminate EC2
- Delete RDS
- Delete S3 bucket

---

## 👨‍💻 Author

Sk Bablu Alam – Cloud Engineer

