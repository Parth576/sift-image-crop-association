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
import math
from PIL import Image,ImageDraw
from imdjango.settings import MEDIA_URL
import os

def home(request):
    if request.method == 'POST' and request.FILES['image'] and request.FILES['crop']:
        if os.path.exists('/media/parth/DATA_VOL/PROJECTS/imdjango/media/result.png'):
            os.remove('/media/parth/DATA_VOL/PROJECTS/imdjango/media/result.png')
        image = request.FILES['image']
        crop = request.FILES['crop']
        fs = FileSystemStorage()
        imagename = fs.save(image.name, image)
        cropname=fs.save(crop.name,crop)
        image_url = str(fs.url(imagename))
        crop_url = str(fs.url(cropname))
        s = '/media/parth/DATA_VOL/PROJECTS/imdjango'+image_url
        newobj = siift(image_url,crop_url)
        res = newobj.predict()
        if len(res)!=1:
            img = Image.open(s, 'r')
            img_w, img_h = img.size
            background = Image.new('RGBA', (img_w, img_h), (255, 255, 255, 255))
            bg_w, bg_h = background.size
            background.paste(img)
            shape=[(res[0],res[1]),(res[2],res[3])]
            im1=ImageDraw.Draw(background)
            im1.rectangle(shape,fill=None,outline="black")
            background.save('/media/parth/DATA_VOL/PROJECTS/imdjango/media/result.png')

            return render(request, 'sift/predict.html', {'w':bg_w,'h':bg_h,'MEDIA_URL':MEDIA_URL})
        else:
            return render(request,'sift/predict.html')
    return render(request,'sift/home.html')

def about(request):
    return render(request,'sift/about.html')

def predict(request):
    return render(request,'sift/predict.html')
