# -*- coding: utf-8 -*- 

import codecs

src="hematopoietic.md"

f = codecs.open('sub/' + src, 'r','utf-8')
head = codecs.open("tmp/tmp_top.md","w","utf-8")
link = codecs.open("tmp/tmp_link.md","w","utf-8")
body = codecs.open("tmp/tmp_body.md","w","utf-8")
title = ""

for row in f:
    head.writelines(row)
    if row.startswith("#"):
        title = row.strip("# ").strip("\r\n")
        break

for row in f:
    if row.startswith("##"):
        link.writelines("\r\n")
        tmp = row.strip("# ").strip("\r\n")
        link.write("* [" + tmp + "](#" + tmp + ")")
        link.writelines("\r\n")
        body.write("[一番上へ]" + "(#"+ title +")" )
        body.writelines("\r\n")
        body.write(row)
        break


for row in f:
    if row.startswith("##"):
        if row.startswith("####"):
            pass
        elif row.startswith("###"):
            tmp = row.strip("# ").strip("\r\n")
            link.write("    * [" + tmp + "](#" + tmp + ")")
            link.writelines("\r\n")
        else:
            body.write("[一番上へ]" + "(#"+ title +")" )
            body.writelines("\r\n")
            tmp = row.strip("# ").strip("\r\n")
            link.write("* [" + tmp + "](#" + tmp + ")")
            link.writelines("\r\n")
    if row.startswith("[一番上へ]"):
        pass
    else:
        body.write(row)


f.close()
head.close()
link.close()
body.close()

f = codecs.open('sub/' + src, 'w','utf-8')
head = codecs.open("tmp/tmp_top.md","r","utf-8")
link = codecs.open("tmp/tmp_link.md","r","utf-8")
body = codecs.open("tmp/tmp_body.md","r","utf-8")

for tar in head:
    f.write(tar)


for  tar in link:
    f.write(tar)

f.write("\r\n")

for tar in body:
    f.write(tar)

f.close()
head.close()
link.close()
body.close()