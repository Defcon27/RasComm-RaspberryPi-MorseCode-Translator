import RPi.GPIO as GPIO
import time
import sys
from morse_code_trans import text2morse_trans
from morse_code_trans import print_morse


PIN = 13
UNIT_TIME = 0.25


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(PIN, GPIO.OUT)


def morse_dot():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(UNIT_TIME)


def morse_dash():
    GPIO.output(PIN, GPIO.HIGH)
    time.sleep(UNIT_TIME*3)


def morse_char_gap():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(UNIT_TIME*3)


def morse_word_gap():
    GPIO.output(PIN, GPIO.LOW)
    time.sleep(UNIT_TIME*7)


text = "hey there"  # input()
morse_code = text2morse_trans(text)
# print(morse_code)


def transmit_morse(morse_code_list):

    for word in morse_code_list:
        if word == " ":
            morse_word_gap()

        else:
            for char in word:
                if char == ".":
                    morse_dot()
                    morse_char_gap()
                elif char == "-":
                    morse_dash()
                    morse_char_gap()
                else:
                    continue


transmit_morse(morse_code)
