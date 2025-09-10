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
frame_h, frame_w = frame.shape[:2]

# Loop principal
while True:
    _, img = cam.read()
    img = cv2.flip(img, 1)
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = face_mesh.process(rgb_img)
    landmark_points = results.multi_face_landmarks

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # identificando pontos necessários
        iris_and_mouth = [landmarks[145], landmarks[159], landmarks[14], landmarks[13]]

        # Checar se a boca esta aberta
        distancia_da_boca = iris_and_mouth[-2].y - iris_and_mouth[-1].y
        print(distancia_da_boca)

        for lm in landmarks:
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            cv2.circle(img, (x, y), 2, (255, 255, 0))

    cv2.imshow('Imagem', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break