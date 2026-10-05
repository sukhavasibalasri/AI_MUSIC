import json
import os
import secrets
import urllib.error
import urllib.request


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MUSIC_DIR = os.path.join(
    os.path.abspath(os.environ.get("APP_DATA_DIR", BASE_DIR)),
    "music"
)

MOOD_SONGS = {
    "happy": (
        "Create an original short upbeat pop song with clearly sung vocals and a catchy chorus. "
        "Mood: joyful, hopeful, and celebratory. Bright piano, warm bass, crisp drums, and a memorable melody. "
        "Write and sing original lyrics about finding sunshine and sharing a happy moment. "
        "Use a friendly expressive lead vocal. Complete song, not an instrumental."
    ),
    "sad": (
        "Create an original short emotional ballad with clearly sung vocals and a memorable chorus. "
        "Mood: wistful and vulnerable, but gently hopeful. Intimate piano, soft strings, and restrained drums. "
        "Write and sing original lyrics about working through a difficult day and finding the strength to continue. "
        "Use a tender expressive lead vocal. Complete song, not an instrumental."
    ),
    "relaxed": (
        "Create an original short relaxed song with clearly sung vocals and a gentle chorus. "
        "Mood: peaceful, warm, and unhurried. Soft acoustic guitar, mellow keys, and subtle percussion. "
        "Write and sing original lyrics about slowing down, breathing, and enjoying a quiet moment. "
        "Use a soft intimate lead vocal. Complete song, not an instrumental."
    ),
    "romantic": (
        "Create an original short romantic song with clearly sung vocals and a heartfelt chorus. "
        "Mood: tender and affectionate. Warm piano, soft strings, gentle bass, and a flowing melody. "
        "Write and sing original lyrics about two people sharing a meaningful moment together. "
        "Use an expressive intimate lead vocal. Complete song, not an instrumental."
    ),
    "energetic": (
        "Create an original short high-energy pop-rock song with clearly sung vocals and an anthemic chorus. "
        "Mood: bold, driven, and empowering. Punchy drums, electric guitar, strong bass, and a dynamic melody. "
        "Write and sing original lyrics about taking action and moving forward with confidence. "
        "Use a powerful expressive lead vocal. Complete song, not an instrumental."
    ),
}


class SongGenerationError(Exception):
    pass


class SongGenerationNotConfigured(SongGenerationError):
    pass


def generate_ai_song(mood):
    mood = mood.lower()
    if mood not in MOOD_SONGS:
        raise ValueError(f"Unsupported song mood: {mood}")

    api_key = os.environ.get("ELEVENLABS_API_KEY")
    if not api_key:
        raise SongGenerationNotConfigured(
            "AI vocal songs are not configured yet. Add ELEVENLABS_API_KEY to the Render service environment."
        )

    request_body = json.dumps({
        "model_id": "music_v2_5",
        "music_length_ms": 60000,
        "force_instrumental": False,
        "prompt": MOOD_SONGS[mood],
    }).encode("utf-8")
    generation_request = urllib.request.Request(
        "https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128",
        data=request_body,
        headers={
            "Content-Type": "application/json",
            "xi-api-key": api_key,
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(generation_request, timeout=180) as response:
            song_audio = response.read()
    except urllib.error.HTTPError as error:
        detail = error.read(1000).decode("utf-8", errors="replace")
        raise SongGenerationError(
            f"AI song service returned HTTP {error.code}: {detail}"
        ) from error
    except urllib.error.URLError as error:
        raise SongGenerationError(
            f"Could not connect to the AI song service: {error.reason}"
        ) from error

    if not song_audio:
        raise SongGenerationError("The AI song service returned an empty audio track.")

    os.makedirs(MUSIC_DIR, exist_ok=True)
    filename = f"ai_song_{mood}_{secrets.token_hex(8)}.mp3"
    with open(os.path.join(MUSIC_DIR, filename), "wb") as track:
        track.write(song_audio)

    return f"/music/{filename}"
