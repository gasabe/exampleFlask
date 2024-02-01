from flask import Flask,render_template

app= Flask(__name__)
@app.route("/")
def index():
    #return "<h1>aguante boquita papa- la mitad +1 </h1>"
    cursos=["PHP","PYTHON","SQL","FLASK","KOTLIN"]
    data={
        "titulo":"index",
        "bienvenida":"Bienvenido la cantidad de cursos que tenemos son ",
        "cursos": cursos,
        "numero_cursos":len(cursos)
    }
    return render_template('index.html',data=data)
if __name__=="__main__":
    app.run(debug=True,port=5000)