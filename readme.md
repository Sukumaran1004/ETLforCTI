#IP Threat Analysis and Reporting System
This repository contains a Python-based system that fetches, processes, and visualizes IP threat data from two security sources: AbuseIPDB and VirusTotal. The data is merged, cleaned, and stored in a MongoDB database. The system further provides functionalities for querying and analyzing malicious IP trends over time.

Table of Contents
Installation
Requirements
Usage
Fetching Data from APIs
Data Transformation
MongoDB Integration
Visualization and Analysis
API References
License
Installation
Clone this repository:

bash
Copy code
git clone https://github.com/your-repo-name.git
Install required Python packages:

bash
Copy code
pip install -r requirements.txt
Requirements
To run the code, ensure you have the following:

Python 3.7+

MongoDB Atlas (or local MongoDB instance)

API Keys:

AbuseIPDB API Key
VirusTotal API Key
Required Python packages:

pandas
requests
json
csv
pymongo
matplotlib
seaborn
Usage
1. Fetching Data from APIs
The script collects data for a predefined list of IP addresses from two sources: AbuseIPDB and VirusTotal.

AbuseIPDB data includes details like country, abuse confidence score, ISP, and total reports.
VirusTotal provides data on detected URLs, samples, and malicious engine counts.
To fetch data, use the following functions:

python
Copy code
fetch_AbuseIPDB(api_key)   # Replace `api_key` with your AbuseIPDB API key
fetch_virustotal(api_key)  # Replace `api_key` with your VirusTotal API key
Output files:

abuseipdb.csv (AbuseIPDB data)
totalvirus.csv (VirusTotal data)
2. Data Transformation
After fetching the data, it is standardized, cleaned, and merged. The script handles IP address standardization and removes duplicates. The data is saved as Cleaned_Data.csv.

Run the following code for transformation:

python
Copy code
Tranformation(file1, file2)  # `file1` and `file2` should be paths to 'abuseipdb.csv' and 'totalvirus.csv'
3. MongoDB Integration
The cleaned data is loaded into MongoDB using the create_DB function. The data is stored in the SecurityData database and the ipAddress1 collection.

To connect and store data in MongoDB:

python
Copy code
client = MongoDb_Connect(uri)      # `uri` is your MongoDB connection URI
create_DB(client, dataPath)        # `dataPath` should be the path to `Cleaned_Data.csv`
4. Visualization and Analysis
The script provides two types of data analysis:

Top K Malicious IPs: Visualizes the top 5 IPs with the most reports.
Trend Analysis: Plots the trend of new threat reports over the past 14 days.
To perform analysis:

python
Copy code
retrieve_data(client)
This function retrieves data from MongoDB and generates the visualizations using matplotlib and seaborn.

API References
AbuseIPDB API
Base URL: https://api.abuseipdb.com/api/v2/check
Required Header: API Key
Data Provided: IP details such as country, total reports, ISP, and abuse confidence score.
VirusTotal API
Base URL: https://www.virustotal.com/vtapi/v2/ip-address/report
Required Header: API Key
Data Provided: Detected URLs, malicious samples, country, ASN, and AS owner.