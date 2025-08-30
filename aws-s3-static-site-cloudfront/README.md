## 🔹 Author
Mainak Banerjee – [GitHub Profile](https://github.com/mainakhetc/aws-projects/)

Project: Static Website Hosting on S3 with CloudFront

Objective: Host a personal portfolio or blog as a static website using AWS S3 and CloudFront (both free tier eligible for limited usage). No optional services with charges will be included.

Step 1: Create an S3 Bucket
Go to S3 service.
Click Create bucket.
Enter a globally unique bucket name (e.g.,  mb-static-site-08302025).
Uncheck “Block all public access” (we need the website to be public). AWS will warn you—acknowledge it.
Click Create bucket.

Step 2: Upload Website Files
Created index.html and style.css files. 
Go to your bucket → Upload → drag your files → Upload.
Once uploaded, select index.html → Properties → Object URL. This is your temporary website link

Step 3: Configure Bucket for Static Website Hosting
Go to Properties → Static website hosting → Enable.
Select Host a static website.
Enter index.html as the index document.
Save changes.

Step 4: Set Bucket Policy for Public Access
Go to Permissions → Bucket Policy → Edit.
Add the following JSON or create using AWS Policy Generator (replace mb-static-site-08302025 with your bucket name):
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mb-static-site-08302025/*"
        }
    ]
}
3. Save changes. 

Step 5: Use CloudFront for CDN
Go to CloudFront → Create Distribution → Name as “Static Site”.
Under Origin Domain, select your S3 bucket.
For Web Application Firewall (WAF), do not enable security protections.
Keep default settings and create distribution.
Copy the CloudFront domain name (e.g., d2zhcrz0ql8xli.cloudfront.net) — this will now serve your website globally with faster loading.


