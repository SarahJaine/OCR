#OCR
##optical character recognition
These projects require Tesseract Open Source OCR Engine v3.02.02 with Leptonica.

**I followed these install steps:**
  - $ pip install homebrew
  - $ brew install tesseract
  - $ pip install Pillow

**To test that tesseract is properly installed:**

(remember, test_image.png will need to be saved in the directory you are in)
  - $ tesseract test_image.png textoutput | cat textoutput.txt

You will get a message "cat: textoutput.txt: No such file or directory" the first time this is run.
Despite this message, the textoutput.txt file will be created.

