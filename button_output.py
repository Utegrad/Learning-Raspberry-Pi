#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import sys
import os

class ButtonPush():
    def __init__(self):
        self.in_channel = 24
        self.out_channel = 4
        self.count = 0
                
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.IN)
        GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)

    def toggle_out(self, channel):
        self.report_out(self.out_channel)
        GPIO.output(channel, not GPIO.input(channel))

    def report_out(self, channel):
        state = GPIO.input(channel)
        print("State of channel " + str(channel) + " : " + str(state) + ".")
    
    def get_out(self, channel):
        state = GPIO.input(channel)
        return state

    def watch_input(self):
        try:
            while True:
                input_value = GPIO.input(self.in_channel) 
                if (input_value == True):
                    self.count = self.count + 1
                    print("Button pressed " + str(self.count) + " times.")
                    self.toggle_out(self.out_channel)
                    time.sleep(0.5)
                time.sleep(0.05)
        except Exception, e:
            GPIO.cleanup( [4, 24] )
            top = traceback.extract_stack()[-1]
            detail = " ".join([type(e).__name__, os.path.basename(top[0]), ])
            message = "Exception: " + repr(e) + " : " + detail


def main():
    button_push = ButtonPush()
    button_push.watch_input()
     

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted")
        GPIO.cleanup( [4, 24] )
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


