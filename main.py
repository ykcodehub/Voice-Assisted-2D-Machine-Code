import speech_recognition as sr
import time
import serial
import subprocess
def generate_gcode(shape):
    if shape == "square":
        import serial
        import time

        serial_port = 'COM6'
        baud_rate = 115200
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2)
        square_size = 20
        feed_rate = 300
        start_point = (0,0)
        ser.write(("G0 X{} Y{} F{}\n".format(start_point[0], start_point[1], feed_rate)).encode())
        for corner in [(square_size, 0), (square_size, square_size), (0, square_size), (0, 0)]:
            ser.write(("G1 X{} Y{} F{}\n".format(corner[0], corner[1], feed_rate)).encode())
        ser.write(("G1 X{} Y{} F{}\n".format(start_point[0], start_point[1], feed_rate)).encode())
        time.sleep(2)

        ser.close()


    elif shape == "triangle":
        import serial
        import time
        serial_port = 'COM6'
        baud_rate = 115200
        ser = serial.Serial(serial_port, baud_rate)
        time.sleep(2)

        vertex1 = (20, 20)
        vertex2 = (40, 40)
        vertex3 = (10, 40)
        # vertex1 = (0, 0)
        # vertex2 = (40, 0)
        # vertex3 = (20, 20)

        feed_rate = 700

        ser.write(("G0 X{} Y{} F{}\n".format(vertex1[0], vertex1[1], feed_rate)).encode())

        ser.write(("G1 X{} Y{} F{}\n".format(vertex2[0], vertex2[1], feed_rate)).encode())
        ser.write(("G1 X{} Y{} F{}\n".format(vertex3[0], vertex3[1], feed_rate)).encode())
        ser.write(("G1 X{} Y{} F{}\n".format(vertex1[0], vertex1[1], feed_rate)).encode())

        ser.write(("G1 X0 Y0 F{}\n".format(feed_rate)).encode())

        time.sleep(2)

    elif shape=="hello":
        print("yes")
    else:
        gcode = ""


def send_gcode(gcode):
    serial_port = 'COM6'

    baud_rate = 115200
    ser = serial.Serial(serial_port, baud_rate)
    time.sleep(2)
    gcode_command = "G0 X10 Y10"
    ser.write((gcode + '\n').encode())
    time.sleep(2)
    ser.close()

recognizer = sr.Recognizer()
while True:
    with sr.Microphone() as source:
        print("Listening.......")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        if command == "exit":
            print("Exiting...")
            break
        else:
            gcode = generate_gcode(command)
            print(gcode)
            if gcode:
                send_gcode(gcode)
            else:
                print("Invalid command.")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand your command.")
    except sr.RequestError as e:
        print("Error:", e)