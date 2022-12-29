#!/usr/bin/env python3
import struct
import pyaudio
import pvporcupine
import os

porcupine = None
PyAudio = None
audio_stream = None

porcupine_key = os.environ.get("PORCUPINE_KEY")

try:
    porcupine = pvporcupine.create(
        keyword_paths=["../porcupine_keywords/hey-daniel_en_mac_v2_1_0.ppn"],
        access_key=porcupine_key)

    PyAudio = pyaudio.PyAudio()

    audio_stream = PyAudio.open(rate=porcupine.sample_rate,
                                channels=1,
                                format=pyaudio.paInt16,
                                input=True,
                                frames_per_buffer=porcupine.frame_length)

    while True:
        pcm = audio_stream.read(porcupine.frame_length)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print("Hotword Detected")
finally:
    if porcupine is not None:
        porcupine.delete()

    if audio_stream is not None:
        audio_stream.close()

    if PyAudio is not None:
        PyAudio.terminate()
