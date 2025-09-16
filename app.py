#(python)

from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)

@app.route('/' ,methods=['GET','POST'])
def bmi_calculator():
    bmi = None
    if request.method == 'POST' and 'weight' and 'height' in request.form:
        weight = request.form.get('weight')
        height = request.form.get('height')
        try:
            weight = float(weight)
            height = float(height)
            if height <=0 and weight <=0:
                flash("Error: Enter valid and positive number")
                return redirect(url_for('bmi_calculator'))
            elif height > 0:
                height_m = height/100
                bmi =round(weight/(height_m**2),1)
        except(ValueError,TypeError):
            bmi = "Invalid input.Please enter valid number" 
        return redirect(url_for('bmi_calculator',bmi=bmi))
    bmi = request.args.get('bmi')
    return render_template('index.html',bmi=bmi)

#@app.errorhandler(404)
#def page_not_found():
    
        

    
if __name__ == '__main__':
    app.run(debug=True)