from pymodbus.client.sync import ModbusTcpClient
import time

client = ModbusTcpClient('127.0.0.1')
client.connect()
i=1
while 1:
    try:
        response = client.read_holding_registers(address=250, count=1, unit=247)
    except:
        print("No connection")
    else:
        rg = response.registers[0]
        if rg == 247:
            client.write_register(250, i)
            print("zapisal")
        i += 1
    time.sleep(1)

client.close()
