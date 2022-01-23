import webbrowser
import pathlib
import openpyxl
import os

# ブックを取得
book = openpyxl.load_workbook('入力シート.xlsx')
# シートを取得 
sheet1 = book['Sheet1']
# セルを取得
title = sheet1['B2'].value
subTitle = sheet1['B3'].value

table = "";
if sheet1['B4'].value == "○":
  loopNumC = sheet1['C5'].value
  i=1
  table = "<div><table border='1'>"
  for num in range(loopNumC):
    arrayB = "B"+str(5+i)
    arrayC = "C"+str(5+i)
    arrayD = "D"+str(5+i)
    arrayE = "E"+str(5+i)
    arrayF = "F"+str(5+i)
    tableDataRow = sheet1[arrayB].value
    tableDataA_i=sheet1[arrayC].value
    tableDataB_i=sheet1[arrayD].value
    tableDataC_i=sheet1[arrayE].value
    tableDataD_i=sheet1[arrayF].value
    table+="<tr><td>"+str(tableDataRow)+"</td>"
    table+="<td "+'id="'+tableDataC_i+'"'+' class='+tableDataD_i+'"'">"+tableDataA_i+"</td>"
    table+="<td>"+tableDataB_i+"</td></tr>"
    i=i+1
  table+="</table></div>"


#シート変数.cell(row=行No.,column=列No.).value

index = sheet1['B1'].value

if(os.path.isfile("C:\\Users\\user\\Documents\\python\\html\\"+index+".html")):
  html= pathlib.Path("C:\\Users\\user\\Documents\\python\\html\\"+index+"_copy.html")
else:
  html= pathlib.Path("C:\\Users\\user\\Documents\\python\\html\\"+index+".html")

html.touch()

head = "<DOCTYPE html><html lang='ja'><head>"
head += "<meta name='viewport' content='width=device-width,initial-scale=1'>"
head += "<link rel='stylesheet' href='../css/default.css'>"
head += "<title>"+title+"</title>"
head += "</head>"
cssFile= pathlib.Path("C:\\Users\\user\\Documents\\python\\css\\default.css")

with open(cssFile, mode="w") as f:
        f.write("html,body{background:rgb(29,29,29);color:rgb(200,200,200);}table{width:"+sheet1['E5'].value+";height:"+sheet1['F5'].value+";}")

with open(html, mode="w") as f:
        f.write(head)
        f.write("<body>")
        f.write("<h1>"+title+"</h1>")
        f.write("<h2>"+subTitle+"</h2>")
        if table!="":
        	f.write(table)
        else: 
            f.write("")
        f.write("</body>")
        f.write("</html>")
        
webbrowser.open(html)