import os
import subprocess


def volume_up(arg):
    volume = subprocess.check_output(['amixer', 'get', 'Master']).decode("utf-8").split("\n")
    volume = volume[len(volume) - 2].split()
    volume = int(volume[len(volume) - 2][1:3])
    if volume >= 90:
        os.system("pactl set-sink-volume @DEFAULT_SINK@ 100%")
    else:
        os.system("pactl set-sink-volume @DEFAULT_SINK@ +15%")

