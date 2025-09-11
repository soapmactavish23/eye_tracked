import cv2
import mediapipe as mp
import pyautogui

pyautogui.FAILSAFE = False
SENSIBILIDADE_DO_MODELO = 3

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
        #print(distancia_da_boca)

        if distancia_da_boca > 0.042:
            pass
        else:
            iris_principal = iris_and_mouth[0]
            x = int(iris_principal.x * frame_w) * SENSIBILIDADE_DO_MODELO
            y = int(iris_principal.y * frame_h) * SENSIBILIDADE_DO_MODELO

            pyautogui.moveTo(x, y)

            # Logica de clique
            distancia_da_iris = iris_and_mouth[0].y - iris_and_mouth[1].y

            if distancia_da_iris < 0.008:
                pyautogui.click()
                pyautogui.sleep(1)


        for lm in iris_and_mouth:
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)
            cv2.circle(img, (x, y), 2, (255, 255, 0))

    cv2.imshow('Imagem', img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break