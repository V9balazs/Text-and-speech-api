import os
import uuid
import warnings

warnings.filterwarnings("ignore", category=UserWarning, module="pydantic")

from dotenv import load_dotenv
from elevenlabs import VoiceSettings, play
from elevenlabs.client import ElevenLabs

load_dotenv(".env")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
client = ElevenLabs(api_key=ELEVENLABS_API_KEY)


def text_to_speech_file(text):
    # Calling the text_to_speech conversion API with detailed parameters
    response = client.text_to_speech.convert(
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam pre-made voice
        output_format="mp3_22050_32",
        enable_logging=False,
        text=text,
        model_id="eleven_turbo_v2_5",  # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.1,
            similarity_boost=0.3,
            style=0.2,
            use_speaker_boost=True,
        ),
    )

    # uncomment the line below to play the audio back
    play(response)


def main():
    text_to_speech_file("Hello, this is a test of the text to speech API.")


if __name__ == "__main__":
    print("Program indítása")
    main()
