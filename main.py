import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False

# Lendo a câmera e inicializando a solução
cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

# Coletar o tamanho da nossa tela
tela_w, tela_h = pyautogui.size()

# Coletar especificações da nossa camera
_, frame = cam.read()
frame_h, frame_w = frame.shape
import pdb; pdb.set_trace()

# Loop principal
while True:

    # Esperando a letra q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break