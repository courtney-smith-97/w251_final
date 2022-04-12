# w251_final

To run training in EC2:

File Structure:  
    data  (Downlaod data here: https://drive.google.com/file/d/1uVFT3pbONUImLhz149Nbe3cS7pgZS4-W/view?usp=sharing)
    w251_final (this repo)  
    yolov5 (ultralitics yolov5 repo: https://github.com/ultralytics/yolov5)  

Training:  
  
Run the ec2_training_script.ipynb file within this repo. Relative paths may need to be modified to point to the train.py file in the yolov5 repo and to the data in the data directory.


Evaluation:

Pull the train.py file out of the w251_final directory so that the file structure is as follows:
w251_final (this repo)  
train.py   
yolov5 (ultralitics yolov5 repo: https://github.com/ultralytics/yolov5)  

Run the train.py file. Be sure to include your aws ACCESS_KEY and ACCESS_SECRET, as well as updating the s3 buckt name you want to save your files. 
The train.py file will evaluate on a video, file containing images, or vide stream from a web camera, this can be adjusted by changing the source argument in the run_detection function within the train.py script. This script can be run on a local device, cloud enviornment, or jetson device.

The Dockerfile in this container is a recommended envionrment to use for training and evaluation, though similar enviornments with the appropriate dependencies will also work.
