from bottle import route, run
import dataset
import time
import os


db_user = os.environ['db_user']
db_pass = os.environ['db_pass']

url = 'postgresql://%(user)s:%(pass)s@localhost:5432/dev_tracker' % {
        'user': db_user,
        'pass': db_pass
        }
db = dataset.connect(url)
table = db['tasks']

@route('/task/done/<trelloid>/<user>/<hashed>')
def task_done(trelloid, user, hashed):
    task = table.find_one(trello_id=trelloid, user=user, hashed=hashed)
    if task:
        task['done_at'] = time.time()
        table.update(task, ['id'])
    return ""

@route('/task/start/<trelloid>/<user>/<hashed>')
def task_start(trelloid, user, hashed):
    table.insert({
        "trello_id": trelloid,
        "user": user,
        "hashed": hashed,
        "start_at": time.time(),
        "done_at": time.time()
    })
    return ""

run(host='0.0.0.0', port=8765, debug=True)
