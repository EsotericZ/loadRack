from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

if __name__ == "__main__":
    # app.run()
    # app.run(host='0.0.0.0', port='5000', threaded=True)
    app.run(host='0.0.0.0', port=5000)
    # socketio.run(app, host='0.0.0.0')
    # app.run(host='0.0.0.0', port=9000, threaded=True)
    # app.debug = True
    # app.run(host='10.0.1.100', port=5000)
    # app.run(host='10.0.1.187', port='5000')
    # app.run(host='10.0.1.187', port=9000)
