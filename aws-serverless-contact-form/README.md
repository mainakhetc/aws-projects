## 🔹 Author

Mainak Banerjeee – [GitHub Profile](https://github.com/mainakhetc/aws-projects/)


Project 2: Serverless Contact Form with AWS Lambda, API Gateway, and SES

Objective: Build a serverless backend for a contact form.
Website frontend (HTML form) hosted on S3/CloudFront (you already know from Project 1).


Backend:

API Gateway → Accepts form submissions.

Lambda → Processes the request.

Amazon SES → Sends you an email notification with the form content.



Step 1: Prepare the Contact Form

Create an index.html with a simple form. 


Step 2: Create a Lambda Function

Go to AWS Lambda → Create function.

Name: contactFormHandler.

Runtime: Python 3.13

Create the lambda_function python file.

Set Configurations → Environment Variables → Edit:

SENDER_EMAIL → Your verified SES sender email.

RECIPIENT_EMAIL → Your verified SES recipient email.


Step 3: Verify Emails in Amazon SES

Go to SES (Simple Email Service) → Verified Identities.

Verify sender email and recipient email (both must be verified if SES is in sandbox mode).

Once verified, SES can send emails.


Step 4: Create API Gateway Endpoint

Go to API Gateway → Create API → HTTP API.

Add API Name - Contactless-form.

Add Integration - Select Lambda -> Select the Lambda function

Create a route with Method as Post, Resource Path as /contact & Integration target as contactFormHandler.

Integrate it with your Lambda function.

Deploy the API and copy the Invoke URL.

Replace "https://n6hlyvpqf1.execute-api.us-east-1.amazonaws.com/" in the HTML form script (index.html) with Invoke URL.


Step 5: Deploy and Test

Upload updated index.html to your S3 bucket.

Open your site → Fill out the contact form.

You should get an email from SES with the message.
