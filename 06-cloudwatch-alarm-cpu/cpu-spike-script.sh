#!/bin/bash
sudo yum install -y stress
stress --cpu 2 --timeout 300
