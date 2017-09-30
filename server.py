import os
from pytrends.request import TrendReq
from flask import Flask, send_from_directory

app = Flask(__name__)

TRENDS = TrendReq()

@app.route('/gettrends')
def get_trends():
    TRENDS.build_payload(kw_list=['pizza', 'bagel'])
    # This data is a pandas dataframe. Feel free to google how that works
    interest_over_time_df = TRENDS.interest_over_time()

    return str(interest_over_time_df.head())

@app.route('/js/<path:path>')
def send_js(path):
    ''' returns any requested javascript file '''
    return send_from_directory('js', path)

@app.route('/')
def serve_page():
    ''' Returns the application '''
    return app.send_static_file('index.html')

app.run()
