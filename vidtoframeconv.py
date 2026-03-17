from moviepy.video.io.VideoFileClip import VideoFileClip
import os
from PIL import Image

def video_to_frames(video_path, output_folder, target_fps):

    print(f"Extracting frames from {video_path} at {target_fps} fps")
    clip = VideoFileClip(video_path)
    duration = clip.duration
    os.makedirs(output_folder, exist_ok=True)

    # Loop through the video and extract frames at target_fps
    for i, t in enumerate(range(0, int(duration * target_fps))):
        print(f"Extracting frame {i+1}/{int(duration * target_fps)}")
        time = t / target_fps  # Convert frame index back to time
        frame = clip.get_frame(time)
        frame_filename = os.path.join(output_folder, f"frame_{i:04d}.png")
        img = Image.fromarray(frame)
        img.save(frame_filename)

    print("Video frames extracted")
    print(f"Frames extracted: {i+1}")

def extract_audio(video_path, output_folder):

    print(f"Extracting audio from {video_path}")
    try:
        os.makedirs(output_folder, exist_ok=True)
        clip = VideoFileClip(video_path)
        if clip.audio is None:
            print("No audio track found in the video.")
            return
        audio_filename = os.path.join(output_folder, "audio.mp3")
        clip.audio.write_audiofile(audio_filename)
        print(f"Audio successfully extracted to {audio_filename}")
    except Exception as e:
        print(f"Error extracting audio: {e}")


