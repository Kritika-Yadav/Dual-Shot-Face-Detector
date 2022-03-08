# DUAL SHOT FACE DETECTOR
Python based Pytorch Implementation of Dual Shot Face Detector Model.

# Download Requirements:-
 
i.	Download the DSFD framework through the following link https://github.com/Tencent/FaceDetection-DSFD and upload it to Google Drive. Mount Google Drive in Google Colaboratory.

ii.	Install the following requirements to your Colab {in order as mentioned}:-
A.	Python==3.7 (Preinstalled in Google Colab)
B.	Numpy==1.19.5(Preinstalled in Google Colab)
C.	Torch==0.4.1.post2 {Using : !pip install torch==0.4.1.post2}
D.	Torchvision==0.2.1 {Using : !pip install torchvision==0.2.1}
E.	Open-CV
F.	Scipy
G.	Matplotlib {Using : !pip install opencv-python matplotlib scipy }

iii.	Download the Pretrained DSFD Model from the following link https://drive.google.com/file/d/1WeXlNYsM6dMP3xQQELI-4gxhwKUQxc3-/view, upload it to drive and save it in a new directory 'weights' inside folder containing DSFD Framework.

iv.	Download the Widerface Dataset along with the face annotations from the following link http://shuoyang1213.me/WIDERFACE/, upload it to drive and store it in 'data' directory inside folder containing DSFD Framework.

v.	Download the Evaluation Code and Validation Results from the following link http://shuoyang1213.me/WIDERFACE/, upload it to drive, move it inside folder containing DSFD framework and rename it as 'eval__tools'.

For plotting Precision-Recall Curve

vi. Download the following Github repository https://github.com/peteryuX/retinaface-tf2#Models, delete and folders except widerface_evaluate and upload it to drive, move it into the folder containing DSFD framework.

# Results:-

![image](https://user-images.githubusercontent.com/86051282/156579286-ce75cd88-7e01-4ef4-a92d-f589fa30ff16.png)
![image](https://user-images.githubusercontent.com/86051282/156579340-7b97bdaa-4b73-463f-8f3b-319faed470cb.png)
![image](https://user-images.githubusercontent.com/86051282/156579408-8dc54940-ecb1-4f2f-b38a-e29985622458.png)
