#!/bin/bash
module load miniforge
source activate ds2002


AMI="ami-0ec10929233384c7f"             
INSTANCE_TYPE="t2.nano"                 
INSTANCE_NAME="ds2002-sub5gd"  
KEY_NAME="key-ec2"                      
SECURITY_GROUP_ID="sg-0be6679b34372f15a" 
SUBNET_ID="subnet-085a38474f2e3b60c"     


echo "Launching EC2 instance: $INSTANCE_NAME..."

aws ec2 run-instances \
  --image-id $AMI \
  --instance-type $INSTANCE_TYPE \
  --key-name $KEY_NAME \
  --security-group-ids $SECURITY_GROUP_ID \
  --subnet-id $SUBNET_ID \
  --tag-specifications "ResourceType=instance,Tags=[{Key=Name,Value=$INSTANCE_NAME}]"

echo "Launch request sent!"