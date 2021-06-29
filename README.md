# FireProof
An innovative way to detect fire and thus execute safety protocol for residents in a buliding.

## Table of Contents

- [Problem Statement](#Problem-Statement)
- [Solution](#Our-solution)
- [Machine Learning Model](#ML-model)
- [How to run](#Instruction)
- [Demo](#Demo)
- [Project Links](#Important-links)
- [Team Members](#Team)  


## Problem Statement
Every day, about 60 people die due to a fire hazard in India. It causes countless lives, mostly due to late detection of fire and people not being able to find a safe route to escape the burning buildings. The excess amount of smoke and gas in case of fire cause difficult visibility, rendering all escape plans useless.

## Our solution
A web app which takes images from various CCTV  in building cameras runs a Neural Net and incase of a fire sends an alert  and suggests best possible escape route to users. Right now we have demonstrated on images but since the model is small enough and the latency is low, it can be used with live video stream.
  
The path in general
![The path in general](https://github.com/old-school-kid/FireProof/blob/main/media/graph.png)


## ML model 
1. We used data which consisted of images from CCTV to make it as real as possible.
2. We have used MobileNetV2 as the base model and achieved 96% accuracy on train and 95% on test with 4 fold train-test data split.
3. With the help OpenCV tools we measure the percent area recorded by camera that is affected by fire and assign a weight to that node.  
4. Training and validation Accuracy and Loss graph
![Training and validation Accuracy and Loss graph](https://github.com/old-school-kid/FireProof/blob/main/media/Accuracy%20Loss%20graph%20.png)


## Instruction
1. Clone the project
```
cd /path/to/directory

```
2. Install all the dependencies
 ```
pip install -r requirements.txt
```
3. Save photos in images folder
4. execute while in the directory
 ```
python app.py
```

## Demo
The landing page
![The landing page](https://github.com/old-school-kid/FireProof/blob/main/media/Landing%20page.png)  
Path if there is a fire
![Path if there is a fire](https://github.com/old-school-kid/FireProof/blob/main/media/Path.png)  
If no fire is detected
![If no fire is detected](https://github.com/old-school-kid/FireProof/blob/main/media/No%20fire.png)

## Important Links
[Presentation](https://docs.google.com/presentation/d/15hfhQHfEvQtafrqppfLhot6F5t3R4naEtEJJR1Avqv0/edit?usp=sharing)

## Team 
[Harsh Kumar Singh](https://github.com/harsh-hks-580)  
[Sonali Verma](https://github.com/sonaliverma82276)  
[Somya Jain](https://github.com/somyaj15)  
[Surya Prakash Mishra](https://github.com/old-school-kid)  