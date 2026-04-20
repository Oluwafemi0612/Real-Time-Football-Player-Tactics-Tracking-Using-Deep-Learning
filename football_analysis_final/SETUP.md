# Setup Guide

This project runs from the Jupyter notebook in this workspace and uses the helper modules in the surrounding folders.

## Install Dependencies

Install the packages used by the notebook:

```bash
pip install ultralytics supervision opencv-python numpy matplotlib pandas
```

If you are working in a virtual environment, activate it first and then run the install command above.

## Open The Notebook

Open `football_analysis_Notebook.ipynb` in Jupyter Notebook, JupyterLab, or VS Code.

## Add Your Files

- Place input videos in `input_videos/`.
- Place your YOLO weights in `models/`, typically as `models/best.pt`.
- The repository already includes an example model and sample output files.

## Run The Project

1. Open the notebook.
2. Run the cells from top to bottom.
3. In the video selection cell, change `selected_index` to choose which input video to process.
4. The processed video will be saved to `output_videos/output_video.avi`.

## Included Folders

- `camera_movement_estimator/`: camera motion estimation helpers.
- `player_ball_assigner/`: ball-to-player assignment logic.
- `speed_and_distance_estimator/`: speed and distance calculations.
- `team_assigner/`: team classification logic.
- `trackers/`: tracking utilities.
- `utils/`: shared helper functions.
- `view_transformer/`: perspective transformation code.

## Notes

- Supported input formats include `.mp4`, `.avi`, and `.mov`.
- If you replace the included model with your own weights, keep the filename and path consistent with the notebook cells.