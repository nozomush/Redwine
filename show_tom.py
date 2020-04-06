# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:16:07 2020

@author: snozo
"""

import cv2

path = 'image/tom.jpg'

def main():
    img = cv2.imread(path)
    cv2.imshow('tom',img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()