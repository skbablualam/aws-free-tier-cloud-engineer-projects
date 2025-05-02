#!/bin/bash

cd /home/ec2-user/backend-ec2/

# Install dependencies
pip3 install -r requirements.txt

# Export environment variables (or use dotenv)
export DB_HOST=your-db-host
export DB_USER=admin
export DB_PASSWORD=yourpassword
export DB_NAME=myapp

# Kill existing process if running
pkill -f app.py

# Run app
nohup python3 app.py > app.log 2>&1 &
