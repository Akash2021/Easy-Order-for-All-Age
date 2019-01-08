# Easy Order for everyone

<img src="">
This is a simple framework provide different user interface by age group.
It estimates age from a user's face image.


## Easy User Interface for all ages.

When we buy some stuff, we are frequently encountered web user interface.
for example, kiosk ordering without human cashier continue to spread, to make their workflow smarter and reduce labor costs.
It means, even if we are not online.
If we want to go grocery shopping, have a coffee or buy a hamburger,
than have to be fluency on their user interface.

relatively young people easily dealing with it,
but older people often fail to use it.

Do you think it just because of that older people less exposed to IT products?
Maybe yes in some sense, but mainly because of **unfriendly user interfaces for the elderly**.
Even their physical aspects are ignored.


<a href="https://youtu.be/1BzqctRGgaU" target="_blank"><img src="http://img.youtube.com/vi/1BzqctRGgaU/0.jpg" width="360" height="240" border="10"/></a>

Look at this lady who can not order the desired menu, because font size is too small for her.

Providing a suitable UI for each age group will contribute to improving user experience and preventing digital alienation against certain ages.


## Code Overview
- webpage/
    - static/
    - templates/
    - app.py   
- 

## Progress

- [build torch custom dataset](https://github.com/minh364/Easy-Order-for-All-Age/blob/master/docs/Train_with_CustomDataset.ipynb)
- train model(progress)
- build webpage (progress)
- publish it
- add function with live steam web cam

## How it works

first detects the face in image
and then extracts the CNN predi
ctions 

## Datasets labeled by age
- [IMDB-WIKI](https://data.vision.ee.ethz.ch/cvl/rrothe/imdb-wiki/) 
- [FGnet](http://www-prima.inrialpes.fr/FGnet/html/benchmarks.html) 
- [UTKFace](https://susanqq.github.io/UTKFace/) `consists of 20k+ face images in the wild (only single face in one image)` `labelled by age, gender, and ethnicity`
- [Adience collection of unfiltered faces](https://talhassner.github.io/home/projects/Adience/Adience-data.html)`Total number of photos: 26,580` `Number of age groups / labels: 8 (0-2, 4-6, 8-13, 15-20, 25-32, 38-43, 48-53, 60-)`

## Citation
    
    [Deep expectation of real and apparent age from a single image without facial landmarks](https://www.vision.ee.ethz.ch/en/publications/papers/articles/eth_biwi_01299.pdf)International Journal of Computer Vision (IJCV), 2016
    
