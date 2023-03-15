# AI Programming with Python Project. Dog Image Classification using Pytorch models.

Project code for Udacity's AI Programming with Python Nanodegree program. In this project, code was developed for an image classifier built with PyTorch.

The image classifier recognizes different breeds of dogs. The dataset used contains 50 images of dogs.

In Image Classifier Project Resnet18, Alexnet, VGG16 from torchvision.models pre-trained models were used. It was loaded as a pre-trained network, in which input images are transformed and resized for better prediction. 

## Dataset used :     
* Dog Breed Images from ImageNet        
* Dog images can be downloaded from [here](http://vision.stanford.edu/aditya86/ImageNetDogs/menu_frame.html)

## Neural Network used : 
* [Resnet18](https://resources.wolframcloud.com/NeuralNetRepository/search/?i=resnet18)
* [VGG16](https://resources.wolframcloud.com/NeuralNetRepository/resources/VGG-16-Trained-on-ImageNet-Competition-Data/)
* [Alexnet](https://www.kaggle.com/code/blurredmachine/alexnet-architecture-a-complete-guide/notebook)
       
You can download Resnet18 [here](https://www.kaggle.com/code/yhn112/resnet18-baseline-pytorch-ignite)     
You can download VGG16 [here](https://www.kaggle.com/code/carloalbertobarbano/vgg16-transfer-learning-pytorch)   
You can download Alexnet [here](https://www.kaggle.com/code/msripooja/dog-images-classification-using-keras-alexnet)    

## Refresher on Neural Network :
[Gradient Descent](https://medium.com/secure-and-private-ai-writing-challenge/playing-with-gradient-descent-intuition-e5bde385078)   
[Backpropogation](https://medium.com/secure-and-private-ai-writing-challenge/playing-with-backpropagation-algorithm-intuition-10c42578a8e8)        


## Command line applications available:

For command-line applications, there is an option to select either Alexnet or VGG16 or Resnet models. 

Following arguments mandatory or optional for check_images.py 

1. `--dir`. 'Provide data directory of Dog Images.', type = str, default = 'pet_images/'   
2. `--dogfile`. 'Provide data directory of names of dogs,' type = str, default = 'dognames.txt'   
3. `--arch`. 'Alexnet or Resnet can be used if this argument is specified, otherwise, VGG16 will be used', type = str      


## Run on windows - 
Make sure you have installed Python, Pytorch and Jupyter Notebook.

* _Download all the folders and files_     
`git clone https://github.com/GauravG-20/Dog-Image-Classifier.git`              
* _Then open Visual Studio Code (or powershell) and change the directory to the path where all the files are located._       
`cd Dog-Image-Classifier`      
* _Now run the following commands_ -        
       1. `python check_images.py` -- will download the models and then will predict the breeds of the dogs with default parameters.        
       2. `sh run_models_batch.sh` -- will run the program from the command line within Project Workspace (see run_models_batch.sh for further clarification)      
       3. `sh run_models_batch_uploaded.sh` -- will run the program from the command line within Project Workspace (see run_models_batch_uploaded.sh for further clarification)
