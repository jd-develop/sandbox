#!/usr/bin/env python3
# coding:utf-8
import PySimpleGUI as sg

layout = [
    [
        sg.Text("Choisissez:", key='-TEXT-'),
        sg.OptionMenu(['item 1', 'item 2'], default_value='item 1', key="-OPTION_MENU1-"),
        sg.Button("pouf", key="-BUTTON1-")
    ],
    [
        sg.Input('Choisissez: ', key='-INPUT1-', enable_events=True),
        sg.Button("pouf2", key="-BUTTON2-")
    ],
    [
        sg.Text("Ce texte est cliquable", enable_events=True, key="-TEXT1-")
    ],
    [
        sg.Spin([*range(100)], key="Spin1")
    ]
]

window = sg.Window("Converter", layout=layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "-BUTTON1-":
        print(values['-OPTION_MENU1-'])

    if event == "-BUTTON2-":
        window['-TEXT-'].update(values['-INPUT1-'])

    if event == "-TEXT1-":
        print("Ah oui en effet")

    if event == '-INPUT1-':
        print(values['-INPUT1-'])

window.close()
