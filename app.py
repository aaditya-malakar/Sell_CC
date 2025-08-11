import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def calculate():
    name= request.form['user_name']
    crop = request.form['crop'].replace(" ","").lower()
    region = request.form['region'].replace(" ","").lower()
    land = float(request.form['land'])
    total_yield = float(request.form['total_yield'])
    residue = request.form['residue'].replace(" ","").lower()

    yield_per_ha = total_yield / land

    acc_crops = " Wheat, Rice, Maize, Sugarcane, Soyabean, Cotton, Groundnut, Mustard "
    acc_regions1 = " Madhya Pradesh, Uttar Pradesh, Punjab "

    if (acc_crops.lower()).find(crop) == -1:
        return render_template("index.html", result="Choose a valid crop.")

    if region == "madhyapradesh":
        pass
    elif region == "uttarpradesh":
        pass
    elif region == "punjab":
        pass
    else:
        return render_template("index.html", result="Choose a valid region.")

               # MADHYA PRADESH
    if region in ["madhyapradesh"]:
        if crop=="wheat":
            R,HI,S_f,Se_f=1.0,0.45,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.2,0.25,0.2,0.012,1.1,0.02
        elif crop=="rice":
            R,HI,S_f,Se_f=1.5,0.50,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=2.0,0.26,0.32,0.017,1.5,0.026
        elif crop=="maize":
            R,HI,S_f,Se_f=1.5,0.50,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.2,0.21,0.09,0.008,1.3,0.01
        elif crop=="sugarcane":
            R,HI,S_f,Se_f=0.3,0.50,1.0,1.1
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.9,0.14,0.8,0.029,0.7,0.039
        elif crop=="soyabean":
            R,HI,S_f,Se_f=1.5,0.40,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=0.35,0.16,0.75,0.008,0.6,0.01
        elif crop=="cotton":
            R,HI,S_f,Se_f=2.5,0.40,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.2,0.24,0.14,0.012,1.0,0.018
        elif crop=="groundnut":
            R,HI,S_f,Se_f=1.2,0.35,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.2,0.18,0.22,0.011,1.3,0.02
        elif crop=="mustard":
            R,HI,S_f,Se_f=1.5,0.30,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.4,0.26,0.21,0.014,1.1,0.017
    # Emissions and net
        if residue=="yes":
            E_f=1.4
            residue_burnt=yield_per_ha*R*E_f
            emissions=(N+L+E+P+W+H)+residue_burnt
        else:
            emissions=(N+L+E+P+W+H)
        CO2_net=CO2_gross-emissions

# UTTAR PRADESH
    elif region in ["uttarpradesh"]:
        if crop=="wheat":
            R,HI,S_f,Se_f=1.0,0.45,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.44,0.27,0.23,0.014,1.3,0.022
        elif crop=="rice":
            R,HI,S_f,Se_f=1.5,0.50,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=2.2,0.28,0.34,0.018,1.6,0.028
        elif crop=="maize":
            R,HI,S_f,Se_f=1.5,0.50,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.3,0.22,0.10,0.009,1.4,0.011
        elif crop=="sugarcane":
            R,HI,S_f,Se_f=0.3,0.50,1.0,1.1
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=2.0,0.15,0.85,0.03,0.8,0.04
        elif crop=="soyabean":
            R,HI,S_f,Se_f=1.5,0.40,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=0.4,0.17,0.80,0.009,0.7,0.012
        elif crop=="cotton":
            R,HI,S_f,Se_f=2.5,0.40,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.3,0.25,0.15,0.013,1.1,0.02
        elif crop=="groundnut":
            R,HI,S_f,Se_f=1.2,0.35,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.3,0.19,0.24,0.012,1.4,0.021
        elif crop=="mustard":
            R,HI,S_f,Se_f=1.5,0.30,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.45,0.27,0.22,0.015,1.2,0.018
    # Emissions
        if residue=="yes":
            E_f=1.4
            residue_burnt=yield_per_ha*R*E_f
            emissions=(N+L+E+P+W+H)+residue_burnt
        else:
            emissions=(N+L+E+P+W+H)
        CO2_net=CO2_gross-emissions

# PUNJAB 
    elif region in ["punjab"]:
        if crop=="wheat":
            R,HI,S_f,Se_f=0.25,0.45,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.60,0.28,0.23,0.014,1.4,0.022
        elif crop=="rice":
            R,HI,S_f,Se_f=0.25,0.50,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=2.3,0.29,0.34,0.018,1.5,0.028
        elif crop=="maize":
            R,HI,S_f,Se_f=0.25,0.40,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.4,0.23,0.11,0.009,1.5,0.011
        elif crop=="sugarcane":
            R,HI,S_f,Se_f=0.20,0.75,1.0,1.1
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=2.1,0.16,0.9,0.03,0.8,0.04
        elif crop=="soyabean":
            R,HI,S_f,Se_f=0.40,0.35,1.0,1.0
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=0.42,0.18,0.78,0.009,0.65,0.012
        elif crop=="cotton":
            R,HI,S_f,Se_f=0.40,0.35,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.35,0.26,0.16,0.013,1.1,0.02
        elif crop=="groundnut":
            R,HI,S_f,Se_f=0.20,0.30,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.35,0.20,0.25,0.012,1.45,0.021
        elif crop=="mustard":
            R,HI,S_f,Se_f=0.40,0.35,1.0,0.85
            CO2_gross=yield_per_ha*((1+R)/HI)*0.45*3.67*S_f*Se_f
            N,L,E,P,W,H=1.50,0.28,0.23,0.015,1.25,0.018
    # Emissions 
        if residue=="yes":
            E_f=1.4
            residue_burnt=yield_per_ha*R*E_f
            emissions=(N+L+E+P+W+H)+residue_burnt
        else:
            emissions=(N+L+E+P+W+H)
        CO2_net=CO2_gross-emissions

    Total_CO2_net=CO2_net*land
    carbon_credits=Total_CO2_net



    return render_template("result.html", name=name, crop=crop, region=region, land=land, total_yield=total_yield, residue=residue, carbon_credits=carbon_credits,  result=f"Carbon Credits Generated: {carbon_credits:.2f}")

@app.route("/sell", methods=["POST"])
def sell():
    sell = request.form["sell"]
    name = request.form["name"]
    crop = request.form["crop"]
    region = request.form["region"]
    land = request.form["land"]
    total_yield = request.form["total_yield"]
    residue = request.form["residue"]
    carbon_credits = request.form["carbon_credits"]
    response= None

    if sell=="yes":
        data={"name":name,"crop":crop,"region":region,"land":land,"total_yield":total_yield,"residue":residue,"carbon_credits":carbon_credits}
        url="https://script.google.com/macros/s/AKfycbzhKLIvvfiz-7AURmwQOtjaGUYjsXRv1XEZivotD7L0VCSlx9_Zd6CWUQbEJwWdbnc/exec"
        response=requests.post(url,json=data)
        if response and response.status_code==200:
            return render_template("msg.html", msg=f"Your data has been saved, and credits have been sent for certification")
    else: 
        return render_template("msg.html", msg=f"Your data has not been saved")
    

if __name__ == '__main__':
    app.run(debug=True)

