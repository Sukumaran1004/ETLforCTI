import pandas as pd
from DatabaseDesign import MongoClient
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import seaborn as sns


def displayTopKMalicious(collection):
    top_ips = collection.aggregate([
    {
        "$group": {
            "_id": "$IP Address",
            "total_reports": {"$sum": "$Total Reports"}  # Assuming this field counts reports
        }
    },
    {
        "$sort": {"total_reports": -1}  # Sort in descending order
    },
    {
        "$limit": 5  # Limit to top 5
    }
    ])

    top_ips_df = pd.DataFrame(list(top_ips))
    # Visualizing Top 5 IPs
    plt.figure(figsize=(10, 6))
    plt.bar(top_ips_df["_id"], top_ips_df["total_reports"], color='blue')
    plt.xlabel('IP Address')
    plt.ylabel('Total Reports')
    plt.title('Top 5 Most Frequently Reported Malicious IPs')
    plt.xticks(rotation=45)
    plt.show()

def TrendDataAnalysis(collection):
    # Calculate the date range for the last week
    end_date = datetime.now()
    start_date = end_date - timedelta(days=14)

    # Query for the number of new threats reported each day
    trend_analysis = collection.find({
    "Last Reported At": {
        "$gte": start_date.isoformat(),
        "$lt": end_date.isoformat()
    }
    })

    data = []
    for doc in trend_analysis:
        # Append the date and the number of reports
        data.append({
            'date': doc['Last Reported At'],  # This will be a string
            'total_new_threats': doc.get('Total Reports', 0)  # Adjust according to your field
        })

    # Create a DataFrame
    trend_analysis_df = pd.DataFrame(data)

    # Convert 'date' column to datetime format if needed
    trend_analysis_df['date'] = pd.to_datetime(trend_analysis_df['date'].str.replace("Z", "+00:00"))

    # Group by date to get the total new threats per day
    trend_analysis_df = trend_analysis_df.groupby(trend_analysis_df['date'].dt.date).sum().reset_index()
    trend_analysis_df['date'] = pd.to_datetime(trend_analysis_df['date'])
    
    #To visualize the TrendAnalysis
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=trend_analysis_df, x='date', y='total_new_threats', marker='o')
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Number of New Threats')
    plt.title('Trend of New Threats Over the Past Week')
    plt.grid()
    plt.show()


def retrieve_data(client):
    db = client['SecurityData']
    collection = db['ipAddress']
    displayTopKMalicious(collection)
    TrendDataAnalysis(collection)


if __name__ == "__main__":
    uri = "mongodb+srv://sukumaran1004:4U9q6quOS9PhJiLS@threatsecurity.r95nm.mongodb.net/?retryWrites=true&w=majority&appName=ThreatSecurity"
    client = MongoClient(uri)
    retrieve_data(client)
