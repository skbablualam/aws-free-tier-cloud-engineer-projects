# 📦 Lambda Snapshot Backup (EC2 EBS)

This Lambda function creates EBS snapshots of all volumes that are tagged with `Backup=True`. It's triggered daily via CloudWatch Events.

## 🛠️ How It Works

1. Lambda runs daily via a scheduled CloudWatch Event.
2. It scans for all volumes with the tag `Backup=True`.
3. Creates a snapshot with proper tagging.

---

## 🧾 Prerequisites

- EC2 volumes must be tagged with:
  - `Key: Backup`
  - `Value: True`
- IAM Role for Lambda must have:
  - `ec2:DescribeVolumes`
  - `ec2:CreateSnapshot`
  - `ec2:CreateTags`

---

## 🔄 Setup Steps

1. **Create Lambda Function**
   - Runtime: Python 3.12
   - Paste `lambda_function.py` code.
   - Assign proper IAM role.

2. **Add a Trigger**
   - Go to CloudWatch → Rules → Create rule
   - Use schedule `rate(1 day)`
   - Set target to your Lambda function.

3. **Tag Volumes**
   ```bash
   aws ec2 create-tags \
     --resources vol-xxxxxxx \
     --tags Key=Backup,Value=True

📤 Cleanup
To delete everything:

```
aws lambda delete-function --function-name snapshot-backup
aws events remove-targets --rule <rule-name> --ids "1"
aws events delete-rule --name <rule-name>
```

👨‍💻 Author
Sk Bablu Alam – Cloud Engineer | DevOps Enthusiast

---

## ✅ IAM Role Policy for Lambda

Make sure your Lambda function uses an IAM Role with this inline policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeVolumes",
        "ec2:CreateSnapshot",
        "ec2:CreateTags"
      ],
      "Resource": "*"
    }
  ]
}
