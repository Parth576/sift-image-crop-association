from imports import *
import json
import glob
import sift_feature_matching
from sift_feature_matching import predict
images=glob.glob('../crops/ML_Dataset_Problem1/images/*')
res={}
new_images=[]
for i in images:
    i = i[36:]
    res[i]=[]
    new_images.append(i)
res['NA']=[]
temp_na=[]
crops=glob.glob('../crops/ML_Dataset_Problem1/crops/*')
new_crops=[]
for c in crops:
    c = c[35:]
    new_crops.append(c)
ctr=1
for i in new_images:
    print("Image {} of 143".format(ctr))
    ctr+=1
    i_path='../crops/ML_Dataset_Problem1/images/'+i
    for c in new_crops:
        c_path='../crops/ML_Dataset_Problem1/crops/'+c
        p=predict(i_path,c_path)
        if len(p)==1:
            temp_na.append(c)
        else :
            if c in temp_na:
                temp_na.remove(c)
            res[i].append([c,p])

for temps in temp_na:
    res['NA'].append([temps,[]])

# def myconverter(obj):
#         if isinstance(obj, np.integer):
#             return int(obj)
#         elif isinstance(obj, np.floating):
#             return float(obj)
#         elif isinstance(obj, np.ndarray):
#             return obj.tolist()
#         elif isinstance(obj, datetime.datetime):
#             return obj.__str__()

# json_object=json.dumps(res)

# with open('preyes.json','w') as outfile:
#     json.dumps(res,outfile,indent=4,sort_keys=False)

j=json.dumps(res,indent=4)
f=open('preyes.json','w')
print(j,file=f)
f.close()
    