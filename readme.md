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


