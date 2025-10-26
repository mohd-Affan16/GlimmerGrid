import webrtcvad
import pyaudio
import collections
import sys

# Initialize Voice Activity Detector
vad = webrtcvad.Vad(2)  # Aggressiveness: 0-3 (0=least, 3=most aggressive)

# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000  # webrtcvad works best at 16kHz
FRAME_DURATION = 30  # ms
FRAME_SIZE = int(RATE * FRAME_DURATION / 1000)

# Initialize microphone
pa = pyaudio.PyAudio()
stream = pa.open(format=FORMAT,
                 channels=CHANNELS,
                 rate=RATE,
                 input=True,
                 frames_per_buffer=FRAME_SIZE)

print("🎤 Speak something... (Press Ctrl+C to stop)\n")

try:
    while True:
        frame = stream.read(FRAME_SIZE, exception_on_overflow=False)
        is_speech = vad.is_speech(frame, RATE)

        if is_speech:
            print("🔊 Voice detected!")
        else:
            print("🤫 Silence...")
except KeyboardInterrupt:
    print("\n✅ Stopped by user")
    stream.stop_stream()
    stream.close()
    pa.terminate()
    sys.exit()
