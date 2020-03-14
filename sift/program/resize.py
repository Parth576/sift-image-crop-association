import cv2
def resize_image(img,template):
    height_temp, width_temp = template.shape[:2]
    height_img, width_img = img.shape[:2]
    if height_temp > height_img or width_temp > width_img:
        height = 0.5 * height_img
        width = 0.5 * width_img
        dim = (int(width), int(height))
        template = cv2.resize(template, dim, interpolation=cv2.INTER_AREA)
    return template