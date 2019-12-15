from flask import Flask, render_template, url_for, jsonify, request
import unplagiarize as up

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("main.html")
    

@app.route('/unplagiarize', methods=['POST'])
def unplagiarize():
    text = request.json["text"]
    print(text)
    new_text = up.unplagiarize(text)
    print(new_text)        
    return jsonify({'text': new_text}), 201

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5002, debug=True)
