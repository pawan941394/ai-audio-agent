from gtts import gTTS
from agno.tools import Toolkit
from agno.utils.log import logger
import os

class TextToSpeechToolkit(Toolkit):
    def __init__(self, **kwargs):
        super().__init__(name="text_to_speech", tools=[self.generate_speech], **kwargs)
    
    def generate_speech(self, text: str, language: str = 'en', slow: bool = False, filename: str = "generated_audio.mp3") -> str:
        """
        Generate speech from text using Google Text-to-Speech.
        
        Args:
            text: The text to convert to speech
            language: Language code (default: 'en')
            slow: Whether to speak slowly (default: False)
            filename: Output filename (default: 'generated_audio.mp3')
        
        Returns:
            str: Path to the generated audio file
        """
        try:
            logger.info(f"Generating speech for text: {text[:50]}...")
            # Ensure audio_generations directory exists
            os.makedirs("audio_generations", exist_ok=True)
            
            # Create gTTS object
            myobj = gTTS(text=text, lang=language, slow=slow)
            
            # Save to file
            filepath = f"audio_generations/{filename}"
            myobj.save(filepath)
            
            logger.info(f"Audio saved to: {filepath}")
            return f"Audio generated successfully and saved to: {filepath}"
        except Exception as e:
            logger.warning(f"Failed to generate audio: {e}")
            return f"Error generating audio: {str(e)}"