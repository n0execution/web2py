import requests
import json


def index():
    form=FORM(TEXTAREA(_name='pulse', requires=IS_NOT_EMPTY()), INPUT(_type='submit')).process()
    if form.accepted:
        redirect(URL('pulse',args=form.vars.pulse))
    return dict(form=form)



def pulse():
    session.m=[]
    url = 'http://text-processing.com/api/sentiment/'

    #first item
    text_first = request.vars.first_item
    text_first = text_first.split('_')
    text_first = ' '.join(text_first)
    data = {'text': text_first}
    r_first = requests.post(url, data=data)
    session.m.append(r_first.content)

    #second item
    text_second = request.vars.second_item
    text_second = text_second.split('_')
    text_second = ' '.join(text_second)
    data = {'text': text_second}
    r_second = requests.post(url, data=data)
    session.m.append(r_second.content)

    session.m.sort()
    return text_first, text_second, TABLE(*[TR(v) for v in session.m]).xml()
