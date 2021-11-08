#python --version
#pip install flask


from flask import Flask, render_template  
capstone = Flask(__name__)             

@capstone.route("/")                          
def index():                    
    return render_template("index.html")

@capstone.route("/programming")                          
def programming():                    
    return render_template("programming.html")

@capstone.route("/webandappdevelopment")                          
def web():                    
    return render_template("web.html")  

@capstone.route("/microsoft365")                          
def microsoft():                    
    return render_template("microsoft.html")  

@capstone.route("/collaboration")                          
def collaboration():                    
    return render_template("collaboration.html")  


         
capstone.run(debug=True)                   
