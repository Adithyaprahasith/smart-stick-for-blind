import RPi.GPIO as GPIO
import time
import pyttsx
engine = pyttsx.init()
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
VIB=21
while 1:

    GPIO.setmode(GPIO.BCM)
    print "Distance Measurement In Progress"
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    GPIO.setup(VIB,GPIO.OUT)
    GPIO.output(TRIG, False)
    print "Waiting For Sensor To Settle"
    time.sleep(1)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    print "Distance:",distance,"cm"
    if distance <= 100:
        GPIO.output(VIB,GPIO.HIGH)
        engine.say("Alert less than 1 metre")
        engine.runAndWait()
        time.sleep(1)
        GPIO.output(VIB,GPIO.LOW)
    GPIO.cleanup()
