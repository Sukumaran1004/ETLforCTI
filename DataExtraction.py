import requests
import pandas as pd
import json
import csv
import time


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

def fetch_virustotal(api_key):
    result_file = "Data/totalvirus.csv"  # Location to store the fetched data

    # List of IP addresses to check
    ip_addresses = [
        '8.8.8.8', '1.1.1.1', '208.67.222.222', '208.67.220.220', '9.9.9.9',
        '198.51.100.1', '203.0.113.1', '185.228.168.9', '185.228.169.9', '77.88.8.1',
        '91.239.100.100', '156.154.70.1', '156.154.71.1', '80.80.80.80', '37.235.1.174',
        '37.235.1.177', '64.6.64.6', '64.6.65.6', '84.200.69.80', '84.200.70.40'
    ]

    url = 'https://www.virustotal.com/vtapi/v2/ip-address/report'
    
    # Headers for the API request
    headers = {
        'Accept': 'application/json',
        'Key': api_key
    }

    # List of CSV columns to fetch data
    csv_columns = [
        "IP Address",
        "Country",
        "ASN",
        "AS Owner",
        "Detected URLs",
        "Detected Samples",
        "Total Malicious Engines"
    ]

    # Create CSV file and write header
    with open(result_file, "w", newline='') as filecsv:
        writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
        writer.writeheader()

    # Loop through each IP address
    for ip in ip_addresses:
        parameters = {
            'apikey': api_key,  # Correct parameter for VirusTotal API
            'ip': ip
        }

        response = requests.get(url=url, headers=headers, params=parameters)

        # Check if the response is successful
        if response.status_code == 200:
            json_data = response.json()

            # Extract relevant information from the JSON response
            result = {
                "IP Address": ip,
                "Country": json_data.get("country", "N/A"),
                "ASN": json_data.get("asn", "N/A"),
                "AS Owner": json_data.get("as_owner", "N/A"),
                "Detected URLs": len(json_data.get("detected_urls", [])),
                "Detected Samples": len(json_data.get("detected_downloaded_samples", [])),
                "Total Malicious Engines": len(json_data.get("last_analysis_stats", {}).get("malicious", [])),
            }

            # Write data to CSV
            with open(result_file, "a", newline='') as filecsv:
                writer = csv.DictWriter(filecsv, fieldnames=csv_columns)
                writer.writerow(result)

        else:
            print(f"Error fetching data for IP {ip}: {response.status_code}")

        # Sleep to handle rate-limiting (adjust the time according to API limits)
        time.sleep(15)



if __name__ == '__main__':
    # fetch_AbuseIPDB('a8f31fd6dca8483d502af1f369bf357416e606c40a92f358bb012f577ddd986241bcf77c84d77549')
    fetch_virustotal('6fa38c01fc09b67fa87cd7887269d167f0fcf0802747ea296feb49bbc9e6c5dc')