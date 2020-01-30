import bluetooth

name = "P504497"

devices = bluetooth.discover_devices()
address = None

for addr in devices:
    if name == bluetooth.lookup_name(addr):
        address = addr
        break

if address == None:
    print("Failed to find bluetooth speaker")
else:
    print(f"Found address of bluetooth speaker: {address}")
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    print("Connecting...")
    sock.connect((address, 1))

    sock.send("Ping")
    sock.close()
