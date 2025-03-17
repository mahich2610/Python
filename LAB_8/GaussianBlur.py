import cv2

IMAGE_PATH = 'images/variant-2.png'

if __name__ == '__main__':
    image = cv2.imread(IMAGE_PATH)

    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
    blurred_image = cv2.resize(blurred_image ,None,fx=0.5, fy=0.5)
    cv2.imwrite('blurred_image.png', blurred_image)

    cv2.imshow('Blurred Image', blurred_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()