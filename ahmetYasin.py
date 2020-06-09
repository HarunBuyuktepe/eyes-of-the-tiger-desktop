import cv2
import ctypes as ct
import pyautogui
import pygame
import numpy as np
from pymouse import PyMouse
from mouse_handler import MouseHandler
from blink import Blink
from GUI import GUI
from Tiger import Tiger

from multiprocessing import Process, Manager, Value
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import feature_extraction as fe
from subprocess import Popen
import os, signal
import json
import pickle
import psutil


tigerGonna_pid = 0
username = "harun"

class Info(ct.Structure):
    _fields_ = [("image", ((ct.c_ubyte * 3) * 640) * 480),
                ("landmark_2d", (ct.c_float * 2) * 68),
                ("landmark_3d", (ct.c_float * 3) * 68),
                ("gaze_direction_0", (ct.c_float * 3) * 1),
                ("gaze_direction_1", (ct.c_float * 3) * 1),
                ("gaze_angle", (ct.c_float * 2) * 1),
                ("pose", (ct.c_float * 6) * 1),
                ("gaze_direc", (ct.c_float * 2) * 4),
                ("action_units", (ct.c_double * 2) * 18),
                ("align_size", (ct.c_int *2))]

def createCalibrationDots(width, height):
    default_space = 5
    calibrationDots = []
    calibrationDots.append((int(width / 2), default_space))
    calibrationDots.append((int(width / 2), int(height / 2)))
    calibrationDots.append((default_space, default_space))
    calibrationDots.append((default_space, int(height / 2)))
    calibrationDots.append((default_space, height - default_space))
    calibrationDots.append((int(width / 2), height - default_space))
    calibrationDots.append((width - default_space, height - default_space))
    calibrationDots.append((width - default_space, int(height / 2)))
    calibrationDots.append((width - default_space, default_space))
    calibrationDots.append((int(width / 4), int(height / 4)))
    calibrationDots.append((int(width / 4), int(0.75 * height)))
    calibrationDots.append((int(0.75 * width), int(height / 4)))
    calibrationDots.append((int(0.75 * width), int(0.75 * height)))

    return calibrationDots


def getInput():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            inp = pygame.key.name(event.key)
            return inp


mouse_handler = MouseHandler()
blink = Blink(mouse=mouse_handler)

width, height = pyautogui.size()
calibrationDots = createCalibrationDots(width, height)


CppLib = ct.cdll.LoadLibrary('./libFeatureExtraction.so')

image_processing_only_gaze = CppLib.image_processing_only_gaze
image_processing_only_gaze.argtypes = [ct.POINTER(Info)]
image_processing_only_gaze.restype = ct.POINTER(ct.c_ubyte)

init_cpp = CppLib.init_values
init_cpp.argtypes = None
init_cpp.restype = None

align = CppLib.get_align
align.argtypes = [ct.POINTER(Info)]
align.restype = ct.POINTER(ct.c_ubyte)

webcam = cv2.VideoCapture(0)

init_cpp()

info = Info()
info_left = Info()
info_right = Info()

mouse = PyMouse()

tiger = Tiger(width, height, calibrationDots, mouse, image_processing_only_gaze, info, info_left, info_right)

def calibrate(userName):
    print(userName)
    username = userName
    gui = GUI(width=width, height=height)
    i = 0

    while i != len(calibrationDots):
        _, frame = webcam.read()
        gui.drawCircle(calibrationDots[i])
        j = 0
        key = getInput()
        if key == 'a':
            while j != tiger.sample_size_per_dot:
                tiger.getArgs(frame)
                j = j + 1
                _, frame = webcam.read()

            i = i + 1
        elif key == 'escape':
            gui.quit()
            break

    gui.quit()

    tiger.train()
    tiger.verify()
    
    #Save models to seperate folder for each user
    # try:
    #     with open("model_x_"+username+"_.pkl", 'wb') as f:
    #         return pickle.load(tiger.model_x)
    # except FileNotFoundError:
    #     return 0  # start with 0 if no storage present
    print("kaydetme")
    try:
        pickle.dump(tiger.model_x, open( "model_x_"+username+"_.pkl", 'wb'))                        # x coord SVR
        pickle.dump(tiger.model_y, open("model_y_"+username+"_.pkl", 'wb'))                        # y coord SVR
        pickle.dump(tiger.mm_scaler, open("mm_scaler_"+username+"_.pkl", 'wb'))                         # to scale inputs
        pickle.dump(tiger.res_x_scaler, open("res_x_scaler_"+username+"_.pkl", 'wb'))                 # to scale result x
        pickle.dump(tiger.res_y_scaler, open("res_y_scaler_"+username+"_.pkl", 'wb'))                # to scale result y
    except:
        print("kaydedemedi")
        pass
    
                

 

def tigerGonnaHunt():
    print(username)
    # load the model from disk   
    try:            
        tiger.model_x = pickle.load(open( "user_data/model_x_"+username+"_.pkl", 'rb'))               # x coord SVR
        tiger.model_y = pickle.load( open("user_data/model_y_"+username+"_.pkl", 'rb'))                                # y coord SVR
        tiger.mm_scaler = pickle.load(open("user_data/mm_scaler_"+username+"_.pkl", 'rb'))                 # to scale inputs
        tiger.res_x_scaler = pickle.load(open("user_data/res_x_scaler_"+username+"_.pkl", 'rb'))        # to scale result x
        tiger.res_y_scaler = pickle.load(open("user_data/res_y_scaler_"+username+"_.pkl", 'rb'))             # to scale result y
    except Exception as e: 
        print("okutamadım")
    

    # tiger.train()
    # tiger.verify()

    #move_per_frame = 3
    mode = "both"
    lastInput = 98

    i = 1


    counter_left_vis = [0]
    counter_right_vis = [0]
    counter_both_vis = [0]
    run_bool = True

    while True:
        if run_bool:
            # print(run_bool)
            # print("Çalılıyor")
            _, frame = webcam.read()

            cv2.putText(frame, "per frame : " + str(tiger.move_per_frame), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
            cv2.putText(frame, "mode : " + mode, (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
            cv2.putText(frame, "per frame : " + str(tiger.move_per_frame), (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
            #cv2.putText(frame, "thres y : " + str(threshold_y), (10, 115), cv2.FONT_HERSHEY_SIMPLEX, 1, 255)

            cv2.putText(frame, "counter left : {}".format(counter_left_vis[0]), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "counter right : {}".format(counter_right_vis[0]), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
            cv2.putText(frame, "counter both : {}".format(counter_both_vis[0]), (10, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)



            info.image = np.ctypeslib.as_ctypes(frame)
            vis_frame_ptr = image_processing_only_gaze(ct.byref(info))

            leftEye = info.landmark_2d[42:48]   #reel sol
            rightEye = info.landmark_2d[36:42]  #reel sağ

            blink.click(leftEye, rightEye, counter_left_vis, counter_right_vis, counter_both_vis, frame)
            cv2.imshow("live", frame)

            if i == tiger.move_per_frame:
                if mode == "both":
                    tiger.moveMouse(frame)
                    tiger.x_pred_total = 0
                    tiger.y_pred_total = 0
                elif mode == "x":
                    tiger.moveMouseX(frame)
                    tiger.x_pred_total = 0
                    tiger.y_pred_total = 0
                elif mode == "y":
                    tiger.moveMouseY(frame)
                    tiger.x_pred_total = 0
                    tiger.y_pred_total = 0
                i = 1
            else:
                tiger.notMoveMouse(frame)
                i += 1



        key = cv2.waitKey(1)

        if key != -1:
            lastInput = key

        if lastInput == 27:
            break
        elif lastInput == 120:  # x
            mode = "x"
        elif lastInput == 121:  # y
            mode = "y"
        elif lastInput == 98:  # b
            mode = "both"
        elif lastInput == ord('w'):             # increase move per frame number
            tiger.move_per_frame += 1
            lastInput = ord(mode[0])
        elif lastInput == ord('e'):             # decrease move per frame number
            if tiger.move_per_frame > 2:
                tiger.move_per_frame -= 1
            else:
                tiger.move_per_frame = 1
            lastInput = ord(mode[0])
        elif lastInput == ord('p'):     #PAUSE
            run_bool = False
        elif lastInput == ord('r'):     #RESUME
            run_bool = True

def tigerStartToWork():
    tigerGonna = Process(target=tigerGonnaHunt)
    tigerGonna.start()
    tigerGonna_pid = tigerGonna.pid
    print(tigerGonna_pid)
    return tigerGonna_pid


def killTiger(pid):
    print(pid)
    psutil.Process(pid=pid).terminate()

def getUsers():
    users = []
    with open('users.txt', 'r') as reader:
    # Read and print the entire file line by line
        for line in reader:
            line = line.rstrip("\n")
            print(line)
            users.append(line)
    return users

def addUser(user):
    users = getUsers()
    users.append(user)
    with open('users.txt', 'w') as fileWriter:
        for user in users:
            fileWriter.write('%s' % user)

from flask import Flask, request, jsonify
from flask_json import FlaskJSON, JsonError, json_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)





@app.route('/start_without_calibration/<string:user>',methods=['GET'])
def start_without_calibration(user):
    username = user
    pid = tigerStartToWork()
    res = {
        "username": username,
        "pid":pid
    }
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    response.headers['pid'] = pid
    return response


@app.route('/kill_program/<int:pide>',methods=['GET'])
def kill_program(pide):
    
    pid = pide
    killTiger(int(pide))
    res = {
        "Message": "Tiger Stoped",
    }
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response



@app.route('/get_users',methods=['GET'])
def get_users():
    response = app.response_class(
        response=json.dumps(getUsers()),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/calibrate/<string:user>',methods=['GET'])
def calibratet(user):
    username=user
    calibrate(user)
    res = {
        "message": "success",
    }
    response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
    return response

app.run(host='0.0.0.0', port=9099)