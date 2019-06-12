#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def parseData(data, filename):
    cspt_data = []
    cspt_struct = []

    # 2016_분석방법
    if(filename == "2016_분석방법.csv"):
        cspt_struct = [
            'Name(),',
            'Analysis(',
            '    (',
            '        Method,',
            '        Element(',
            '            SiO2(Condition, Value),',
            '            Al2O3(Condition, Value),',
            '            Fe2O3(Condition, Value),',
            '            TiO2(Condition, Value),',
            '            CaO(Condition, Value),',
            '            Na2O(Condition, Value),',
            '            K2O(Condition, Value),',
            '            Loss(Condition, Value)',
            '        )',
            '    )',
            ')',
        ]

        # make data
        _i = 0
        _data = []
        _row = []
        for row in data:
            if _i > 0:
                if len(_row) > 0 and row[0] != _row[0]:
                    if(_i > 1):
                        _data.append(')')
                        _data.append(')')
                        _data.append('<=(' + '\n'.join(cspt_struct) + ')')

                    cspt_data.append('\n'.join(_data))
                    _data = []

                    _data.append('(')
                    _data.append('(\'' + row[0] + '\'), (')

                _data.append('(\'' + row[1] + '\', (')

                _k = 0
                _d = row[2:]
                for _item in _d:
                    if _item[:1] == '<':
                        _data.append('(\'<\', ' + _item[1:] + '),')
                    else:
                        _data.append('(\'=\', ' + _item.replace('-', '0.0') + '),')

                    _k = _k + 1

                _data.append(')),')

            _i = _i + 1
            _row = row

        # finish
        if len(_row) > 0:
            _data.append('    )')
            _data.append(')')
            _data.append('<=(' + '\n'.join(cspt_struct) + ')')
            cspt_data.append('\n'.join(_data))
            _data = []
        
        for line in cspt_data:
            if len(line) > 0:
                data_all.append('cspt' + line.replace(' ', '').replace('\n', '').replace('-,', '0.0,').replace(',)', ')'))
    
    # 2016_분석성분, 2017_성분분석_정제전, 2017_성분분석_정제후, 2018_성분분석, 2018_장석_성분_별첨
    if filename == "2016_분석성분.csv" or filename == "2017_성분분석_정제전.csv" or filename == "2017_성분분석_정제후.csv" or filename == "2018_성분분석.csv" or filename == "2018_장석_성분_별첨.csv":
        cspt_struct = [
            'Name(),',
            'Element(',
            '   SiO2(Condition, Value),',
            '   Al2O3(Condition, Value),',
            '   Fe2O3(Condition, Value),',
            '   CaO(Condition, Value),',
            '   MgO(Condition, Value),',
            '   Na2O(Condition, Value),',
            '   TiO2(Condition, Value),',
            '   MnO(Condition, Value),',
            '   P2O5(Condition, Value),',
            '   ZrO2(Condition, Value),',
            '   Li2O(Condition, Value),',
            '   SrO(Condition, Value),',
            '   ZnO(Condition, Value),',
            '   Cr2O3(Condition, Value),',
            '   BaO(Condition, Value),',
            '   Loss(Condition, Value)',
            ')'
        ]
        
        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0

            if _k > 0:
                _data.append('(')
                
                for row in data:
                    if _i > 0:
                        _item = row[_k]
                        if _item[:1] == '<':
                            _data.append('(\'<\', ' + _item[1:] + '),')
                        else:
                            _data.append('(\'=\', ' + _item.replace('-', '0.0') + '),')
                    else:
                        _data.append('(\'' + row[_k] + '\'),(')
                    _i = _i + 1
                
                _data.append('))')
                
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))

            _k = _k + 1
            _data = []
            
    # 2016_입도, 2017_입도, 2018_입도
    if filename == "2016_입도.csv" or filename == "2017_입도.csv" or filename == "2018_입도.csv":
        cspt_struct = [
            'Name(),',
            'GrainSize(',
            '    MeanSize(Condition, Value),',
            '    D10(Condition, Value),',
            '    D50(Condition, Value),',
            '    D90(Condition, Value)',
            ')'
        ]
        
        # make data
        _i = 0
        _data = []
        _row = []
        for row in data:
            if _i > 0:
                if len(_row) > 0 and row[0] != _row[0]:
                    if(_i > 1):
                        _data.append(')')
                        _data.append(')')
                        _data.append('<=(' + '\n'.join(cspt_struct) + ')')

                    cspt_data.append('\n'.join(_data))
                    _data = []

                    _data.append('(')
                    _data.append('(\'' + row[0] + '\'), (')

                _data.append('(\'' + row[1] + '\', (')

                _k = 0
                _d = row[2:]
                for _item in _d:
                    if _item[:1] == '<':
                        _data.append('(\'<\', ' + _item[1:] + '),')
                    else:
                        _data.append('(\'=\', ' + _item.replace('-', '0.0') + '),')

                    _k = _k + 1

                _data.append(')),')

            _i = _i + 1
            _row = row

        # finish
        if len(_row) > 0:
            _data.append('    )')
            _data.append(')')
            _data.append('<=(' + '\n'.join(cspt_struct) + ')')
            cspt_data.append('\n'.join(_data))
            _data = []
        
        for line in cspt_data:
            if len(line) > 0:
                data_all.append('cspt' + line.replace(' ', '').replace('\n', '').replace('-,', '0.0,').replace(',)', ')'))

    # 2017_조성_주입
    if filename == "2017_조성_주입.csv":
        cspt_struct = [
            'Name(),'
            'Composition(',
            '    Slipcasting(',
            '        Stone(Condition, Value),',
            '        Kaolin(Condition, Value),',
            '        H2O(Condidion, Value),',
            '        CMC(Condition, Value),',
            '        PVA(Condition, Value),',
            '        CF44(Condition, Value)',
            '    )',
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0

            if _k > 0:
                _data.append('((')
                
                for row in data:
                    if _i > 0:
                        _item = row[_k]
                        if _item[:1] == '<':
                            _data.append('(\'<\', ' + _item[1:] + '),')
                        else:
                            _data.append('(\'=\', ' + _item.replace('-', '0.0') + '),')
                    else:
                        _data.append('(\'' + row[_k] + '\'),(')
                    _i = _i + 1
                
                _data.append(')))')
                
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))

            _k = _k + 1
            _data = []
            
    # 2017_조성_소지
    if filename == "2017_조성_소지.csv":
        cspt_struct = [
            'Name(),'
            'Composition(',
            '    Bodycasting(',
            '        Stone(Condition, Value),',
            '        Kaolin(Condition, Value),',
            '        H2O(Condidion, Value),',
            '        CMC(Condition, Value),',
            '        PVA(Condition, Value),',
            '        CF44(Condition, Value)',
            '    )',
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0

            if _k > 0:
                _data.append('((')
                
                for row in data:
                    if _i > 0:
                        _item = row[_k]
                        if _item[:1] == '<':
                            _data.append('(\'<\', ' + _item[1:] + '),')
                        else:
                            _data.append('(\'=\', ' + _item.replace('-', '0.0') + '),')
                    else:
                        _data.append('(\'' + row[_k] + '\'),(')
                    _i = _i + 1
                
                _data.append(')))')
                
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))

            _k = _k + 1
            _data = []

    # 2016_함유량, 2018_장석_함유량_별첨
    if filename == "2016_함유량.csv" or filename == "2018_장석_함유량_별첨.csv":
        cspt_struct = [
            'Name(),',
            'Content(',
            '    Quartz(Condition, Value, ~Subsequent),',
            '    Kaolinite(Condition, Value, ~Subsequent),',
            '    Muscovite(Condition, Value, ~Subsequent),',
            '    Andesine(Condition, Value, ~Subsequent),',
            '    Gibbsite(Condition, Value, ~Subsequent)',
            '    Rutile(Condition, Value, ~Subsequent),',
            '    Halloysite(Condition, Value, ~Subsequent),',
            '    Rp(Condition, Value, ~Subsequent),',
            '    Rwp(Condition, Value, ~Subsequent),',
            '    Rexp(Condition, Value, ~Subsequent),',
            '    X2(Condition, Value, ~Subsequent)',
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0

            if _k > 0:
                _data.append('(')
                
                for row in data:
                    if _i > 0:
                        _item = row[_k]
                        if _item[:1] == '<':
                            _data.append('(\'<\', ' + _item[1:] + '),')
                        else:
                            _data.append('(\'=\', ' + _item.replace('-', '0.0') + '),')
                    else:
                        _data.append('(\'' + row[_k] + '\'),(')
                    _i = _i + 1
                
                _data.append('))')
                
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))

            _k = _k + 1
            _data = []
    
    # 2016_조사광산, 2017_조사광산, 2018_조사광산, 2018 조사소지
    if filename == "2016_조사광산.csv" or filename == "2017_조사광산.csv" or filename == "2018_조사광산.csv" or filename == "2018_조사소지.csv":
        cspt_struct = [
            'Name(),'
            'Tag()'
        ]

        # make data
        _i = 0
        for row in data:
            if _i > 0:
                words = ' '.join(row[2:]).replace('(', ' ').replace(')', ' ').split(' ')
                words = [x for x in words if x != []]
                data_all.append('cspt' + ('((\'' + row[1] + '\'),(\'' + '\',\''.join(words) + '\'))<=(' + ''.join(cspt_struct) + ')').replace(' ', ''))
            _i = _i + 1

    # 2016_흡축_고령토_소지_산화, 2016_흡축_도석_소지_산화, 2018_흡축_점토_산화 (소지로 추정함)
    if filename == "2016_흡축_고령토_소지_산화.csv" or filename == "2017_흡축_도석_소지_산화.csv" or filename == "2018_흡축_점토_산화.csv":
        cspt_struct = [
            'Name(),',
            'Absorption(',
            '    Oxidation(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]
        
        cspt_struct2 = [
            'Name(),',
            'Contraction(',
            '    Oxidation(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]

        # make data
        _i = 0
        for row in data:
            if _i > 0:
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[3] + ', \'body\')))<=(' + ''.join(cspt_struct) + ')').replace(' ', ''))
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[4] + ', \'body\')))<=(' + ''.join(cspt_struct2) + ')').replace(' ', ''))
            _i = _i + 1

    # 2017_흡축_도석_소지_환원, 2018_흡축_점토_환원 (소지로 추정함)
    if filename == "2017_흡축_도석_소지_환원.csv" or filename == "2018_흡축_점토_환원.csv":
        cspt_struct = [
            'Name(),',
            'Absorption(',
            '    Reduction(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]
        
        cspt_struct2 = [
            'Name(),',
            'Contraction(',
            '    Reduction(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]

        # make data
        _i = 0
        for row in data:
            if _i > 0:
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[3] + ', \'body\')))<=(' + ''.join(cspt_struct) + ')').replace(' ', ''))
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[4] + ', \'body\')))<=(' + ''.join(cspt_struct2) + ')').replace(' ', ''))
            _i = _i + 1
            
    # 2017_흡축_도석_주입_산화
    if filename == "2017_흡축_도석_주입_산화.csv":
        cspt_struct = [
            'Name(),',
            'Absorption(',
            '    Oxidation(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]
        
        cspt_struct2 = [
            'Name(),',
            'Contraction(',
            '    Oxidation(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]

        # make data
        _i = 0
        for row in data:
            if _i > 0:
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[3] + ', \'slip\')))<=(' + ''.join(cspt_struct) + ')').replace(' ', ''))
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[4] + ', \'slip\')))<=(' + ''.join(cspt_struct2) + ')').replace(' ', ''))
            _i = _i + 1
            
    # 2017_흡축_도석_주입_환원
    if filename == "2017_흡축_도석_주입_환원.csv":
        cspt_struct = [
            'Name(),',
            'Absorption(',
            '    Reduction(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]
        
        cspt_struct2 = [
            'Name(),',
            'Contraction(',
            '    Reduction(',
            '        (Temperture, Value, ~Casting)',
            '    )',
            ')',
        ]

        # make data
        _i = 0
        for row in data:
            if _i > 0:
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[3] + ', \'slip\')))<=(' + ''.join(cspt_struct) + ')').replace(' ', ''))
                data_all.append('cspt' + ('((\'' + '\',\''.join(row[2].split(' ')) + '\'), (((' + row[0] + ', ' + row[4] + ', \'slip\')))<=(' + ''.join(cspt_struct2) + ')').replace(' ', ''))
            _i = _i + 1

    # 2016_색도_산화_1200, 2018_색도_산화_1200
    if filename == "2016_색도_산화_1200.csv" or filename == "2018_색도_산화_1200.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Oxidation(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1200, (')

                    _i = _i + 1
                    
                _data.append(')))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []
            
    # 2016_색도_산화_1250, 2018_색도_산화_1250
    if filename == "2016_색도_산화_1250.csv" or filename == "2018_색도_산화_1250.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Oxidation(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1250, (')

                    _i = _i + 1
                    
                _data.append(')))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []
            
    # 2016_색도_환원_1200, 2018_색도_환원_1200
    if filename == "2016_색도_환원_1200.csv" or filename == "2018_색도_환원_1200.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Reduction(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1250, (')

                    _i = _i + 1
                    
                _data.append(')))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # 2016_색도_환원_1250, 2018_색도_환원_1250
    if filename == "2016_색도_환원_1250.csv" or filename == "2018_색도_환원_1250.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Reduction(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1250, (')

                    _i = _i + 1
                    
                _data.append(')))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []
            
    # 2017_색도_산처리전
    if filename == "2017_색도_산처리전.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Acid(',
            '        Before(',
            '            Cie(L, a, b)',
            '        )',
            '        ~Casting',
            '    )',
            ')'
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((((')

                    _i = _i + 1
                    
                _data.append(')))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []
            
    # 2017_색도_산처리후
    if filename == "2017_색도_산처리후.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Acid(',
            '        After(',
            '            Cie(L, a, b)',
            '        )',
            '        ~Casting',
            '    )',
            ')'
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((((')

                    _i = _i + 1
                    
                _data.append(')))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # 2017_색도_산화_소지_1200
    if filename == "2017_색도_산화_소지_1200.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Oxidation(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1200, (')

                    _i = _i + 1
                    
                _data.append('), \'body\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # 2017_색도_산화_소지_1250
    if filename == "2017_색도_산화_소지_1250.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Oxidation(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1250, (')

                    _i = _i + 1
                    
                _data.append('), \'body\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # 2017_색도_산화_주입_1200
    if filename == "2017_색도_산화_주입_1200.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Oxidation(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1200, (')

                    _i = _i + 1
                    
                _data.append('), \'slip\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # 2017_색도_산화_주입_1250
    if filename == "2017_색도_산화_주입_1250.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Oxidation(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1250, (')

                    _i = _i + 1
                    
                _data.append('), \'slip\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # 2017_색도_환원_소지_1200
    if filename == "2017_색도_환원_소지_1200.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Reduction(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1200, (')

                    _i = _i + 1
                    
                _data.append('), \'body\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # 2017_색도_환원_소지_1250
    if filename == "2017_색도_환원_소지_1250.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Reduction(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1250, (')

                    _i = _i + 1
                    
                _data.append('), \'body\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []
            
    # 2017_색도_환원_주입_1200
    if filename == "2017_색도_환원_주입_1200.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Reduction(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1200, (')

                    _i = _i + 1
                    
                _data.append('), \'slip\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []
            
    # 2017_색도_환원_주입_1250
    if filename == "2017_색도_환원_주입_1250.csv":
        cspt_struct = [
            'Name(),',
            'Color(',
            '    Reduction(',
            '        (Temperture, Cie(L, a, b), ~Casting)',
            '    )'
            ')',
        ]

        # make data
        _i = 0
        _k = 0
        _data = []
        _row = []
        _mk = len(data[0])
        while _k < _mk:
            _i = 0
            if _k > 0:
                for row in data:
                    if _i > 0:
                        _data.append(row[_k] + ',')
                    else:
                        _data.append('((\'' + row[_k] + '\'),((')
                        _data.append('(1250, (')

                    _i = _i + 1
                    
                _data.append('), \'slip\'))))');
                data_all.append('cspt' + (''.join(_data) + '<=(' + ''.join(cspt_struct) + ')').replace(' ', '').replace(',)', ')'))
            
            _k = _k + 1
            _data = []

    # view infomation
    print("> Target File: " + str(filename))
    print("> Structure:")
    print("\n".join(cspt_struct))
    print("> Data:")
    #print("\n".join(cspt_data))
    
    return cspt_data

def parseLine(line):
    return line.replace('\n', '').split(',')

def parse(filename):
    lines = []

    filepath = os.path.join(data_dir, filename)
    with open(filepath) as fp:
       line = fp.readline()
       while line:
           lines.append(parseLine(line))
           line = fp.readline()

    parseData(lines, filename)

def do():
    for filename in os.listdir(data_dir):
        if filename.endswith('.csv'):
            parse(filename)

def main(args):
    do();
    
    print '\n'.join(data_all)
    
    return 0

if __name__ == '__main__':
    import sys
    import os

    # set directory
    data_dir = './data'

    # data
    data_all = []

    sys.exit(main(sys.argv))

