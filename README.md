# Corigine Technical assesment

## Program description
This program takes in a positive integer as an argument and computes the sum of all the individual digits of the factorial of this number. 

## How to install
First the repository needs to be cloned to your local directiory. This can be done with the following command:
```
git clone https://github.com/meet-me-half-way/corigine_TA.git
```
The application is packed as a docker container. Thus, in order to install this application you need docker installed. The docker image can be built using the following command: 
```
docker build -t image_name .
```   
Here ```image_name``` is the name you choose for your image. 

## How to use
Once the docker image, ```image_name``` , is created, the program can be run using the following command: 
```
docker run --rm image_name num
```
Here ```num``` is the positive integer that you want to pass to the application. 
