from flask import Flask, request, render_template
import joblib
import requests 
#import jsonify 

app = Flask(__name__) # initialising flask app

model = joblib.load('Car Resale Value Prediction') # load machine learning model

@app.route('/', methods=['GET'])
def home():
    return render_template('index page1.html')
@app.route('/predict', methods=['POST', 'GET'])
def predict():
 if request.method == 'POST':
    SELLER_TYPE = request.form['seller']
    ABTEST=request.form['abtest']
    VEHICLE_TYPE=request.form['vehicleType']
    YEAR_OF_REGISTRATION = int(request.form['yearOfRegistration'])
    POWER_IN_PS=float(request.form['powerPS'])
    KILOMETERS_DRIVEN=float(request.form['kilometer'])
    MONTH_OF_REGISTRATION=int(request.form['monthOfRegistration'])
    FUEL_TYPE= request.form['fuelType']
    NOT_REPAIRED_DAMAGE=request.form['notRepairedDamage']
    NUMBER_OF_PICTURES=int(request.form['nrOfPictures'])
    POSTAL_CODE=int(request.form['postalCode'])
    OFFER_TYPE=request.form['offerType_Gesuch']
    GEARBOX_MANUELL=request.form['gearbox_manuell']
    if SELLER_TYPE == 'private':
       SELLER_TYPE = 0
    else:
       SELLER_TYPE = 1
    if ABTEST == 'test':
       ABTEST = 0
    else:
       ABTEST = 1
    if VEHICLE_TYPE == 'limousine':
       VEHICLE_TYPE= 0
    elif VEHICLE_TYPE == 'kleinwagen':
       VEHICLE_TYPE = 1
    elif VEHICLE_TYPE == 'kombi':
       VEHICLE_TYPE = 2
    elif VEHICLE_TYPE == 'bus':
       VEHICLE_TYPE = 3
    elif VEHICLE_TYPE == 'carbio':
       VEHICLE_TYPE = 4
    elif VEHICLE_TYPE == 'coupe':
       VEHICLE_TYPE = 5
    elif VEHICLE_TYPE == 'suv':
       VEHICLE_TYPE = 6
    else :
       VEHICLE_TYPE =7
    if FUEL_TYPE == 'benzin' :
       FUEL_TYPE == 0
    elif FUEL_TYPE == 'diesel' :
       FUEL_TYPE = 1
    elif FUEL_TYPE == 'lpg':
       FUEL_TYPE = 2
    elif FUEL_TYPE == 'cng':
       FUEL_TYPE = 3
    elif FUEL_TYPE == 'hybrid':
       FUEL_TYPE =4
    elif FUEL_TYPE == 'andere':
      FUEL_TYPE =5
    else:
      FUEL_TYPE = 6
    if NOT_REPAIRED_DAMAGE == 'nein':
      NOT_REPAIRED_DAMAGE = 0
    else:
      NOT_REPAIRED_DAMAGE = 1
    if OFFER_TYPE == 'Angebot':
       OFFER_TYPE = 0
    else:
       OFFER_TYPE = 1
    if GEARBOX_MANUELL == 'manuell':
       GEARBOX_MANUELL = 1
    else :
       GEARBOX_MANUELL = 0

    prediction =model.predict[[SELLER_TYPE,ABTEST,VEHICLE_TYPE,YEAR_OF_REGISTRATION,POWER_IN_PS,KILOMETERS_DRIVEN,MONTH_OF_REGISTRATION,FUEL_TYPE,NOT_REPAIRED_DAMAGE,NUMBER_OF_PICTURES,POSTAL_CODE,OFFER_TYPE,GEARBOX_MANUELL]]
    output=prediction[0]
    if(output==0):
    #model = joblib.load(open('model', 'rb')) # load ml model
    #print("Scoring response")
           return render_template('index page1.html', prediction_text="Predicted Price Of Your Car Is {} $".format       (prediction))
    else:
       return render_template('index page1.html')
if __name__ == '__main__':
     app.run(debug=True)