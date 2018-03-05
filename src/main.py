from datetime import datetime
import time

import schedule
from twilio.rest import Client as TwilioClient

import settings


twilio_client = TwilioClient(
    settings.TWILIO_ACCOUNT_SID,
    settings.TWILIO_AUTH_TOKEN
)


def send_twilio_reminder():
    # Send message
    twilio_client.messages.create(
        to=settings.RECIPIENT_PHONE_NUMBER,
        from_=settings.SENDER_PHONE_NUMBER,
        body=settings.MESSAGE
    )

    # Logging
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("{}: Sent 1 message".format(timestamp))



if __name__ == '__main__':
    schedule.every(settings.PERIOD_SECONDS).seconds.do(send_twilio_reminder)

    while True:
        schedule.run_pending()
        time.sleep(1)
