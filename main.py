from utils import read_video, save_video

def main():
    #Read Video
    video_path = read_video('input_videos/E3c993bd2_0 (74).mp4')
    # frames = read_video(video_path)
    # print(f"Number of frames read: {len(frames)}")

    # save Video
    save_video(video_path, 'output_videos/output_video.avi')

if __name__ == "__main__":
    main()