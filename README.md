# Google Cloud Functions
## Starting a new project
To start a new project in google cloud, we can go to
[Firebase Console](https://console.firebase.google.com) 
or [Google Cloud Plataform Console](https://console.cloud.google.com)

##Creating a virtual environment
First you have to install `python3-venv` with the following command:
``` 
Sudo brew install python3-venv
```
Then we execute the following command
```
python3 -m venv venv
```
to activate the environment we do:
```
source venv/bin/activate
```
In order to add new packages to our new virtual environment we create a file called `requirements.txt`and execute the following command:
```
pip install -r requirements.txt
```

##Deploying our functions
First, we have to set our project ID with the following command:
```
gcloud config set project [YOUR_PROJECT_ID]
```
Then we deploy our functions with this command:
```
gcloud function deploy [FUNCTION_NAME] --runtime python37 --trigger-http
```
