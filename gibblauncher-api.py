from flask import Flask, jsonify, request
import time
import random
import os
import hawkeye


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

    bounces = hawkeye.get_bounces()

    response_bounces = {
        'bounces': [
            {
              'x': bounces[0][0],
              'y': bounces[0][1],
            },
            {
              'x': bounces[1][0],
              'y': bounces[1][1],
            },
            {
              'x': bounces[2][0],
              'y': bounces[2][1],
            },
            {
              'x': bounces[3][0],
              'y': bounces[3][1],
            },
            {
              'x': bounces[4][0],
              'y': bounces[4][1],
            },
            {
              'x': bounces[5][0],
              'y': bounces[5][1],
            },
            {
              'x': bounces[6][0],
              'y': bounces[6][1],
            },
            {
              'x': bounces[7][0],
              'y': bounces[7][1],
            },
            {
              'x': bounces[8][0],
              'y': bounces[8][1],
            },
            {
              'x': bounces[9][0],
              'y': bounces[9][1],
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
    print(response_bounces)
    return response_bounces
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')