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
        height = request.form.get('height','')
        
        session['weight'] = weight
        session['height'] = height
        try:
            weight_val = float(weight)
            height_val = float(height)
            if 20 <= weight_val <= 300 and 50 <= height_val <= 250:
                session['bmi'] = round(weight_val/((height_val /100)**2),2)
                session['bmi_error'] = ''
            else:
                session['bmi_error'] = "Error! Please enter realistic values for height and weight"
        except ValueError:
            session['bmi_error'] = "Invalid input! Please enter values!"
        return redirect(url_for('bmi_calculator'))
    bmi = session.pop('bmi','')
    bmi_error = session.pop('bmi_error','')
    weight = session.pop('weight','')
    height = session.pop('height','')
    return render_template('index.html',bmi=bmi,bmi_error=bmi_error,weight=weight,height=height)

    
    
if __name__ == '__main__':
    app.run(debug=True)