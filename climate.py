##http://flask.pocoo.org/docs/0.12/patterns/sqlalchemy/

## using modules from the flask orm classwork

import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt 

engine = create_engine("sqlite:///Resources/hawaii.sqlite", echo=False)

app = Flask(__name__)

Base = automap_base 

Base.prepare(engine, reflect=True)

Measurement = Base.classes.Measurement

Station = Base.classes.Station

session = Session(Engine)

app = Flask(__name__)


@app.route("/")
def welcome():
    """List of available API routes"""
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/<start>
    /api/v1.0/<end>

@app.route("/api/v1.0/precipitation")
def Precipitation():
    last_measurement_date = session.query(Measurement.date)./
    order_by(Measurement.date.desc()).first() 
    
    final_date = dt.datetime.strptime(last_measurement_date, "%Y-%m_%d")
    
    year_ago = last_measurement_date - dt.timedelta(days=365)
    
    last_years_prcp = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= year_ago).\
            order_by(Measurement.date)

    precipictation_dict = 

@app.route("/api/v1.0/stations")
def Stations():
    
    stations =  session.query(Station.station).\
        group_by(Station.station).all()

    stations_list = list(np.rsvel(stations))
    
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    last_measurement_date = session.query(Measurement.date)./
    order_by(Measurement.date.desc()).first() 
    
    final_date = dt.datetime.strptime(last_measurement_date, "%Y-%m_%d")
    
    year_ago = last_measurement_date - dt.timedelta(days=365)

    tobs = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= year_ago).\
            filter(Measurement.station == 'USC00519281').\
                group_by(Measurement.date).all()

    tobs_list = list(tobs)

    return jsonify(tobs_list)

@app.route(/api/v1.0/<start>)
def start():

    start = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).\
            group_by(Measurement.date)

    start_list = list(start)

    return jsonify(start_list)

@app.route(/api/v1.0/<end>)
def end():
    end = session.query(Measurement.date, func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= end_date).\
            group_by(Measurement.date)
    
    end_list = list(end)

    return jsonify(end_list)

    
if __name__ == '__main__':
    app.run(debug=True)



    









