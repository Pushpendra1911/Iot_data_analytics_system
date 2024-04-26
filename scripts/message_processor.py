from pymongo import MongoClient
from datetime import datetime
import logging

# MongoDB configuration
client = MongoClient('mongodb://localhost:27017/')
db = client['iot_database']
collection = db['iot_collection']

def process_message(message):
    try:
        # Add timestamp to the message
        message['timestamp'] = datetime.now()

        # Insert the message into MongoDB
        result = collection.insert_one(message)
        logging.info(f"Message inserted with ID: {result.inserted_id}")
    except Exception as e:
        logging.error(f"Error processing message: {e}")
