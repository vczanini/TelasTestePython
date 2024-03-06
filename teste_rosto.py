import cv2
import mediapipe as mp
import pyautogui
import time
import os
import numpy as np

'''
O QUE FAZER AQUI.
DEFINIR OS PONTOS  MAXIMOS DA NOSSA TELA
PEGAR O VALOR PRA CIMA E PARA A ESQUERDA PARA DEFINIR ONDE COMEÇA NOSSO FRAME
PEGAR OS OUTROS VALORES E SUBTRAIR PARA SABER A AREA
Xini - Xfinal = areaX
Yni - Yfinal = areaY.
Anotar os dadaos em um bloco de notas e passar para o teste_pisca.py
'''

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks = True)
screen_w, screen_h = pyautogui.size()

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape
    
    if landmark_points:
       landmarks = landmark_points[0].landmark

       for id, landmark in enumerate(landmarks[5:6]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            #print(landmark.x, landmark.y)
            cv2.circle(frame, (x,y), 3, (0,255,0))
            if id == 0:
                screen_x = (screen_w/frame_w) * x
                screen_y = (screen_h/frame_h) * y
                pyautogui.moveTo(screen_x,screen_y)
                print(x, y)
    cv2.imshow('Eye Controlled Mouse', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('c'):
        break


