from flask import Flask, render_template, request
import ciphers

app = Flask(__name__)

@app.route('/encryptions', methods=["GET", "POST"])
def web():
    with app.app_context():
        output = None 

        if request.method == "POST":
            input_type = request.form["input_type"]
            user_input = request.form["user_input"]
            key_caesar = int(request.form["key_caesar"])
            action = request.form["action"]

            if input_type == "caesar":
                if action == "encrypt":
                    output = ciphers.caesarCipherEncrypt(user_input, key_caesar)
                elif action == "decrypt":
                    output = ciphers.caesarCipherDecrypt(user_input, key_caesar)

        return render_template('index.html', output=output)
