import cv2
import sys

def read_video(video_path):
    """Read frames from a video path into memory with basic progress logging."""
    cap = cv2.VideoCapture(video_path)
    frames = []
    count = 0
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print(f"EOF reached at frame {count}")
                break
            frames.append(frame)
            count += 1
            if count % 100 == 0:
                print(f"Read {count} frames")
            if count > 1000:  # Safety limit
                print(f"Reached 1000 frame limit")
                break
    except Exception as e:
        print(f"Error reading frame {count}: {e}")
    finally:
        cap.release()
    
    print(f"Total frames read: {len(frames)}")
    return frames

def save_video(ouput_video_frames, output_video_path):
    """Write frames to disk using imageio when available, else OpenCV fallback."""
    try:
        import imageio
        print(f"Using FFmpeg for faster encoding...")
        writer = imageio.get_writer(output_video_path, fps=30)
        total = len(ouput_video_frames)
        for i, frame in enumerate(ouput_video_frames):
            writer.append_data(frame)
            if (i + 1) % 100 == 0:
                print(f"  Written {i + 1}/{total} frames...")
        writer.close()
        print(f"✓ Video saved to {output_video_path}")
    except ImportError:
        print("FFmpeg not available, using OpenCV...")
        # Fallback to OpenCV
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = 30
        frame_size = (ouput_video_frames[0].shape[1], ouput_video_frames[0].shape[0])
        out = cv2.VideoWriter(output_video_path, fourcc, fps, frame_size)
        
        total = len(ouput_video_frames)
        for i, frame in enumerate(ouput_video_frames):
            out.write(frame)
            if (i + 1) % 100 == 0:
                print(f"  Written {i + 1}/{total} frames...")
        out.release()
        print(f"✓ Video saved to {output_video_path}")
