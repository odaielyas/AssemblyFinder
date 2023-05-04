import boto3
import io
import csv
import cv2
import os
from PIL import Image, ImageDraw, ExifTags, ImageColor, ImageFont


def split(video):

    video = cv2.VideoCapture(video)
    if not os.path.exists('frames'):
        os.makedirs('frames')

    frame_count = 0
    fps = video.get(cv2.CAP_PROP_FPS)

    while True:
        ret,frame = video.read()
        if not ret: 
            break

        frame_count += 1
        file_name = f'frames/frame{frame_count:04d}.jpg'

        if frame_count % round(fps*2) == 0:
            cv2.imwrite(file_name, frame)

    video.release()

    return fps, frame_count

def show_custom_labels(model,photo, min_confidence, fps): 

    with open ('mkal_accessKeys.csv', 'r') as f:
        next(f)
        reader = csv.reader(f)
        
        for row in reader:
            access_key_id = row[0]
            secret_access_key = row[1]

    client=boto3.client('rekognition', region_name = 'us-east-2', aws_access_key_id = access_key_id, aws_secret_access_key = secret_access_key)

    pil_image = Image.open(photo)
    stream = io.BytesIO()
    pil_image.save(stream, format="JPEG")
    image = stream.getvalue()

    #Call DetectCustomLabels
    response = client.detect_custom_labels(Image={'Bytes': image},
        MinConfidence=min_confidence,
        ProjectVersionArn=model)
    
    detected_labels = response['CustomLabels']

    draw = ImageDraw.Draw(pil_image)
    font = ImageFont.truetype("arial.ttf", 20)

    for label in detected_labels:
        print(f'Image: {photo}, Detected label: {label["Name"]}, Confidence: {label["Confidence"]:.2f}%')
        
        if label['Name'] == 'assembled':
            box = label['Geometry']['BoundingBox']
            left = pil_image.width * box['Left']
            top = pil_image.height * box['Top']
            width = pil_image.width * box['Width']
            height = pil_image.height * box['Height']

            points = (
                (left, top),
                (left + width, top),
                (left + width, top + height),
                (left, top + height),
                (left, top)
            )

            draw.line(points, fill='white', width=5)
            draw.text((left, top - 25), label['Name'], fill='white', font=font)
            pil_image.save('static/assembled.jpg', 'JPEG')
            break

    #Save last image in static directory
    pil_image.save('static/assembled.jpg', 'JPEG')


    return len(detected_labels)

def main():


    min_confidence=95    
    model_arn='arn:aws:rekognition:us-east-2:696327820520:project/AssemblyFinder4/version/AssemblyFinder4.2023-04-25T16.20.38/1682454037596'

    vid_file = 'video'
    video = None

    for file in os.listdir(vid_file):
        if file.endswith('.mp4'):
            video = os.path.join(vid_file, file)
            break

    if video is None:
        print('No video found in directory')
        return
            
    split(video)
    fps, frame_count = split(video)
    files = os.listdir('frames')
    label_count = 0
    detection_time = frame_count/fps
    
    for file in files:
        if file.endswith('.jpg'):
            if show_custom_labels(model_arn,f'frames/{file}', min_confidence, fps):
                print('Assembly detected in video frame: ' + file, 'at ' + str(round(int(os.path.splitext(os.path.basename(file))[0][5:])/fps)), ' seconds')
                break
            
    detection_time = str(round(int(os.path.splitext(os.path.basename(file))[0][5:])/fps))

    return detection_time
 

if __name__ == "__main__":
    main()
