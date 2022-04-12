import os
import pandas as pd
from datetime import datetime
import boto3
from yolov5 import detect

def run_detection():
    print('detecting')
    weights = 'w251_final/helmet_detector_small.pt' # path to best.pt file
    source = 'w251_final/ski_lift_detection.mp4' # path to source files
    conf_thres = 0.47 # confidence threshold with best results
    device = 0 # cuda device
    line_thickness = 3 # pixel width of bounding boxes
    hide_labels = False # toggle for label names display
    hide_conf = False # toggle for confidence display
    save_txt = True
    detect.run(weights=weights,
               source=source,
               conf_thres=conf_thres,
               device = device,
               line_thickness=line_thickness,
               hide_labels=hide_labels,
               save_txt=save_txt,
               hide_conf=hide_conf)

if __name__=="__main__":
    run_detection()
    directory = os.listdir('yolov5/runs/detect/')[-1]
    new_lines = []
    for file in os.listdir(f'yolov5/runs/detect/{directory}/labels/'):
        with open('yolov5/runs/detect/exp3/labels/test_1000.txt') as f:
            lines = f.readlines()
            for line in lines:
                new_line = line[:-1].split(' ')
                new_lines.append(new_line)
    test_df = pd.DataFrame(new_lines)
    test_df.to_csv(f'yolov5/runs/detect/{directory}/df.csv')
    key = f'{str(datetime.now())}_df.csv'
    file_path = f'yolov5/runs/detect/{directory}/df.csv'
    ACCESS_KEY=os.getenv('ACCESS_KEY')
    ACCESS_SECRET=os.getenv('ACCESS_SECRET')
    s3_client = boto3.client('s3', region_name='us-east-1', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=ACCESS_SECRET)
    bucket = 'w251spr2022-final-project'
    s3_client.upload_file(file_path, bucket, key)
