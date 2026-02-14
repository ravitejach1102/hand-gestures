import mediapipe as mp

print("MediaPipe path:", mp.__file__)
print("Has solutions:", hasattr(mp, "solutions"))