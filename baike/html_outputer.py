#!/usr/bin/python env
# -*- coding: utf-8 -*-



class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            fout.write("<tr>")
            # fout.write("<td>%s</td>" % data['url'])
            # fout.write("<td>%s</td>" % data['title'])
            # fout.write("<td>%s</td>" % data['summary'])
            fout.write("<td style=\"width:20%%;border:1px solid\">%s</td>" % data['url'])
            fout.write("<td style=\"width:20%%;border:1px solid\">%s</td>" % data['title'])
            # fout.write("<td style=\"width:60%%;border:1px solid\">%s</td>" % data['summary'].replace(u'\xa0', u' '))
            fout.write("<td style=\"width:60%%;border:1px solid\">%s</td>" % data['summary'])
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")