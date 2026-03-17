import cv2
import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip

def frames_to_video(input_folder, output_video_path, target_fps=24, frame_size=None):
    print(f"Converting frames from {input_folder} to video at {target_fps} fps")

    frame_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.png')])
    
    # If frame_size is not specified, use the size of the first frame
    if frame_size is None and frame_files:
        first_frame = cv2.imread(os.path.join(input_folder, frame_files[0]))
        frame_size = (first_frame.shape[1], first_frame.shape[0])  # (width, height)
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Codec for .mp4 format
    video_writer = cv2.VideoWriter(output_video_path, fourcc, target_fps, frame_size)
    
    #Each frame into the video
    for frame_file in frame_files:
        frame_path = os.path.join(input_folder, frame_file)
        frame = cv2.imread(frame_path)
        video_writer.write(frame)
    
    video_writer.release()
    print(f"Video saved to: {output_video_path}")

def add_audio_to_video(video_path, audio_path, output_video_path):
    print(f"Adding audio from {audio_path} to {video_path}")
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)

    # Match audio duration to video duration
    if audio.duration > video.duration:
        audio = audio.subclipped(0, video.duration)

    video = video.with_audio(audio)
    video.write_videofile(output_video_path, codec="libx264", audio_codec="aac", temp_audiofile="temp-audio.m4a", remove_temp=True)
    print(f"Audio added to video: {output_video_path}")




        
        

