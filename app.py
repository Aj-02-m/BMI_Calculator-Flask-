#(python)

from flask import Flask, request, render_template, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "123e4r555"

@app.route('/' ,methods=['GET','POST'])
def bmi_calculator():
   # bmi = None
    #if request.method == 'POST' and 'weight' and 'height' in request.form:
     #   weight = request.form.get('weight')
     #   height = request.form.get('height')
      #  try:
       #     weight = float(weight)
         #   height = float(height)
        #    if height <=0 and weight <=0:
         #       flash("Error: Enter valid and positive number")
          #      return redirect(url_for('bmi_calculator'))
           # elif height > 0:
            #    height_m = height/100
             #   bmi =round(weight/(height_m**2),1)
        #except(ValueError,TypeError):
         #   bmi = "Invalid input.Please enter valid number" 
        #return redirect(url_for('bmi_calculator',bmi=bmi))
    #bmi = request.args.get('bmi')
    #return render_template('index.html',bmi=bmi,height=height,weight=weight)
    
    
    if request.method == 'POST':
        weight = request.form.get('weight','')
        height_ft = request.form.get('height_ft','')
        height_in = request.form.get('height_in','')
        
        session['weight'] = weight
        session['height_ft'] = height_ft
        session['height_in'] = height_in
        try:
            weight_val = float(weight)
            height_ft = int(height_ft) if height_ft else 0
            height_in = int(height_in) if height_in else 0
            height_val = ((height_ft * 12 + height_in)*2.54)/100
            if 20 <= weight_val <= 300 and 0.5 <= height_val <= 2.5:
                session['bmi'] = round(weight_val/((height_val)**2),2)
                session['bmi_error'] = ''
            else:
                session['bmi_error'] = "Error! Please enter realistic values for height and weight"
        except ValueError:
            session['bmi_error'] = "Invalid input! Please enter values!"
        return redirect(url_for('bmi_calculator'))
    bmi = session.pop('bmi','')
    bmi_error = session.pop('bmi_error','')
    weight = session.pop('weight','')
    height_ft = session.pop('height_ft','')
    height_in = session.pop('height_in','')
    return render_template('index.html',bmi=bmi,bmi_error=bmi_error,weight=weight,height_ft=height_ft,height_in=height_in)

    
    
if __name__ == '__main__':
    app.run(debug=True)