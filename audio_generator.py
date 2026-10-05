import math
import os
import secrets
import struct


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = os.path.join(
    os.path.abspath(os.environ.get("APP_DATA_DIR", BASE_DIR)),
    "music"
)

MOOD_TRACKS = {
    "happy": {
        "tempo": 112,
        "subdivision": 2,
        "progression": [
            (261.63, 329.63, 392.00),
            (220.00, 261.63, 329.63),
            (174.61, 220.00, 261.63),
            (196.00, 246.94, 293.66),
        ],
        "melody": (523.25, 587.33, 659.25, 783.99, 659.25, 587.33, 523.25, 392.00),
    },
    "sad": {
        "tempo": 68,
        "subdivision": 1,
        "progression": [
            (220.00, 261.63, 329.63),
            (196.00, 246.94, 293.66),
            (174.61, 220.00, 261.63),
            (196.00, 233.08, 293.66),
        ],
        "melody": (440.00, 392.00, 349.23, 329.63, 293.66, 329.63, 392.00, 349.23),
    },
    "relaxed": {
        "tempo": 76,
        "subdivision": 1,
        "progression": [
            (293.66, 349.23, 440.00),
            (261.63, 329.63, 392.00),
            (220.00, 293.66, 349.23),
            (246.94, 293.66, 369.99),
        ],
        "melody": (587.33, 523.25, 440.00, 392.00, 440.00, 523.25, 493.88, 440.00),
    },
    "romantic": {
        "tempo": 84,
        "subdivision": 1,
        "progression": [
            (174.61, 220.00, 261.63),
            (196.00, 246.94, 293.66),
            (146.83, 196.00, 246.94),
            (164.81, 220.00, 261.63),
        ],
        "melody": (523.25, 493.88, 440.00, 392.00, 440.00, 493.88, 587.33, 523.25),
    },
    "energetic": {
        "tempo": 128,
        "subdivision": 2,
        "progression": [
            (329.63, 415.30, 493.88),
            (261.63, 329.63, 392.00),
            (293.66, 369.99, 440.00),
            (220.00, 277.18, 329.63),
        ],
        "melody": (659.25, 783.99, 987.77, 783.99, 880.00, 783.99, 659.25, 493.88),
    },
}


def generate_ambient_track(mood):
    mood = mood.lower()
    if mood not in MOOD_TRACKS:
        raise ValueError(f"Unsupported music mood: {mood}")

    os.makedirs(MUSIC_DIR, exist_ok=True)
    preset = MOOD_TRACKS[mood]
    sample_rate = 22050
    duration = 16.0
    num_samples = int(sample_rate * duration)
    beat_duration = 60.0 / preset["tempo"]
    note_duration = beat_duration / preset["subdivision"]
    pcm_data = bytearray()

    for index in range(num_samples):
        time = index / sample_rate
        beat = time / beat_duration
        chord = preset["progression"][int(beat // 4) % len(preset["progression"])]
        melody_index = int(time / note_duration) % len(preset["melody"])
        melody_phase = (time % note_duration) / note_duration

        pad = sum(
            math.sin(2 * math.pi * frequency * time) * 0.7
            + math.sin(2 * math.pi * frequency * 1.003 * time) * 0.3
            for frequency in chord
        ) / len(chord)
        melody_envelope = min(1.0, melody_phase * 12) * max(0.0, 1.0 - melody_phase)
        melody = math.sin(2 * math.pi * preset["melody"][melody_index] * time)
        pulse = 0.88 + 0.12 * math.sin(2 * math.pi * time * preset["tempo"] / 240)

        envelope = min(1.0, time / 1.5, (duration - time) / 1.5)
        sample = (pad * 0.55 + melody * melody_envelope * 0.24) * pulse * max(0.0, envelope)
        pcm_data.extend(struct.pack("<h", max(-32768, min(32767, int(sample * 22000)))))

    data_size = len(pcm_data)
    header = (
        b"RIFF"
        + struct.pack("<I", 36 + data_size)
        + b"WAVEfmt "
        + struct.pack("<IHHIIHH", 16, 1, 1, sample_rate, sample_rate * 2, 2, 16)
        + b"data"
        + struct.pack("<I", data_size)
    )

    filename = f"mood_{mood}_{secrets.token_hex(8)}.wav"
    with open(os.path.join(MUSIC_DIR, filename), "wb") as track:
        track.write(header)
        track.write(pcm_data)

    return f"/music/{filename}"


if __name__ == "__main__":
    print(f"Generated track: {generate_ambient_track('relaxed')}")
