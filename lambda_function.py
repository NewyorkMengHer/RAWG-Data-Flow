import http.client
import json
from datetime import datetime
import boto3

def lambda_handler(event, context):
    conn = http.client.HTTPSConnection("api.rawg.io")
    api_key = "2742617ed7754ec98ad8cee4436f1bfe"
    current_date = datetime.today().strftime('%Y-%m-%d')
    conn.request("GET", f"/api/games?dates=2019-09-01,{current_date}&platforms=18,1,7&key={api_key}")
    res = conn.getresponse()
    data = res.read()

    # Parse data
    data_dict = json.loads(data.decode("utf-8"))

    # Write data_dict to S3 bucket
    s3 = boto3.resource('s3')
    s3.Bucket('valorant-esport-data-bucket').put_object(Key='rawg_games_data.json', Body=json.dumps(data_dict))

    return {
        'statusCode': 200,
        'body': json.dumps(data_dict)
    }

