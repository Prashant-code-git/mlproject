## Flask url routing 


from flask import Flask ,render_template,request

## create simple flask application

app = Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "Welcome to Varanasi "

@app.route("/index",methods=["GET"])
def index():
    return "Welcome to Index Varanasi "

#variable rule 
@app.route('/success/<int:score>')
def success(score):
    return "the person has passes and the score is : "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the score is : "+str(score)


@app.route('/form',methods=["GET","POST"])
def form():
    if request.method =="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science =float(request.form['science'])
        history=float(request.form['history'])

        average_marks =(maths+science+history)/3

        return  render_template('form.html',score=average_marks)




if __name__ =="__main__":
    app.run(debug=True)