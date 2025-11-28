from flask import Flask, render_template, request
import ciphers

app = Flask(__name__)
e, d, n = ciphers.generateKeys()

@app.route('/encryptions', methods=["GET", "POST"])
def web():
    output = None 
    input_type = None
    user_input = None
    key_caesar = None

    if request.method == "POST":
        input_type = request.form["input_type"]
        user_input = request.form["user_input"]
        action = request.form["action"]

        if input_type == "caesar":
            key_caesar = int(request.form["key_caesar"])
            if action == "encrypt":
                output = ciphers.caesarCipherEncrypt(user_input, key_caesar)
            elif action == "decrypt":
                output = ciphers.caesarCipherDecrypt(user_input, key_caesar) 
        
        elif input_type == "rsa":
            if action == "encrypt":
                output = ciphers.encryptRSA(user_input, e, n)
            elif action == "decrypt":
                output = ciphers.decryptRSA(user_input, d, n)

        elif input_type == "hashing":
            if action == "encrypt":
                output = ciphers.hashing(user_input)

    return render_template('index.html', output=output, input_type=input_type, user_input=user_input, key_caesar=key_caesar)
