from flask import Flask, render_template
import json, os

path_to_json = './database/'
json_files = os.listdir(path_to_json)
results_merged = []

for i in range(0,len(json_files)):
    file = json_files[i]
    with open(os.path.join(path_to_json, file)) as f:
       data_json = json.load(f)
       data = data_json['data']
       results = data['result']
       results_merged = results_merged + results

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', results_merged=results_merged)