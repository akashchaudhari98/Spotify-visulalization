from flask import Flask
from analysis import analysis_
import json
app = Flask(__name__)

@app.route('/songs/', methods=['GET', 'POST'])
def print_songs():
    analysis = analysis_()
    songs_df = analysis.create_df()
    #z = json.dumps(songs_df) 
    return songs_df.to_json()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)