# -*- coding: utf-8 -*-

import codecs
import markdown
import os
from html.parser import HTMLParser

sub_dir = "sub_/"
tmp_dir = "tmp/"

parser_flag="none"
html_dir =  tmp_dir + "tmp.html" 
link_dir =  tmp_dir + "link.md"

top = codecs.open(tmp_dir + "top.md", "w", "utf-8")

md = markdown.Markdown()

class myparser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        None
    def handle_endtag(self, tag, attrs):
        None
    def handle_data(self, data):
        None





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
        #parser.close()

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
    

