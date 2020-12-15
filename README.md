# Speech-to-text-convertor-&-tone-Analyzer
In this Project we have made use of Watson API to convert Speech into text and then to analyse it's tone i.e whether the tone of text is sad, happy, anger etc.

Major Frameworks and languages used are : Django, Javascript, Semantic UI, Html/Css

To run this you need to create your virtual enviroment and then install the required things.

* Clone using `$ git clone https://github.com/Sanji515/Speech-to-text-convertor-and-tone-Analyzer.git speech-to-text && cd speech-to-text`

## Run

* Install virtualenv
    - on Ubuntu: `$ sudo apt install python-virtualenv`
    - on Windows: `$ pip install virtualenv`
    
* Create a virtual environment
    - on Ubuntu: `$ virtualenv venv -p python3.6`
    - on Windows: `$ virtualenv venv`
    
* Activate the environment:
    - on Ubuntu: `$ source venv/bin/activate`
    - on Windows: `$ ./venv/Scripts/activate`
    
* Install the requirements:
    - `$ pip install -r requirements.txt`

* Make migrations `$ python manage.py makemigrations`
* Migrate the changes to the database `$ python manage.py migrate`
* Run the server `$ python manage.py runserver`

That's it. Open web browser and hit the url [http://127.0.0.1:8000](http://127.0.0.1:8000)


### You can also download the video (Emotion Analyzer Mp4) of this project form the main page of this repo
### Here are some of the screenshots for the reference

![speech to text 1](https://user-images.githubusercontent.com/37772172/47526961-34d59600-d856-11e8-8b6f-8f1aae634df7.png)


![speech to text 2](https://user-images.githubusercontent.com/37772172/47527138-a57cb280-d856-11e8-96c5-d47877e50f10.png)


![speech to text 3](https://user-images.githubusercontent.com/37772172/47527177-baf1dc80-d856-11e8-9c7b-07df87af1131.png)
