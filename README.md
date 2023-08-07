# QuestionDB-SCE
College Project

# Prerequisites : 

```
pdf2image package & image2docx package
```
# Installing : 

How to install pdf2image
```
pip install pdf2image
```
1. change the following line in pdf2image.py file in your site-packages:
```fmt="ppm"``` to ```fmt="png"``` so it will convert to .png format

2. change the following line in generators.py file in your site-packages:
```yield str(uuid4())``` to ```yield str('Question')```

how to install image2docx

```
pip install python-docx
```
1. change the path where your .png files are:
```r.add_picture(f'PATH/{files_name[i]}', width=Cm(15), height=Cm(17))```
2. (optional) change the name of the docx file:
```document.save('PATH/demo.docx')```
Default path is the working directory.
