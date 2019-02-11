#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def printLabels():
    print "===== printLabels ====="
    num = 0
    for label in gl_labels:
        num += 1
        print str(num) + " " + str(label)

def printRows():
    print "===== printRows ====="
    num = 0
    for row in gl_rows:
        num += 1
        print str(num) + " " + ', '.join(str(v) for v in row)

def parseData(data, filename, step):
    # 2017년도 도자 라벨
    if step == 1 and filename == "2017_조사광산개요.csv":
        i, j = (0, 0)
        for row in data:
            j = 0
            if i > 0:
                el_name = row[1].replace("도석", "")
                el_grade = row[2].replace("급", "").replace("-", "")
                gl_labels.append(''.join([el_name, el_grade]))
                gl_labels.append(''.join([el_name, el_grade , "정제"]))
            i += 1

    # 2016년도 고령토 라벨
    if step == 2 and filename == "2016_분석성분.csv":
        i, j = (0, 0)
        for row in data:
            j = 0
            if i == 0:
                for col in row:
                    if j > 0:
                        gl_labels.append(col.replace(' ', ''))
                    j += 1
            else:
                break

            i += 1

    # 2017년도 성분분석(정제전, 정제후), 2016년 분석성분 자료
    if step == 3 and (filename == "2017_성분분석_정제전.csv" or filename == "2017_성분분석_정제후.csv" or filename == "2016_분석성분.csv"):
        i, j = (0, 0)

        lo_prefix = 'element'
        lo_labels = []
        lo_name = ''
        for row in data:
            j = 0
            for col in row:
                lo_id = 0

                if i > 0:
                    lo_row = []
                    if j > 0:
                        lo_value = str(col)
                        lo_cond = 'eq'
                        lo_id = gl_labels.index(lo_labels[j]) + 1
                        
                        if lo_value.startswith('<'):
                            lo_cond = 'lt'
                            lo_value = lo_value[1:]
                            
                        if lo_value == '-':
                            lo_value = "0.00"
                            
                        if lo_name == "감열감량":
                            lo_name = "loss"

                        lo_key = lo_prefix + '.' + lo_name.lower()

                        gl_rows.append([lo_prefix, lo_id, lo_labels[j], lo_key, lo_name, lo_cond, lo_value])
                    else:
                        lo_name = col

                else:
                    if j > 0:
                        el_name = col.replace(' ', '').replace(')', '').replace('(', '').replace('급', '').strip()
                    else:
                        el_name = ''
                    lo_labels.append(el_name)

                # up to 1
                j += 1
                
            # up to 1
            i += 1

    # 2016년도 입도, 2017년도 입도
    if step == 4 and (filename == "2017_시료입도_크기.csv" or filename == "2016_시료입도_크기.csv"):
        i, j = (0, 0)

        lo_prefix = 'mean'
        lo_labels = []
        for row in data:
            j = 0
            el_name = ''
            for col in row:
                if i > 0:
                    if j > 0:
                        lo_id = gl_labels.index(el_name) + 1
                        lo_name = lo_labels[j]
                        lo_key = lo_prefix + '.' + lo_name.lower()

                        lo_cond = 'eq'
                        lo_value = str(col)
                        gl_rows.append([lo_prefix, lo_id, lo_labels[j], lo_key, lo_name, lo_cond, lo_value])
                    else:
                        el_name = col.replace(' ', '').replace(')', '').replace('(', '').replace('급', '').strip()
                else:
                    lo_labels.append(col.replace(' ', '').replace('(㎛)', '').strip())

                # up to 1
                j += 1

            # up to 1
            i += 1

    # 2016년 색도, 2017년 색도
    if step == 5 and (filename == "2016_색도_편집본.csv" or filename == "2017_색도_편집본.csv"):
        i, j = (0, 0)

        lo_prefix = 'color'
        lo_labels = []
        lo_name = ''
        for row in data:
            j = 0
            for col in row:
                lo_id = 0

                if i > 0:
                    lo_row = []
                    if j > 0:
                        lo_value = str(col)
                        lo_cond = 'eq'
                        
                        lo_id = gl_labels.index(lo_labels[j]) + 1
                        
                        if lo_value.startswith('<'):
                            lo_cond = 'lt'
                            lo_value = lo_value[1:]
                            
                        if lo_value == '-' or lo_value == '':
                            lo_value = "0.00"

                        lo_key = lo_prefix + '.' + lo_name.lower().replace('*', '')

                        gl_rows.append([lo_prefix, lo_id, lo_labels[j], lo_key, lo_name, lo_cond, lo_value])
                    else:
                        lo_name = col

                else:
                    if j > 0:
                        el_name = col.replace(' ', '').replace(')', '').replace('(', '').replace('급', '').strip()
                    else:
                        el_name = ''
                    lo_labels.append(el_name)

                # up to 1
                j += 1
                
            # up to 1
            i += 1

def parseLine(line):
    return line.replace('\n', '').split(',')

def parseFile(filename, step):
    data = []

    filepath = os.path.join(gl_directory, filename)
    with open(filepath) as fp:  
       line = fp.readline()
       while line:
           data.append(parseLine(line))
           line = fp.readline()

    parseData(data, filename, step)

def do():
    for i in range(1, 10):
        for filename in os.listdir(gl_directory):
            if filename.endswith(".csv"): 
                parseFile(filename, i)

    printLabels()
    printRows()

def set_gl_step(step):
    gl_step = step

def main(args):
    do();
    return 0

if __name__ == '__main__':
    import sys
    import os

    # set directory
    gl_directory = './data'

    # set global_data
    gl_rows = []
    gl_labels = []
    gl_step = 0

    sys.exit(main(sys.argv))
