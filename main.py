import os
import PySimpleGUI as sg
import mpv
import anime4k

sg.theme('BlueMono')
icon = f'{os.path.dirname(__file__) + os.sep}favicon.ico'


# folder = sg.popup_get_folder(
#     'Выберите папку с медиа', title='Выбор папки', icon=icon, font='Consolas', history=True,
#     size=(30, 40)).replace('/', os.sep)


def list_files():
    return [os.path.join(folder, f) for f in os.listdir(
        folder) if (f.lower().endswith('.m4a') or f.lower().endswith('.mp4') or f.lower().endswith('.mp3'))]


def list_filenames():
    return [f for f in os.listdir(folder) if
            (f.lower().endswith('.m4a') or f.lower().endswith('.mp4') or f.lower().endswith('.mp3'))]


# files = list_files()
# filenames_only = list_filenames()

with open(f'{os.path.dirname(__file__) + os.sep}txt{os.sep}GLSL_Instructions_Advanced_ru.txt', 'r',
          encoding='utf-8') as file:
    reference = file.read()

folder = ''
files = []
filenames_only = []
filenum = -1
if len(files) != 0:
    filename = files[0]
else:
    filename = ''

modes = []
for quality in anime4k.qualities:
    modes += [f'Mode {mode} ({quality})' for mode in anime4k.modes]


def menu_shaders():
    tab = []
    for quality in anime4k.qualities:
        tab += [f'Качество {quality}', [f'Mode {mode} ({quality})' for mode in anime4k.modes]]
    tab += [f'Ultra HQ', list(anime4k.presets.keys())[7:]]
    return tab


menu = [
    ['Файл', ['Открыть URL-адрес', 'Открыть папку', 'Выход']],
    ['Увеличение качества изображения', ['Отключить'] + menu_shaders()],
    ['Другое', ['Справка', 'О программе']]
]

col_files = [
    [
        sg.Text(f'Файл {filenum + 1} из {len(files)}', size=(15, 1), key='-FILENUM-'),
        sg.Text('', key='-VIDEO_INFO-')
    ],
    [
        sg.Text(folder, key='-FOLDER-')
    ],
    [
        sg.Listbox(values=filenames_only, size=(50, 30), key='-FILELIST-', enable_events=True)
    ]
]

col = [
    [
        sg.Image('', key='-VID_OUT-')
    ],
    [
        sg.Slider(orientation='h', key='-TIME-', enable_events=True, expand_x=True, range=(0, 0),
                  disable_number_display=True)
    ],
    [
        sg.Text('00:00 / 00:00', key='-VIDEO_TIME-'),
        sg.Button('ПРЕД', size=(8, 2)),
        sg.Button('ИГРАТЬ', key='-PLAY-', size=(8, 2)),
        sg.Button('СЛЕД', size=(8, 2)),
        sg.Button('ПОЛН', size=(8, 2)),
        sg.Slider(orientation='h', key='-VOLUME-', default_value=100, enable_events=True, range=(0, 100), size=(15, 30))
    ],
]

layout = [
    [
        sg.Menu(menu)
    ],
    [
        sg.Col(col_files, vertical_alignment='top'),
        sg.Col(col, expand_y=True, expand_x=True)
    ]
]

window = sg.Window('Anime Player', layout, icon=icon, resizable=True, finalize=True, font='Consolas',
                   size=(1140, 540))

window['-VID_OUT-'].expand(True, True)

player: mpv.MPV = mpv.MPV(wid=window['-VID_OUT-'].Widget.winfo_id(), input_default_bindings=True,
                          input_vo_keyboard=True, osc=True, scale='ewa_lanczossharp', cscale='ewa_lanczossharp',
                          dscale='ewa_lanczossharp', keep_open=True)

while True:
    event, values = window.read(timeout=500)
    # --------------------- Кнопки ---------------------
    if event == sg.WIN_CLOSED:
        break
    elif event == '-VOLUME-':
        player.volume = values['-VOLUME-']
    elif event == '-TIME-' and player.duration is not None:
        player.time_pos = values['-TIME-']
        window['-VIDEO_TIME-'].update(value="{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(int(player.time_pos), 60),
                                                                                   *divmod(int(player.duration), 60)))
    elif event in 'СЛЕД' and filenum < len(files) - 1:
        player.stop()
        window['-PLAY-'].update('ИГРАТЬ')
        filenum += 1
        filename = os.path.join(folder, filenames_only[filenum])
        window['-FILELIST-'].update(set_to_index=filenum, scroll_to_index=filenum)
        player.play(filename)
        player.pause = True
    elif event in 'ПРЕД' and filenum > 0:
        player.stop()
        window['-PLAY-'].update('ИГРАТЬ')
        filenum -= 1
        filename = os.path.join(folder, filenames_only[filenum])
        window['-FILELIST-'].update(set_to_index=filenum, scroll_to_index=filenum)
        player.play(filename)
        player.pause = True
    elif event == '-PLAY-':
        if player.duration == 0:
            player.play(filename)
            window['-PLAY-'].update('ПАУЗА')
        elif not player.pause:
            player.pause = True
            window['-PLAY-'].update('ИГРАТЬ')
        else:
            player.pause = False
            window['-PLAY-'].update('ПАУЗА')
    elif event == 'ПОЛН':
        if player.duration is not None:
            player.wid = -1
            player.vo = 'null'
            player.fullscreen = True
            player.vo = ''
            player.wait_for_property('fullscreen', lambda val: not val)
            player.fullscreen = True
            if player.pause and window['-PLAY-'] != 'ИГРАТЬ':
                window['-PLAY-'].update('ИГРАТЬ')
            elif not player.pause:
                window['-PLAY-'].update('ПАУЗА')
            player.wid = window['-VID_OUT-'].Widget.winfo_id()
            player.vo = 'null'
            player.vo = ''

    elif event == 'Выход':
        break
    elif event == '-FILELIST-':
        if len(filenames_only) != 0:
            filename_temp = os.path.join(folder, values['-FILELIST-'][0])
            if filename != filename_temp:
                player.stop()
                window['-PLAY-'].update('ИГРАТЬ')
                filename = filename_temp
                filenum = files.index(filename)
                player.play(filename)
                player.pause = True
    # ----------------- Верхнее меню -----------------
    if event == 'Открыть URL-адрес':
        link = sg.popup_get_text(
            'Введите URL-адрес', title='Ввод ссылки', icon=icon, font='Consolas', size=(30, 40))
        if link != '' and link is not None:
            player.stop()
            window['-PLAY-'].update('ИГРАТЬ')
            folder = 'Ссылка'
            files = [link]
            filenames_only = []
            window['-FILELIST-'].update(values=files)
            player.play(link)
            player.pause = True
            window.refresh()
            filenum = 0
            filename = link

    elif event == 'Открыть папку':
        new_folder = sg.popup_get_folder(
            'Выберите папку с медиа', title='Выбор папки', icon=icon, font='Consolas', history=True,
            size=(30, 40))
        if new_folder != '' and new_folder is not None:
            new_folder = new_folder.replace('/', os.sep)
            player.stop()
            window['-PLAY-'].update('ИГРАТЬ')
            folder = new_folder
            files = list_files()
            filenames_only = list_filenames()
            window['-FILELIST-'].update(values=filenames_only)
            window.refresh()
            filenum = 0
            if len(files) != 0:
                filename = files[0]
            else:
                filename = ''
    if event == 'Отключить':
        player.glsl_shaders = ''
    elif event in anime4k.presets.keys():
        player.glsl_shaders = anime4k.to_string(anime4k.presets[event])
    elif event in modes:
        quality = event.replace(')', '').split('(')[1]
        mode = event.split(' ')[1]
        player.glsl_shaders = anime4k.to_string(anime4k.create_preset(quality, mode))
    elif event == 'Справка':
        sg.popup_scrolled(reference, size=(200, 0), title='Справка', icon=icon, font='Consolas')
    elif event == 'О программе':
        sg.popup('Версия 0.1\nПрограмму создал Мазур Денис Олегович в 2023 году', title='О программе',
                 icon=icon)

    duration = player.duration
    time_pos = player.time_pos
    codec = player.video_format if player.video_format is not None else player.audio_codec_name

    # Обновление имени файла
    window['-FOLDER-'].update(folder)
    # Обновление номера файла
    window['-FILENUM-'].update(f'Файл {filenum + 1} из {len(files)}')
    window['-VIDEO_INFO-'].update(f'Кодек: {codec}, Потеряно кадров: {player.frame_drop_count}')
    if duration is not None and player.pause:
        window['-PLAY-'].update('ИГРАТЬ')
    elif filename != '' and duration is None and player.play:
        player.pause = True
        window['-PLAY-'].update('ИГРАТЬ')
        player.play(filename)
    elif duration is not None and player.play:
        window['-VIDEO_TIME-'].update(value="{:02d}:{:02d} / {:02d}:{:02d}".format(*divmod(int(time_pos), 60),
                                                                                   *divmod(int(duration), 60)))
        window['-TIME-'].update(range=(0, duration), value=time_pos)
    else:
        window['-TIME-'].update(range=(0, 0), value=0)
        window['-VIDEO_TIME-'].update(value='00:00 / 00:00')

window.close()
