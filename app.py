import cv2
import mediapipe as mp

# Inicializar MediaPipe para la detección de caras, manos y poses
mp_face_detection = mp.solutions.face_detection
mp_hands = mp.solutions.hands
mp_pose = mp.solutions.pose

# Configurar modelos de MediaPipe
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Iniciar la captura de video
cap = cv2.VideoCapture(0)  # Usa la cámara principal

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a RGB (MediaPipe lo requiere)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # 1. Detección Facial
    face_results = face_detection.process(rgb_frame)
    if face_results.detections:
        for detection in face_results.detections:
            # Dibujar el cuadro de detección
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = frame.shape
            bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                   int(bboxC.width * iw), int(bboxC.height * ih)
            cv2.rectangle(frame, bbox, (0, 255, 0), 2)
            cv2.putText(frame, 'Face', (bbox[0], bbox[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 2. Seguimiento de Manos
    hand_results = hands.process(rgb_frame)
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            cv2.putText(frame, 'Hand', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # 3. Seguimiento de Cuerpo (Pose)
    pose_results = pose.process(rgb_frame)
    if pose_results.pose_landmarks:
        mp.solutions.drawing_utils.draw_landmarks(frame, pose_results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.putText(frame, 'Pose', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Mostrar el video con las detecciones
    cv2.imshow('Object Detection', frame)

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()