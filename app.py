from flask import Flask,render_template,redirect,request

app = Flask(__name__)



#this is the  NOT offical page
@app.route("/",methods=['GET','POST'])
def index():
    message = ''
    if request.method == 'POST':
        name_of_medicine = request.form['medicine']
        message = name_of_medicine
    else:
        name_of_medicine = ''  # Provide a default value if the request method is not 'POST'
        
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
    
    