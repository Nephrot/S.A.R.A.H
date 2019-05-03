#!/usr/bin/env python3
import numpy as np
import sounddevice as sd

duration = 100000 #in seconds

def audio_callback(indata, frames, time, status):
   volume_norm = np.linalg.norm(indata) * 5
   t  = ("||" * int(volume_norm))
   print(t)


stream = sd.InputStream(callback=audio_callback)
with stream:
   sd.sleep(duration * 1000)