# docstringFormatter

Format docstring to be able to entry in DeepL or GoogleTranslate.

    Main function:
        1. Remove newline
        2. Reduce extra spaces
        3. Output result as txt-file

"docstringFormatter" releases you from boring duties to reform the docstring string in the Entry of DeepL or GoogleTranslate so that these get  correct translation.

# DEMO
Below show the console display when get docstring of `logging.Logger` object.  

____ _"[logging](https://docs.python.org/3/library/logging.html)" is one of the standard libraries of Python._  

Compared with "Original Sentence" section,  the strings of "Formatted Sentence"  is converted in one line by removing newlines and extra spaces that consist of indention of left side.  

Only the left thing you do is copy & paste the strings of "Formatted Sentence" in the Entry of Translating Web Application like DeepL or GoogleTranslate.  

```
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
   Formatted Sentence   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 Instances of the Logger class represent a single logging channel. A "logging channel" indicates an area of an application. Exactly how an "area" is defined is up to the application developer. Since an application can have any number of areas, logging channels are identified by a unique string. Application areas can be nested (e.g. an area of "input processing" might include sub-areas "read CSV files", "read XLS files" and "read Gnumeric files"). To cater for this natural nesting, channel names are organized into a namespace hierarchy where levels are separated by periods, much like the Java or Python package namespace. So in the instance given above, channel names might be "input" for the upper level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels. There is no arbitrary limit to the depth of nesting. 

■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
   Original Sentence   
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    Instances of the Logger class represent a single logging channel. A
    "logging channel" indicates an area of an application. Exactly how an
    "area" is defined is up to the application developer. Since an
    application can have any number of areas, logging channels are identified
    by a unique string. Application areas can be nested (e.g. an area
    of "input processing" might include sub-areas "read CSV files", "read
    XLS files" and "read Gnumeric files"). To cater for this natural nesting,
    channel names are organized into a namespace hierarchy where levels are
    separated by periods, much like the Java or Python package namespace. So
    in the instance given above, channel names might be "input" for the upper
    level, and "input.csv", "input.xls" and "input.gnu" for the sub-levels.
    There is no arbitrary limit to the depth of nesting.
    
```
 
# Features
1. Easy to Use  
__ You can use the function just adjust content of `main()` in code.
2. Easy to Read  
__ Console display is designated simply and reasonably.
3. Easy to Introduce  
__ Ofcourse introducing to your code is also simple.  
__ First import at top in your cord.  
__ And Just copy & paste the content of `main()` to the appropriate line.  
__ main() is showed on "Usage" below.
```python
# import sentences example in case you'll copy & paste contents of main()
from docstringFormatter import docstring_formatter
from docstringFormatter import console_constructor
from docstringFormatter import txt_outputter
```
  

# Requirement
 
"docstringFormatter" (ver.1.0.0) doesn't require third-party Library.
Probably, it works on over Python3.7.x Envelopment.

* Python 3.7.x
 
# Installation
 
Install "docstringFormatter" with pip command.
 
```bash
pip install docstringFormatter
```
 
# Usage
 
Open the python file named "docstringFormatter.py" with any text editor and so on.  

Then change the assignment for var `name_object` in `main()` to the identifier of the object you want to get docstring.  

If you want the result as a txt-file, revalue the arguments of `txt_outputter()` appropriately.  

See the comments in the below code for details.

```python
def main():
    """
    You can try the function here.
    """

    # If the object requires import of module, you do so like the under example 'logging'
    import logging
    # Assign the identifier of object to 'name_object'
    name_object = logging.Logger
    # Default Setting at main() --> name_obj=name_object, times_red=2, rmv_t=True, rmv_n=True
    str_result = docstring_formatter(name_obj=name_object, times_red=2, rmv_t=True, rmv_n=True)

    console_constructor(str_result, name_object.__doc__)

    # If you need the output txt-file, revalue the 'output' arg to True.
    # You can change the output file name by rewriting 'filename' arg.
    txt_outputter(output=False, filename='docstring_formatted')

    # When you want the output is the same as 'Original Sentence' displayed on console,
    # revalue the arguments setting of docstring_formatter() like below.
    #
    # Setting at main() --> name_obj=name_object, times_red=0, rmv_t=False, rmv_n=False

```
 
# Note
 
I don't test the Environments under Linux and Mac.
 
# Author

* Auther: **Aoi Natsuki (蒼井 夏樹)**
* Work: [Blau Tine](https://sites.google.com/view/blau-tinte)
* E-mail: blautinte8`☆`gmail.com  
_- - - - - > Replace '☆' for '@'_
        

* Twitter ( or "X")
    <dl>
    <dt>Auther</dt>
     <dd><a href="https://twitter.com/Aoi_NatsuSolar">Aoi Natsuki(蒼井 夏樹)</a></dd>
     <dt>Workplace</dt>
     <dd><a href="https://twitter.com/BlauTinte">Blau Tinte</a></dd>
    </dl> 
* LinkedIn: [Aoi Natsuki](https://www.linkedin.com/in/aoi-natsuki)
 
# License

 
"docstringFormatter" is under [MIT license](https://opensource.org/license/mit).
