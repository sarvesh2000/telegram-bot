TOKEN = '1094258301:AAFtCHuBwqp4yN5GdFYl8YFqZbSWPwTyyrg'
NGROK_URL = 'http://ec2-100-25-216-78.compute-1.amazonaws.com'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}&reply_markup={}'