import cv2
from sympy import fps

def read_video(video_path):
    """
    Reads a video file and returns a list of frames.
    
    Args:
        video_path (str): The path to the video file.

    Returns:
        list: A list of frames (numpy arrays).
    """
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    # cap.release()
    return frames


def save_video(output_video_frames, output_video_path):
    """
    Saves a list of frames as a video file.
    
    Args:
        output_video_frames (list): A list of frames (numpy arrays).
        output_video_path (str): The path to save the video file.
    """
    # if not output_video_frames:
    #     print("No frames to save.")
    #     return
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    
    for frame in output_video_frames:
        out.write(frame)
    
    out.release()


