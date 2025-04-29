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
- Volume Attached
- Disk List `lsblk`
- After Formatting
- After Mounting
- Edited `/etc/fstab`
- After Reboot Mount Verified

## ✅ Outcome
Successfully attached and mounted EBS Volume to EC2 instance with persistence after reboot.

## 🧠 Skills Practiced
- Elastic Block Store (EBS) management
- Linux filesystem management
- Mount persistence setup
