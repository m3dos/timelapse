import cv2
import os
import datetime
import time

# Time interval between shots in seconds (600 seconds = 10 minutes)
interval = 600
save_path = "timelapse_images"
save_count = 1260  # Starting count - using this until we implement a better way to track where the last execution left off.  ffmpeg needs contiguous file names.

# Define disabled period hours (24 hour clock) set these to the same value to disable the feature.
disabled_start_hour = 2
disabled_end_hour = 8

print("Initializing webcam...")
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
print("Webcam initialized and resolution set.")

if not os.path.exists(save_path):
    os.makedirs(save_path)

last_saved = datetime.datetime.now()
disabled = False

print(f"Beginning Capture Every {interval} Seconds...")
try:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture image")
            continue

        cv2.imshow('Video Feed', frame)
        
        now = datetime.datetime.now()
        current_hour = now.hour

        # Determine if we are in the disabled period.
        if disabled_start_hour < disabled_end_hour:
            # The period does NOT span midnight. Set the disabled flag based on the current hour.
            disabled = disabled_start_hour <= current_hour < disabled_end_hour
        else:
            # The period DOES span midnight. Set the disabled flag based on the current hour.
            disabled = current_hour >= disabled_start_hour or current_hour < disabled_end_hour

        # If everything is good, save the image.
        if not disabled and (now - last_saved).total_seconds() >= interval:
            filename = os.path.join(save_path, f"time_lapse_{save_count:05d}.jpg")
            cv2.imwrite(filename, frame, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
            print(f"{now} Image saved: {filename}")
            save_count += 1
            last_saved = now

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
        time.sleep(0.018)

except KeyboardInterrupt:
    print("Time lapse capture stopped.")
finally:
    cap.release()
    cv2.destroyAllWindows()
    print("Capture ended.")