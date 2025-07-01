import socket
import cv2
import time

while True:
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SERVER_HOST = 'YOUR_IP'
        SERVER_PORT = 8080
        server_address = (SERVER_HOST, SERVER_PORT)

        client_socket.connect(server_address)
        print("Connected to server")

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        cv2.destroyAllWindows()

        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, encimg = cv2.imencode('.jpg', frame, encode_param)

        client_socket.sendall(encimg.tobytes())

        client_socket.close()
        print("Disconnected from server")

        time.sleep(5)

    except ConnectionRefusedError:
        print("Server is not available. Waiting for 5 seconds...")
        time.sleep(5)

    except Exception as ex:
        print(ex)
        time.sleep(5)
