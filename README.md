# Russian Conversion
A program that transforms English type into Russian type at runtime.    <br>
Translates English into Russian through layer translating.    <br>
```
Examples.

privet -> привет
ljudi -> люди
kak delа u tebe -> как дела у тебе
```
![russian-conversion example](russian-conversion.gif)

## Features
- conversion from english --> russian (or any language you map)
- simple implementation of spell checking (can be turned on an off -- TO BE IMPLEMENTED)

## Installation
First install python3 (recommended version python3.8):

On Linux:
```shell
sudo apt install python3.8 python3.8-pip
```

On Mac:
```shell
brew install python3.8
brew install python3.8-pip
```

On Windows:   <br>
Navigate to the python website and install from there.    <br>
```https://www.python.org/downloads/```

To install the requirements run the following command:
```shell
pip3 install -r requirements.txt 
``` 

## Usage
Clone the repo through ssh or html and cd into the directory with 
```shell
git clone git@github.com:mgoldgirsh/russian-conversion.git
cd russian-coversion
```

Then to use, run the script with the following
```shell
chmod +x russian-script
./russian-script 
```   
or run the following your terminal window
```shell
python3 main.py
```
<br>
Once the process is running you can start typing in English and then click the __spacebar__ key to transform the text into Russian.
To exit the process click the __esc__ key on your keyboard. 

## Things to Add (WIP Project)
- Add machine learning so words would autocorrect (complicated)
- Add tab autocomplete so it knows what character to go to 
