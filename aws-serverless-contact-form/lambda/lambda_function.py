import json
import boto3
import os

ses = boto3.client("ses", region_name="us-east-1")  # Free Tier available in this region

SENDER = os.environ["SENDER_EMAIL"]   # Verified SES sender email
RECIPIENT = os.environ["RECIPIENT_EMAIL"]  # Verified SES recipient email

def lambda_handler(event, context):
    body = json.loads(event["body"])
    name = body["name"]
    email = body["email"]
    message = body["message"]
    
    email_subject = f"New Contact Form Submission from {name}"
    email_body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"
    
    ses.send_email(
        Source=SENDER,
        Destination={"ToAddresses": [RECIPIENT]},
        Message={
            "Subject": {"Data": email_subject},
            "Body": {"Text": {"Data": email_body}}
        }
    )
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Email sent successfully"})
    }

