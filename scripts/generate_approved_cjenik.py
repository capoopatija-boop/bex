from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from pathlib import Path
out=Path('downloads/BEX_cjenik_bazna_10-09-2026_bez_PDV.pdf')
out.parent.mkdir(exist_ok=True)
pdfmetrics.registerFont(TTFont('DV','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('DVB','/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
rows=[
('DOLAZAK PO AUTO','20,00 €'),('PODNO PRANJE VOZILA','6,00 €'),('VANJSKO PRANJE AUTA MALI','12,00 €'),('VANJSKO PRANJE AUTA SREDNJI','13,00 €'),('VANJSKO PRANJE AUTA VELIKI (SUV/JEEP)','15,00 €'),('KOMPLET PRANJE AUTO MALI','25,00 €'),('KOMPLET PRANJE AUTO SREDNJI (MONOVOLUMEN/LIMUZINA)','27,00 €'),('KOMPLET PRANJE AUTO VELIKI (SUV/JEEP)','33,00 €'),('KOMPLET PRANJE KOMBI SREDNJI - VANJSKO','20,00 €'),('KOMPLET PRANJE KOMBI SREDNJI - UNUTARNJE','25,00 €'),('KOMPLET PRANJE KOMBI SREDNJI','40,00 €'),('KOMPLET PRANJE KOMBI VELIKI - VANJSKO','20,00 €'),('KOMPLET PRANJE KOMBI VELIKI - UNUTARNJE','35,00 €'),('KOMPLET PRANJE KOMBI VELIKI','50,00 €'),('UNUTARNJE ČIŠĆENJE AUTA MALI ILI SREDNJI','20,00 €'),('EKSTREMNO PRLJAVO VOZILO (PSEĆE DLAKE I SL.)','7,00 €'),('DUBINSKO ČIŠĆENJE SJEDALA (1 kom)','30,00 €'),('DUBINSKO ČIŠĆENJE SJEDALA U AUTU kpl.','125,00 €'),('DUBINSKO ČIŠĆENJE TAPISONA U AUTU 4 kom.','15,00 €'),('DUBINSKO ČIŠĆENJE POD/STROP','70,00 €'),('DUBINSKO ČIŠĆENJE PRTLJAŽNIK','20,00 €'),('ZAŠTITNI PREMAZ KOŽE SJEDALA kpl.','80,00 €'),('DETAILING PRANJE AUTA','250,00 €'),('DETAILING PRANJE KABINE KAMIONA','300,00 €'),('PRANJE KUĆNIH TEPIHA (MANJI) KOM','20,00 €'),('PRANJE KUĆNIH TEPIHA (SREDNJI) KOM','40,00 €'),('PRANJE TEPIHA (m²)','7,00 €'),('PRANJE MOTORKOTAČA','15,00 €'),('PRANJE MOTORNOG PROSTORA','30,00 €'),('SKIDANJE NALJEPNICA / VINJETA','1,00 €')]
W,H=A4
c=canvas.Canvas(str(out),pagesize=A4)
navy=HexColor('#15314a')
muted=HexColor('#4c5b66')
light=HexColor('#eef3f6')
border=HexColor('#d8e0e5')
x=36
right=W-36
c.setFillColor(navy)
c.rect(0,H-8,W,8,stroke=0,fill=1)
c.setFont('DVB',12)
c.drawString(x,H-37,'BEX obrt za usluge')
c.setFont('DV',8.5)
for i,line in enumerate(['vl. Bekim Kaqandolli','Stubište Lipovica 3, 51410 Opatija','OIB: 36219517898','Tel: +385 91 306 99 99','E-mail: autopraonabex@gmail.com']):
 c.drawString(x,H-53-i*12,line)
c.setFont('DVB',17)
c.setFillColor(navy)
c.drawCentredString(W/2,H-142,'CJENIK USLUGA')
c.setFont('DV',9)
c.setFillColor(muted)
c.drawCentredString(W/2,H-157,'CAR WASH BEX | Usporedba s baznom cijenom na dan 10.09.2026.')
cols=[x,390,464,right]
top=H-177
rowh=16.4
c.setFillColor(navy)
c.roundRect(x,top-28,right-x,28,4,fill=1,stroke=0)
c.setFillColor(HexColor('#ffffff'))
c.setFont('DVB',8)
c.drawString(x+7,top-17,'USLUGA')
c.drawCentredString((cols[1]+cols[2])/2,top-12,'CIJENA')
c.drawCentredString((cols[2]+cols[3])/2,top-12,'BAZNA CIJENA')
c.setFont('DV',6.4)
c.drawCentredString((cols[2]+cols[3])/2,top-22,'10.09.2026.')
y=top-28
for i,(name,price) in enumerate(rows):
 y-=rowh
 if i%2==0:
  c.setFillColor(light)
  c.rect(x,y,right-x,rowh,fill=1,stroke=0)
 c.setStrokeColor(border)
 c.setLineWidth(.4)
 c.line(x,y,right,y)
 c.setFillColor(HexColor('#1f2f38'))
 size=7.35
 while pdfmetrics.stringWidth(name,'DV',size)>cols[1]-x-13:
  size-=.15
 c.setFont('DV',size)
 c.drawString(x+6,y+5,name)
 c.setFont('DVB',7.7)
 c.drawRightString(cols[2]-8,y+5,price)
 c.setFont('DV',7.7)
 c.drawRightString(right-7,y+5,price)
c.setStrokeColor(border)
for xx in (x,right,cols[1],cols[2]):
 c.line(xx,top-28,xx,y)
c.setFillColor(muted)
c.setFont('DV',7.6)
c.drawString(x,y-17,'Bazne cijene na dan 10.09.2026. jednake su prikazanim cijenama usluga.')
c.setFont('DV',6.8)
c.drawString(x,69,'PDV nije obračunat sukladno članku 90. stavku 1. Zakona o porezu na dodanu vrijednost.')
c.drawString(x,58,'Mali porezni obveznik.')
c.setFont('DV',7)
c.drawString(x,42,'BEX obrt za usluge  |  vl. Bekim Kaqandolli  |  Opatija')
c.drawRightString(right,42,'Cjenik • 1/1')
c.save()
print('Generated:',out,'services',len(rows),'bytes',out.stat().st_size)
