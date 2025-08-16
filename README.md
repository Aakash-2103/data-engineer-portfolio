🚀📊 Near Real-Time Stock Data Pipeline — API → AWS S3 → Snowflake








In today’s trading world, ⏳ speed = money.
This project demonstrates how to design and implement an end-to-end stock market data pipeline that fetches daily stock prices from the MarketStack API, processes and stores them in AWS S3, and makes them analytics-ready in Snowflake for fast BI visualizations.

🛠 Tech Stack

Extraction → MarketStack REST API (GET request, Access Key Auth) tested via Postman, automated with Python (requests, pandas)

Transformation → Python (pandas) for cleaning, deduplication, timestamp formatting

Storage → AWS S3 (secure landing zone, integrated with Snowflake via IAM Role & ARN)

Analytics → Snowflake (external stage from S3, optimized for BI queries)

⚙ Workflow
1️⃣ API Data Extraction

Tested API endpoints using Postman (GET request with access key auth)

Endpoint: http://api.marketstack.com/v1/eod

Automated with extract_market.py (reads API key from config.json)

2️⃣ Data Transformation

Script: transform.py

Steps:

Removed duplicates

Filled missing values

Converted timestamps to analytics-friendly formats

Exported as transformed_stock_data_<timestamp>.csv

3️⃣ AWS S3 Storage

Configured AWS credentials via config.json

Script: s3.py → uploads transformed CSV to S3 bucket

IAM Role created with required policies & ARN

Bucket policies attached to enable Snowflake access

4️⃣ Snowflake Integration

Created Snowflake Storage Integration linked to AWS IAM Role

Defined External Stage pointing to S3 bucket

Loaded data into MARKET_STACK table using snowflake_etl.sql

Optimized for fast BI queries, reducing query times for analysts

📂 Repository Structure
├── config.json                      # API keys & credentials (ignored in repo)
├── extract_market.py                # Fetch stock data from MarketStack API
├── transform.py                     # Clean & transform raw data
├── s3.py                            # Upload transformed data to AWS S3
├── snowflake_etl.sql                # SQL script for Snowflake stage + load
├── raw_stock_data_<timestamp>.csv   # Example raw dataset
├── transformed_stock_data_<ts>.csv  # Example transformed dataset
├── README.md                        # Project documentation
└── .DS_Store                        # (ignore, MacOS artifact)

💡 Why This Architecture?

☁ AWS S3 → Low-cost, scalable storage, easy integration with Snowflake

⚡ Snowflake External Stage → Directly queries S3 data, reducing ingestion overhead

📊 BI-Ready Data → Analysts can access clean, transformed stock data with minimal latency

📈 Business Impact

⚡ Faster Decisions → Traders access fresh daily stock data within minutes

📊 Scalability → Pipeline handles large historical + real-time datasets

💰 Cost-Efficient → Pay-as-you-go storage + Snowflake compute only when needed

📉 Reduced Query Time → Snowflake staging + optimized schema cuts BI query time significantly

🚀 How to Run Locally

Clone this repo:

git clone https://github.com/Aakash-2103/data-engineer-portfolio.git
cd data-engineer-portfolio


Install dependencies:

pip install -r requirements.txt


Create config.json (not in repo) with your credentials:

{
  "marketstack_api_key": "YOUR_API_KEY",
  "aws_access_key": "YOUR_AWS_ACCESS_KEY",
  "aws_secret_key": "YOUR_AWS_SECRET_KEY",
  "snowflake_user": "YOUR_USER",
  "snowflake_password": "YOUR_PASSWORD",
  "snowflake_account": "YOUR_ACCOUNT"
}


Run pipeline step by step:

python extract_market.py
python transform.py
python s3.py


Run Snowflake script:

-- snowflake_etl.sql
CREATE STAGE marketstack_stage URL='s3://<bucket-name>' STORAGE_INTEGRATION = my_integration;
COPY INTO MARKET_STACK FROM @marketstack_stage FILE_FORMAT = (TYPE = CSV);

📌 Future Improvements

 Automate with Airflow or AWS Lambda

 Add real-time streaming with Kafka/Kinesis

 Implement CI/CD pipeline for cloud deployment

✨ Author

👤 Aakash Sandela
🔗 LinkedIn • GitHub
