from django.shortcuts import render
# from convertor.models import filesUpload
from convertor.models import ImageUpload
from pathlib import Path
import os
#import win32com.client
# import pythoncom
# import comtypes
# import comtypes.client
from PIL import Image
from docx2pdf import convert
# import datetime
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys
from io import StringIO
from PIL import Image
from PIL import ImageDraw
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile



BASE_DIR = Path(__file__).resolve().parent.parent


def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,"about.html")

def result(request):
    print(result)
    return render(request,'result.html')

def backgroundremover(request):
    if request.method=="POST":
        try:
            file2=request.FILES["file"]
            document=ImageUpload.objects.create(File=file2)
            document.save()
            infile_path=str(BASE_DIR)+"\\"+str(document.File.url)
            outfile_path=str(BASE_DIR)+"\\media\\images\\abc.png"
            blur_remove(infile_path,outfile_path)
            document1=ImageUpload.objects.create(File=outfile_path)
            document1.save()
            return render(request,"result.html",{"Dlink":document1.File.url})
        except:
            return render(request,"errorpage.html")
    return render(request,"background.html")


def imageconvertor(request):
    if request.method=="POST":
        #Converting JPG TO PNG

        if request.POST.get("jpg2png"):
            try:
                print("Converting JPG TO PNG")
                file2=request.FILES["file"]
                file_content = ContentFile(file2.read())
                new_file = ImageUpload() 
                new_file.File.save('converted'+'.png', file_content)
                new_file.save()


        #         document=ImageUpload.objects.create(File=file2)
        #         document.save()

        #         file_content = ContentFile(document.File.read())
        #         document.File.close()
        #         img = Image.open(file_content)
        #         newimg=img.convert("RGB")
        #         buffer = StringIO()
        #         print("hello")
        #         print(newimg)
        #         newimg.save(buffer, format="PNG")
        #         print("hello")
        #         print("hello")
        #         image_file = InMemoryUploadedFile(buffer, None, "temp", 'image/png', buffer.len, None)
        #         print("hello")
        #         document.File.save("temp",image_file)
        #         print('The image conversion from JPG to PNG is successful')
        #         return render(request,"result.html",{"Dlink":document.File.url})
        #     except:
        #         print("wrong")
        #         return render(request,"errorpage.html")

        # #Converting JPG to WEBP
        # if request.POST.get("jpg2webp"):
        #     try:
        #         print("Converting JPG TO WEBP")
        #         for i in os.listdir(x):
        #             os.remove(x+i)
        #         file2=request.FILES["file"]
        #         document=ImageUpload.objects.create(File=file2)
        #         document.save()
        #         imgPath=str(BASE_DIR)+"\\"+str(document.File.url)
        #         img = Image.open(imgPath).convert("RGB")
        #         img.save(x+'newData.webp')
        #         document1=ImageUpload.objects.create(File=(x+'newData.webp'))
        #         document1.save()
        #         print('The image conversion from JPG to WEBP is successful')
                return render(request,"result.html",{"Dlink":new_file.File.url})
            except:
                return render(request,"errorpage.html")

        #Converting PNG TO JPG
        if request.POST.get("png2jpg"):
            try:
                print("Converting PNG TO JPG")
                file2=request.FILES["file"]
                file_content = ContentFile(file2.read())
                new_file = ImageUpload() 
                new_file.File.save('converted'+'.jpg', file_content)
                new_file.save()
                # for i in os.listdir(x):
                #     os.remove(x+i)
                # file2=request.FILES["file"]
                # document=ImageUpload.objects.create(File=file2)
                # document.save()
                # imgPath=str(BASE_DIR)+"\\"+str(document.File.url)
                # img = Image.open(imgPath).convert("RGB")
                # img.save(x+'newData.jpg')
                # document1=ImageUpload.objects.create(File=(x+'newData.jpg'))
                # document1.save()
                # print('The image conversion from PNG TO JPG is successful')
                return render(request,"result.html",{"Dlink":new_file.File.url})
            except:
                return render(request,"errorpage.html")


        #Converting JPG TO PNG
        if request.POST.get("png2webp"):
            try:
                print("Converting PNG TO WEBP")
                file2=request.FILES["file"]
                file_content = ContentFile(file2.read())
                new_file = ImageUpload() 
                new_file.File.save('converted'+'.webp', file_content)
                new_file.save()
                # for i in os.listdir(x):
                #     os.remove(x+i)
                # file2=request.FILES["file"]
                # document=ImageUpload.objects.create(File=file2)
                # document.save()
                # imgPath=str(BASE_DIR)+"\\"+str(document.File.url)
                # img = Image.open(imgPath).convert("RGB")
                # img.save(x+'newData.webp')
                # document1=ImageUpload.objects.create(File=(x+'newData.webp'))
                # document1.save()
                # print('The image conversion from PNG TO WEBP is successful')
                return render(request,"result.html",{"Dlink":new_file.File.url})
            except:
                return render(request,"errorpage.html")

        #Converting WEBP TO JPG
        if request.POST.get("webp2jpg"):
            try:
                print("Converting WEBP TO JPG")
                file2=request.FILES["file"]
                file_content = ContentFile(file2.read())
                new_file = ImageUpload() 
                new_file.File.save('converted'+'.jpg', file_content)
                new_file.save()
                # for i in os.listdir(x):
                #     os.remove(x+i)
                # file2=request.FILES["file"]
                # document=ImageUpload.objects.create(File=file2)
                # document.save()
                # imgPath=str(BASE_DIR)+"\\"+str(document.File.url)
                # img = Image.open(imgPath).convert("RGB")
                # img.save(x+'newData.jpg')
                # document1=ImageUpload.objects.create(File=(x+'newData.jpg'))
                # document1.save()
                # print('The image conversion from PNG TO WEBP is successful')
                return render(request,"result.html",{"Dlink":new_file.File.url})
            except:
                return render(request,"errorpage.html")

        #Converting WEBP TO PNG
        if request.POST.get("webp2png"):
            try:
                print("Converting WEBP TP PNG")
                file2=request.FILES["file"]
                file_content = ContentFile(file2.read())
                new_file = ImageUpload() 
                new_file.File.save('converted'+'.png', file_content)
                new_file.save()
                # for i in os.listdir(x):
                #     os.remove(x+i)
                # file2=request.FILES["file"]
                # document=ImageUpload.objects.create(File=file2)
                # document.save()
                # imgPath=str(BASE_DIR)+"\\"+str(document.File.url)
                # img = Image.open(imgPath).convert("RGB")
                # img.save(x+'newData.png')
                # document1=ImageUpload.objects.create(File=(x+'newData.png'))
                # document1.save()
                # print('The image conversion from PNG TO WEBP is successful')
                return render(request,"result.html",{"Dlink":new_file.File.url})
            except:
                return render(request,"errorpage.html")

    return render(request,"imageconvertor.html")



# def fileconvertor(request):
#     x= os.path.join(BASE_DIR, "media\\")
#     if request.method=="POST":

#         # Converting PPT To PDF
#         if request.POST.get('ppt2pdf'):
#             try:
#                 print("Convering PPT TO PDF")
#                 file2 = request.FILES["file"]
#                 document = filesUpload.objects.create(file=file2)
#                 document.save()
#                 y=str(BASE_DIR)+"\\"+str(document.file.url)
#                 z=os.path.splitext(y)[0]
#                 PPT_to_PDF(y,z)
#                 z=z+".pdf"
#                 document1= filesUpload.objects.create(file=z)
#                 document1.save()
#                 return render(request,"result.html",{"Dlink":document1.file.url})
#             except:
#                 return render(request,"errorpage.html")


#         #Converting PDF TO DOC
#         if request.POST.get('pdf2doc'):
#             try:
#                 print("Converting PDF TO DOC")
#                 file2 = request.FILES["file"]
#                 document = filesUpload.objects.create(file=file2)
#                 document.save()
#                 y=str(BASE_DIR)+"\\"+str(document.file.url)
#                 z=os.path.splitext(y)[0]
#                 PDF_to_DOC(y,z)
#                 z=str(z)+'.docx'
#                 document1= filesUpload.objects.create(file=z)
#                 document1.save()
#                 print(z)
#                 return render(request,"result.html",{"Dlink":document1.file.url})
#             except:
#                 return render(request,"errorpage.html")


#         # Conveting DOC TO PDF
#         if request.POST.get('doc2pdf'):
#             try:
#                 print("Converting DOC TO PDF")
#                 file2 = request.FILES["file"]
#                 document = filesUpload.objects.create(file=file2)
#                 document.save()
#                 y=str(BASE_DIR)+"\\"+str(document.file.url)
#                 z=x+"abc.pdf"
#                 DOC_to_PDF(y,z)
#                 document1= filesUpload.objects.create(file=z)
#                 document1.save()
#                 return render(request,"result.html",{"Dlink":document1.file.url})
#             except:
#                 return render(request,"errorpage.html")

#         # Converting XLS TO PDF
#         if request.POST.get('xls2pdf'):
#             print("Converting XLS TO PDF")
#             file2=request.FILES["file"]
#             document=filesUpload.objects.create(file=file2)
#             document.save()
#             infile_path=str(BASE_DIR)+"\\"+str(document.file.url)
#             outfile_path=str(BASE_DIR)+"\\"+str("\\media\\xlscon.pdf")
#             XLS_to_PDF(infile_path,outfile_path)
#             document1=filesUpload.objects.create(file=outfile_path)
#             document1.save()
#             return render(request,"result.html",{"Dlink":document1.file.url})
            


#         # Converting JPG TO PDF
#         if request.POST.get('jpg2pdf'):
#             try:
#                 print("Converting JPG TO PDF")
#                 file2=request.FILES['file']
#                 document=filesUpload.objects.create(file=file2)
#                 document.save()
#                 infile_path=str(BASE_DIR)+"\\"+str(document.file.url)
#                 outfile_path=str(BASE_DIR)+"\\media\\jpg2pdf.pdf"
#                 JPG_to_PDF(infile_path,outfile_path)
#                 document1=filesUpload.objects.create(file=outfile_path)
#                 document1.save()
#                 return render(request,"result.html",{"Dlink":document1.file.url})
#             except:
#                 return render(request,"errorpage.html")


#         # Converting PNG TO PDF
#         if request.POST.get('png2pdf'):
#             try:
#                 print("Converting PNG TO PDF")
#                 file2=request.FILES['file']
#                 document=filesUpload.objects.create(file=file2)
#                 document.save()
#                 infile_path=str(BASE_DIR)+"\\"+str(document.file.url)
#                 outfile_path=str(BASE_DIR)+"\\media\\png2pdf.pdf"
#                 PNG_to_PDF(infile_path,outfile_path)
#                 document1=filesUpload.objects.create(file=outfile_path)
#                 document1.save()
#                 return render(request,"result.html",{"Dlink":document1.file.url})
#             except:
#                 return render(request,"errorpage.html")


#     return render(request,"fileconvertor.html")


# Function used for converting PPT TO PDF
# def PPT_to_PDF(inputFileName, outputFileName):
#     pythoncom.CoInitialize()
#     powerpoint = win32com.client.Dispatch("Powerpoint.Application")
#     deck = powerpoint.Presentations.Open(inputFileName)
#     deck.SaveAs(outputFileName,32)
#     deck.Close()
#     powerpoint.Quit()


# #Function used for converting PDF TO DOC
# def PDF_to_DOC(infile_path, outfile_path):
#     pythoncom.CoInitialize()
#     word = win32com.client.Dispatch("Word.Application")
#     wb = word.Documents.Open(infile_path, False, False, False)
#     wb.SaveAs2(outfile_path, 16)
#     wb.Close()
#     word.Quit()


# #Function used for converting DOC to PDF
# def DOC_to_PDF(infile_path,outfile_path):
#     pythoncom.CoInitialize()
#     convert(infile_path,outfile_path)
    


# #Function used for converting EXCEL to PDF
# def XLS_to_PDF(infile_path,outfile_path):
#     pythoncom.CoInitialize()
#     excel = win32com.client.Dispatch("Excel.Application")
#     sheets = excel.Workbooks.Open(infile_path)
#     work_sheets = sheets.Worksheets[0]
#     work_sheets.ExportAsFixedFormat(0,outfile_path)


#Function used for converting JPG TO PDF
def JPG_to_PDF(infile_path,outfile_path):
    image1 = Image.open(infile_path)
    im1 = image1.convert('RGB')
    im1.save(outfile_path)



#Function used for converting PNG to PDF
def PNG_to_PDF(infile_path,outfile_path):
    image1 = Image.open(infile_path)
    im1 = image1.convert('RGB')
    im1.save(outfile_path)



def blur_remove(infile_path,outfile_path):
    img = cv.imread(infile_path, cv.IMREAD_UNCHANGED)
    original = img.copy()

    l = int(max(5, 6))
    u = int(min(6, 6))

    ed = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.GaussianBlur(img, (21, 51), 3)
    edges = cv.cvtColor(edges, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(edges, l, u)

    _, thresh = cv.threshold(edges, 0, 255, cv.THRESH_BINARY  + cv.THRESH_OTSU)
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
    mask = cv.morphologyEx(thresh, cv.MORPH_CLOSE, kernel, iterations=4)

    data = mask.tolist()
    sys.setrecursionlimit(10**8)
    for i in  range(len(data)):
        for j in  range(len(data[i])):
            if data[i][j] !=  255:
                data[i][j] =  -1
            else:
                break
        for j in  range(len(data[i])-1, -1, -1):
            if data[i][j] !=  255:
                data[i][j] =  -1
            else:
                break
    image = np.array(data)
    image[image !=  -1] =  255
    image[image ==  -1] =  0

    mask = np.array(image, np.uint8)

    result = cv.bitwise_and(original, original, mask=mask)
    result[mask ==  0] =  255
    cv.imwrite('bg.png', result)

    img = Image.open('bg.png')
    img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] ==  255  and item[1] ==  255  and item[2] ==  255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    img.putdata(newData)
    img.save(outfile_path, "PNG")
