TOKEN = '1094258301:AAFtCHuBwqp4yN5GdFYl8YFqZbSWPwTyyrg'
NGROK_URL = 'https://tvs-telegram-bot.herokuapp.com'
BASE_TELEGRAM_URL = 'https://api.telegram.org/bot{}'.format(TOKEN)
LOCAL_WEBHOOK_ENDPOINT = '{}/webhook'.format(NGROK_URL)
TELEGRAM_INIT_WEBHOOK_URL = '{}/setWebhook?url={}'.format(BASE_TELEGRAM_URL, LOCAL_WEBHOOK_ENDPOINT)
TELEGRAM_SEND_MESSAGE_URL = BASE_TELEGRAM_URL + '/sendMessage?chat_id={}&text={}&reply_markup={}'