import cv2, sys
from pyzbar.pyzbar import decode, ZBarSymbol

# Write Recognized
log = open('codes.log', 'w')

# Open the default camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_CONTRAST, 100)
cam.set(cv2.CAP_PROP_SATURATION, 0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

last_data = ""

while True:
    ret, frame = cam.read()

    barcodes = decode(frame)

    if barcodes:
        if barcodes[0].data == b'0733968975478':
            break


        if last_data != barcodes[0].data:
            last_data = barcodes[0].data
            print(str(last_data) + " scanned!")

# Release the capture and writer objects
cam.release()
log.close()
cv2.destroyAllWindows()