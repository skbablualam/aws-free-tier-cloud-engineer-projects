# VPC: Public and Private Subnet Project

## Goal
To create a custom VPC with a public and private subnet using AWS. This helps understand secure network segregation for public-facing and backend components.

## Architecture
See `architecture-diagram.png`

## Components
- Custom VPC: 10.0.0.0/16
- Public Subnet: 10.0.1.0/24 (with IGW)
- Private Subnet: 10.0.2.0/24 (no IGW)
- EC2 Public: SSH and pingable from internet
- EC2 Private: Accessible only from public EC2 (via SSH)

## How to Test
1. SSH into public EC2 using key pair.
2. From public EC2, SSH into private EC2 using its private IP.

## Security
- Security Groups allow SSH only from your IP.

