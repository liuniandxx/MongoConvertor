#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
from Attraction import Attraction

import sys
from Brands import Brands

reload(sys)
sys.setdefaultencoding('utf8')


# 这个文件负责整个travel3的导入
def main():
    address_old = '192.168.199.254'
    port_old = 27017

    address_new = '192.168.199.254'
    port_new = 27017

    print('convert latestattractions to attraction.')
    Attraction.convert_attraction(address_old, port_old, address_new, port_new)
    
    #print('convert travel1Brands to travel3Brands.')
    #Brands.convert_Brands(address_old, port_old, address_new, port_new)

    print("OK")


if __name__ == "__main__":
    main()
