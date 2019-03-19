from aip import AipSpeech
def Read(txt,no):
    APP_ID = '15578315'
    APP_KEY = 'FqP29Ul6uO4z1hG7S7NdzQGr'
    SECRET_KEY = 'odtw1Fy7vwI4w8XjYELDTsFrUh4XdGYB'
    client = AipSpeech(APP_ID, APP_KEY, SECRET_KEY)
    res = client.synthesis(txt,
                           'zh',
                           1,
                           {
                               'vol':5,
                               'spd':4,
                               'pit':6,
                               'per':4
                           }
                           )
    with open('GameApp/static/sounds/'+no+'.mp3','wb') as f:
        f.write(res)
