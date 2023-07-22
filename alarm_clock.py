import tkinter as tk
import tkinter.ttk as ttk
import time
import pygame

class Application(tk.Frame):
  def __init__(self, root):
    super().__init__(root, width=762, height=500, borderwidth=1, relief='groove')
    self.root = root
    self.pack()
    self.pack_propagate(False)
    self.create_widgets()
    self.alarm_playing = False

  def create_widgets(self):
    self.clock_text = tk.Label(self, font=('Yu Gothic UI', '72', 'normal'))
    self.clock_text.place(x=70, y=90)
    self.clock()

    hour_text = tk.Label(self, text='時', font=('Yu Gothic UI', '16', 'normal'))
    hour_text.place(x=300, y=360)

    min_text = tk.Label(self, text='分', font=('Yu Gothic UI', '16', 'normal'))
    min_text.place(x=445, y=360)

    self.hour_combobox = ttk.Combobox(self, values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23'], state='readonly', width=15)
    self.hour_combobox.place(x=185, y=370)

    self.min_combobox = ttk.Combobox(self, values=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59'], state='readonly', width=15)
    self.min_combobox.place(x=330, y=370)

    set_btn = tk.Button(self, text='アラームセット', width=10)
    set_btn['command'] = self.set_time
    set_btn.place(x=476, y=368)

    self.snooz_btn = tk.Button(self, text='スヌーズ', width=7, height=1, font=('Yu Gothic UI', '12', 'normal'))
    self.snooz_btn['command'] = self.snooz_process
    self.snooz_btn.place_forget()

    self.stop_btn = tk.Button(self, text='停止', width=7, height=1, font=('Yu Gothic UI', '12', 'normal'))
    self.stop_btn['command'] = self.stop_process
    self.stop_btn.place_forget()

  def clock(self):
    now = time.strftime('%H時%M分%S秒')
    self.clock_text.config(text=now)
    self.clock_text.after(1000, self.clock)

  def set_time(self):
    hour_text = self.hour_combobox.get() if int(self.hour_combobox.get()) >= 10 else '0' + self.hour_combobox.get()
    min_text = self.min_combobox.get() if int(self.min_combobox.get()) >= 10 else '0' + self.min_combobox.get()
    self.set_time_text = tk.Message(self, width=300, font=('Yu Gothic UI', '24', 'normal'))
    self.set_time_text.place(x=220, y=305)
    self.set_time_text['text'] = '設定時刻:' + hour_text + '時' + min_text + '分'
    current_hour = int(time.strftime('%H'))
    current_min = int(time.strftime('%M'))
    current_sec = int(time.strftime('%S'))
    if(current_hour < int(hour_text)):
      self.set = (int(hour_text) - current_hour) * 60 * 60 + (int(min_text) - current_min) * 60 - current_sec
    elif(current_hour == int(hour_text) and current_min < int(min_text)):
      self.set = (int(hour_text) - current_hour) * 60 * 60 + (int(min_text) - current_min) * 60 - current_sec
    elif(current_min >= int(min_text)):
      self.set = (24 - current_hour + int(hour_text)) * 60 * 60 - (int(min_text) - current_min) * 60 - current_sec
    else:
      self.set = (24 - current_hour + int(hour_text)) * 60 * 60 - (int(min_text) - current_min) * 60 - current_sec
    self.alerm()

  def alerm(self):
    self.root.after(self.set * 1000, self.alerm_process)

  def alerm_process(self):
    self.alerm_text = tk.Label(self, text='時間です。', font=('Yu Gothic UI', '16', 'normal'))
    self.alerm_text.place(x=340, y=70)
    self.snooz_btn.place(x=295 ,y=450)
    self.stop_btn.place(x=380 ,y=450)
    if not self.alarm_playing:
      self.alarm_playing = True
      pygame.mixer.init()
      pygame.mixer.music.load('C:\\python\\Sound\\Clock-Alarm03-01(Mid-Loop).wav')
      pygame.mixer.music.play(-1)

  def stop_process(self):
    self.alerm_text.place_forget()
    self.snooz_btn.place_forget()
    self.stop_btn.place_forget()
    self.set_time_text.place_forget()
    pygame.mixer.music.stop()
    self.alarm_playing = False

  def snooz_process(self):
    self.alerm_text.place_forget()
    self.snooz_btn.place_forget()
    self.stop_btn.place_forget()
    self.set = 600
    pygame.mixer.music.stop()
    self.alarm_playing = False
    self.alerm()

root = tk.Tk()
root.title('時計')
root.geometry('762x500')
app = Application(root=root)
root.mainloop()
