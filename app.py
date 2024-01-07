
from flask import Flask,send_file
from flask_googlemaps import GoogleMaps
from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import os
import csv

app = Flask(__name__)

app.config['GOOGLEMAPS_KEY'] = "aiya key mukje"

GoogleMaps(app)




app = Flask(__name__)
GoogleMaps(app)

@app.route('/home')
def home():
    os.system('python ../DROP/DROP.py  -o static/outputCSV/tmp.csv ../DROP/sample-data/DAT-Files/FLY000.DAT')
    return render_template("Home.html")


@app.route("/")
def mapview():
    # creating a map in the view
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )
    sndmap = Map(
        identifier="sndmap",
        lat=37.4419,
        lng=-122.1419,
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 37.4419,
             'lng': -122.1419,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ]
    )
    print("Map END POIT : ", mymap ,sndmap)
    return render_template('Map.html', mymap=mymap, sndmap=sndmap)


@app.route('/csvroute')
def csv_route():
    os.system('python ../DROP/DROP.py  -o static/outputCSV/tmp.csv ../DROP/sample-data/DAT-Files/FLY000.DAT')
    f = open("static/outputCSV/tmp.csv",'rb')
    return send_file(f,as_attachment=True,download_name="abcd.csv")

@app.route('/csvroute1')
def csv_route1():
    os.system('python ../DROP/DROP.py  -o static/outputCSV/tmp.csv ../DROP/sample-data/DAT-Files/FLY000.DAT')
    f = open("static/outputCSV/tmp.csv")
    readdata = csv.reader(f)
    headers = next(readdata)
    data = [headers]
    cnt=0
    for row in readdata:
        if cnt>10:
            break
        cnt+=1
        data.append(row)
    print(len(data))
    return data

if __name__ == "__main__":
    app.run(debug=True)
