# AWS CloudWatch Alarm for EC2 CPU

## Goal
To create an automated CloudWatch alarm that triggers when EC2 CPU usage exceeds 70% for more than 2 minutes.

## Components
- CloudWatch Alarm
- SNS Topic & Email Subscription
- EC2 Instance (monitored)
- (Optional) CPU Load Generator via `stress`

## Steps
1. Created SNS topic and confirmed email subscription.
2. Attached alarm to monitor `CPUUtilization` metric.
3. Used `stress` tool to simulate a CPU spike.
4. Received alarm notification via email.

## Alarm Settings
- Threshold: 70%
- Evaluation Periods: 2
- Period: 60 seconds
- Action: SNS Email Alert

## Notes
To avoid charges, delete alarm and SNS after test.

