import json
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

client = WebClient(token="<xoxp-****-****-****-****>")    # replace your own OAuth Token(including <>)

# Initialize conversation_history's list
conversation_history = []

channel_id = "<C**********>"                                # replace channel id which you want to get conversations(including <>)

try:
    result_conversations_history = client.conversations_history(channel=channel_id)

    conversation_history = result_conversations_history["messages"]

    conversation_history_js = json.dumps(conversation_history, indent=2)

    print(type(conversation_history_js))    #class 'str'

    hoge = json.loads(conversation_history_js)

    poyo = [0] * 10
    #print(type(hoge))                   #class 'list'
    message_num = 0

    for i in range(10):
        print(hoge[i]['text'])
        poyo[i] = hoge[i]['text']
        if poyo[i] == "リマインダー" or poyo[i] == "ﾘﾏｲﾝﾀﾞｰ" or poyo[i] == "りまいんだー" or poyo[i] == "reminder" or poyo[i] == "REMINDER" or poyo[i] == "Reminder" or poyo[i] == "りまいんだぁ":
            message_num = i
            print("cognitive--------------------------->")
            break
        elif poyo[i] == "キャンセル" or poyo[i] == "ｷｬﾝｾﾙ" or poyo[i] == "cancel" or poyo[i] == "CANCEL" or poyo[i] == "Cancel" or poyo[i] == "りまいんだぁ":
            exit(1)

    message_channel = hoge[i-1]['text']
    message_text = hoge[i-2]['text']
    message_post_at = hoge[i-3]['text']

    # todo : make motion of cancel

    #print("channel : ",hoge[i-1]['text'])
    #print("text : ",hoge[i-2]['text'])
    #print("post_at : ",hoge[i-3]['text'])

    #message_ts = hoge[i+1]['text']

    #client = WebClient(token="<xoxb-****-****-****-****>")   # change OAuth Token if you want(including <>)
    result = client.chat_scheduleMessage(
        channel=message_channel,    #<class 'str'>
        text=message_text,          #<class 'str'>
        post_at=float(message_post_at),    #<class 'float'>
    )

    result = client.chat_postMessage(
        channel=channel_id,
        text="リマインダーを受け付けました。ご利用ありがとうございました。:love_letter:"
    )


    #print(json.dumps(conversation_history, indent=2))


except SlackApiError as e:
    print("error!!!")
