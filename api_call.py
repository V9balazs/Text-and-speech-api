import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

from dotenv import load_dotenv
from elevenlabs import Voice, VoiceSettings, play, voices
from elevenlabs.client import ElevenLabs

load_dotenv(".env")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


def avaliable_voices():
    return client.voices.get_all()


def text_to_speech(text, id):
    response = client.text_to_speech.convert(
        voice_id=id,
        output_format="mp3_22050_32",
        enable_logging=False,
        text=text,
        model_id="eleven_turbo_v2_5",
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    play(response)
