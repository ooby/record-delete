
# -*- coding: utf-8 -*-
import os
import sys
import xml.etree.ElementTree as et


def get_id(polis, filename):
    """Возвращает ID из случая и удаляет случаи соответствующие списку полисов"""
    result = []
    root = filename.getroot()
    for zap in root.findall('ZAP'):
        if int(zap.find('PACIENT/NPOLIS').text) == int(polis):
            result.append(zap.find('PACIENT/ID_PAC').text)
            root.remove(zap)
    return result


def get_pers(idx, filename):
    """Находит и удаляет персональные данные с соответствующим ID"""
    tempf1 = None
    tempf2 = None
    root = filename.getroot()
    for pers in root.findall('PERS'):
        if pers.find('ID_PAC').text == idx:
            root.remove(pers)
    tempf1 = root.find('ZGLV/FILENAME1').text
    tempf2 = root.find('ZGLV/FILENAME').text
    return [tempf1, tempf2]


def main():
    """Main"""
    file1 = et.parse(sys.argv[1])
    file2 = et.parse(sys.argv[2])
    print 'Количество случаев до обработки:', len(file1.getroot().findall('ZAP'))
    print 'Количество персональных данных до обработки:', len(file2.getroot().findall('PERS'))
    files = []
    ids = []
    with open(sys.argv[3], 'r') as plist:
        for polis in plist:
            ids.extend(get_id(polis, file1))
    print 'Найдено соответсвующих полисов:', len(ids)
    for idx in ids:
        files.extend(get_pers(idx, file2))
    if not os.path.exists(os.path.join(os.getcwd(), 'out')):
        os.mkdir('out')
    os.chdir('out')
    print 'Количество случаев после обработки:', len(file1.getroot().findall('ZAP'))
    print 'Количество персональных данных после обработки:', len(file2.getroot().findall('PERS'))
    file1.write(files[0] + '.xml', encoding='cp1251')
    file2.write(files[1] + '.xml', encoding='cp1251')


if __name__ == "__main__":
    main()
