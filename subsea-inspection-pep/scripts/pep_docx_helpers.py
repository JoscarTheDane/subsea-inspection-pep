#!/usr/bin/env python3
"""
Reusable python-docx helpers for generating PEP .docx files.
Copy to your working directory, import, or adapt.

Usage:
    from pep_docx_helpers import (
        add_restricted_header, add_blue_heading,
        add_shaded_table_header, add_table_row,
        init_pep_document
    )

    doc = init_pep_document()
    add_restricted_header(doc)
    add_blue_heading(doc, "1  Introduction", 1)
    ...
    doc.save("output.docx")
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml


def init_pep_document():
    """Create a new Document with subsea PEP standard page setup."""
    doc = Document()
    for section in doc.sections:
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(2.5)
        section.right_margin = Cm(2.5)
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    font.size = Pt(10.5)
    style.paragraph_format.space_after = Pt(4)
    style.paragraph_format.line_spacing = 1.15
    return doc


def add_restricted_header(doc):
    """Add Restricted banner + ECCN copyright notice."""
    if doc.paragraphs:
        p = doc.paragraphs[0]
    else:
        p = doc.add_paragraph()
    run = p.add_run("Restricted")
    run.bold = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0xCC, 0x00, 0x00)
    p2 = doc.add_paragraph()
    run2 = p2.add_run(
        "ECCN:  EAR 99 Deminimus\n"
        "This document is made available subject to the condition that the recipient will neither use "
        "nor disclose the contents except as agreed in writing with the copyright owner. "
        "Copyright is vested in [Company Name].© All rights reserved.\n"
        "Neither the whole nor any part of this document may be reproduced or distributed in any form "
        "or by any means (electronic, mechanical, reprographic, recording or otherwise) without the "
        "prior written consent of the copyright owner."
    )
    run2.font.size = Pt(7.5)
    run2.font.color.rgb = RGBColor(0x66, 0x66, 0x66)
    doc.add_paragraph()


def add_blue_heading(doc, text, level=1):
    """Add a heading with dark blue styling matching example PEPs."""
    h = doc.add_heading(text, level=level)
    for run in h.runs:
        run.font.color.rgb = RGBColor(0x00, 0x33, 0x66)
    return h


def set_cell_shading(cell, color):
    """Apply background shading to a table cell."""
    shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
    cell._tc.get_or_add_tcPr().append(shading)


def add_styled_header_row(table, headers):
    """Add a dark blue header row to a table."""
    row = table.rows[0] if table.rows else table.add_row()
    for cell in row.cells:
        cell.text = ''
    for i, header in enumerate(headers):
        if i >= len(row.cells):
            break
        cell = row.cells[i]
        p = cell.paragraphs[0]
        run = p.add_run(header)
        run.bold = True
        run.font.size = Pt(9)
        run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
        set_cell_shading(cell, "003366")


def add_table_row(table, cells_data, bold=False):
    """Add a formatted data row to a table (9pt font)."""
    row = table.add_row()
    for i, text in enumerate(cells_data):
        if i >= len(row.cells):
            break
        cell = row.cells[i]
        cell.text = ''
        p = cell.paragraphs[0]
        run = p.add_run(str(text))
        run.font.size = Pt(9)
        run.bold = bold
    return row


def add_styled_table(doc, headers, data):
    """Convenience: create table with styled header + data rows."""
    table = doc.add_table(rows=1, cols=len(headers))
    table.style = 'Table Grid'
    add_styled_header_row(table, headers)
    for row_data in data:
        add_table_row(table, row_data)
    doc.add_paragraph()
    return table


def add_bullet(doc, text, level=0):
    """Add a bullet list item."""
    p = doc.add_paragraph(text, style='List Bullet')
    p.paragraph_format.left_indent = Cm(1.27 + level * 0.63)
    return p


def add_numbered(doc, text):
    """Add a numbered list item."""
    return doc.add_paragraph(text, style='List Number')


def add_title_page(doc, title, subtitle, client, info_rows):
    """Add a centered title page with info table.
    
    info_rows: list of (label, value) tuples
    """
    for _ in range(4):
        doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.bold = True
    run.font.size = Pt(22)
    run.font.color.rgb = RGBColor(0x00, 0x33, 0x66)
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(subtitle)
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    doc.add_paragraph()
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(client)
    run.bold = True
    run.font.size = Pt(14)
    doc.add_paragraph()
    doc.add_paragraph()
    table = doc.add_table(rows=len(info_rows), cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, (label, val) in enumerate(info_rows):
        c0 = table.rows[i].cells[0]
        c0.text = ''
        r = c0.paragraphs[0].add_run(label)
        r.bold = True
        r.font.size = Pt(10)
        set_cell_shading(c0, "E8F0FE")
        c1 = table.rows[i].cells[1]
        c1.text = ''
        c1.paragraphs[0].add_run(val).font.size = Pt(10)
    doc.add_page_break()


def add_revision_history(doc):
    """Add a revision history table."""
    add_blue_heading(doc, "Revision History", 1)
    table = doc.add_table(rows=1, cols=4)
    table.style = 'Table Grid'
    add_styled_header_row(table, ["Rev", "Date", "Author", "Description of Change"])
    add_table_row(table, ["P01", "[Date]", "[Author]", "Initial Issue for Tender Review"])
    doc.add_paragraph()
