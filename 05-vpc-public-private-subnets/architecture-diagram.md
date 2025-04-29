🧱 What You Will Build
---
You'll manually create a custom VPC with 2 subnets:

Public Subnet (e.g., 10.0.1.0/24) → can access internet

Private Subnet (e.g., 10.0.2.0/24) → no direct internet access

Other components:

Internet Gateway (IGW) → attached to VPC

Route Tables → public has IGW, private does not

EC2 Instances → 1 in public subnet, 1 in private subnet

Security Groups to allow SSH from your IP

---

VPC (10.0.0.0/16)

Public Subnet (10.0.1.0/24)

EC2 with Public IP

Private Subnet (10.0.2.0/24)

EC2 without Public IP

Internet Gateway connected to Public Subnet only

Route table arrow showing internet access from public subnet
