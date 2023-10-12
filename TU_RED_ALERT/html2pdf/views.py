from django.shortcuts import render
from django.template import Template, Context
from django.http import HttpResponse

import os
import pdfkit
from datetime import datetime, timedelta

def html2pdf(request):
    thai_time_now = datetime.now() + timedelta(hours=7)
    thai_month = ['มกราคม', 'กุมภาพันธ์', 'มีนาคม', 'เมษายน', 'พฤษภาคม', 'มิถุนายน', 'กรกฎาคม', 'สิงหาคม', 'กันยายน', 'ตุลาคม', 'พฤศจิกายน', 'ธันวาคม']

    context = {
        'place': 'องค์การนักศึกษามหาวิทยาลัยธรรมศาสตร์',
        'day': thai_time_now.day,
        'month': thai_month[thai_time_now.month-1],
        'year': thai_time_now.year + 543,
        'title': 'เทวทูตปรากฎตัวแล้ว',
        'to': 'NERV สาขาธรรมศาสตร์',
        'complainants': [
            {
                'name': 'ภูรี เพ็ญหิรัญ',
                'role': 'นักศึกษาชั้นปีที่ 2',
                'department': 'คณะวิศวกรรมศาสตร์',
                'campus': 'รังสิต',
                'email': 'heart@gmail.com',
                'signature': 'ภูรี',
            },
            {
                'name': 'โจเซฟ โจสตาร์',
                'role': 'อาจารย์',
                'department': 'คณะวิศวกรรมศาสตร์',
                'campus': 'รังสิต',
                'email': 'dr.jostar@gmail.com',
                'signature': 'โจเซฟ',
            },
        ],
        'complain_to': 'NERV สาขาธรรมศาสตร์',
        'because': 'เทวทูตขโมยหัวใจ',
        'want_to': 'เอาหัวใจกลับมา',
        'attachments': [
            {
                'name': 'ภาพแมว'
            },
        ]
    }

    options = {
        'page-size':'A4',
        'encoding': 'UTF-8',
    }

    this_dir = os.path.dirname(__file__)
    template_path = os.path.join(this_dir, 'assets/report_template.html')

    with open(template_path, 'r') as f:
        template = Template(f.read())

    html = template.render(Context(context))
    # output_path = os.path.join(this_dir, 'outputs/report.pdf')
    # pdf = pdfkit.from_string(html, output_path, options=options)
    css_path = os.path.join(this_dir, 'assets/report_style.css')
    pdf = pdfkit.from_string(html, False, options=options, css=css_path)
    
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report"'

    return response
