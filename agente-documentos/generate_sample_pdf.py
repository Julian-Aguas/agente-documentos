"""
Script to generate a sample PDF document for testing the Agente Local de Documentos.
Run this once to create sample_document.pdf in the samples/ directory.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from datetime import datetime
import os

def create_sample_pdf():
    """Creates a sample PDF document in Spanish for testing."""
    
    # Create samples directory if it doesn't exist
    samples_dir = os.path.join(os.path.dirname(__file__), '..', 'samples')
    os.makedirs(samples_dir, exist_ok=True)
    
    pdf_path = os.path.join(samples_dir, 'sample_document.pdf')
    
    # Create PDF
    doc = SimpleDocTemplate(pdf_path, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#1f4788'),
        spaceAfter=30,
        alignment=1
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2e5c8a'),
        spaceAfter=12,
        spaceBefore=12
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        alignment=4,
        spaceAfter=12
    )
    
    # Title
    story.append(Paragraph("Propuesta de Implementación: Sistema de Gestión de Documentos", title_style))
    story.append(Spacer(1, 0.3*inch))
    
    # Document info
    info_data = [
        ['Documento:', 'Propuesta Estratégica 2024'],
        ['Fecha:', datetime.now().strftime('%d de %B de %Y')],
        ['Versión:', '1.0 Final'],
        ['Clasificación:', 'Confidencial']
    ]
    info_table = Table(info_data, colWidths=[1.5*inch, 4*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#e8f0f7')),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
    ]))
    story.append(info_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Executive Summary
    story.append(Paragraph("1. Resumen Ejecutivo", heading_style))
    story.append(Paragraph(
        """Este documento presenta una propuesta integral para la implementación de un nuevo sistema 
        de gestión de documentos empresariales. El objetivo principal es centralizar, organizar y 
        facilitar el acceso a todos los documentos críticos de la organización, mejorando la eficiencia 
        operacional en un 35% y reduciendo los tiempos de búsqueda de documentos en un 60%.""",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Objectives
    story.append(Paragraph("2. Objetivos Estratégicos", heading_style))
    
    objectives = [
        "Centralizar la gestión de documentos en una plataforma unificada",
        "Mejorar la seguridad y el control de acceso a documentos sensibles",
        "Automatizar los procesos de archivo y recuperación de documentos",
        "Reducir los costos operacionales asociados con gestión manual de documentos",
        "Cumplir con regulaciones y normativas de gobierno corporativo"
    ]
    
    for i, obj in enumerate(objectives, 1):
        story.append(Paragraph(f"• {obj}", body_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    # Implementation Plan
    story.append(Paragraph("3. Plan de Implementación", heading_style))
    
    impl_data = [
        ['Fase', 'Actividades', 'Duración', 'Equipo'],
        ['Fase 1: Análisis', 'Auditoría de documentos actuales', '2 semanas', 'IT + RH'],
        ['Fase 2: Diseño', 'Diseño de arquitectura del sistema', '3 semanas', 'Consultores'],
        ['Fase 3: Desarrollo', 'Desarrollo e integración', '8 semanas', 'Dev Team'],
        ['Fase 4: Pruebas', 'QA y validación', '4 semanas', 'QA Team'],
        ['Fase 5: Despliegue', 'Capacitación y rollout', '2 semanas', 'Todo el equipo'],
    ]
    
    impl_table = Table(impl_data, colWidths=[1.2*inch, 2.2*inch, 1.2*inch, 1.4*inch])
    impl_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2e5c8a')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f0f0f0')])
    ]))
    story.append(impl_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Key Risks
    story.append(Paragraph("4. Riesgos y Mitigaciones", heading_style))
    
    risks_data = [
        ['Riesgo', 'Probabilidad', 'Impacto', 'Mitigación'],
        ['Resistencia del usuario', 'Alta', 'Alto', 'Programa de capacitación extenso'],
        ['Pérdida de datos', 'Media', 'Crítica', 'Backups redundantes y recuperación disaster'],
        ['Retrasos en implementación', 'Media', 'Medio', 'Planificación detallada y buffer temporal'],
        ['Presupuesto insuficiente', 'Baja', 'Medio', 'Fases incrementales y revisión cuatrimestral'],
    ]
    
    risks_table = Table(risks_data, colWidths=[1.5*inch, 1.2*inch, 1.2*inch, 1.6*inch])
    risks_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#c1440e')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#ffe6d5')])
    ]))
    story.append(risks_table)
    story.append(Spacer(1, 0.3*inch))
    
    # Budget
    story.append(Paragraph("5. Presupuesto Estimado", heading_style))
    story.append(Paragraph(
        """El presupuesto total estimado para la implementación es de $250,000 USD, 
        distribuido de la siguiente manera: Licencias de software (40%), Servicios de integración (35%), 
        Capacitación del personal (15%), Contingencia (10%).""",
        body_style
    ))
    story.append(Spacer(1, 0.2*inch))
    
    # Timeline
    story.append(Paragraph("6. Cronograma", heading_style))
    story.append(Paragraph(
        """La implementación completa se ejecutará en un período de 19 semanas, 
        con entregas parciales cada dos semanas para validación. El sistema estará disponible 
        completamente para toda la organización en Q3 2024.""",
        body_style
    ))
    story.append(Spacer(1, 0.3*inch))
    
    # Conclusion
    story.append(Paragraph("7. Conclusión", heading_style))
    story.append(Paragraph(
        """Cette implémentation stratégique du système de gestion de documents représente 
        un investissement critique pour l'avenir opérationnel de l'organisation. Avec une planification 
        appropriée, une gestion des risques rigoureuse et l'implication des parties prenantes, 
        le projet peut être réalisé avec succès et fournir un retour sur investissement 
        mesurable dans les 18 mois suivant le déploiement. Nous recommandons vivement 
        l'approbation de cette proposition.""",
        body_style
    ))
    
    # Build PDF
    doc.build(story)
    print(f"✅ PDF de prueba creado: {pdf_path}")
    return pdf_path

if __name__ == "__main__":
    create_sample_pdf()
