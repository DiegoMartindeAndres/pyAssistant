import os


def volume_down(arg):
    os.system("pactl set-sink-volume @DEFAULT_SINK@ -15%")
