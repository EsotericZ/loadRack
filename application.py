


# from random import random
# from time import sleep
# from threading import Thread, Event
# from cellfunc import getvr




import pusher
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, url_for, copy_current_request_context, request, redirect
from flask_login import current_user, login_user, logout_user, login_required, LoginManager, UserMixin
from dbcn import racks
from database import db_session
from models import Job

__author__ = 'slynn'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

#turn the flask app into a socketio app
socketio = SocketIO(app)
# socketio = SocketIO(app, async_mode="threading")

pusher_client = pusher.Pusher(
    app_id='945487',
    key='6fd0f7485811f36fa809',
    secret='b55640e24608ecee8622',
    cluster='us3',
    ssl=True)

#random number Generator Thread
# thread = Thread()
# thread_stop_event = Event()

#class RandomThread(Thread):
#    def __init__(self):
#        self.delay = 1
#        super(RandomThread, self).__init__()

#    def randomNumberGenerator(self):
#        """
#        Generate a random number every 1 second and emit to a socketio instance (broadcast)
#        Ideally to be run in a separate thread?
#        """
#        #infinite loop of magical random numbers
#        print("Making random numbers")
#        rack = racks()
#        r = rack.values.tolist()
#        while not thread_stop_event.isSet():
#            num = getvr()

#            # RACK 01 - ALS .125 5052 48x120
#            numr1 = num[0]
#            print('This is Rack 01 raw - ', numr1)
#            # wtr1 = 1.813   #lb/sq-ft
#            # shr1 = 40      #sq-ft
#            wtr1 = r[0][6]   #lb/sq-ft
#            shr1 = r[0][2]      #sq-ft
#            print(wtr1, shr1)
#            n1r1 = sum(numr1) * 1000
#            n2r1 = round(((1132.6*n1r1)-41.924-562),0)
#            n1 = round((n2r1/(wtr1*shr1)),0)
#            if n1 < 0:
#                number1 = 'No Rack'
#            elif n1 == 0:
#                number1 = 'Empty Rack'
#            else:
#                number1 = n1
#            print('Number of sheets Rack 01 - ', number1)

#            # RACK 02 - ALS .100 5052 48x120
#            numr2 = num[1]
#            print('This is Rack 02 raw - ', numr2)
#            wtr2 = 1.438   #lb/sq-ft
#            shr2 = 40      #sq-ft
#            # wtr1 = r[1][6]   #lb/sq-ft
#            # shr1 = r[1][2]      #sq-ft
#            n1r2 = sum(numr2) * 1000
#            n2r2 = round(((1159.04*n1r2)-112.14-562),0)
#            n2 = round((n2r2/(wtr2*shr2)),0)
#            if n2 < 0:
#                number2 = 'No Rack'
#            elif n2 == 0:
#                number2 = 'Empty Rack'
#            else:
#                number2 = n2
#            print('Number of sheets Rack 02 - ', number2)

#	    # RACK 03 - ALS .090 5052 48x120
#            numr3 = num[2]
#            print('This is Rack 03 raw - ', numr3)
#            wtr3 = 1.280   #lb/sq-ft
#            shr3 = 40      #sq-ft
#            # wtr1 = r[2][6]   #lb/sq-ft
#            # shr1 = r[2][2]      #sq-ft
#            n1r3 = sum(numr3) * 1000
#            n2r3 = round(((1115.14*n1r3)-101.05-361),0)
#            n3 = round((n2r3/(wtr3*shr3)),0)
#            if n3 < 0:
#                number3 = 'No Rack'
#            elif n3 == 0:
#                number3 = 'Empty Rack'
#            else:
#                number3 = n3
#            print('Number of sheets Rack 03 - ', number3)

## # # # # # # # # #

#	    # RACK 19 - ALS .080 5052 48x120
#            numr19 = num[3]
#            print('This is Rack 19 raw - ', numr19)
#            wtr19 = 1.140   #lb/sq-ft
#            shr19 = 40      #sq-ft
#            # wtr1 = r[18][6]   #lb/sq-ft
#            # shr1 = r[18][2]      #sq-ft
#            n1r19 = sum(numr19) * 1000
#            n2r19 = round(((1091.95*n1r19)-101.44-572),0)
#            n19 = round((n2r19/(wtr19*shr19)),0)
#            if n19 < 0:
#                number19 = 'No Rack'
#            elif n19 == 0:
#                number19 = 'Empty Rack'
#            else:
#                number19 = n19
#            print('Number of sheets Rack 19 - ', number19)

#	    # RACK 20 - ALS .063 5052 48x120
#            numr20 = num[4]
#            print('This is Rack 20 raw - ', numr20)
#            wtr20 = 0.905   #lb/sq-ft
#            shr20 = 40      #sq-ft
#            # wtr1 = r[19][6]   #lb/sq-ft
#            # shr1 = r[19][2]      #sq-ft
#            n1r20 = sum(numr20) * 1000
#            n2r20 = round(((1143.80*n1r20)-106.89-569),0)
#            n20 = round((n2r20/(wtr20*shr20)),0)
#            if n20 < 0:
#                number20 = 'No Rack'
#            elif n20 == 0:
#                number20 = 'Empty Rack'
#            else:
#                number20 = n20
#            print('Number of sheets Rack 20 - ', number20)

## # # # # # # # # #

#            socketio.emit('newnumber', {'number': [number1,number2,number3,number19,number20]}, namespace='/test')
#            sleep(self.delay)

#    def run(self):
#        self.randomNumberGenerator()

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/')
def index():
    r = racks()
    rack = r.values.tolist()
    mtl = []
    for r in rack:
        if r[3] != '':
            mtl.append([r[1], r[2], r[3], r[4], r[5]])
    sorter = lambda x: (x[2], x[0], x[1], x[3], x[4])
    mtl = sorted(mtl, key=sorter)
    return render_template('index.html', rack=rack, mtl=mtl)

@app.route('/rack01')
def rack01():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('rack01.html', rows=rows, rack=rack)

@app.route('/rack02')
def rack02():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    #only by sending this page first will the client be connected to the socketio instance
    return render_template('rack02.html', rows=rows, rack=rack)

@app.route('/rack03')
def rack03():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack03.html', rows=rows, rack=rack)

@app.route('/rack04')
def rack04():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack04.html', rows=rows, rack=rack)

@app.route('/rack05')
def rack05():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack05.html', rows=rows, rack=rack)

@app.route('/rack06')
def rack06():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack06.html', rows=rows, rack=rack)

@app.route('/rack07')
def rack07():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack07.html', rows=rows, rack=rack)

@app.route('/rack08')
def rack08():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack08.html', rows=rows, rack=rack)

@app.route('/rack09')
def rack09():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack09.html', rows=rows, rack=rack)

@app.route('/rack10')
def rack10():
    r = racks()
    rack = r.values.tolist()
    # rows = Job.query.all()
    for r in rack:
        indv = [];
        if r[0] > 102:
            if r[5] != '':
                indSplit = r[5].split(";");
                finalCut = "\n".join(indSplit)
                r.append(finalCut)
            else:
                r.append('-')
    return render_template('rack10.html', rack=rack)

@app.route('/rack11')
def rack11():
    r = racks()
    rack = r.values.tolist()
    rows = Job.query.all()
    return render_template('rack11.html', rows=rows, rack=rack)

@socketio.on('connect', namespace='/test')
def test_connect():
    # need visibility of the global thread object
    global thread
    print('Client connected')

    #Start the random number generator thread only if the thread has not been started before.
    if not thread.isAlive():
        print("Starting Thread")
        thread = RandomThread()
        thread.start()

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
     print('Client disconnected')

@app.route('/backend', methods=["POST", "GET"])
def backend():
    if request.method == "POST":
        rack = request.form["rack"]
        row = request.form["row"]
        matl = request.form["matl"]
        size = request.form["size"]
        note = request.form["note"]
        weight = request.form["weight"]
        phidget = request.form["phidget"]

        new_row = Job(rack, row, matl, size, note, weight, phidget)
        db_session.add(new_row)
        db_session.commit()

        data = {
            "id": new_row.id,
            "rack": rack,
            "row": row,
            "matl": matl,
            "size": size,
            "note": note,
            "weight": weight,
            "phidget": phidget}

        pusher_client.trigger('table', 'new-record', {'data': data})

        return redirect("/backend", code=302)
    else:
        rows = Job.query.all()
        return render_template('backend.html', rows=rows)

@app.route('/edit/<int:id>', methods=["POST", "GET"])
def update_record(id):
    if request.method == "POST":
        rack = request.form["rack"]
        row = request.form["row"]
        matl = request.form["matl"]
        size = request.form["size"]
        note = request.form["note"]
        weight = request.form["weight"]
        phidget = request.form["phidget"]

        update_row = Job.query.get(id)
        update_row.rack = rack
        update_row.row = row
        update_row.matl = matl
        update_row.size = size
        update_row.note = note
        update_row.weight = weight
        update_row.phidget = phidget

        db_session.commit()

        data = {
            "id": id,
            "rack": rack,
            "row": row,
            "matl": matl,
            "size": size,
            "note": note,
            "weight": weight,
            "phidget": phidget}

        pusher_client.trigger('table', 'update-record', {'data': data})

        return redirect('/', code=302)
    else:
        new_row = Job.query.get(id)
        return render_template('update_row.html', data=new_row)

@app.route('/advedit/<int:id>', methods=["POST", "GET"])
def adv_update_record(id):
    if request.method == "POST":
        rack = request.form["rack"]
        row = request.form["row"]
        matl = request.form["matl"]
        size = request.form["size"]
        note = request.form["note"]
        weight = request.form["weight"]
        phidget = request.form["phidget"]

        update_row = Job.query.get(id)
        update_row.rack = rack
        update_row.row = row
        update_row.matl = matl
        update_row.size = size
        update_row.note = note
        update_row.weight = weight
        update_row.phidget = phidget

        db_session.commit()

        data = {
            "id": id,
            "rack": rack,
            "row": row,
            "matl": matl,
            "size": size,
            "note": note,
            "weight": weight,
            "phidget": phidget}

        pusher_client.trigger('table', 'adv-update-record', {'data': data})

        return redirect('/', code=302)
    else:
        new_row = Job.query.get(id)
        return render_template('advupdate.html', data=new_row)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
