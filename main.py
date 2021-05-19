import serial                                 # add Serial library for Serial communication

Arduino_Serial = serial.Serial('com3',9600)  #Create Serial port object called arduinoSerialData
print (Arduino_Serial.readline())               #read the serial data and print it as line
print ("Enter 1 to ON LED and 0 to OFF LED")

while 1:
    input_data = input()
    print ("you entered", input_data)
    if (str(input_data) == 'A'):
        Arduino_Serial.write(b'A')
        print ("LED ON")
        print('\n')

    if (str(input_data) == 'B'):
        Arduino_Serial.write(b'B')
        print ("LED OFF")
        print('\n')

    if (str(input_data) == 'C'):
        Arduino_Serial.write(b'C')
        print ("LED ON")
        print('\n')

    if (str(input_data) == 'D'):
        Arduino_Serial.write(b'D')
        print ("LED OFF")
        print('\n')

    if (str(input_data) == 'E'):
        Arduino_Serial.write(b'E')
        print ("LED ON")
        print('\n')

    if (str(input_data) == 'F'):
        Arduino_Serial.write(b'F')
        print ("LED OFF")
        print('\n')