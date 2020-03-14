from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import imForm
from .models import im
from django.core.files.storage import FileSystemStorage
# Create your views here.
from .program import imports
from .program import sift_feature_matching
from .program.sift_feature_matching import siift
from .program import resize
import cv2
import matplotlib.pyplot as plt
#from django.http import HttpResponse
#from matplotlib import pylab
#from pylab import *
#import PIL, PIL.Image, StringIO

def home(request):
    if request.method == 'POST' and request.FILES['image'] and request.FILES['crop']:
        image = request.FILES['image']
        crop = request.FILES['crop']
        fs = FileSystemStorage()
        imagename = fs.save(image.name, image)
        cropname=fs.save(crop.name,crop)
        image_url = str(fs.url(imagename))
        crop_url = str(fs.url(cropname))
        print(image_url)
        print(type(image_url))
        s = '/media/parth/DATA_VOL/PROJECTS/imdjango'+image_url
        img = cv2.imread(s)
        newobj = siift(image_url,crop_url)
        res = newobj.predict()
        #if len(res) is not 1:
         #   x1=res[0]
          #  y1=res[1]
           # x2=res[2]
            #y2=res[3]
            #imgnew = cv2.rectangle(img,(x1,y1),(x2,y2),255,2)


        #res=predict(image_url,crop_url)
        return render(request, 'sift/predict.html', {
            'imagename': imagename, 'cropname' : cropname, 'res':res
        })
    return render(request,'sift/home.html')

def about(request):
    return render(request,'sift/about.html')

def predict(request):
    return render(request,'sift/predict.html')
