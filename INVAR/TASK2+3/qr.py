import pyqrcode
import png

def createQr(content, module_color, background, file_format, scale):
  """
    Создание QR-кода на основе переданной в программу текстовой строки
    В качестве аргументов выступают: content - искомая строка
                                     module_color - цвет сгенерируемого QR-кода
                                     background - фон
                                     scale - масштаб сгенерируемого QR-кода
  """
    qrcode = pyqrcode.create(content)
    if file_format == 'png':
        qrcode.png('qrimg.png', module_color = module_color, background=background,scale=scale)
    elif file_format == 'svg':
        qrcode.svg('qrimg.svg', module_color = module_color, background=background,scale=scale)

result = input("Введите нужную строку: ")
createQr(result, (178,5,93), (2,5,6), file_format = 'png', scale = 8)
