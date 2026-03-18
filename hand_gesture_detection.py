import cv2
import mediapipe as mp
import webbrowser

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

last_character = None   # track last gesture

def detect_character(landmarks):
    global last_character

    thumb_is_open = False
    index_is_open = False
    middle_is_open = False
    ring_is_open = False
    pinky_is_open = False

    if landmarks[mp_hands.HandLandmark.THUMB_TIP].y < landmarks[mp_hands.HandLandmark.THUMB_MCP].y:
        thumb_is_open = True

    if landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y:
        index_is_open = True

    if landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y:
        middle_is_open = True

    if landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y < landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y:
        ring_is_open = True

    if landmarks[mp_hands.HandLandmark.PINKY_TIP].y < landmarks[mp_hands.HandLandmark.PINKY_PIP].y:
        pinky_is_open = True

    # Default
    current_character = 'Unknown'

    if thumb_is_open and index_is_open and not middle_is_open and not ring_is_open and not pinky_is_open:
        current_character = 'L'
        url = "https://youtube.com"

    elif not thumb_is_open and index_is_open and not middle_is_open and not ring_is_open and not pinky_is_open:
        current_character = 'I'
        url = "https://google.com"

    elif not thumb_is_open and index_is_open and middle_is_open and not ring_is_open and not pinky_is_open:
        current_character = 'V'
        url = "https://linkedin.com"

    elif thumb_is_open and not index_is_open and not middle_is_open and not ring_is_open and not pinky_is_open:
        current_character = 'E'
        url = "https://gmail.com"

    elif thumb_is_open and index_is_open and middle_is_open and ring_is_open and pinky_is_open:
        current_character = '5'
        url = "https://irctc.com"

    elif thumb_is_open and index_is_open and not middle_is_open and not ring_is_open and pinky_is_open:
        current_character = 'Y'
        url = "https://facebook.com"

    else:
        return current_character

    # ✅ Open only if gesture changed
    if current_character != last_character:
        webbrowser.open(url)
        last_character = current_character

    return current_character


with mp_hands.Hands(min_detection_confidence=0.7,
                    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():

        success, frame = cap.read()
        if not success:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = hands.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS
                )

                character = detect_character(hand_landmarks.landmark)

                cv2.putText(
                    image,
                    f'Character: {character}',
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255, 0, 0),
                    2
                )

        cv2.imshow('Hand Gesture Detection', image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()