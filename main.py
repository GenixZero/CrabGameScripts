import pymem
import re

pm = pymem.Pymem('Crab Game.exe')
client = pymem.process.module_from_name(pm.process_handle, 'GameAssembly.dll')

print('Crab Game Cheats\nTo disable you have to restart your game.\n')
print('[1] CE Speed Hack Bypass')
print('[2] FastSlap')
print('[3] Air Jump')
print('[4] Anti KB')

engine = False
fastSlap = False
airJump = False
antiKb = False

while True:
    e = int(input("Enter Cheat ID (EG. 1): "))
    if e == 1:
        if not engine:
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\x40\x53\x48\x83\xEC\x20\x48\x8B\xD9\x48\x85\xC9\x74\x71', clientModule).start()

            pm.write_bytes(address, b"\xC3\x90", 2)
            print('Enabled CE Speed Hack Bypass.')
            engine = True
        else:
            print('CE Speed Hack Bypass is already enabled.')
    elif e == 2:
        if not fastSlap:
            fastSlap = True
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\xC6\x43\x24\x00\x48\x8B\xCB', clientModule).start() + 3

            pm.write_uchar(address, 1)
            print('Enabled Fast Slap.')
        else:
            print('Fast Slap is already enabled.')
    elif e == 3:
        if not airJump:
            airJump = True
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\x80\xBB.....\x74\x09\x80\xBB.....', clientModule).start()
            pm.write_bytes(address, b"\x90\x90\x90\x90\x90\x90\x90\x90\x90", 9)
            print('Enabled Air Jump.')
        else:
            print('Air Jump is already enabled.')
    elif e == 4:
        if not antiKb:
            antiKb = True
            clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
            address = client.lpBaseOfDll + re.search(rb'\x48\x89\x5C\x24.\x48\x89\x74\x24.\x57\x48\x83\xEC.\x80\x3D.....\x48\x8B\xF2\x48\x8B\xD9\x75.\x48\x8D\x0D....\xE8....\x48\x8D\x0D....\xE8....\xC6\x05.....\x48\x8B\x7B',
                                                    clientModule).start()

            pm.write_bytes(address, b"\xC3\x90\x90\x90\x90", 5)
            print('Enabled Anti KB.')
        else:
            print('Anti KB is already enabled.')
