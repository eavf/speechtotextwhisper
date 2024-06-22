import whisper

model = whisper.load_model("base")
result = model.transcribe("data/as1.mp3")
print(result["text"])