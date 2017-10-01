# -*- coding: utf-8 -*-

import codecs
import markdown
import os
import glob
from html.parser import HTMLParser



sub_dir = "sub/"
tmp_dir = "tmp/"


top = codecs.open("README.md", "w", "utf-8")
top.write("""
# 医師国家試験のメモ

## What's about?
医師国家試験の勉強にあたり個人的に作成したメモを公開しています。

## それぞれの科目へのリンク
""" + "\r\n")

def toID(src):
    return src.strip("･").strip(",").strip("#").strip("\r\n").strip().lower()

# ディレクトリの中身を全部取得
files = os.listdir(sub_dir)
for file in files:
    # markdownだけ処理
    if ".md" in file:
        print("start: ",file)
        body = codecs.open(tmp_dir + "body.md", "w", "utf-8")
        link = codecs.open(tmp_dir + "link.md", "w", "utf-8")
        src = codecs.open(sub_dir + file,"r","utf-8")

        flag = 0
        page_title = ""
        page_id = ""

        # bodyの処理
        for row in src:
            if row.startswith("####"):
                link.write("        * [" + row.strip("## ").strip("\r\n") + "](#" + toID(row) + ")\r\n")
            elif row.startswith("###"):
                link.write("    * [" + row.strip("## ").strip("\r\n") + "](#" + toID(row) + ")\r\n")
            elif row.startswith("##"):
                flag = 1
                body.write("[一番上へ](#"  + page_id + ")\r\n")
                link.write("* [" + row.strip("## ").strip("\r\n") + "](#" + toID(row) + ")\r\n")
            elif row.startswith("#"):
                page_title = row.strip("# ").strip("\r\n")
                page_id = toID(row)
            if flag == 1 and not row.startswith("[一番上へ]"):
                body.write(row)
        
        body.close()
        link.close()
        src.close()

        tar = codecs.open(sub_dir  + file , "w","utf-8")
        tar.write("[一覧に戻る](../README.md)")
        tar.write("\r\n\r\n")
        tar.write("# " + page_title)
        tar.write("\r\n\r\n")
        rs = codecs.open(tmp_dir + "link.md" , "r","utf-8")
        for r in rs:
            tar.write(r)
        tar.write("\r\n\r\n")
        rs = codecs.open(tmp_dir + "body.md" , "r","utf-8")
        for r in rs:
            tar.write(r)
        
        top.write("* [" + page_title + "](/sub/" + file + ")\r\n")
top.write("""
## よろしければ
活用してください。あとみんなで作りましょうpull request歓迎します。\r\n\r\n""")
top.close()

    

