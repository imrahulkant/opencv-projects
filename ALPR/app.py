from flask import Flask, render_template, Response, request
from numberplate import getcarnumber
import glob
import os
import requests
import xmltodict
import json

path = os.getcwd()
dir = os.path.join(path, "uploads")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = dir
@app.route('/')
def index():
    return render_template('index.html')

def get_vehicle_info(plate_number):
    r = requests.get(
        "http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=himanshukr0007".format(str(plate_number)))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1

@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        carnum = getcarnumber(f.filename)
        data = get_vehicle_info(carnum)
        vehdes = data['Description']
        reg = data['RegistrationYear']
        carDesc = data["CarMake"]["CurrentTextValue"]
        carModel = data["CarModel"]["CurrentTextValue"]
        carVariant = data["Variant"]
        carEngineSize = data["EngineSize"]["CurrentTextValue"]
        NumberOfSeats = data["NumberOfSeats"]["CurrentTextValue"]
        vehIDnum = data["VechileIdentificationNumber"]
        engNo = data["EngineNumber"]
        fuelType = data["FuelType"]["CurrentTextValue"]
        regdate = data["RegistrationDate"]
        vehType = data["VehicleType"]
        loc = data["Location"]
        return render_template(
            "success.html", 
            name = f.filename, 
            carn = carnum,
            vehdesc = vehdes,
            reg = reg,
            carDesc = carDesc, 
            carModel = carModel,
            carVariant = carVariant,
            carEngineSize = carEngineSize,
            NumberOfSeats = NumberOfSeats,
            vehIDnum = vehIDnum,
            engNo = engNo,
            fuelType = fuelType,
            regdate = regdate,
            vehType = vehType,
            loc = loc
        ) 




if __name__ == '__main__':
    app.run(debug=True)