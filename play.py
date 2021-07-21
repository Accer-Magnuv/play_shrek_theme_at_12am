from playsound import playsound
from pynput.keyboard import KeyCode, Controller

controller = Controller()

def volumeUp():
    for i in range(50):
        controller.press(KeyCode.from_vk(0xAF))

def play():
    playsound("shrektheme.mp3")

