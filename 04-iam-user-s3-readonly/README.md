# 04 - IAM User with S3 ReadOnly Access

## Objective
Create an IAM user with a custom policy that grants **read-only access to all S3 buckets**. Then verify the access using AWS CLI.

## Files
- `policy.json` — Custom policy granting `s3:Get*` and `s3:List*` permissions
- `aws-cli-commands.txt` — Commands used to create and verify the IAM user
- `README.md` — Documentation

## Steps Performed
1. Created a custom IAM policy (`S3ReadOnlyAccessCustom`) from `policy.json`
2. Created a new IAM user: `s3readonly-user`
3. Attached the read-only policy to the user
4. Generated access keys for the IAM user
5. Configured AWS CLI with the user's credentials
6. Verified:
   - ✅ Able to list S3 buckets
   - ❌ Unable to create new buckets (as expected)

## Validation
The S3 readonly user was able to run `aws s3 ls` but **failed** when trying `aws s3 mb`, confirming correct permissions.

