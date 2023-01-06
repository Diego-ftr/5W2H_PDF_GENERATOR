import os
#import py5w2h

from fpdf import FPDF

def generate_pdf(data):
    # Create a new PDF document
    pdf = FPDF()

    # Add a page
    pdf.add_page()

    # Set font and size
    pdf.set_font('Arial', 'B', 16)

    # Insert a logo
    pdf.image('logo.png', x=10, y=8, w=30)

    # Move to the right
    pdf.cell(80)

    # Add title
    pdf.cell(30, 10, 'Mapeo de procesos usando metodlogía 5W2H', 0, 1, 'C')

    # Set font and size
    pdf.set_font('Arial', '', 12)

    # Add header
    pdf.cell(40, 10, 'Proceso:', 0, 0, 'L')
    pdf.cell(50, 10, data['process'], 0, 1, 'L')
    # Add Line
    pdf.cell(40, 10, 'Área:', 0, 0, 'L')
    pdf.cell(50, 10, data['area'], 0, 1, 'L')
    # Add 5W2H data
    #pdf.set_font("Times", size=10)
    line_height = pdf.font_size * 4.5
    col_width = pdf.epw / 7  # distribute content evenly
    datas = (
    ("¿Por Qué?", "¿Qué?", "¿Quién?", "¿Dónde?",'¿Cuándo?','¿Cómo?','¿Cuánto?'),
    (data['why'], data['what'], data['who'], data['where'],data['when'],data['how'],data['how much']),)
 
    count=0
    for row in datas:
        count+=1
        for datum in row:
            if count ==1:
                pdf.set_fill_color(255, 204, 153)
                #pdf.set_font('Times', '', 10)
                pdf.cell(col_width, line_height, str(datum), border=1, align='L', fill=1)
            else:
                line_height = pdf.font_size * 20.5
                pdf.multi_cell(col_width, line_height, datum, border=1,align="L",
                        new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height)
    # Save the PDF
    pdf.output('process_mapping.pdf', 'F')

if __name__ == '__main__':
    data = {
        'process': 'Nombre del Proceso',
        'area': 'Nombre del Área',
        'why': 'Razón de este proceso',
        'what': 'Descripción del Proceso',
        'who': 'Persona responsable por este proceso',
        'where': 'Donde se realiza este proceso',
        'when': 'Cuando se hace el proceso',
        'how': 'Como se hace el proceso',
        'how much': 'Costo del proceso',
    }
    generate_pdf(data)