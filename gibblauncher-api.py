from flask import Flask, jsonify, request
import time
import random
import os
import hawkeye
import socket

IP_MUTEX = None
app = Flask(__name__)
dictionary_shots_position = {(2, 'Forehand Cruzado - Longo'): 'a', 
                             (2, 'Backhand Cruzado - Centro'): 'b',
                             (2, 'Backhand Paralelo - Longo'): 'c',
                             (2, 'Forehand Cruzado - Curto'): 'd',
                             (2, 'Backhand Paralelo - Curto'): 'e',
                             (1, 'Forehand Cruzado - Longo'): 'f',
                             (1, 'Backhand Paralelo - Centro'): 'g',
                             (1, 'Backhand Cruzado - Longo'): 'h',
                             (1, 'Forehand Cruzado - Curto'): 'i',
                             (1, 'Backhand Cruzado - Curto'): 'j',
                             (0, 'Forehand Paralelo - Longo'): 'k',
                             (0, 'Backhand Cruzado - Centro'): 'l',
                             (0, 'Backhand Cruzado - Longo'): 'm',
                             (0, 'Forehand Paralelo - Curto'): 'n',
                             (0, 'Backhand Cruzado - Curto'): 'o'}

@app.route('/', methods=['GET'])
def hello():
  return jsonify({'data': "Get Confirm!"})


@app.route('/', methods=['POST'])
def start_request():
  global IP_MUTEX
  requestIP = str(request.get_json()['ip'])

  if IP_MUTEX == None or IP_MUTEX == requestIP:
    # print("IP_MUTEX = " + str(IP_MUTEX))
    IP_MUTEX = requestIP
    listOfPlay = getPlay(request)
    #TODO put method call file C passing listOfPlay
    response = set_players()
  else :
    response = checkIp(requestIP)
  # Change local
  create_socket()
  
  return jsonify(response)


def getPlay(request):
  position = request.get_json()['launcherPosition']
  
  listOfShots = request.get_json()['shots']
  
  listOfConvertShots = []

  for shot in listOfShots:
    listOfConvertShots.append(dictionary_shots_position.get((position, shot)))

  print(listOfConvertShots)

  return listOfConvertShots

def checkIp(requestIP):
  global IP_MUTEX
  if isAvailable() != 0 :
    # print("verificou o ip")
    responseJson = set_players()
    IP_MUTEX = requestIP 
  else :
    responseJson = {'data': "Ocupado!"}
    print("Ocupado...")

  return responseJson

def isAvailable() :
  response = os.system("ping -c 1 " + IP_MUTEX)
  # print("Response ping: " + str(response))
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
    # print(request.json)
 
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

    # print("\n")
    # print(response_bounces)
    return response_bounces
    

def create_socket():
  s = socket.socket()
  s.connect((IP_MUTEX , 4444))
  s.send("Você é um batatão! Errou quase Tudo.".encode())
  s.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0')