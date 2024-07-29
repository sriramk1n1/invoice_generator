from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
import datetime
import database


date=datetime.date.today().strftime("%d/%m/%Y")
month=datetime.date.today().strftime("%B")

def generatepdf(billno,d1,d2,d3,d4):

    data = getdata(billno,d1,d2,d3,d4)
    # Define the styles for the table
    style = TableStyle([('OUTLINE', (0, 0), (-1, -1), 1, colors.black),
                        ('ALIGN', (0, 4), (-1, -1), 'CENTER'),
                        ('ALIGN', (3, 1), (3, 1), 'CENTER'), 
                        ('ALIGN', (3, 0), (3, 0), 'CENTER'),            
                        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                        ('TEXTCOLOR', (1, 1), (1, 1), colors.red),
                        ('TEXTCOLOR', (3, 1), (3, 1), colors.red),
                        ('TEXTCOLOR',(3,0),(3,0),colors.red),
                        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
                        ('FONTSIZE', (0, 0), (-1, -1), 11),
                        ('FONTSIZE', (3,1),(3,1) , 16),
                        ('FONTSIZE', (3,0),(3,0) , 12),
                        ('FONTNAME', (3, 1), (3, 1), 'Times-BoldItalic'),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 7),
                        ('TOPPADDING',(3,1),(3,1),5),
                        ('GRID', (0, 4), (-1, -4), 1, colors.black),
                        ('GRID', (-1, -3), (-1, -3), 1, colors.black),
                        ('SPAN', (5,1),(6,1)),
                        ('SPAN',(-3,2),(-1,2))])

    # Create the table and add the data and styles
    table = Table(data,colWidths=[40,60,75,190,85,60,60])
    table.setStyle(style)

    # Create the PDF document and add the table
    doc = SimpleDocTemplate("bills/Bill_No_"+billno+".pdf", pagesize=letter, leftMargin=100, rightMargin=100, topMargin=10, bottomMargin=20)

    doc.build([table])


def getdata(billno,d1,d2,d3,d4): 
    res=list()
    str1="Internship II project - Invoice Generator" if d2=="" else d2
    str2="To, _______________________________________________________________________________________" if d1=="" else "To, "+d1
    res.append([None,None,None,str1,None,None,None])
    res.append(["Bill No. : ","  "+billno.zfill(3),None,"INVOICE",None,"    Date : "+d3,None])
    res.append([None,None,None,None,f"                   Billing Month : {d4}",None,None])
    res.append([str2,None,None,None,None,None,None])
    res.append(["S.No.","Date","Consig. No.","Consignee","Dest.","Weight","Amount"])
    li=list()
    total=0


    for entry in database.allrows(billno):
        li=list()
        li.append(entry[0])
        li.append(entry[1])
        li.append(entry[2])
        li.append(entry[3])
        li.append(entry[4])
        li.append(entry[5])
        if entry[6]=="":
            li.append(0)
        else:
            li.append(entry[6])
        
        res.append(li)
        total+=li[-1]

    if len(res)<=30:
        res.extend([[None]*7]*(33-len(res)))
    else:
        res.extend([[None]*7]*3)
    res[-3]=[None,None,None,None,None,"TOTAL",total]
    res[-1]=[None,"Seal & Signature",None,None,None,None,None]
    return res
















