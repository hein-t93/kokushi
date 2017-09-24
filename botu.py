# -*- coding: utf-8 -*-

import codecs
import markdown
import os
from html.parser import HTMLParser

sub_dir = "sub_/"
tmp_dir = "tmp/"


top = codecs.open(tmp_dir + "top.md", "w", "utf-8")


extensions = ['extra', 'admonition', 'codehilite(css_class=highlight)',
              'nl2br', 'sane_lists', 'toc', 'del_ins']

md = markdown.Markdown(extensions)


html_dir =  tmp_dir + "tmp.html" 
link_dir =  tmp_dir + "link.md"
link_row = []
page_id = ""
page_title = ""

class myparser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._flag = ""
        self._id = ""
    def handle_starttag(self, tagname, attribute):
        self._flag = tagname 
        for attr in attribute:
            print(attr)
            if attr[0].lower() == "id":
                self._id = attr[1]
                if tagname == "h1":
                    page_id = self._id
    def handle_endtag(self, tag):
        self._flag = ""
        self._id = "" 
    def handle_data(self, data):
        if self._flag == "h1":
            page_title = data
        elif self._flag == "h2":
            link_row.append("*[" + data + "](#" + self._id + ")\r\n")
        elif self._flag == "h3":
            link_row.append("   *[" + data + "](#" + self._id + ")\r\n")
        

# ディレクトリの中身を全部取得
files = os.listdir(sub_dir)
for file in files:
    # markdownだけ処理
    if ".md" in file:
        head = codecs.open(tmp_dir + "head.md", "w", "utf-8")
        body = codecs.open(tmp_dir + "tmp.md", "w", "utf-8")
        src = codecs.open(sub_dir + file,"r","utf-8")

        # htmlに変換して保存
        tmp_html = codecs.open(tmp_dir + "tmp.html","w","utf-8")
        tmp_html.write(md.convert(src.read()))
        tmp_html.close()

        #パーサーしてlink.mdに保管
        tmp_html = codecs.open(tmp_dir + "tmp.html","r","utf-8")
        parser = myparser()
        parser.feed(tmp_html.read())
        parser.close()

        for row in link_row:
            print(row)
        
        # bodyの処理
        for row in src:
            if row.startswith("##"):
                flag = 1
                if row.startswith("###"):
                    None
                else:
                    body.write("[一番上へ](#" + parser.h1 + ")\r\n")
            if row.startswith("[一番上へ]"):
                None
            else:
                body.write(row)
    

