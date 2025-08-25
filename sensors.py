import time
import smbus
from smbus2 import SMBus
from mlx90614 import MLX90614
from heartrate_monitor import HeartRateMonitor

# LCD and I2C config
LCD_ADDR = 0x3F
LCD_BACKLIGHTON = 0x08
ENABLE = 0b00000100
E_PULSE = 0.0005
E_DELAY = 0.0005

bus = smbus.SMBus(1)
bus2 = SMBus(1)
sensor = MLX90614(bus2, address=0x5A)

# Heart Rate Monitor
hrm = HeartRateMonitor(print_raw=False, print_result=False)
hrm.start_sensor()

def lcd_byte(bits, mode):
    bits_high = mode | (bits & 0xF0) | LCD_BACKLIGHTON
    bits_low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHTON
    bus.write_byte(LCD_ADDR, bits_high)
    lcd_toggle_enable(bits_high)
    bus.write_byte(LCD_ADDR, bits_low)
    lcd_toggle_enable(bits_low)

def lcd_toggle_enable(bits):
    time.sleep(E_DELAY)
    bus.write_byte(LCD_ADDR, (bits | ENABLE))
    time.sleep(E_PULSE)
    bus.write_byte(LCD_ADDR, (bits & ~ENABLE))
    time.sleep(E_DELAY)

def lcd_init():
    lcd_byte(0x33, 0)
    lcd_byte(0x32, 0)
    lcd_byte(0x06, 0)
    lcd_byte(0x0C, 0)
    lcd_byte(0x28, 0)
    lcd_byte(0x01, 0)
    time.sleep(E_DELAY)

def lcd_string(message, line):
    message = message.ljust(16, " ")
    lcd_byte(0x80 | line, 0)
    for char in message:
        lcd_byte(ord(char), 1)

def get_sensor_data():
    ambient_temp = sensor.get_ambient()
    object_temp = sensor.get_object_1()
    bpm = hrm.bpm
    return ambient_temp, object_temp, bpm

# Initialize LCD
lcd_init()
