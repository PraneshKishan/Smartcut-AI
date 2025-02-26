import ffmpeg as ff
import whisper
import streamlit as st
import json

model = whisper.load_model("small")

st.title("Smartcut AI")

input_vid = st.file_uploader("Upload your video here", type='mp4', accept_multiple_files=False)
output_aud = 'smartcut_V2A.mp3'

def vid_to_aud(input_video_path, output_path):
    ff.input(input_video_path).output(output_path).run()

if input_vid is not None:
    with open('saved_inp_vid.mp4', "wb") as f:
        f.write(input_vid.read())

    vid_to_aud('saved_inp_vid.mp4', output_aud)
    
    st.audio(output_aud)

    transcription_result = model.transcribe(output_aud, word_timestamps=True)
    
    # for segment in transcription_result["segments"]:
    #     for word in segment["words"]:
    #         st.write(f"{word['start']}s - {word['end']}s: {word['word']}")


    for segment in transcription_result["segments"]:
        start_time = segment["start"]
        end_time = segment["end"]
        text = segment["text"]
        
        max_chunk_len = 8
        
        words = text.split()
        
        for i in range(0,len(words),max_chunk_len):
            chunks = words[i:i + max_chunk_len]
        
        chunk_start = start_time
        time_step = (end_time - start_time) / len(chunks) #distributing timestamps evenly
        
        for chunk in chunks:
            chunk_end = chunk_start + time_step
            chunk_text = " ".join(chunk)
            st.write(f"{chunk_start:.2f}s - {chunk_end:.2f}s: {chunk_text}")
            chunk_start = chunk_end