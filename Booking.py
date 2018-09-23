rom flask import Flask
from flask import request
from flask_mysqldb import MySQL
mysql = MySQL()
app = Flask(__name__)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# My SQL Instance configurations 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
app.config['MYSQL_USER'] = 'web'
app.config['MYSQL_PASSWORD'] = 'webPass'
app.config['MYSQL_DB'] = 'booking'
app.config['MYSQL_HOST'] = 'localhost' #for demo
mysql.init_app(app)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test to Check if app is Running 
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/")
def hello():
    return("Hello World! Booking App Running")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Show All Bookings Data
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/showall") # Show All Bookings Data
def booking(): # 
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM bookings''') # execute an SQL statement to get booking data
    rv = cur.fetchall() #Retreive all rows returend by the SQL statement
    ret = "All Bookings Data: <BR/>" #Create return string
    for row in rv: #Format the Output Results and add to return string
        ret=ret+'[ Seat ID ] : '+str(row[0])+'[ Seat Name ] : '+row[1]+'[ Is Seat Booked ] : '+str(row[2])+'[ Booked By ] : '+str(row[3])+'<BR/> '
    return ret      #Return the data in a string format
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Show Available
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/showavl") # Show All Bookings Data
def available(): # 
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT seatID, seatName FROM bookings where seatBooked = 0''') # 0 means seat is not booked
    rv = cur.fetchall() #Retreive all rows returend by the SQL statement
    ret = "Availability: <BR/>" #Create return string
    for row in rv: #Format the Output Results and add to return string
        ret=ret+'[ Seat ID ] : '+str(row[0])+'[ Seat Name ] : '+row[1]+'<BR/> '
    return ret      #Return the data in a string format
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Show Booked
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/showbkd") # Show All Bookings Data
def booked(): # 
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT seatID, seatName, bookedBy FROM bookings where seatBooked = 1''') # 1 means seat is booked
    rv = cur.fetchall() #Retreive all rows returend by the SQL statement
    ret = Booked: <BR/>" #Create return string
    for row in rv: #Format the Output Results and add to return string
        ret=ret+'[ Seat ID ] : '+str(row[0])+'[ Seat Name ] : '+row[1]+'[ Booked By ] : '+str(row[2])+'<BR/> '
    return ret      #Return the data in a string format
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Show JSON
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/json") # Show All Bookings Data
def booking(): # 
    cur = mysql.connection.cursor() #create a connection to the SQL instance
    cur.execute('''SELECT * FROM bookings''') # execute an SQL statement to get booking data
    rv = cur.fetchall() #Retreive all rows returend by the SQL statement
    ret = '{"Results":[' #Create return string
    first=True
    for row in rv: #Format the Output Results and add to return string
        if not first:
            ret=ret+','
        else:
            first=False
        ret=ret+'{"SeatID": 'str(row[0])+', "SeatName": "'+row[1]+'", "SeatBooked": '+str(row[2])+', "BookedBy": '+str(row[3])+'}'
    ret=ret+']}'
    return ret      #Return the data in a string format

#
if __name__ == "__main__":
        # avoid WARNING: Do not use the development server in a production environment.
        app.env = 'development'
        app.run(host='0.0.0.0', port='80') #Run the flask app at port 80 for demo

