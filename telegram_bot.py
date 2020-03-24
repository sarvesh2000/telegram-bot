import requests
import json
from config import TELEGRAM_SEND_MESSAGE_URL

class TelegramBot:

    def __init__(self):
        """"
        Initializes an instance of the TelegramBot class.

        Attributes:
            chat_id:str: Chat ID of Telegram chat, used to identify which conversation outgoing messages should be send to.
            text:str: Text of Telegram chat
            first_name:str: First name of the user who sent the message
            last_name:str: Last name of the user who sent the message
        """

        self.chat_id = '-1001403080681'
        self.text = None
        self.first_name = None
        self.last_name = None
        self.inline_keyboard = '{"inline_keyboard": [[{"text":"Yes", "callback_data": "Yes"}],[{"text":"No", "callback_data": "No"}]]}'
        self.data = None


    def parse_webhook_data(self, data):
        """
        Parses Telegram JSON request from webhook and sets fields for conditional actions

        Args:
            data:str: JSON string of data
        """
        print(data)
        new_data = json.dumps(data)
        if('channel_post' in new_data):
            message = data['channel_post']
            self.incomming_message_text = message['text'].lower()
        if('data' in new_data):
            message = data['callback_query']
            self.data = message['data'].lower()
        if('callback_query' in new_data):
            message = data['callback_query']
            self.incomming_message_text = message['data'].lower()
        # message = data['message']

        # #self.chat_id = message['chat']['id']
        # self.incoming_message_text = message['text'].lower()
        # self.first_name = message['from']['first_name']
        # #self.last_name = message['from']['last_name']

    def action(self):
        """
        Conditional actions based on set webhook data.

        Returns:
            bool: True if the action was completed successfully else false
        """
        success = None
        if self.incomming_message_text == '/hello':
            self.outgoing_message_text = "Hello"
            success = self.send_message()
        if self.data =='yes':
            self.outgoing_message_text = "Access Granted"
            self.inline_keyboard = None
            success = self.send_message()
        if self.data == 'no':
            self.outgoing_message_text = "Access Denied"
            self.inline_keyboard = None
            success = self.send_message()
        
        return success
    
    def send_message(self):
        """
        Sends message to Telegram servers.
        """
        res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text, self.inline_keyboard))

        return True if res.status_code == 200 else False

    # def action(self):
    #     """
    #     Conditional actions based on set webhook data.

    #     Returns:
    #         bool: True if the action was completed successfully else false
    #     """

    #     success = None

    #     if self.incoming_message_text == '/hello':
    #         self.outgoing_message_text = "Hello {} !".format(self.first_name)#, self.last_name)
    #         success = self.send_message()
        
    #     if self.incoming_message_text == '/rad':
    #         self.outgoing_message_text = '🤙'
    #         success = self.send_message()
        
    #     return success


    # def send_message(self):
    #     """
    #     Sends message to Telegram servers.
    #     """

    #     res = requests.get(TELEGRAM_SEND_MESSAGE_URL.format(self.chat_id, self.outgoing_message_text))

    #     return True if res.status_code == 200 else False
    

    @staticmethod
    def init_webhook(url):
        """
        Initializes the webhook

        Args:
            url:str: Provides the telegram server with a endpoint for webhook data
        """

        requests.get(url)

