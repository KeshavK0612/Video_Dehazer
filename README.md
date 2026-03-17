# 🌫️ AI Video Dehazer

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Gradio](https://img.shields.io/badge/Gradio-Interactive%20UI-orange)
![Deployment](https://img.shields.io/badge/Deployment-HuggingFace-yellow)

An AI-powered system that **removes haze from videos using computer vision algorithms**.
The application processes videos frame-by-frame and reconstructs a clearer video while preserving the original audio.

🚀 **Live Demo:**
https://huggingface.co/spaces/KeshavK0612/Video_Dehazer

---


The system allows users to:

* Upload hazy videos
* Select a dehazing algorithm
* Process the video automatically
* Download the dehazed output

---

# 📌 Features

✔ Video haze removal
✔ Two classical dehazing algorithms
✔ Frame-by-frame processing pipeline
✔ Audio preservation
✔ Interactive web interface
✔ Cloud deployment

---

# 🧠 Algorithms Implemented

## 1️⃣ AMEF (Adaptive Multi-Exposure Fusion)

AMEF enhances visibility by generating multiple exposure variations of an image and fusing them.

Pipeline:

Hazy Frame
→ Gamma Corrections
→ Histogram Equalization
→ Exposure Fusion
→ Enhanced Frame

Advantages:

* Fast
* Improves contrast
* Effective for moderate haze

---

## 2️⃣ Boundary Constraint Dehazing

Based on the ICCV 2013 paper:

**Efficient Image Dehazing with Boundary Constraint and Contextual Regularization**

Pipeline:

Hazy Frame
→ Airlight Estimation
→ Transmission Map Estimation
→ Regularization
→ Scene Radiance Recovery
→ Dehazed Frame

Advantages:

* Physically grounded model
* Handles dense haze better

---

# 🏗️ System Architecture

Video Input
↓
Frame Extraction
↓
Frame Dehazing (AMEF / Boundary Constraint)
↓
Frame Reconstruction
↓
Audio Reattachment
↓
Dehazed Video Output

---

# 📁 Project Structure

```
video-dehazing-ai
│
├── app.py
├── requirements.txt
├── image_dehazer.py
├── vidtoframeconv.py
├── frametovidconv.py
│
├── dehaze
│   ├── amef.py
│   ├── exposure_fusion.py
│   └── pyramid_operations.py
│
└── README.md
```

---

# ⚙️ Installation

Clone the repository:

```
git clone https://github.com/yourusername/video-dehazing-ai.git
cd video-dehazing-ai
```

Install dependencies:

```
pip install -r requirements.txt
```

Run locally:

```
python app.py
```

---

# 💻 Usage

1. Upload a hazy video
2. Select the dehazing algorithm
3. Click **Submit**
4. Download the processed video

Recommended input:

* Video length: **< 10 seconds**
* Resolution: **≤ 720p**

---

# 🚀 Deployment

This application is deployed using:

* Python
* OpenCV
* Gradio
* Hugging Face Spaces

Live app:

https://huggingface.co/spaces/KeshavK0612/Video_Dehazer

---

# 🧰 Tech Stack

| Tool                | Purpose                   |
| ------------------- | ------------------------- |
| Python              | Core programming language |
| OpenCV              | Image processing          |
| NumPy               | Numerical computation     |
| MoviePy             | Video manipulation        |
| Gradio              | Web interface             |
| Hugging Face Spaces | Cloud deployment          |

---

# 🔮 Future Improvements

* Deep learning based dehazing models
* Real-time video processing
* GPU acceleration
* Before/after comparison slider
* Streaming pipeline without disk I/O

---

# 👨‍💻 Author

Keshav

---

# 📄 License

MIT License
