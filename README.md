# DAT 617 - Enterprise Analytics Strategy Report (MTN Group)

Individual assessment for **DAT 617: Data Management, Visualization and Presentation**
(M.Sc. Data Science). The report positions the author as a Senior Data Analytics
Consultant developing an integrated enterprise analytics, visualization, and AI strategy
for **MTN Group** in the telecommunications sector.

## Deliverables

| File | Description |
|------|-------------|
| `MTN_Enterprise_Analytics_Strategy.pdf` | Final submission (Times New Roman 12pt, 1.5 spacing, justified, numbered pages, APA 7th) |
| `MTN_Enterprise_Analytics_Strategy.docx` | Editable Word version of the same report |
| `figures/` | The three source diagrams (DIKW pyramid, analytical workflow, executive dashboard mock-up) |
| `source/` | Python scripts that generate the figures and render the report |

## Report structure

Cover page, Executive Summary, and eleven sections: Organizational Background;
Business Problem Analysis; DIKW Framework; Enterprise Data Management Strategy;
Enterprise Analytical Workflow; Data Visualization Strategy; AI-Augmented Analytics
Strategy; Prompt Engineering; Ethical and Governance Considerations; Strategic
Recommendations; and Conclusion. Followed by 20 APA 7th references and an appendix.

## Rebuilding

```bash
cd source
python3 diagrams.py       # regenerate the three figures
python3 render_docx.py     # build the .docx
python3 render_pdf.py      # build the .pdf
```

Requires `python-docx`, `matplotlib`, `reportlab`, and `Pillow`.
