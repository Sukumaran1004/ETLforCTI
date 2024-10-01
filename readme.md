# IP Threat Analysis and Reporting System

This repository contains a Python-based system that fetches, processes, and visualizes IP threat data from two security sources: **AbuseIPDB** and **VirusTotal**. The data is merged, cleaned, and stored in a MongoDB database. The system further provides functionalities for querying and analyzing malicious IP trends over time.

---

## Table of Contents

1. [Installation](#installation)
2. [Requirements](#requirements)
3. [Usage](#usage)
   - [Fetching Data from APIs](#fetching-data-from-apis)
   - [Data Transformation](#data-transformation)
   - [MongoDB Integration](#mongodb-integration)
   - [Visualization and Analysis](#visualization-and-analysis)
4. [API References](#api-references)
5. [License](#license)

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Sukumaran1004/ETLforCTI.git

## Requirements
    To successfully run this project, ensure you have the following:

1. Python 3.7+
2. MongoDB Atlas (or a local MongoDB instance)
3. API Keys:
    1. AbuseIPDB API Key
    2. VirusTotal API Key
4. Required Python packages:
    1. pandas
    2. requests
    3. json
    4. csv
    5. pymongo
    6. matplotlib
    7. seaborn
5. You can install all dependencies by running:
    ```bash
    pip install -r requirements.txt


# Usage
1. Fetching Data from APIs
    The script collects data for a predefined list of IP addresses from AbuseIPDB and VirusTotal. You will need your respective API keys to access their data.

    ## AbuseIPDB Data
        The fetch_AbuseIPDB function fetches abuse reports from AbuseIPDB, including details such as:
            1. Country
            2. Abuse Confidence Score
            3. ISP
            4. Total Reports
        To fetch data from AbuseIPDB:
        ```bash
            fetch_AbuseIPDB('your_abuseipdb_api_key')
    ## VirusTotal Data
        The fetch_virustotal function retrieves data on:

            1. Detected URLs
            2. Detected Malicious Samples
            3. Malicious Engines
        To fetch data from VirusTotal:
        ```bash
            fetch_virustotal('your_virustotal_api_key')
    ### Output Files
        abuseipdb.csv: Stores AbuseIPDB data.
        totalvirus.csv: Stores VirusTotal data.
2. Data Transformation
    After fetching the data, the transformation function Tranformation(file1, file2) processes, cleans, and merges the datasets. This involves:
    1. Standardizing IP addresses
    2. Removing duplicates
    3. Formatting the date fields
    The final output is saved in Cleaned_Data.csv.
        ```bash
        Tranformation('Data/abuseipdb.csv', 'Data/totalvirus.csv')
3. MongoDB Integration
Once the data is cleaned, it can be stored in a MongoDB database for further analysis. Use the provided MongoDB connection URI to connect to the database and insert data.

To connect to MongoDB:
    ```bash
    client = MongoDb_Connect('your_mongodb_uri')
To store the cleaned data in MongoDB:
    ```bash
    create_DB(client, 'Data/Cleaned_Data.csv')
4. Visualization and Analysis
    The system includes two primary visualizations:

    Top 5 Malicious IPs
    Displays the top 5 IPs with the most abuse reports:
        ```bash
            displayTopKMalicious(collection)
    Trend Analysis
    Shows the trend of new threats reported over the past 14 days:
        ```bash
        TrendDataAnalysis(collection)
Both visualizations use matplotlib and seaborn to generate charts.
