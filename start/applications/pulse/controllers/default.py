import requests
import json


def index():
    form=FORM(TEXTAREA(_name='pulse', requires=IS_NOT_EMPTY()), INPUT(_type='submit')).process()
    if form.accepted:
        redirect(URL('pulser',args=form.vars.pulse))
    return dict(form=form)


def pulser():
    text = request.args(0)
    text = text.split('_')
    text = ' '.join(text)
    url = 'http://text-processing.com/api/sentiment/'
    data = {'text': text}
    r = requests.post(url, data=data)
    binary = r.content
    output = json.loads(binary)
    label = output["label"]
    return dict(text=text, label=label)
