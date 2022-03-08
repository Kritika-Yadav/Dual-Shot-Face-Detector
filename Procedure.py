
# After fulfilling download requirements take the following steps:

# i.	Inside 'eval__tools' directory create a new directory named 'eval_tools'.

# ii.	Run
!export CUDA_VISIBLE_DEVICES=0

# iii.	Make the following amends to the downloaded DSFD framework.
# A.	In layers/modules/multibox_loss.py: 
# •	Corrections: 
# •	Line 13 : Change to - 
from ..box_utils import (log_sum_exp, match, refine_match, sfd_match)
 
# B.	 In data/widerface.py 
# •	Correction:
# •	Line 25 : Change to -   
WIDERFace_ROOT = './data/'
 
# C.	In demo.py
# •	Correction:
# a. Line 29 : Add
from warnings import filterwarnings
filterwarnings("ignore")
# b.	Line 70 : Add
with torch.no_grad():
# c.	Line 71 : Change to
x = Variable(x.unsqueeze(0))
# And shift this line by one space.
# d.	Line 85: Add
score = score.cpu().numpy()
# e.	Line 171 : Add
torch.set_grad_enabled(False)
 
# D.	In widerface_val.py
# •	Correction:
# a. Line 61 : Add 
with torch.no_grad():
# b.	Line 62 : Change to
x = Variable(x.cuda())
# And shift this line by one space.
# c.	Line 283 : Add
with torch.no_grad()
# And shift lines beneath from 283 to 306 by one space.
 
# E.	In face_ssd.py
# •	Correction:
# a.	Line 191 : Add
with torch.no_grad():
# b.	Line 192 : Change to
prior = Variable( priorbox.forward())
# And shift this line by one space.
 
# F.	In layers/functions/detection.py
# a.	Line 70: Change to
    if scores.dim() == 0 or scores.numel() == 0:
 
# iv.	Check results on demo image using: 
!python demo.py 

# o	Result to be stored in eval__tools folder as 'face.png'. 
# o	 We can change the image for demo in demo.py - Line 43 : Change to
parser.add_argument('--img_root', default='Path of image', help='Location of test images directory')
 
# v.	Evaluate on widerface validation set using:
!python widerface_val.py --visual_threshold 0.1

# o	Text files with detections stored in eval__tools/eval_tools/
# o	Delete folder WIDERFace_DSFD_RES152_results with demo results
# o	Ensure the directories containing detection files are named as 0--Parade, 1--Handshaking and so on...if the format is as WIDERFace_DSFD_RES152_results_0--Parade then rename.
 
For Precision Recall Curve

# i.	Set the current working directory to widerface_evaluate folder using:
%cd 'Path of widerface_evaluate'

# ii.	Run 
!python3 setup.py build_ext –inplace

# iii.	Make the following amends to widerface_evaluate.
# In widerface_evaluate/evaluation.py
# •	Correction:
# a.	Line 15 : Add 
import matplotlib.pyplot as plt
# b.	Line 283 : Add following lines
plt.plot(recall, propose, color = 'tab:green') 
plt.savefig("Precision-Recall curve.png",bbox_inches="tight")
plt.title('Precision-Recall Curve')
plt.xlabel('Recall')
plt.ylabel('Precision')

# iv.	Run 
!python3 evaluation.py -p Path of eval__tools/eval_tools -g Path of eval__tools/ground_truth

# v.	The precision-recall curve can be found as 'Precision-Recall curve' in widerface_evaluate
