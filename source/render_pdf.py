# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Image, Table, TableStyle, PageBreak, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
import content as C

OUT = os.path.join(C.SC, "MTN_Enterprise_Analytics_Strategy.pdf")
LS = "/usr/share/fonts/truetype/liberation"
pdfmetrics.registerFont(TTFont("TNR", f"{LS}/LiberationSerif-Regular.ttf"))
pdfmetrics.registerFont(TTFont("TNR-Bold", f"{LS}/LiberationSerif-Bold.ttf"))
pdfmetrics.registerFont(TTFont("TNR-Italic", f"{LS}/LiberationSerif-Italic.ttf"))
pdfmetrics.registerFont(TTFont("TNR-BoldItalic", f"{LS}/LiberationSerif-BoldItalic.ttf"))
pdfmetrics.registerFontFamily("TNR", normal="TNR", bold="TNR-Bold",
                              italic="TNR-Italic", boldItalic="TNR-BoldItalic")

def esc(t):
    return (C.clean(t).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;"))

LEAD = 12*1.5  # 18
body = ParagraphStyle("body", fontName="TNR", fontSize=12, leading=LEAD,
                      alignment=TA_JUSTIFY, spaceAfter=6)
body_sm = ParagraphStyle("body_sm", parent=body, fontSize=11, leading=16)
body_sm_ind = ParagraphStyle("body_sm_ind", parent=body_sm, leftIndent=0.3*inch)
h1 = ParagraphStyle("h1", fontName="TNR-Bold", fontSize=13, leading=16,
                    alignment=TA_LEFT, spaceBefore=16, spaceAfter=6)
h2 = ParagraphStyle("h2", fontName="TNR-Bold", fontSize=12, leading=15,
                    alignment=TA_LEFT, spaceBefore=10, spaceAfter=4)
cap = ParagraphStyle("cap", fontName="TNR", fontSize=10.5, leading=13,
                     alignment=TA_LEFT, spaceBefore=2, spaceAfter=10)
ref = ParagraphStyle("ref", fontName="TNR", fontSize=12, leading=LEAD,
                     alignment=TA_LEFT, spaceAfter=6, leftIndent=0.5*inch, firstLineIndent=-0.5*inch)
cover_c = ParagraphStyle("cover_c", fontName="TNR", fontSize=12, leading=18, alignment=TA_CENTER, spaceAfter=3)

def cap_para(num, text):
    return Paragraph(f'<b>{esc(num)}</b> <i>{esc(text)}</i>', cap)

CONTENT_W = A4[0] - 2*inch
story = []

# cover
story.append(Spacer(1, 1.2*inch))
for txt, size, bold in C.COVER:
    if txt == "__gap__":
        story.append(Spacer(1, 0.28*inch)); continue
    st = ParagraphStyle(f"cov{size}{bold}", parent=cover_c, fontSize=size,
                        leading=size*1.35, fontName="TNR-Bold" if bold else "TNR")
    story.append(Paragraph(esc(txt), st))
story.append(PageBreak())

for el in C.DOC:
    k = el["k"]
    if k == "h1":
        story.append(Paragraph(esc(el["t"]), h1))
    elif k == "h2":
        story.append(Paragraph(esc(el["t"]), h2))
    elif k == "p":
        stl = body_sm_ind if el.get("indent") else (body_sm if el.get("size")==11 else body)
        story.append(Paragraph(esc(el["t"]), stl))
    elif k == "prompt5":
        p5 = ParagraphStyle("p5", fontName="TNR", fontSize=12, leading=LEAD,
                            alignment=TA_JUSTIFY, spaceAfter=2,
                            leftIndent=0.5*inch, firstLineIndent=-0.3*inch)
        for lab, txt in el["items"]:
            story.append(Paragraph(f'<b>{esc(lab)}:</b> {esc(txt)}', p5))
    elif k == "pagebreak":
        story.append(PageBreak())
    elif k == "fig":
        from PIL import Image as PILImage
        iw, ih = PILImage.open(el["path"]).size
        w = el["w"]*inch; h = w*ih/iw
        img = Image(el["path"], width=w, height=h)
        img.hAlign = "CENTER"
        story.append(Spacer(1,6))
        story.append(KeepTogether([img, cap_para(el["num"], el["cap"])]))
    elif k == "table":
        story.append(cap_para(el["num"], el["cap"]))
        data = [[Paragraph(f'<b>{esc(h)}</b>', ParagraphStyle("th",fontName="TNR-Bold",fontSize=10.5,leading=13)) for h in el["headers"]]]
        for row in el["rows"]:
            data.append([Paragraph(esc(v), ParagraphStyle("td",fontName="TNR",fontSize=10.5,leading=13)) for v in row])
        widths=[w*inch for w in el["widths"]]
        # scale widths to content width
        scale = CONTENT_W/sum(widths); widths=[w*scale for w in widths]
        t = Table(data, colWidths=widths, hAlign="CENTER")
        t.setStyle(TableStyle([
            ("BACKGROUND",(0,0),(-1,0),colors.HexColor("#EBEBEB")),
            ("GRID",(0,0),(-1,-1),0.75,colors.HexColor("#AAAAAA")),
            ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
            ("LEFTPADDING",(0,0),(-1,-1),6),("RIGHTPADDING",(0,0),(-1,-1),6),
            ("TOPPADDING",(0,0),(-1,-1),4),("BOTTOMPADDING",(0,0),(-1,-1),4),
        ]))
        story.append(t); story.append(Spacer(1,8))
    elif k == "annot":
        annot = ParagraphStyle("annot", fontName="TNR", fontSize=11, leading=16,
                               alignment=TA_JUSTIFY, spaceAfter=8,
                               leftIndent=0.3*inch, firstLineIndent=-0.3*inch)
        html = (f'<b>{esc(el["label"])}</b> &#8220;{esc(el["quote"])}&#8221; '
                f'<i>({esc(el["prov"])})</i>')
        story.append(Paragraph(html, annot))
    elif k == "refs":
        for r in el["items"]:
            story.append(Paragraph(esc(r), ref))

def footer(canv, doc):
    canv.saveState()
    canv.setFont("TNR", 10)
    canv.drawCentredString(A4[0]/2, 0.6*inch, str(doc.page))
    canv.restoreState()

frame = Frame(inch, inch, CONTENT_W, A4[1]-2*inch, id="main")
doct = BaseDocTemplate(OUT, pagesize=A4, leftMargin=inch, rightMargin=inch,
                       topMargin=inch, bottomMargin=inch)
doct.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=footer)])
doct.build(story)
print("pdf saved:", OUT)
