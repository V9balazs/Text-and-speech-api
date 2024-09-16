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
        voice_id="cgSgspJ2msm6clMCkdW9",  # Adam pre-made voice
        output_format="mp3_22050_32",
        enable_logging=False,
        text=text,
        model_id="eleven_turbo_v2_5",  # use the turbo model for low latency
        voice_settings=VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            style=0.5,
            use_speaker_boost=True,
        ),
    )

    # uncomment the line below to play the audio back
    play(response)


def main():
    text_to_speech_file("Szia a nevem Jessica. Örülök, hogy megismerhetlek")


if __name__ == "__main__":
    main()
