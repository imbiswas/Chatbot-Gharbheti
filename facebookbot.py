# Python libraries that we need to import for our bot
import random,requests,json
from flask import Flask, request,redirect
from pymessenger.bot import Bot
import handler

app = Flask(__name__)
ACCESS_TOKEN = 'EAACwIMzZBpDABAEI6BOCMLSvle2w6PAF12aA1JZChV7sVW1W3FBRowTD3riFa5Isx9bXwaUi9asgedZA472kfRauAQpONQlc9ClxBpYnULvHV3yjPJKskKlWRMz36gSY8hE3KFf92fMZC2B0g7kJxz5ZCYb5RceFkfZBfpve2FskQqqyBeO3M1'
VERIFY_TOKEN = 'GHARBHETI213213'
bot = Bot(ACCESS_TOKEN)


# We will receive messages that Facebook sends our bot at this endpoint
@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        """Before allowing people to message your bot, Facebook has implemented a verify token
        that confirms all requests that your bot receives came from Facebook."""
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    # if the request was not get, it must be POST and we can just proceed with sending a message back to user
    else:
        # get whatever message a user sent the bot
        output = request.get_json()
        print(output)
        for event in output['entry']:
            # print(event)
            # payloading = event['postback']
            # for payloads in payloading:
            #     if payloads.get('postback'):
            #         fb_msg=payloads['postback'].get('payload')
            #         fb_msg=fb_msg.lower()
            #         print(fb_msg)
            #         recipient_id = payloads['sender']['id']
            #         if fb_msg=='admin':
            #             sendPassThread(recipient_id)
            messaging = event['messaging']
            # print(messaging)
            for message in messaging:
                if message.get('postback'):
                    recipient_id = message['sender']['id']
                    fb_msg=message['postback'].get('payload')
                    fb_msg=fb_msg.lower()
                    print(fb_msg)
                    if fb_msg=='admin':
                        sendPassThread(recipient_id)


                if message.get('message'):
                    # Facebook Messenger ID for user so we know where to send response back to
                    recipient_id = message['sender']['id']
                    # print(recipient_id)
                    recipient_id1=recipient_id[0:4]
                    recipient_id2=recipient_id[4:8]
                    recipient_id3=recipient_id[8:12]
                    recipient_id4=recipient_id[12:]
                    userId="FBFBFBFB-0000-1111"+"-"+recipient_id1+"-"+recipient_id2+recipient_id3+recipient_id4
                    # print(userId)
                    fb_msg=message['message'].get('text')
                    fb_msg=fb_msg.lower()
                    # print(fb_msg)
                    if fb_msg=='admin':
                        sendPassThread(recipient_id)
                    else:
                        sender=handler.chat(fb_msg,userId,"facebook","facebook","facebook")
                        receiver=sender.result()
                        if isinstance(receiver, str):
                            receiver=receiver.lower()
                            if 'sorry' in receiver:
                                send_message_button(recipient_id,receiver)

                            else:
                                send_message_text(recipient_id, receiver)

                            # if user sends us a GIF, photo,video, or any other non-text item
                            
                        else:
                            elements = []
                            for property in receiver:
                                url=property[0]
                                image=property[1]
                                ptype=property[2]
                                address=property[3]
                                description=property[4]
                                price=property[5]


                                element = {

                                'title': ptype+", "+address+" -Rs."+price,
                                "subtitle":description,
                                'buttons': [{

                                        'type': 'web_url',
                                        'title': "Get Details",
                                        'url': url

                                    }],

                                'image_url': image

                                }
                                elements.append(element)

                            if fb_msg :
                                send_message(recipient_id, elements)

                            # if user sends us a GIF, photo,video, or any other non-text item
                            if message['message'].get('attachments'):
                                response_sent_nontext = get_message()
                                send_message(recipient_id, response_sent_nontext)
                        if message['message'].get('attachments'):
                                response_sent_nontext = get_message()
                                send_message_text(recipient_id, response_sent_nontext)
    return "Message Processed"


def verify_fb_token(token_sent):
    # take token sent by facebook and verify it matches the verify token you sent
    # if they match, allow the request, else return an error
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge"),200
    return redirect("https://www.gharbheti.com", code=302)
    # return "invalid access"


# chooses a random message to send to the user
def get_message():
    sample_responses = ["Sorry, I cant read this at this moment", "I can read text only.", "I can't help you with attachments.",
                        "PLease send text instead of attachments."]
    # return selected item to the user
    return random.choice(sample_responses)


# uses PyMessenger to send response to user
def send_message(recipient_id, response):
    # sends user the generic message provided via input response parameter
    bot.send_generic_message(recipient_id, response)
    return "success"

def send_message_text(recipient_id, response):
    # sends user the text message provided via input response parameter
    bot.send_text_message(recipient_id, response)
    return "success"

def send_message_button(recipient_id, response):
    message_data = json.dumps({
        "recipient": {
            "id": recipient_id
        },
        "message": {
            "attachment": {
                "type":"template",
                "payload":{
                    "template_type":"button",
                    "text":response,
                    "buttons":[
                    {
                        "type":"postback",
                        "title":"Contact Admin",
                        "payload":"admin"
                    }
                    ]
                }
            }
        }
    })
    call_send_api(message_data)
    return "success"

def call_send_api(message_data):

    params = {
        "access_token": ACCESS_TOKEN
    }
    headers = {
        "Content-Type": "application/json"
    }
    
    requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=message_data)
    
def sendPassThread(senderId):
    params = {
        "access_token": ACCESS_TOKEN
    }

    headers = {
        "Content-Type": "application/json"
    }

    data = json.dumps({
        "recipient": {
            "id": senderId
        },

        "target_app_id":"263902037430900"
        })

    requests.post("https://graph.facebook.com/v2.6/me/pass_thread_control", params=params, headers=headers, data=data)
    


if __name__ == "__main__":
    app.run()