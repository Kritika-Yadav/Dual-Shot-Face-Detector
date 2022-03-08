I have worked upon a Pytorch implementation of the Dual Shot Face Detector using pretrained model provided in the official github repository, the link for which is given below.
https://github.com/Tencent/FaceDetection-DSFD

Due to lack of GPU access I have implemented the model using Google Colaboratory. I have downloaded the WIDERFACE dataset along with the face annotations from the following link. 
I have also downloaded the Evaluation code and Validation results through the same.
http://shuoyang1213.me/WIDERFACE/

I made certain changes and fixed errors in the DSFD framework repository for it to work. I made sure to include all the necessary requirements (such as torch,
torchvision, matplotlib, open-cv, numpy and scipy) with appropriate versions for proper functioning of the model.

For plotting the Precision-Recall curve to check the effectiveness of our framework for detection of easy, medium and hard faces from the WIDERFACEValidation Dataset using our 
DSFD model, I have made use of the github repository given below since the code for generating the curve was given in MATLAB language in the official WIDERFACE Website. 
As this was a python based implementation I opted using a python code for plotting the curve. For this, I downloaded the repository and deleted all folders except widerface_evaluate
which had the necessary files for generation of the curve and I used it in my implementation of DSFD. I ensured making appropriate substitutions in these files for generation of the curve.
https://github.com/peteryuX/retinaface-tf2#Models
