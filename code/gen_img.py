from captcha.image import ImageCaptcha
import random

data_path = 'D:\\ml\\work2\\code\\train\\'


def get_code():
    # chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    chars = '1234567890'
    code = ''
    for index in range(4):
        code += chars[random.randint(0, len(chars) - 1)]
    return code


for x in range(5000):
    # captcha_text = get_code()
    captcha_text = "%.4d" % x
    image = ImageCaptcha(fonts=['fonts/FZSSJW.TTF'])
    image.write(captcha_text, data_path + 'src\\' + captcha_text + '.png')
    with open(data_path + "label.txt", "a") as f:  # 写入标签
        f.write(captcha_text)
        f.writelines("\n")
    pass
