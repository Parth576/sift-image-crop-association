
#!pip install opencv-python==3.3.0.10 opencv-contrib-python==3.3.0.10
from imports import *


def predict(img_path,template_path):
    try:
        img = cv2.imread(img_path,1)
        template = cv2.imread(template_path,1)
        template = resize_image(img,template)

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

