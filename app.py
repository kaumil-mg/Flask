from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def start():
    return render_template('/index.html')

@app.route("/marks/<int:score>")
def marks(score):
    return "Congrats you scored is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return 'Person is fail go and study'

@app.route('/sucsess/<int:score>')
def sucsess(score):
    return 'Party de Pandu'


@app.route('/result/<int:score>')
def result(score):
    results=''
    if score < 50:
        results = 'fail'
    else :
        results='sucsess'
    return redirect(url_for(results,score=score))

@app.route('/submmit',methods=['POST','GET'])
def submmit():
    total_score=0
    if request.method=='POST':
        Math = float(request.form['math'])
        science = float(request.form['science'])
        Computer_science = float(request.form['cs'])
        total_score=(Math+science+Computer_science)/3

    res=''
    if total_score>=50:
        res='sucsess'
    else:
        res='fail'

    return redirect(url_for(res,score=total_score))



if __name__=='__main__':
    app.run(debug=True)
