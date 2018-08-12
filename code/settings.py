INSTALLED_APPS = [  # 添加应用
    # 其他应用...
    'captcha',
]

CAPTCHA_IMAGE_SIZE = (100, 30)  # 设置生成验证码图片的长和宽，单位为像素

CAPTCHA_OUTPUT_FORMAT = u'%(text_field)s %(image)s %(hidden_field)s'  # 设置输出的格式，该插件自动在模板中生成3个元素：一个验证码图片，一个验证码输入框、一个用于存放秘钥的隐藏输入框。可以在此根据需要调整其在模板中生成的先后顺序

CAPTCHA_FOREGROUND_COLOR = 'red'  # 设置验证码图片前景色

CAPTCHA_BACKGROUND_COLOR = '#ffffff'  # 设置验证码图片背景色

CAPTCHA_FONT_SIZE = '20'  # 设置验证码图片中字体大小

CAPTCHA_FONT_PATH = 'RobotoDraft-Medium.ttf'  # 设置字体样式，支持TTF等文件格式

CAPTCHA_LETTER_ROTATION = (-35, 35)  # 设置验证码中字母旋转的角度

CAPTCHA_NOISE_FUNCTIONS = (
'captcha.helpers.noise_arcs', 'captcha.helpers.noise_dots',)  # 是否添加干扰点和干扰线，当值为'captcha.helpers.noise_null'时，表示不添加干扰

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge'  # 设置验证码类型，其内置了三种验证码类型，还包括'captcha.helpers.math_challenge'（数字）和'captcha.helpers.word_challenge'（字典），除此之外，你还可以自己定义验证码生成函数

CAPTCHA_TIMEOUT = '5'  # 设置验证码的有效时间，单位为分钟

CAPTCHA_LENGTH = '4'  # 当验证码类型为字符型时，指定字母个数
