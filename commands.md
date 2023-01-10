esptool.py --port COM7 flash_id

esptool.py --port COM7 erase_flash

esptool.py --chip esp32 --port COM7 write_flash -z 0x1000 file.bin

esptool.py --port COM9 --baud 460800 write_flash --flash_size=detect 0 file.bin
