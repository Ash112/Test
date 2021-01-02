from flask import Flask,request,render_template
from celery import Celery

import time


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://jeduevbw:GVkBafRrF9Gqp3MSXAafw0gUzFZs_N5U@lionfish.rmq.cloudamqp.com/jeduevbw'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'],backend=app.config['CELERY_RESULT_BACKEND'])
#celery.conf.update(app.config)

celery.conf.update(
broker_url='amqp://jeduevbw:GVkBafRrF9Gqp3MSXAafw0gUzFZs_N5U@lionfish.rmq.cloudamqp.com/jeduevbw',
result_backend='rpc://',result_persistent = False
)


def dostuff(num):

    start = time.Time()
    x=0
    for x in range(num):

        x = x+1
    end = time.Time()

    print(totaltime = end - start)

    return x


@celery.task
def my_background_task(arg1, arg2):

    result = arg1 * arg2
    result1 = dostuff(arg1) + result

    return result1


@app.route("/")
def hello():

    return render_template("index.html")


@app.route('/', methods =["GET", "POST"])
def userinput():

    if request.method == "POST":

        task = my_background_task.delay(99, 5)

        output = task.wait()

        print(output)

        return render_template("index.html",output =output )

if __name__ == "__main__":

    # turn off debug when deploying
    app.run(debug=True)
