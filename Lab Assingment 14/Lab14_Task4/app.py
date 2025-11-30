from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    print("NEW LOGIN!")
    print("Roll No :", username)
    print("Password :", password)
    print("SUCCESS!")
    
    return "<h1 style='color:green;text-align:center;margin-top:200px;'>Login Successful!<br>Welcome Zubeda Thasleem (2505B04209)</h1><center><a href='/'>Back</a></center>"

if __name__ == '__main__':
    app.run(debug=True)