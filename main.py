from HardwareInfo import CpuInfo, MemoryInfo, DiskInfo
import time
import os



while True:

    print("===================================================")
    print("================SERVER STATUS======================")
    print(f"CPU USAGE    : {CpuInfo()} % ")
    print(f"Memory USAGE : {MemoryInfo()} % ")
    print(f"Disk space   : {DiskInfo()} % ")
    time.sleep(5)
    os.system('clear')

    











