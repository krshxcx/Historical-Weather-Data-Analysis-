from flask import Flask, render_template
import pandas as pd



app = Flask('hello')
data1 = pd.read_csv('data_small\stations.txt',skiprows=17)
data1 = data1[['STAID','STANAME                                 ']]
@app.route("/")
def home():
    return render_template('home.html',data = data1.to_html())


@app.route("/api/v1/<station>/<date>/")
def about(station,date):
    filename = 'data_small/TG_STAID'+str(station).zfill(6)+".txt"
    df = pd.read_csv(filename,skiprows=20,parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE']==date]['   TG'].squeeze()/10
    return { "station": station, 
            "date": date,
            "temperature" : temperature
        }
    
@app.route("/api/v1/<station>")
def all_data(station):
    filename = 'data_small/TG_STAID' + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df.to_dict()
    return result

app.run(debug=True)