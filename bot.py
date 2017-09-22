import requests
import misc
import json
import failednormal
from time import sleep


token = misc.token
URL = 'https://api.telegram.org/bot' + token + '/'
#https://api.telegram.org/bot403246457:AAF2vL7BJGJRSHku96lmCSpZe0CCBLdBPRc/sendMessage?chat_id=72639045&text=Suck my balls

global last_update_id
last_update_id = 0

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()

def get_message():
    data = get_updates()
    last_object = data['result'][-1]
    chat_id = last_object['message']['chat']['id']
    text = last_object['message']['text']
    if last_object['message']['chat']['type'] == "group":
        group_chat_id = last_object['message']['chat']['id']
    current_update_id = last_object['update_id']

    global last_update_id
    if last_update_id != current_update_id:
        last_update_id = current_update_id
        message = {'chat_id' : chat_id,
                   'text':text
                  }
        return message
    return None


def send_message(chat_id, text='standby'):
    url = URL + 'sendMessage?chat_id={}&text={}'.format(chat_id, text)
    requests.get(url)



def main():
    article=''
    while (True):
        anwser = get_message()

        if anwser != None:
            chat_id = anwser['chat_id']
            text = anwser['text']

#            if '/stop' in text:
#                break

            if '/twitter' in text:
                send_message(chat_id, 'https://twitter.com/iltzys')

            if '/article' in text:
                send_message(chat_id, article)

            if '/chatid' in text:
                send_message(chat_id, chat_id)
        else:
            continue

        checkarticle = failednormal.article

        if checkarticle != article:
            article = checkarticle
            send_message(chat_id, article)
        sleep(3)
#    with open('updates.json', 'w') as file:
#        json.dump(d, file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main()
