import pandas as pd
import ipaddress
from datetime import datetime

def standardize_ip(ip):
    try:
        # Validate and return IP address in standard format
        return str(ipaddress.ip_address(ip))
    except ValueError:
        return None  # Return None for invalid IPs

def Tranformation(file1,file2):
    # Load data from CSV files
    abuseipdb_data = pd.read_csv(file1)
    totalvirus_data = pd.read_csv(file2)

    # Remove duplicates based on IP Address
    abuseipdb_data.drop_duplicates(subset='ipAddress', inplace=True)
    totalvirus_data.drop_duplicates(subset='IP Address', inplace=True)

    # Standardize IP addresses
    abuseipdb_data['ipAddress'] = abuseipdb_data['ipAddress'].str.lower().apply(standardize_ip)
    totalvirus_data['IP Address'] = totalvirus_data['IP Address'].str.lower().apply(standardize_ip)

    #standardize the datetime
    abuseipdb_data['lastReportedAt'] = pd.to_datetime(abuseipdb_data['lastReportedAt'], errors='coerce')

    # Drop rows with invalid IP addresses
    abuseipdb_data.dropna(subset=['ipAddress'], inplace=True)
    totalvirus_data.dropna(subset=['IP Address'], inplace=True)

    # Rename columns for consistency
    abuseipdb_data.rename(columns={
        'ipAddress': 'IP Address',
        'isPublic': 'Is Public',
        'ipVersion': 'IP Version',
        'isWhitelisted': 'Is Whitelisted',
        'abuseConfidenceScore': 'Abuse Confidence Score',
        'countryCode': 'Country Code',
        'usageType': 'Usage Type',
        'isp': 'ISP',
        'domain': 'Domain',
        'hostnames': 'Hostnames',
        'totalReports': 'Total Reports',
        'numDistinctUsers': 'Num Distinct Users',
        'lastReportedAt': 'Last Reported At',
        'isTor': 'Is Tor'
    }, inplace=True)

    # Ensure both DataFrames have consistent column names
    totalvirus_data.rename(columns={
        'Country': 'Country',
        'ASN': 'ASN',
        'AS Owner': 'AS Owner',
        'Detected URLs': 'Detected URLs',
        'Detected Samples': 'Detected Samples',
        'Total Malicious Engines': 'Total Malicious Engines'
    }, inplace=True)
    
    # Merge DataFrames on IP Address
    merged_data = pd.merge(abuseipdb_data, totalvirus_data, on='IP Address', how='outer')
    merged_data.to_csv('Data/Cleaned_Data.csv', index=False)


if __name__ == '__main__':
    file1 = 'Data/abuseipdb.csv'
    file2 = 'Data/totalvirus.csv'
    Tranformation(file1,file2)