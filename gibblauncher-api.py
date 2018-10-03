from flask import Flask, jsonify, request
import time
import random


app = Flask(__name__)

response_bounces = {
        'bounces': [
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
            {
              'x': random.randint(-100,100),
              'y': random.randint(-100,100),
            },
        ]
    }

@app.route('/', methods=['GET'])
def hello():
    return jsonify({'data': "Get Confirm!"})


@app.route('/', methods=['POST'])
def set_players():
    """
    {
        'id': 12,
        'position': -1,
        'shots': [
            50, 12, 33, 77
        ]
    }
    """
    # Sleep to simulate image processing
    time.sleep(20)

    # Print request to confirm post data
    print(request.json)

    # Save in file
    """
    {
        'bounces': [
            {
              'x': 50,
              'y': 30,
            },
            {
              'x': -1,
              'y': -1,
            },...
        ]
    }
    """
    return jsonify(response_bounces)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
