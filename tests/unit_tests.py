import unittest
from unittest.mock import patch
from scripts.message_processor import process_message
from scripts.mqtt_subscriber import on_message
from pymongo import MongoClient
import logging

class TestMessageProcessor(unittest.TestCase):

    @patch('message_processor.collection')
    @patch('message_processor.logging')
    def test_process_message_success(self, mock_logging, mock_collection):
        message = {'key': 'value'}
        process_message(message)
        mock_collection.insert_one.assert_called_once_with(message)
        mock_logging.info.assert_called_once()

    @patch('message_processor.collection')
    @patch('message_processor.logging')
    def test_process_message_exception(self, mock_logging, mock_collection):
        message = {'key': 'value'}
        mock_collection.insert_one.side_effect = Exception("MongoDB error")
        process_message(message)
        mock_collection.insert_one.assert_called_once_with(message)
        mock_logging.error.assert_called_once()



class TestMQTTSubscriber(unittest.TestCase):

    @patch('mqtt_subscriber.process_message')
    def test_on_message(self, mock_process_message):
        payload = b'{"key": "value"}'
        message = {'key': 'value'}
        on_message(None, None, message)
        mock_process_message.assert_called_once_with(message)

if __name__ == '__main__':
    unittest.main()
