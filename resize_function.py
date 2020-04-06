import cv2

def resize(img):
    h, w, c = img.shape
    ratio = h / w
    new_width = 1000

    resized = cv2.resize(img, (new_width, int(new_width * ratio)))
    return resized

if __name__ == '__main__':
    img = cv2.imread('image/tom.jpg')
    resize(img)



