import ffmpeg as ff
import whisper
import json

model = whisper.load_model("small")

output_aud = 'smartcut_V2A.mp3'

def vid_to_aud(input_video_path, output_path):
    ff.input(input_video_path).output(output_path).run()

def process_video(input_vid_path):
    vid_to_aud(input_vid_path, output_aud)
    
    transcription_result = model.transcribe(output_aud, word_timestamps=True)

    for segment in transcription_result["segments"]:
        start_time = segment["start"]
        end_time = segment["end"]
        text = segment["text"]
        print(f"{start_time}s - {end_time}s: {text}")
        
       
# Example usage:
input_vid_path = 'saved_inp_vid.mp4'  # Specify the path to your input video
process_video(input_vid_path)
