# learnpy-app

# Running

Download the files

Install all requirements

```txt
pip install customtkinter
```

then run main.py

# Creating .exe

Make sure that you have pyinstaller installed

```txt
pip install pyinstaller
```

then run this command in the directory the code is located

```txt
 pyinstaller --noconfirm --onedir --windowed --add-data "C:\Users\hkurt\AppData\Local\Programs\Python\Python311\Lib\site-packages/customtkinter;customtkinter/"  "main.py"
```
