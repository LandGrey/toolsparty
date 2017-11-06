#!/usr/bin/env python
# coding:utf-8
# Build by LandGrey 2016-05-04

import os
import sys
import struct


def typelist():
    return{
        # 常见图片格式
        "FFD8FF": "JPEG (jpg | jpeg | jpe)",
        "89504E": "PNG (png)",
        "474946": "GIF (gif)",
        "49492A": "TIFF (tif)",
        "424D": "Win Bitmap (BMP | bmp)",
        # 常见压缩格式
        "504B0304": "ZIP (zip | jar | apk)",
        "52617221": "RAR (rar)",
        "377ABCAF271C": "7Z (7z)",
        "425A68": "Bzip (bz | bz2)",
        "303730373037": "CPIO (tar | cpio)",
        "1F8B": "Gzip File (gz |tar |tgz )",
        # 常见视频与音频格式
        "57415645": "Wave (wav)",
        "4D546864": "MIDI (mid)",
        "41564920": "AVI (avi)",
        "435753": "Flash (swf)",
        "000001BA": "MPEG (mpg)",
        "000001B3": "MPEG (mpg)",
        "6D6F6F76": "Quicktime (mov)",
        "0000001C66747970": "3GPP (3gp)",
        "49443303": "MP3 (mp3)",
        "000000lC667479": "MP4 (mp4)",
        "2E524D46": "RealMedia (rmvb | rm)",
        "3026B2758E66CF11": "Win Media (asf |wmv |wma)",
        # 常见文档格式
        "68746D6C3E": "HTML (html)",
        "3C68746D6C3E": "HTML (htm | html)",
        "3C48544D4C3E": "HTML (htm | html)",
        "3C21444F4354": "HTML (htm | html)",
        "D0CF11E0": "MS Word/Excel (doc | xls)",
        "1234567890FF": "MS word 6.0 (doc)",
        "7FFE340A": "MS word (doc)",
        "25504446": "Adobe Acrobat (pdf)",
        "5F27A889": "JAR (jar)",
        "5374616E64617264204A": "MS Access (mdb)",
        "3C3F786D6C": "XML (xml)",
        "7B5C727466": "Rich Text Format (rtf)",
        "4D5A9000": "Win EXE/DLL (exe | dll)",
        "4C000000011402": "Win Link File (ink)",
        # 其它格式
        "4C01": "Compiled Object (obj)",
        "41433130": "CAD (dwg)",
        "38425053": "Adobe Photoshop (psd)",
        "252150532D41646F6265": "Postscript (eps | ps)",
        "E3828596": "Win Password (pwl)",
        "4D534346": "CAB File (cab)",
        "5245474544495434": "Register table (reg)",
        "00001A00051004": "1-2-3 (123)"
     }


def bytes2hex(bs):
    num = len(bs)
    hexstr = u""
    for i in range(num):
        t = u"%x" % bs[i]
        if len(t) % 2:
            hexstr += u"0"
        hexstr += t
    return hexstr.upper()


def filetype(filename):
    # 以二进制形式读取
    binfile = open(filename, 'rb')
    tl = typelist()
    ftype = "Unknown"
    for FileTypecode in tl.keys():
        # 读字节的长度
        numOfBytes = len(FileTypecode) / 2
        # 定位文件头往后读取
        binfile.seek(0)
        # "B"表示一个字节
        hbytes = struct.unpack_from("B"*numOfBytes, binfile.read(numOfBytes))
        f_type_code = bytes2hex(hbytes)
        if f_type_code == FileTypecode:
            ftype = tl[FileTypecode]
            break
        else:
            ftype = f_type_code[:-2]
    binfile.close()
    return ftype


if __name__ == "__main__":
    try:
        Argv = sys.argv[1]
        FilePath = ""
        if "-h" in Argv:
            print "\n" + r"       Usage:python getFileType.py [options]." + " Build by LandGrey 2016-05-04"
            print r"       Optional arguments: -h, --help            显示帮助 ".decode("utf-8")
            print r"       Target   arguments: [filepath]            判断指定路径文件类型.".decode("utf-8") + "\n"
            print r"       如果判断不出文件类型,则打印出文件头的前三个字节的16进制值".decode("utf-8")
        else:
            pathsplit = str(Argv).split("\\")
            pathlen = len(pathsplit)
            filelen = 0-len(pathsplit[pathlen-1])
            FilePath = os.path.join(Argv[:filelen], pathsplit[pathlen-1])
        if os.path.getsize(FilePath) <= 10:
            print "\n" + "   File contents too little"
            sys.exit()
        name = filetype(FilePath)
        print "The file type is : " + str(name)
    except:
            print "\n" + r"   Please use '-h' or '--help' arguments for help"
            print r'   If file path exists blank key ,please use " " for file path'
