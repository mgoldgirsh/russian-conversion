# Russian Conversion
A program that transforms English type into Russian type at runtime.   <br>
```
Examples.

privet -> привет
ludi -> луди 
kak delа u tebe -> как дела у тебе
```

## Installation
First install python3 (recommended version python3.8):

On Linux:
```
sudo apt install python3.8 python3.8-pip
```

On Mac:
```
brew install python3.8
brew install python3.8-pip
```

On Windows:
Navigate to the python website and install from there.    <br>
```https://www.python.org/downloads/```

To install the requirements run the following command:
``` 
pip3 install -r requirements.txt 
``` 

## Usage
Clone the repo through ssh or html and cd into the directory with 
``` 
git clone git@github.com:mgoldgirsh/russian-conversion.git
cd russian-coversion
```

Then to use, run the script with the following
``` 
chmod +x russian_conversion_script
./russian_conversion_script 
```   
or run the following your terminal window
``` 
python3 russian_conversion_process 
```

Once the process is running you can start typing in English and then click the <spacebar> to transform the text into Russian.
To exit the process click the <esc> key on your keyboard. 

## Things to Add (WIP Project)
- Add machine learning so words would autocorrect (complicated)
- Add better conversion so that russian characters are easier to acces
    - specifically characters that map to "sh" or "sch" that are more than one character
- Add tab autocomplete so it knows what character to go to 
