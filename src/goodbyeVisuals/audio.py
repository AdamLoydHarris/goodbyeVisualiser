import numpy as np
from pydub import AudioSegment
from scipy.signal import butter, filtfilt
# import pyaudio
import struct
import threading
from typing import List, Tuple
import wave

class AudioProcessor:
    def __init__(self, chunk_size: int = 1024, bass_freq_range: Tuple[int, int] = (20, 150)):
        self.CHUNK = chunk_size
        self.FORMAT = pyaudio.paFloat32
        self.CHANNELS = 1
        self.RATE = 44100
        self.bass_range = bass_freq_range
        
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=self.FORMAT,
            channels=self.CHANNELS,
            rate=self.RATE,
            input=True,
            frames_per_buffer=self.CHUNK
        )
        
        # Create butterworth filter
        nyquist = self.RATE / 2
        low = self.bass_range[0] / nyquist
        high = self.bass_range[1] / nyquist
        self.b, self.a = butter(4, [low, high], btype='band')
        
        self.bass_intensity = 0.0
        self._running = True
        self.thread = threading.Thread(target=self._process_audio)
        self.thread.start()
    
    def _process_audio(self):
        while self._running:
            try:
                # Read audio data
                data = self.stream.read(self.CHUNK, exception_on_overflow=False)
                audio_data = np.frombuffer(data, dtype=np.float32)
                
                # Apply bass filter
                filtered = filtfilt(self.b, self.a, audio_data)
                
                # Calculate RMS of filtered signal
                rms = np.sqrt(np.mean(filtered**2))
                
                # Smooth the intensity value
                self.bass_intensity = 0.7 * self.bass_intensity + 0.3 * rms
                
            except Exception as e:
                print(f"Audio processing error: {e}")
                continue
    
    def get_bass_intensity(self) -> float:
        """Return normalized bass intensity between 0 and 1"""
        return min(1.0, self.bass_intensity * 5)  # Adjust multiplier as needed
    
    def cleanup(self):
        self._running = False
        if self.thread.is_alive():
            self.thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()
