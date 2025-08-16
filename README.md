# data-engineer-portfolio
📊 Near Real-Time Stock Data Pipeline — API → AWS S3 → Snowflake

In today’s trading world, ⏳ speed = money.
This project demonstrates how to design and implement an end-to-end stock market data pipeline that fetches fresh stock prices via REST API, processes them in Python, stores them in AWS S3, and makes them analytics-ready in Snowflake.

🛠 Tech Stack

Extraction: MarketStack REST API (Postman for testing, Python requests, pandas)

Transformation: Python (pandas) for cleaning, deduplication, timestamp formatting

Storage: AWS S3 (secure, scalable landing zone)

Analytics: Snowflake (fast queries, scalable compute, BI-ready)

⚙ Workflow

1️⃣ API Data Extraction

Tested MarketStack API endpoints in Postman

Automated Python script (extract_market.py) pulls EOD data for multiple stock symbols

2️⃣ Data Transformation

Script: transform.py

Removed duplicates, filled missing values, formatted dates, sorted for analytics

Saved clean dataset as transformed_stock_data_<timestamp>.csv

3️⃣ Load to AWS S3

Script: s3.py

Created S3 bucket & programmatically uploaded data via Boto3

4️⃣ Snowflake Integration

Created Storage Integration in Snowflake

Defined External Stage pointing to S3 bucket

Loaded staged CSV into MARKET_STACK table

📂 Repository Structure
├── extract_market.py                # Fetch stock data from MarketStack API
├── transform.py                     # Clean & transform raw data
├── s3.py                            # Upload transformed data to AWS S3
├── raw_stock_data_<timestamp>.csv   # Example raw dataset
├── transformed_stock_data_<ts>.csv  # Example transformed dataset
├── README.md                        # Project documentation
└── .DS_Store                        # (ignore, MacOS artifact)

💡 Why This Architecture?

☁ AWS S3 → Cheap, scalable, secure raw data storage

⚡ Snowflake → High-speed analytics, BI integration, and joins with other datasets

📈 Business Impact

⚡ Faster Decisions: Traders access fresh data in minutes

📊 Scalable: Handles millions of rows effortlessly

💰 Cost-Efficient: Pay only when querying/processing in Snowflake

💼 Monetization Ready: Curated datasets can be sold or integrated into premium platforms

🚀 How to Run Locally

Clone this repo:

git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>


Install dependencies:

pip install -r requirements.txt


Configure your API Key (from MarketStack) in extract_market.py

Run the pipeline step by step:

python extract_market.py
python transform.py
python s3.py


Verify Snowflake table load:

SELECT * FROM MARKET_STACK LIMIT 10;

📌 Future Improvements

 Automate pipeline with Airflow or AWS Lambda

 Implement near real-time streaming with Kafka/Kinesis

 Add CI/CD pipeline for deployment

✨ Author

👤 Aakash Sandela

LinkedIn: linkedin.com/in/aakashsandela

GitHub: github.com/Aakash-2103
