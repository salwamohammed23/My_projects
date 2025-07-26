# Face Detection Project

This project demonstrates face detection in videos using the MTCNN (Multi-task Cascaded Convolutional Networks) model from the `facenet-pytorch` library. The workflow includes downloading a YouTube video, processing it to detect faces, and visualizing the results.

## Features

- Downloads videos from YouTube using `yt-dlp`
- Processes videos to extract frames and detect faces
- Uses MTCNN for face detection and InceptionResnetV1 for face recognition (optional)
- Displays the processed video with detected faces

## Requirements

- Python 3.11
- Libraries:
  - `facenet-pytorch`
  - `yt-dlp`
  - `opencv-python`
  - `torch`
  - `torchvision`
  - `Pillow`
  - `numpy`

## Installation

1. Mount Google Drive (if using Google Colab):
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```

2. Install required packages:
   ```python
   !pip install facenet-pytorch yt-dlp
   ```

3. Import necessary libraries:
   ```python
   import os
   import cv2
   import torch
   from facenet_pytorch import MTCNN
   from IPython.display import Video
   ```

## Usage

1. Set up directories:
   ```python
   from pathlib import Path

   project_dir = Path("/content/drive/MyDrive/my_project")
   data_dir = project_dir / "data"
   video_dir = data_dir / "videos"
   images_dir = data_dir / "images"

   for folder in [data_dir, video_dir, images_dir]:
       folder.mkdir(parents=True, exist_ok=True)
   ```

2. Download a YouTube video:
   ```python
   video_url = "https://www.youtube.com/watch?v=5rGNDuRB_GY"
   output_path = str(video_dir / "yawmiaat wanis.mp4")
   !yt-dlp -f best -o "{output_path}" {video_url}
   ```

3. Process the video to detect faces:
   ```python
   # Initialize MTCNN
   device = "cuda" if torch.cuda.is_available() else "cpu"
   mtcnn = MTCNN(keep_all=True, device=device)

   # Process video
   cap = cv2.VideoCapture(output_path)
   while cap.isOpened():
       ret, frame = cap.read()
       if not ret:
           break
       
       # Detect faces
       boxes, _ = mtcnn.detect(frame)
       
       # Draw bounding boxes
       if boxes is not None:
           for box in boxes:
               cv2.rectangle(frame, (int(box[0]), int(box[1])), 
                            (int(box[2]), int(box[3])), (0, 255, 0), 2)
       
       # Display or save the frame
       cv2.imshow('Face Detection', frame)
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break

   cap.release()
   cv2.destroyAllWindows()
   ```

## Project Structure

- `/content/drive/MyDrive/my_project/data/`: Contains project data
  - `videos/`: Stores downloaded videos
  - `images/`: Stores processed frames (optional)

## Notes

- The notebook includes functions for cutting videos into segments and displaying them.
- Face detection performance depends on hardware capabilities (GPU recommended).
- The project can be extended to include face recognition by using the InceptionResnetV1 model from `facenet-pytorch`.
