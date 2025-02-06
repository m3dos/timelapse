import cv2
import time

# Open the webcam (0 is usually the default device)
cap = cv2.VideoCapture(0)

# Set resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Verify Resolution
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f"Resolution set to: {int(width)}x{int(height)}")

# Time interval between shots in seconds
interval = 600

frame_count = 0

try:
    while True:
        ret, frame = cap.read()
        if ret:
            filename = f"time_lapse_{frame_count:05d}.jpg"
            cv2.imwrite(filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            print(f"Saved {filename}")
            frame_count += 1
        else:
            print("Failed to capture image")
        time.sleep(interval)
except KeyboardInterrupt:
    print("Time lapse capture stopped.")
finally:
    cap.release()