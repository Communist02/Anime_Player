import locale

en = {
    'File': 'File',
    'Open URL': 'Open URL',
    'Open folder': 'Open folder',
    'Exit': 'Exit',
    'Increasing image quality': 'Increasing image quality',
    'Disable': 'Disable',
    'Other': 'Other',
    'Reference': 'Reference',
    'About': 'About',
    'Quality': 'Quality',
    'Mode': 'Mode',
    'About program': 'Media player written in Python programming language using PySimpleGUI library for graphical user interface, MPV media player and Anime4K scaling algorithm',
    'Activate SVP': 'Activate SVP',
    'Create config for Android': 'Create config for Android'
}

ru = {
    'File': 'Файл',
    'Open URL': 'Открыть URL-адрес',
    'Open folder': 'Открыть папку',
    'Exit': 'Выход',
    'Increasing image quality': 'Увеличение качества изображения',
    'Disable': 'Отключить',
    'Other': 'Другое',
    'Reference': 'Справка',
    'About': 'О программе',
    'Quality': 'Качество',
    'Mode': 'Режим',
    'About program': 'Медиаплеер, написанный на языке программирования Python с использованием библиотеки графического пользовательского интерфейса PySimpleGUI, мультимедийного проигрывателя MPV и алгоритма масштабирования Anime4K',
    'Activate SVP': 'Активировать SVP',
    'Create config for Android': 'Создать конфиг для Android'
}

match locale.getlocale()[0]:
    case 'Russian_Russia':
        strings = ru
    case _:
        strings = en
