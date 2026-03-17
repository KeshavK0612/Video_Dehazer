import gradio as gr
import cv2
import os
import tempfile
import shutil

import vidtoframeconv as vfc
import frametovidconv as ftc
from dehaze import amef as dh1
import image_dehazer as dh2


def dehaze_video(video_file, model):

    temp_dir = tempfile.mkdtemp()

    input_video = os.path.join(temp_dir, "input.mp4")
    output_video = os.path.join(temp_dir, "output.mp4")

    shutil.copy(video_file, input_video)

    frames_folder = os.path.join(temp_dir, "frames")
    dehazed_folder = os.path.join(temp_dir, "dehazed")

    os.makedirs(frames_folder, exist_ok=True)
    os.makedirs(dehazed_folder, exist_ok=True)

    # IMPORTANT: lower fps for HuggingFace CPU
    target_fps = 10

    # convert video to frames
    vfc.video_to_frames(input_video, frames_folder, target_fps)

    # process frames
    for frame_file in sorted(os.listdir(frames_folder)):

        frame_path = os.path.join(frames_folder, frame_file)
        frame = cv2.imread(frame_path)

        if model == "AMEF":
            dehazed_frame = dh1.amef(frame, 0.010)
        else:
            dehazed_frame, _ = dh2.remove_haze(frame, showHazeTransmissionMap=False)

        cv2.imwrite(os.path.join(dehazed_folder, frame_file), dehazed_frame)

    # rebuild video
    ftc.frames_to_video(dehazed_folder, output_video, target_fps)

    return output_video


demo = gr.Interface(
    fn=dehaze_video,
    inputs=[
        gr.Video(label="Upload Hazy Video"),
        gr.Dropdown(["AMEF", "Image Dehazer"], label="Select Dehazing Model")
    ],
    outputs=gr.Video(label="Dehazed Video"),
    title="AI Video Dehazer",
    description="Upload a hazy video and choose the dehazing algorithm."
)

demo.launch()