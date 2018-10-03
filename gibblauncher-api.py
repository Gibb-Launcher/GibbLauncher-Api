from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'data': "Get Confirm!"})


@app.route('/', methods=['POST'])
def set_players():
    # Sleep to simulate image processing
    time.sleep(20)

    # Print request to confirm post data
    print(request.json)
    return jsonify({'data': "Post Confirm!"})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
