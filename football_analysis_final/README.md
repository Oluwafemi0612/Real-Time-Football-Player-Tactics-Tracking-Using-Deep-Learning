# Football Analysis Notebook

This project is a Jupyter Notebook pipeline for analyzing football match footage. It detects and tracks players, referees, and the ball, assigns players to teams by jersey color, estimates camera movement, maps the pitch into a top-down view, and calculates player speed and distance covered.

![Football analysis screenshot](output_videos/screenshot.png)

## What It Does

- Detects players, referees, and the ball in video frames using YOLO.
- Tracks objects across frames to keep consistent IDs.
- Groups players into teams using jersey color clustering.
- Estimates camera motion so player movement can be measured more accurately.
- Uses perspective transformation to convert pixel movement into real-world pitch movement.
- Calculates speed and distance for each tracked player.

## Project Files

- `football_analysis_Notebook.ipynb`: main notebook to run the full pipeline.
- `camera_movement_estimator/`: camera motion estimation helpers.
- `player_ball_assigner/`: logic for assigning the ball to players.
- `speed_and_distance_estimator/`: player speed and distance calculations.
- `team_assigner/`: team classification based on jersey colors.
- `trackers/`: object tracking utilities.
- `utils/`: shared helper functions.
- `view_transformer/`: perspective and pitch transformation code.
- `models/`: place YOLO weights here, including `best.pt`.
- `input_videos/`: place your source match videos here.
- `output_videos/`: generated results are saved here.

## Requirements

- Python 3.10 or newer
- `ultralytics`
- `supervision`
- `opencv-python`
- `numpy`
- `matplotlib`
- `pandas`

## Setup

1. Install the required packages:

	```bash
	pip install ultralytics supervision opencv-python numpy matplotlib pandas
	```

2. Place your video in `input_videos/`.

3. Put your trained model in `models/`.

4. Open `football_analysis_Notebook.ipynb` in Jupyter or VS Code.

## How To Run

1. Run the notebook cells from top to bottom.
2. In the video selection cell, set `selected_index` to choose which input video to process.
3. The annotated output video is saved to `output_videos/output_video.avi`.

## Notes

- A sample YOLO model is included in `models/`.
- The notebook also works with your own trained model if you want to test different footage.
- If you add more videos, update `selected_index` to process the one you want.

## Sample Output

The repository includes an example processed frame in `output_videos/screenshot.png` and a generated output video in `output_videos/output_video.avi`.