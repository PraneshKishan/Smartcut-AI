import ffmpeg as ff 
import whisper
import streamlit as st


st.title("Smartcut AI")

input_vid = st.file_uploader("Upload your video here",type='mp4',accept_multiple_files=False)
output_aud = 'smartcut_V2A.mp3'

def vid_to_aud(input_vid, output_path):
    ff.input(input_vid).output(output_aud).run()
    
if input_vid is not None:
    with open('saved_inp_vid.mp4',"wb") as f:
        f.write(input_vid.read())
    result = vid_to_aud('saved_inp_vid.mp4',output_aud)
    st.audio(output_aud)
    

