import numpy as np
from pyzbar.pyzbar import decode
import pandas as pd
import cv2
from http import server
from http.server import HTTPServer, BaseHTTPRequestHandler
import paho.mqtt.client as paho
import time
import numpy as np
import cv2

def main():
    PORT = 8080
    server = HTTPServer(('', PORT), Handler)
    print('Server Running on port %s' % PORT)
    server.serve_forever()


if __name__ == '__main__':
    main()


# broker= "192.168.1.104"
# port = 2222

# publisher = paho.Client("Python publisher")
# publisher.connect(broker, port)
# Value = 0



df = pd.read_excel('shipmentdata.xlsx')
df_sort = df[df['Induct Station'] == 1]


cap  = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)
cap3 = cv2.VideoCapture(3)



"""video_capture_0 = cv2.VideoCapture(0)
video_capture_1 = cv2.VideoCapture(1)
video_capture_2 = cv2.VideoCapture(2)"""
while True:
    # Capture frame-by-frame
    ret0, frame0 = cap.read()
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    if (ret0):#for induct 1
        # Display the resulting frame
        #cv2.imshow('Cam 0', frame0)
        for barcode in decode(frame0):
            # print(barcode.data)
            # print(barcode.rect)
            myData = barcode.data.decode('utf-8')
            print(myData)
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame0, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(frame0, myData, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)

            print(df[df['Shipment'] == myData])
            comparison_values = df.values == myData
            rows, cols = np.where(comparison_values == True)
            city = df['Destination'][rows]
            station1 = df['Induct Station'][rows]
            station = str(station1)
            print(station1)

            if ("1.0" in station):
                if ("Ahmedabad" in str(city)):
                    print("Ahmedabad")
                    # publisher.publish("RB1/ROBO1", "RB1XABAD")
                    class Handler(BaseHTTPRequestHandler):
                        def do_GET(self):
                            self.send_response(200)
                            self.send_header('content-type', 'text/html')
                            self.end_headers()
                            self.wfile.write('The Package has been delieverd to '.encode())

                if ("Pune" in str(city)):
                    print("Pune")
                    # publisher.publish("RB1/ROBO1", "RB1XPUNE")
                    class Handler(BaseHTTPRequestHandler):
                        def do_GET(self):
                            self.send_response(200)
                            self.send_header('content-type', 'text/html')
                            self.end_headers()
                            self.wfile.write('The Package has been delieverd to '.encode())
                            # self.wfile.write('The Package has been delieverd to '.encode())

                if ("Mumbai" in str(city)):
                    print("Mumbai")
                    # publisher.publish("RB1/ROBO1", "RB1XMUMBAI")

                if ("Delhi" in str(city)):
                    print("Delhi")
                    # publisher.publish("RB1/ROBO1", "RB1XDELHI")
                    # self.wfile.write('The Package has been delieverd to '.encode())

                if ("Kolkata" in str(city)):
                    print("Kolkata")
                    # publisher.publish("RB1/ROBO1", "RB1XKOLKATA")
                    # self.wfile.write('The Package has been delieverd to '.encode())

                if ("Chennai" in str(city)):
                    print("Chennai")
                    
                if ("Bengaluru" in str(city)):
                    print("Bengaluru")
                    # publisher.publish("RB1/ROBO1", "RB1XBENG")
                    # self.wfile.write('The Package has been delieverd to '.encode())

                if ("Jaipur" in str(city)):
                    print("Jaipur")
                    # publisher.publish("RB1/ROBO1", "RB1XJAIPUR")
                    # self.wfile.write('The Package has been delieverd to '.encode())

                if ("Hyderabad" in str(city)):
                    print("Hyderabad")
                    # publisher.publish("RB1/ROBO1", "RB1XHYDER")
                    # self.wfile.write('The Package has been delieverd to '.encode())

            else:
                print("Invalid station")
        cv2.imshow('INDUCT 1', frame0)
        cv2.waitKey(1)

    if (ret1):#for induct 2
        # Display the resulting frame
        #cv2.imshow('Cam 1', frame1)
        #opens
        for barcode in decode(frame1):
            # print(barcode.data)
            # print(barcode.rect)
            myData1 = barcode.data.decode('utf-8')
            print(myData1)
            pts = np.array([barcode.polygon], np.int32)
            pts = pts.reshape((-1, 1, 2))
            cv2.polylines(frame1, [pts], True, (255, 0, 255), 5)
            pts2 = barcode.rect
            cv2.putText(frame1, myData1, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 255), 2)
            #compares the value to give output
            print(df[df['Shipment'] == myData1])
            comparison_values = df.values == myData1
            rows, cols = np.where(comparison_values == True)
            city = df['Destination'][rows]
            station2 = df['Induct Station'][rows]
            station = str(station2)
            print(station2)

            if ("2.0" in station):
                if ("Ahmedabad" in str(city)):
                    print("Ahmedabad")
                    # publisher.publish("RB2/ROBO2", "RB2XABAD")

                if ("Pune" in str(city)):
                    print("Pune")
                    # self.wfile.write('The Package has been delieverd to '.encode())
                if ("Mumbai" in str(city)):
                    print("Mumbai")
                    # self.wfile.write('The Package has been delieverd to '.encode())
                if ("Delhi" in str(city)):
                    print("Delhi")
                    # self.wfile.write('The Package has been delieverd to '.encode())
                if ("Kolkata" in str(city)):
                    print("Kolkata")
                    # self.wfile.write('The Package has been delieverd to '.encode())
                if ("Chennai" in str(city)):
                    print("Chennai")
                    # self.wfile.write('The Package has been delieverd to '.encode())
                if ("Bengaluru" in str(city)):
                    print("Bengaluru")
                    # self.wfile.write('The Package has been delieverd to '.encode())
                if ("Jaipur" in str(city)):
                    print("Jaipur")
                    # self.wfile.write('The Package has been delieverd to '.encode())
                if ("Hyderabad" in str(city)):
                    print("Hyderabad")
                    # self.wfile.write('The Package has been delieverd to '.encode())
            else:
                print("Invalid station")
        cv2.imshow('INDUCT 2 ', frame1)
        cv2.waitKey(1)

    if (ret2):#for arena cam 1
        #Display the resulting frame
        cv2.imshow('ARENA CAM 1', frame2)
    if (ret3):#for arena cam 2
        #Display the resulting frame
        cv2.imshow('ARENA CAM 2', frame3)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
    
    


# When everything is done, release the capture
cap.release()
cap1.release()
cap2.release()
cap3.release()

cv2.destroyAllWindows()