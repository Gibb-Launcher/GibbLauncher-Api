from flask import Flask, jsonify, request
import time
import random
import os

IP_MUTEX = None
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
  return jsonify({'data': "Get Confirm!"})


@app.route('/', methods=['POST'])
def start_request():
  global IP_MUTEX
  requestIP = str(request.get_json()['ip'])

  if IP_MUTEX == None or IP_MUTEX == requestIP:
    print("IP_MUTEX = " + str(IP_MUTEX))
    IP_MUTEX = requestIP
    response = set_players()
  else :
    response = checkIp(requestIP)

  return jsonify(response)

def checkIp(requestIP):
  global IP_MUTEX
  if isAvailable() != 0 :
    print("verificou o ip")
    responseJson = set_players()
    IP_MUTEX = requestIP 
  else :
    responseJson = {'data': "Ocupado!"}
    print("Ocupado...")

  return responseJson

def isAvailable() :
  response = os.system("ping -c 1 " + IP_MUTEX)
  print("Response ping: " + str(response))
  return response

def set_players():
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
    time.sleep(2)

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
    return response_bounces
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')