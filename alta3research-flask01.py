# !/usr/bin/python3                                                                                                                                                                                                                        
"""                                                                                                                                                                                                                                        
This script enables the user to  track their equipment inventory via a Flask API that accesses an sqlite database"""                                                                                                                       
                                                                                                                                                                                                                                           
import json                                                                                                                                                                                                                                
import sqlite3 as sql                                                                                                                                                                                                                      
                                                                                                                                                                                                                                           
from flask import Flask                                                                                                                                                                                                                    
from flask import render_template                                                                                                                                                                                                          
from flask import request                                                                                                                                                                                                                  
from flask import jsonify                                                                                                                                                                                                                  
                                                                                                                                                                                                                                           
app = Flask(__name__)                                                                                                                                                                                                                      
                                                                                                                                                                                                                                           
# return home.html (this is the landing page)                                                                                                                                                                                              
@app.route('/')                                                                                                                                                                                                                            
def home():                                                                                                                                                                                                                                
    return render_template('home.html')                                                                                                                                                                                                    

                                                                                                                                                                                                                                           
# return equipment.html (it allows adding an equipment to the sqlite database)                                                                                                                                                             
@app.route('/enternew')                                                                                                                                                                                                                    
def new_equipment():                                                                                                                                                                                                                       
    return render_template('equipment.html')                                                                                                                                                                                               
                                                                                                                                                                                                                                           
# Using the form equipment.html generates a POST that is sent to /addrec                                                                                                                                                                   
#   & the info is then added to the sqlite database.                                                                                                                                                                                       
@app.route('/addrec', methods=['POST'])                                                                                                                                                                                                    
def addrec():                                                                                                                                                                                                                              
    try:                                                                                                                                                                                                                                   
        description = request.form['description']  # description of equipment                                                                                                                                                              
        maker = request.form['maker']  # maker of equipment                                                                                                                                                                                
        model = request.form['model']  # model of equipment                                                                                                                                                                                
        serial_number = request.form['serial_number']  # serial number of equipment                                                                                                                                                        
                                                                                                                                                                                                                                           
        # connect to sqliteDB                                                                                                                                                                                                              
        with sql.connect("database.db") as con:                                                                                                                                                                                            
            cur = con.cursor()                                                                                                                                                                                                             
                                                                                                                                                                                                                                           
            # place the info collected from the form into the sqlite database                                                                                                                                                              
            cur.execute("INSERT INTO equipments (description,maker,model,serial_number) VALUES (?,?,?,?)", (description,maker,model,serial_number))                                                                                        
            # commit the transaction to our sqlite database                                                                                                                                                                                
            con.commit()                                                                                                                                                                                                         


# return all entries from the sqlite database as HTML
@app.route('/list')
def list_equipments_as_html():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from equipments")  # pull all information from the table "equipments"

    rows = cur.fetchall()
    return render_template("list.html", rows=rows)  # return all the sqlite database content as HTML


# return all the sqlite database as JSON
@app.route('/list-json')
def list_equipments_as_json():
    con = sql.connect("database.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * from equipments")  # pull all information from the table "equipments"
    rows_data = cur.fetchall()
    extract = [tuple(row) for row in rows_data]

    # Initialize a list of rows
    rows_list = []
    # Fill the list with the rows
    for element in extract:
        rows_list.append(element)
    # Initialize a dictionary
    data_dict = {}
    # Add the key 'data" and the list of rows as its value
    data_dict['data'] = rows_list

    json_data = json.dumps(data_dict)
    return jsonify(json_data)  # return all of the sqliteDB info as JSON


if __name__ == '__main__':
    try:
        # ensure the sqlite database is created
        con = sql.connect('database.db')
        print("Opened database successfully")
        # make sure that the table equipments is ready to be written to
        con.execute('CREATE TABLE IF NOT EXISTS equipments (description TEXT, maker TEXT, model TEXT, serial_number TEXT)')
        print("Table created successfully")
        con.close()
        # begin Flask Application
        # app.run(host="0.0.0.0", port=2224, debug=True)
        app.run(host="0.0.0.0", port=2224, debug=True)
    except:
        print{("App failed on boot")
        