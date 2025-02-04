File structure

/agri-vision-analyzer
│── /src
│   │── analyze_video.py              # Lambda: Process & analyze video from S3
│   │── generate_presigned_url.py     # Lambda: Generate pre-signed URL for upload
│
│── /static
│   │── index.html                    # Frontend UI
│
│── template.yaml                      # AWS SAM template defining resources
│── README.md                          # Documentation for deployment & usage
│── .gitignore                         # Ignore unnecessary files


🚀 Deployment Steps
1️⃣ Navigate to the Project Directory

cd agri-vision-analyzer
2️⃣ Build the Project

sam build
3️⃣ Deploy to AWS

sam deploy --guided

4️⃣ Update the Frontend with API Gateway URLs

After deployment, replace your-api-endpoint.com in with the actual API Gateway URL in your html.

5️⃣ Open index.html and Test
Run your frontend by simply opening index.html in a browser.