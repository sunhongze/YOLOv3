import sys

from people_flow import YOLO
from people_flow import detect_video

if __name__ == '__main__':
    video_path = 'test1.MP4'
    output_path='human_counter-master'
    detect_video(YOLO(), video_path, output_path)
    print('sun')
