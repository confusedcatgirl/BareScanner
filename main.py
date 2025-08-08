import cv2
from pyzbar.pyzbar import decode

# Open the default camera
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_CONTRAST, 100)
cam.set(cv2.CAP_PROP_SATURATION, 0)

# Get the default frame width and height
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'mp4v')
#out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

while True:
    ret, frame = cam.read()

    detectedBarcodes = decode(frame)

    if detectedBarcodes:
        for barcode in detectedBarcodes:  
          
            # Locate the barcode position in image
            (x, y, w, h) = barcode.rect
            
            # Put the rectangle in image using 
            # cv2 to highlight the barcode
            cv2.rectangle(frame, (x-10, y-10),
                          (x + w+10, y + h+10), 
                          (255, 0, 0), 2)
            
            if barcode.data!="":
              
            # Print the barcode data
                print(barcode.data)
                print(barcode.type)

    #out.write(frame)
    cv2.imshow('Camera', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
#out.release()
cv2.destroyAllWindows()