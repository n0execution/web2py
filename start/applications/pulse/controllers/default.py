import requests
import json


def index():
    form=FORM(TEXTAREA(_name='pulse', requires=IS_NOT_EMPTY()), INPUT(_type='submit')).process()
    if form.accepted:
        redirect(URL('pulser',args=form.vars.pulse))
    return dict(form=form)


def pulse():
    session.m=[]
    if request.vars.sentiment:
        text = request.vars.sentiment
        text = text.split('_')
        text = ' '.join(text)
        url = 'http://text-processing.com/api/sentiment/'
        data = {'text': text}
        r = requests.post(url, data=data)
        session.m.append(r.content)
    session.m.sort()
    return text, TABLE(*[TR(v) for v in session.m]).xml()
