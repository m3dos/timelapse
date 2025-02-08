import cv2
import time
import os
import datetime
import subprocess

# Time interval between shots in seconds (600 seconds = 10 minutes)
interval = 600
save_path = "timelapse_images"

print("Initializing webcam...")
cap = cv2.VideoCapture(0)
print("Webcam initialized.")

# Set the resolution to 1080p
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
print("Resolution set.")

# Create the save_path directory if it doesn't exist
if not os.path.exists(save_path):
    os.makedirs(save_path)

last_saved = time.time()  # Record the time of the last saved frame
save_count = 698  # Start the count from 698
print("Beginning Capture...")
try:
    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Video Feed', frame)
            
            current_time = time.time()
            
            # If current_time - last_saved is greater than the interval, save the frame
            if current_time - last_saved >= interval:
                filename = os.path.join(save_path, f"time_lapse_{save_count:05d}.jpg")
                cv2.imwrite(filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
                print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Saved {filename}")
                save_count += 1
                last_saved = current_time  # Update the time of the last saved frame

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            print("Failed to capture image")
            
except KeyboardInterrupt:
    print("Time lapse capture stopped.")
finally:
    cap.release()
    cv2.destroyAllWindows()