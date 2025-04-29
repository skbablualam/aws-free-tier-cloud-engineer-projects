Via AWS CLI
---
aws cloudwatch put-metric-alarm \
  --alarm-name High-CPU-Alarm \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 60 \
  --threshold 70 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=<your-instance-id> \
  --evaluation-periods 2 \
  --alarm-actions arn:aws:sns:REGION:ACCOUNT_ID:ec2-cpu-alert-topic \
  --unit Percent
---

✅ How to Create a CloudWatch Alarm via AWS Console
🧩 Step 1: Go to CloudWatch
Log in to the AWS Console.

Search for “CloudWatch” in the top search bar and open it.

📊 Step 2: Choose "Alarms"
In the left-hand menu, click on "Alarms".

Click "Create alarm" (top-right corner).

📈 Step 3: Select a Metric
Click "Select metric".

Navigate like this:
Browse > EC2 > Per-Instance Metrics

You’ll see a list of your running EC2 instances.

Check the box next to the CPUUtilization metric for your instance.

Click “Select metric” (bottom right).

⚙️ Step 4: Configure Alarm Conditions
Statistic: Average

Period: 1 minute (or 5 minutes if you want fewer checks)

Threshold type: Static

Whenever CPUUtilization is...

Greater than 70

Datapoints to Alarm:

2 out of 2 (this means two consecutive periods must exceed the threshold)

🔔 Step 5: Set Notification
Under Notification, select “In alarm” state.

Click “Create a new topic”, give it a name like ec2-cpu-alert-topic.

Enter your email address and click Create topic.

You'll receive a confirmation email — make sure to click Confirm.

📝 Step 6: Add Alarm Name and Tags
Alarm Name: High-CPU-Alarm

Add any tags if needed (optional)

✅ Step 7: Review and Create
Review all settings.

Click “Create alarm”

🧪 (Optional) Simulate CPU Spike
SSH into your EC2 instance and install a CPU load tool:

bash
Copy
Edit
sudo yum install -y stress
stress --cpu 2 --timeout 300
This will spike the CPU for 5 minutes to trigger your alarm.

🧹 Cleanup After Testing (Avoid Free Tier Limits)
After testing:

Go to CloudWatch > Alarms > Select your alarm > Actions > Delete

Go to SNS > Topics > Delete the SNS topic
