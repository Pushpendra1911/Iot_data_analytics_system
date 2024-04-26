from pymongo import MongoClient

class MongoDBConnector:
    def __init__(self, config):
        self.client = MongoClient(config['host'], config['port'])
        self.db = self.client[config['database']]
        self.collection = self.db[config['collection']]

    def insert_message(self, message):
        try:
            result = self.collection.insert_one(message)
            print(f"Message inserted with ID: {result.inserted_id}")
        except Exception as e:
            print(f"Error inserting message: {e}")

    def close_connection(self):
        self.client.close()

# Example configuration
config = {
    'host': 'localhost',
    'port': 27017,
    'database': 'iot_database',
    'collection': 'iot_collection'
}


if __name__ == "__main__":
    connector = MongoDBConnector(config)
    message = {'key': 'value'}
    connector.insert_message(message)
    connector.close_connection()
