esptool.py --port COM7 flash_id
esptool.py --chip esp32 --port COM7 write_flash -z 0x1000 file.bin