from bluetooth import *
 
#######################################################
# Scan
#######################################################
 
target_name = "TOOTHTEST2"   # target device name
target_address = None
port = 1         # RFCOMM port
 
nearby_devices = discover_devices()
 
# scanning for target device
for bdaddr in nearby_devices:
    print(lookup_name( bdaddr ))
    if target_name == lookup_name( bdaddr ):
        target_address = bdaddr
        break
 
if target_address is not None:
    print('device found. target address %s' % target_address)
else:
    print('could not find target bluetooth device nearby')
 
#######################################################
# Connect
#######################################################
 
# establishing a bluetooth connection
try:
    sock=BluetoothSocket( RFCOMM )
    print('a')
    sock.connect((target_address, port))
    print('b') 
    while True:         
        try:
            print('c')
            recv_data = sock.recv(1024)
            print(recv_data)
            sock.send(recv_data)
        except KeyboardInterrupt:
            print("disconnected")
            sock.close()
            print("all done")
except btcommon.BluetoothError as err:
    print('An error occurred : %s ' % err)
    pass
