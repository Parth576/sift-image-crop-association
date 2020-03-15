
#!pip install opencv-python==3.3.0.10 opencv-contrib-python==3.3.0.10
from .imports import *

class siift:
    def __init__(self,img_path,template_path):
        self.img_path=str(img_path)
        self.template_path = str(template_path)

    def predict(self):
        try:
            self.img_path='/media/parth/DATA_VOL/PROJECTS/imdjango'+self.img_path
            print(self.img_path)
            self.template_path='/media/parth/DATA_VOL/PROJECTS/imdjango'+self.template_path
            img = cv2.imread(self.img_path)
            template = cv2.imread(self.template_path)
            height_temp, width_temp = template.shape[:2]
            height_img, width_img = img.shape[:2]
            if height_temp > height_img or width_temp > width_img:
                height = 0.5 * height_img
                width = 0.5 * width_img
                dim = (int(width), int(height))
                template = cv2.resize(template, dim, interpolation=cv2.INTER_AREA)
            sift = cv2.xfeatures2d.SIFT_create()

            kp1, des1 = sift.detectAndCompute(img,None)
            kp2, des2 = sift.detectAndCompute(template,None)

            if des2 is not None:
                bf = cv2.BFMatcher()
                matches = bf.knnMatch(des1,des2, k=2)
                good = []
                for m,n in matches:
                    
                    if m.distance < 0.5*n.distance:
                            good.append(m)
                    
                src_pts = np.float32([ kp1[m.queryIdx].pt for m in good ]).reshape(-1,1,2)
                dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good ]).reshape(-1,1,2)
                M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)

                if M is not None:

                    pts = src_pts[mask==1]
                    min_x, min_y = np.int32(pts.min(axis=0))
                    max_x, max_y = np.int32(pts.max(axis=0))

                    return [int(min_x-13),int(min_y-13),int(max_x+13),int(max_y+13)]

                else:
                    return [-1]
            
            else:
                return [-1]
        except:
           return [-1]
    

