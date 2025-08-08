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

    barcodes = decode(frame, symbols=[])

    if barcodes:
        if barcodes[0].data != "" and last_data != barcodes[0].data:
            last_data = barcodes[0].data
            # Print the barcode data
            log.write(str(barcodes[0].data) + " | " + barcodes[0].type + "\n")
            print("Scanned!")

    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
log.close()
cv2.destroyAllWindows()