from flask import Flask, request, jsonify
import datetime, string, random, time

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'


@app.route('/jsonify-example')
def jsonify_example():

    str = 'None'
    finalStr = None
    if request.query_string != None :
        str = request.query_string
        s = list(str)
        for idx,val in enumerate(s) :
            if val == '&' :
                s[idx] = ','
            if val == '=' :
                s[idx] = '-'
        finalStr = "".join(s)

    body = None
    if request.data :
        body = request.data

    data = {
                'greeting': 'Hello',
                'key': 1,
                'time': datetime.datetime.utcnow(),
                'method': request.method,
                'header': dict(request.headers), # if request.query_string != None : (required?????)
                'path':  request.path,# if request.query_string != None : (required?????)
                'query': finalStr,
                'body' : body,   #Not Sure!!!!!!!!!!!!!!!!!!!!!!!!!
            }

    r = random.uniform(15.0001, 29.9999)
    time.sleep(r)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
