import cv2

# Load video file
cap = cv2.VideoCapture(0)

# Create background subtractor
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply background subtraction
    fgmask = fgbg.apply(frame)

    # Count non-zero pixels to detect motion
    motion_pixels = cv2.countNonZero(fgmask)

    # Threshold for motion detection
    if motion_pixels > 10000:  # Adjust threshold as needed
        # Motion detected, perform further analysis or classification
        print("Motion detected!")

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgmask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
