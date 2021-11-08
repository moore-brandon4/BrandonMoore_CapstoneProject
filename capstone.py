#python --version
#pip install flask


from flask import Flask, render_template  
capstone = Flask(__name__)             

@capstone.route("/")                          
def index():                    
    return render_template("index.html")
         
capstone.run(debug=True)                   
