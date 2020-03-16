# sift-image-crop-association

Project to find association between crop and original image using SIFT (Scale-invariant Feature Transform).

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

All the ML code (independent of the website) is in the ML folder. It also contains the JSON file that contains all the crop associations for given dataset.

You can find the dataset here - https://drive.google.com/open?id=10dssv1syyIb0YO2WqsLs3IV1WpvRYsIm

### Prerequisites and Installing

A python 3.6 environment is recommended to run this project. Requirements can be installed using the command

```
pip install -r requirements.txt
```


Open the project folder and run migrations, This is necessary for creating the database tables

```
python manage.py makemigrations sift
```
```
python manage.py migrate 
```
Request you to change the universal paths used in views.py and sift-feature-matching.py as absolute paths were used.
Finally run the server and enter the localhost address that is returned

```
python manage.py runserver
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* OpenCV
* Pillow
* Numpy
* Matplotlib
* Django [Web Framework]
* HTML,CSS,Bootstrap [Frontend]


## Authors

* **Priyesh Vakharia** - [Priyesh1202](https://github.com/Priyesh1202)
* **Saurav Kanegaonkar** - [Saurav-Lellouch](https://github.com/Saurav-Lellouch)
* **Riya Gupta** - [RiyaGupta99](https://github.com/RiyaGupta99)
* **Parth Shah** - [Parth576](https://github.com/Parth576)


## Acknowledgments

* OpenCV SIFT Documentation
