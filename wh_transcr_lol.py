import whisper

# Load a larger Whisper model
model = whisper.load_model("medium")

# Load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("data/as1.mp3")
audio = whisper.pad_or_trim(audio)

# Make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# Detect the spoken language
_, probs = model.detect_language(mel)
detected_language = max(probs, key=probs.get)
print(f"Detected language: {detected_language}")

# Decode the audio with options
options = whisper.DecodingOptions(fp16=False)  # Set fp16 to False if running on CPU
result = whisper.decode(model, mel, options)

# Print the recognized text
print(result.text)
