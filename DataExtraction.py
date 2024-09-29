import requests
import pandas as pd
import json
import csv


#Function to fetch the data from AbuseIPdb
def fetch_AbuseIPDB(api_key):
    result_file = "Data/abuseipdb.csv" #location to store the fetched data
    
    #list of ip address to check
    ip_address = [
    '8.8.8.8', '1.1.1.1', '208.67.222.222', '208.67.220.220', '9.9.9.9', 
    '198.51.100.1', '203.0.113.1', '185.228.168.9', '185.228.169.9', '77.88.8.1',
    '91.239.100.100', '156.154.70.1', '156.154.71.1', '80.80.80.80', '37.235.1.174',
    '37.235.1.177', '64.6.64.6', '64.6.65.6', '84.200.69.80', '84.200.70.40'
    ]   

    url = 'https://api.abuseipdb.com/api/v2/check'
    # Headers for the API request
    headers = {
    'Accept': 'application/json',
        'Key': api_key
    }

    #list of csv columns to fetch data 
    csv_columns = ['ipAddress','isPublic','ipVersion','isWhitelisted','abuseConfidenceScore','countryCode','usageType','isp','domain','hostnames','totalReports','numDistinctUsers','lastReportedAt','isTor']
    with open(result_file,"a", newline='') as filecsv:
        writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
        writer.writeheader()

    # Loop through each IP address
    for ip in ip_address:
        parameters = {
            'ipAddress': ip,
            'maxAgeInDays': '90' #Check for reports within the last 90 days
            }

        respnse= requests.get( url=url,headers=headers,params=parameters)
        json_Data = json.loads(respnse.content)
        json_main = json_Data["data"]
        with open(result_file,"a", newline='')as filecsv: #to store the data in csv format
            writer= csv.DictWriter(filecsv,fieldnames=csv_columns)
            writer.writerow(json_main)


if __name__ == '__main__':
    fetch_AbuseIPDB('a8f31fd6dca8483d502af1f369bf357416e606c40a92f358bb012f577ddd986241bcf77c84d77549')