# Task 02: Attach EBS Volume to EC2

## 🎯 Objective
Create and attach a new EBS volume to a running EC2 instance, format it, mount it, and make it persist after reboot.

## 🛠️ Steps Performed

1. Created 8 GiB EBS Volume in same AZ as EC2.
2. Attached Volume to EC2 instance as `/dev/sdf`.
3. Connected to EC2 via SSH.
4. Formatted Volume using ext4 filesystem.
5. Mounted Volume at `/mnt/data`.
6. Edited `/etc/fstab` to make mount persistent.
7. Rebooted EC2 and verified persistent mount.

## 📸 Screenshots

- Volume Created
- ![image](https://github.com/user-attachments/assets/2ee499ff-d041-4e05-a6df-60a35fbd7edb)

- Volume Attached
- ![image](https://github.com/user-attachments/assets/b18cff39-f2d3-48d0-8f86-4cc4661f92ee)

- Disk List `lsblk`
- ![image](https://github.com/user-attachments/assets/7e2f8e6a-5785-49b3-af03-96d58d94ca2d)

- After Formatting
- ![image](https://github.com/user-attachments/assets/2bb3a975-f7a8-4ac0-8184-612cc2a1a5af)

- After Mounting
- ![image](https://github.com/user-attachments/assets/6801e199-7a3f-4e5b-af63-14dd3def419a)

- Edited `/etc/fstab`
- ![image](https://github.com/user-attachments/assets/d59b66dd-c35a-4b24-9065-26c7dec812fa)

- After Reboot Mount Verified

## ✅ Outcome
Successfully attached and mounted EBS Volume to EC2 instance with persistence after reboot.

## 🧠 Skills Practiced
- Elastic Block Store (EBS) management
- Linux filesystem management
- Mount persistence setup
