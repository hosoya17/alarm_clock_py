# alarm_clock_py
[![Open in Visual Studio Code](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=Open%20in%20Visual%20Studio%20Code&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://open.vscode.dev/hosoya17/alarm_clock_py)
## 開発の概要
windows、mac共に動作するアラーム・目覚ましアプリです。<br>
以前公開した[alarm_clock](https://github.com/hosoya17/alarm_clock)のpython版です。
## システムの概要
・コンボボックスで時、分の指定をします。<br>
・指定した時間になったら、wavファイルが再生されます。<br>
・スヌーズ、停止ボタンのいずれかをクリックします。<br>
・停止ボタンの場合、wavファイルが停止されます。<br>
・スヌーズボタンの場合、wavファイルが停止され、10分後にまたwavファイルが再生されます。
### 開発環境
開発環境：Visual Studio Code<br>
開発言語：python3<br>
ライブラリ:tkinter, tkinter.ttk, time, pygame
[![My Skills](https://skillicons.dev/icons?i=vscode,py)](https://skillicons.dev)
### 注意事項
事前にpygameをインストールする必要があります。インストール方法は以下の通りです。<br>
```
pip install pygame
```
<br>
alarm_clock.pyの79行目の""の中はご自身の再生したいwavファイルのパスに変更してからご使用ください。<br>
変更しない場合、プログラムは正しく動作しません。<br>
```
pygame.mixer.music.load('C:\\python\\Sound\\Clock-Alarm03-01(Mid-Loop).wav')//wavファイルのパスを指定してください。
```
