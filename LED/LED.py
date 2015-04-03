import serial, mosquitto, random

port = serial.Serial("/dev/tty.usbmodem1451",9600,timeout=2)

def messageReceived(broker, obj, msg):
        print("Message " + msg.topic + " containing: " + msg.payload)
        if (msg.payload == 'ON') :
            port.write("1")
        
        elif (msg.payload == 'OFF') :
            port.write("0")


#   Create a client wrapper
client = mosquitto.Mosquitto("FaraSuhaili")

#    Connect to the broker (in this case the local one)
client.connect("127.0.0.1")

client.subscribe("lights")
client.on_message = messageReceived


while (client != None): client.loop()




while True:
    command = raw_input("insert command: ")
    if (command == '1') :
        port.write("1")
    
    elif (command == '0') :
        port.write("0")
