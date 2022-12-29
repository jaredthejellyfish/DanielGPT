import speech_recognition as sr
import whisper
import torch
import numpy as np


def speech_recognizer(energy=300,
                      pause=0.8,
                      dynamic_energy=False,
                      save_file=False):
    audio_model = whisper.load_model("base")

    #load the speech recognizer and set the initial energy threshold and pause threshold
    r = sr.Recognizer()
    r.energy_threshold = energy
    r.pause_threshold = pause
    r.dynamic_energy_threshold = dynamic_energy

    with sr.Microphone(sample_rate=16000) as source:
        while True:
            #get and save audio to wav file
            audio = r.listen(source)
            torch_audio = torch.from_numpy(
                np.frombuffer(audio.get_raw_data(), np.int16).flatten().astype(
                    np.float32) / 32768.0)
            audio_data = torch_audio

            result = audio_model.transcribe(audio_data, fp16=False)

            predicted_text = result["text"]
            return predicted_text


print(speech_recognizer())
