
import time

from adafruit_servokit import ServoKit

# i2c = busio.I2C(board.SCL, board.SDA)
# hat = adafruit_pca9685.PCA9685(i2c)

kit = ServoKit(channels=16)

kit.servo[3].angle = 180
kit.continuous_servo[4].throttle = 1
time.sleep(1)
kit.continuous_servo[4].throttle = -1
time.sleep(1)
kit.servo[3].angle = 0
kit.continuous_servo[4].throttle = 0
