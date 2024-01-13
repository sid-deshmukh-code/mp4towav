import os
import subprocess

def convert_mp4_to_wav(input_file, output_file):
    # Ensure FFmpeg is installed
    try:
        subprocess.run(['ffmpeg', '-version'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError:
        print("FFmpeg is not installed. Please install it: https://ffmpeg.org/download.html")
        return

    # Convert MP4 to WAV using FFmpeg
    command = f'ffmpeg -i "{input_file}" -acodec pcm_s16le -ar 44100 -ac 1 "{output_file}"'
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Specify the input MP4 file and the desired output WAV file
    input_file_path = "Lover - Taylor Swift (Lyrics).mp4"
    output_file_path = "woow.wav"

    convert_mp4_to_wav(input_file_path, output_file_path)
