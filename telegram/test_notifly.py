import unittest
from unittest import mock, TestCase
import os
import tempfile
from telegram import notifly

token = ''
bot = notifly.BotHandler(token)


class NotiflyTestCase(TestCase):

    tmpfilepath = os.path.join(tempfile.gettempdir(), 'conversation.json')
    
    def setUp(self):
        with open(self.tmpfilepath, 'w+') as jsonfile:
            jsonfile.write('[]')
            
    def tearDown(self):
        if os.path.exists(self.tmpfilepath):
            os.remove(self.tmpfilepath)

    def test_receive_message_and_append_to_file(self):
        result = bot.receive_messages(self.tmpfilepath)
        
        assert len(result) == 2
        
    def test_receive_message_with_file_is_not_exist(self):
        self.tearDown()

        result = bot.receive_messages(self.tmpfilepath)
        
        assert len(result) == 2

if __name__ == '__main__':
    unittest.main()
