# This is a sample Python script.
import math

from PIL import Image


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def addShuiYin():
    im = Image.open("target.jpeg")
    w, h = im.size
    print('target size: %sx%s' % (w, h))

    mark = Image.open("mark.jpeg")
    m_w, m_h = mark.size
    print('mark size: %sx%s' % (w, h))

    process_m_w = w

    process_m_h = math.floor(m_h * (w / m_w))

    mark.resize((process_m_w, process_m_h))
    print('mark resize size: %sx%s' % (process_m_w, process_m_h))

    result = Image.new('RGB', (process_m_w, process_m_h + h))
    result.paste(im, (0, 0))
    result.paste(mark, (0, h))
    result.save("result.jpg")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    addShuiYin()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
