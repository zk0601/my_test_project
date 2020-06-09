#!/usr/bin/env python
# encoding: utf-8


# python2
def str_to_zhongwen(var):
    print "str_to_zhongwen : ",var

    not_end = True
    while not_end:
        start1 = var.find("\\x")
        if start1>-1:
            str1=var[start1+2:start1+4]

            start2 = var[start1+4:].find("\\x")+start1+4
            if start2>-1:
                str2=var[start2+2:start2+4]

                start3 = var[start2+4:].find("\\x")+start2+4
                if start3>-1:
                    str3=var[start3+2:start3+4]
        else:
            not_end = False
        if start1>-1 and start2>-1 and start3>-1:
            str_all=str1+str2+str3
            str_all = str_all.decode('hex')

            str_re = var[start1:start3+4]
            # print str_all, "   " ,str_re
            var = var.replace(str_re,str_all)
    # print var.decode('utf-8')
    return var

a = '方方圈子'
# b = a.decode('unicode-escape')
# b = 'æ¹æ¹åå­'.decode('utf-8')
b = a.decode('utf-8')
c = b.encode('unicode-escape')
# print a
# print b
# print c
# print d
# print c.decode('utf-8')
print str_to_zhongwen(c)



