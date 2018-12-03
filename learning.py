from flask import Flask, url_for, request, jsonify
import datetime, string, random, time, re

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

def show_the_login_form():
    return 'Lawl'


@app.route('/user/<username>/')
def show_user_profile(username):
    return '{}\'s profile'.format(username)


@app.route('/query-example')
def query_example():
    language = request.args.get('language')
    framework = request.args['framework']

    return '''<h1> The language is: {}</h1>
              </h2>The framework is: {}</h2>'''.format(language,framework)

@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form['framework']

        return '''<h1> The language is: {}</h1>
                  </h2>The framework is: {}</h2>'''.format(language,framework)


    return '''<form method="POST">
                    Language: <input type="text" name="language"><br>
                    Framework: <input type="text" name="framework"><br>
                    <input type="submit" value="Submit"><br>
            </form>'''

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    req_data = request.get_json()
    language = None
    if 'language' in req_data:
        language = request.json['language']
    framework = request.json['framework']
    python_version = req_data['version_info']['python'] #two keys are needed because of the nested object
    example = req_data['examples'][0] #an index is needed because of the array
    boolean_test = req_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


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

   

with app.test_request_context():
    print(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
