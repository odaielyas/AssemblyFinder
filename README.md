# AssemblyFinder
This project was developed to aid in the detection of protien assemblies from video files obtained from AFK testing. A computer vision model was created using Amazon Custom Labels, where the model was trained using the AWS interface and utilizes the bounding boxes feature for image labeling. The developed model takes an mp4 file as input, splits the video into frames, and runs the module on each frame till protien assembly is detected. The module will then display the frame at which assembly occurs along with bounded boxes surrounding the object detected, in addition to the time at which protien assemble is found in the input video to reduce the amount of time researches spend detecting protien assemblies in large video files. This project demonstrates the potential of using Amazon Rekognition and Custom Labels for object detection purposes for similar research opportunities. 

This project conatains a user interface created using Python Flask, the HTML interface allows the user to upload the sample video, run the model, and display the results. The given results will contain the first frame where protien assembly is detected, and the time the assembly was found in the sample file as shown in the images below:


<p align = "center">
<img width = "400" height = "500" src ="https://user-images.githubusercontent.com/77697922/236269130-48e9823b-25d9-4633-b425-dc59402cc6a3.jpg" >
</p>

<p align = "center">
<img width = "400" height = "500" src ="https://user-images.githubusercontent.com/77697922/236269342-e532d434-d8e2-4072-9a8b-e94cd250b73b.jpg">
</p>

## Packages:
* Boto3: Amazon software development kit that allows interaction with Amazon Web Services tools using Python
* Python Flask: Web framework used to develop HTML webpage using Python
* CSV: Python interaction with CSV files
* Pillow: Python Imageing library
* OpenCV (CV2): Python video capture package used to split sample video

## Steps:
1. Install required packages (Boto3, Flask, CSV, Pillow, CV2)
2. run start.py in command line to start and access the model on Amazon Web Services
3. run web.py to in command line to start user interface
4. Upload video sample on webpage
5. Run model on webpage
6. Display Results

This code was developed as part of the Engineering Computation and Data Science class at MIT for the Spring 2023 semester instructed by Professor John Williams, and Professor Able Sanchez. For further inquiries or feedback please contact Maxwell Kalinowski (mkal@mit.edu)  or Odai Elyas (oaelyas2@mit.edu).
7. Run stop.py in command line once analysis is complete.




