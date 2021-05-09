import datetime
import pytz
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="<xoxp-****-****-****-****>")    #replace your own User OAuth Token(including <>)

tomorrow = datetime.date.today() + datetime.timedelta(days=1)
hogehoge = datetime.date.today()
scheduled_time = datetime.time(hour=23, minute=33)  #at least 20 minutes after
tz = pytz.timezone('Asia/Tokyo')

schedule_timestamp = datetime.datetime.combine(hogehoge, scheduled_time,).timestamp()

channel_id = "****"   # relace channel ID which you want to send message

text1 = str(datetime.datetime.now())
text1 += "--->"
text1 += str(hogehoge)
text1 += " "
text1 += str(scheduled_time)
print(text1)


try:
    result = client.chat_scheduleMessage(
        channel=channel_id,
        text=text1,
        post_at=schedule_timestamp,
    )

except SlackApiError as e:
    print("error!!")
