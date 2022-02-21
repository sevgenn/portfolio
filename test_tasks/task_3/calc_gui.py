"""
Модуль графического приложения "Геометрический кальккулятор".

Позволяющет выбирать плоские или объемные фигуры из определенного набора, задавать им параметры и получать расчетные
характеристики периметра, площади, объема, апофемы, соответствующие введенным данным, в зависимости от наличия данных
характеристик у выбранной фигуры. Предусмотрена возможность вывода изображения выбранной фигуры.
Импортирует следующие модули:
tkinter - для реализации графического представления,
sys - для получения из модуля имени класса (getattr(sys.modules[__name__], text)),
shapes - содержит классы ипользуемых фигур с методами их расчета,
Обработка ошибок ввода пользователя осуществляется на уровне экземпляра класса фигуры. При некорректном вводе
исходному параметру присваивается нулевое значение. В дальнейшем все некорректные данные выводят сообщение об ошибке.
Кнопки "Circle", "Square", "Rectangle", "Triangle", "Trapeze", "Rhombus", "Ball", "Cube", "Box", "Pyramid", "Cylinder",
"Cone" выбирают фигуру.
Кнопка "Calculate" - рассчитать.
Кнопка "С" - сброс в исходное состояние.
Кнопка "Draw" - вывести изображение.
Кнопка "Exit" - выход из приложения.
"""

import tkinter as tk
import sys
from shapes import *


class Main(tk.Frame):
    """Класс формирующий графический интерфейс и включающий логику обработки действий пользователя."""

    def __init__(self, window):
        """Инициализирует окно программы, метод его формирования и обрабатываемый экземпляр класса фигуры."""
        super().__init__()
        self.window = window
        self.create_form()
        self.obj = None

    def create_form(self):
        """Создает разметку окна программы и объявляет глобальные переменные."""
        global entry_lst
        global result_lst
        global param_lst
        global res_apothem
        global res_perimeter
        global res_area
        global res_volume

        for i in range(4):
            self.window.grid_columnconfigure(i, minsize=200)
        for i in range(10):
            self.window.grid_rowconfigure(i, minsize=50)
        self.window.title("Геометрический калькулятор")
        self.window.resizable(False, False)

        btns_res = ["Apothem", "Perimeter", "Area", "Volume"]
        btns_shapes = ["Circle", "Square", "Rectangle", "Triangle", "Trapeze", "Rhombus"]
        btns_solids = ["Ball", "Cube", "Box", "Pyramid", "Cylinder", "Cone"]

        param_lst = []
        for i in range(4):
            btn = self.make_button(text='', bg_color='grey', fg_color='#000')
            btn.grid(row=i, column=0, stick='wens', padx=2, pady=2)
            param_lst.append(btn)
            btn.bind('<Button-1>', self.focus_entry)

        entry_lst = []
        for i in range(4):
            param = self.make_entry()
            param.grid(row=i, column=1, stick='wens', padx=2, pady=2)
            entry_lst.append(param)

        result_lst = []
        res_apothem = self.make_label('', '#000', '#fff', font=('Arial', 18))
        result_lst.append(res_apothem)
        res_perimeter = self.make_label('', '#000', '#fff', font=('Arial', 18))
        result_lst.append(res_perimeter)
        res_area = self.make_label('', '#000', '#fff', font=('Arial', 18))
        result_lst.append(res_area)
        res_volume = self.make_label('', '#000', '#fff', font=('Arial', 18))
        result_lst.append(res_volume)
        res_apothem.grid(row=4, column=0, stick='wens', padx=2, pady=2)
        res_perimeter.grid(row=4, column=1, stick='wens', padx=2, pady=2)
        res_area.grid(row=4, column=2, stick='wens', padx=2, pady=2)
        res_volume.grid(row=4, column=3, stick='wens', padx=2, pady=2)

        for i in range(4):
            label_res = self.make_label(text=btns_res[i], bg_color='sky blue', fg_color='#000')
            label_res.grid(row=5, column=i, stick='wens', padx=2, pady=2)

        for i in range(len(btns_shapes)):
            k = i // 2
            j = i % 2
            btn = self.make_button(text=btns_shapes[i], bg_color='light cyan')
            btn.grid(row=6 + k, column=j, stick='wens', padx=2, pady=2)
            btn.bind('<Button-1>', self.on_click)

        for i in range(len(btns_solids)):
            k = i // 2
            j = 2 + i % 2
            btn = self.make_button(text=btns_solids[i], bg_color='lightBlue')
            btn.grid(row=6 + k, column=j, stick='wens', padx=2, pady=2)
            btn.bind('<Button-1>', self.on_click)

        btn0 = self.make_button(text='1', command=lambda: self.add_digit('1'))
        btn0.grid(row=9, column=0, stick='wens', padx=2, pady=2)
        btn1 = self.make_button(text='2', command=lambda: self.add_digit('2'))
        btn1.grid(row=9, column=1, stick='wens', padx=2, pady=2)
        btn2 = self.make_button(text='3', command=lambda: self.add_digit('3'))
        btn2.grid(row=9, column=2, stick='wens', padx=2, pady=2)
        btn3 = self.make_button(text='4', command=lambda: self.add_digit('4'))
        btn3.grid(row=9, column=3, stick='wens', padx=2, pady=2)
        btn4 = self.make_button(text='5', command=lambda: self.add_digit('5'))
        btn4.grid(row=10, column=0, stick='wens', padx=2, pady=2)
        btn5 = self.make_button(text='6', command=lambda: self.add_digit('6'))
        btn5.grid(row=10, column=1, stick='wens', padx=2, pady=2)
        btn6 = self.make_button(text='7', command=lambda: self.add_digit('7'))
        btn6.grid(row=10, column=2, stick='wens', padx=2, pady=2)
        btn7 = self.make_button(text='8', command=lambda: self.add_digit('8'))
        btn7.grid(row=10, column=3, stick='wens', padx=2, pady=2)
        btn8 = self.make_button(text='9', command=lambda: self.add_digit('9'))
        btn8.grid(row=11, column=0, stick='wens', padx=2, pady=2)
        btn9 = self.make_button(text='0', command=lambda: self.add_digit('0'))
        btn9.grid(row=11, column=1, stick='wens', padx=2, pady=2)
        btn10 = self.make_button(text=',', command=lambda: self.add_digit('.'))
        btn10.grid(row=11, column=2, stick='wens', padx=2, pady=2)

        del_symbol_btn = self.make_button(text='<')
        del_symbol_btn.grid(row=11, column=3, stick='wens', padx=2, pady=2)
        del_symbol_btn.bind('<Button-1>', self.delete_symbol)

        exit_btn = self.make_button(text='Exit', bg_color='grey', fg_color='red', command=self.exit_out)
        exit_btn.grid(row=0, column=3, stick='wens', padx=2, pady=2)

        reset_btn = self.make_button(text='C', bg_color='light grey', fg_color='red')
        reset_btn.grid(row=1, column=3, stick='wens', padx=2, pady=2)
        reset_btn.bind('<Button-1>', self.reset)

        calc_btn = self.make_button(text='Calculate', bg_color='light grey')
        calc_btn.grid(row=2, column=3, stick='wens', padx=2, pady=2)
        calc_btn.bind('<Button-1>', self.calculate)

        draw_btn = self.make_button(text='Draw', bg_color='light grey', command=self.draw_picture)
        draw_btn.grid(row=3, column=3, stick='wens', padx=2, pady=2)

    def make_button(self, text='', bg_color='#fff', fg_color='#000', command=None):
        """Создает виджет типа Button."""
        return tk.Button(text=text, bd=2, bg=bg_color, fg=fg_color, font=('Arial', 13), command=command)

    def make_label(self, text, bg_color='#000', fg_color='#fff', font=('Arial', 13)):
        """Создает виджет типа Label."""
        return tk.Label(self.window, text=text, bg=bg_color, fg=fg_color, font=font)

    def make_entry(self):
        """Создает виджет типа Entry."""
        return tk.Entry(self.window, state=tk.DISABLED, justify=tk.RIGHT, bg='grey', fg='#000', font=('Arial', 13))

    def add_digit(self, digit):
        """Добавляет символ в окно Entry, если окно активно."""
        for entry in entry_lst:
            if entry == self.window.focus_get():
                value = entry.get() + str(digit)
                if value[0] == '0':
                    value = value[1:]
                entry.delete(0, tk.END)
                entry.insert(0, value)

    def delete_symbol(self, event):
        """Удаляет последний введенный символ из активного окна Entry."""
        for entry in entry_lst:
            if entry == self.window.focus_get():
                value = entry.get()[:-1]
                entry.delete(0, tk.END)
                entry.insert(0, value)

    def get_entry(self):
        """Получает лист введенных значений из всех активированных окон Entry."""
        entry_list = []
        for entry in entry_lst:
            if entry.cget('state') == tk.NORMAL:
                if entry.get() != '':
                    entry_list.append(float(entry.get()))
                else:
                    entry_list.append(0.0)
        return entry_list

    def clear_labels(self, lst):
        """Удаляет надписи из определенного списка виджетов типа Label."""
        for label in lst:
            label.config(text='')

    def clear_entries(self):
        """Очищает все окна ввода."""
        for entry in entry_lst:
            entry.delete(0, tk.END)

    def change_params_labels(self):
        """Устанавливает надписи на кнопках, соответствующие параметрам выбранной фигуры."""
        self.clear_entries()
        self.clear_labels(result_lst)
        self.clear_labels(param_lst)
        for i in range(len(obj.names)):
            param_lst[i].config(text=obj.names[i])

    def get_figure(self, event):
        """Создает экземпляр класса фигуры."""
        global obj
        text = event.widget.cget('text')
        class_obj = getattr(sys.modules[__name__], text)
        obj = class_obj()
        return obj

    def on_click(self, event):
        """
        Активирует действия по клику на выбранную фигуру.

        Создает экземпляр класса, выводит надписи соответствующих параметров, активирует соответствующие окна ввода
        параметров.
        """
        self.get_figure(event)
        self.change_params_labels()
        self.activate_entry()

    def focus_entry(self, event):
        """Фокусирует операции ввода-редактирования на окне, соответствующем выбранному параметру."""
        ind = param_lst.index(event.widget)
        entry_lst[ind].focus_set()

    def activate_entry(self):
        """Делает активными только окна, предназначенные для ввода данных."""
        for i in range(4):
            if param_lst[i].cget('text') != '':
                entry_lst[i].config(state=tk.NORMAL)
            else:
                entry_lst[i].config(state=tk.DISABLED)

    def deactivate_entries(self):
        """Делает недоступными все окна ввода."""
        for entry in entry_lst:
            entry.config(state=tk.DISABLED)

    def set_params(self):
        """Присваивает значения из окон ввода параметрам экземпляра фигуры."""
        values = self.get_entry()
        params = list(obj.__dict__)
        for i in range(len(params)):
            setattr(obj, params[i], values[i])
        # obj.__dict__ = {key: value for key, value in zip(obj.__dict__.keys(), values)}

    def calculate(self, event):
        """
        Активирует действия по клику пользователя на окне Calculate.

        Передает введенные данные в экземпляр фигуры и записывает расчетные данные в соответствующие окна
        вывода информации.
        """
        self.set_params()
        if obj.calculate(Apothem()):
            a = obj.calculate(Apothem())
            res_apothem.config(text=a)
        if obj.calculate(Perimeter()):
            p = obj.calculate(Perimeter())
            res_perimeter.config(text=p)
        if obj.calculate(Area()):
            s = obj.calculate(Area())
            res_area.config(text=s)
        if obj.calculate(Volume()):
            v = obj.calculate(Volume())
            res_volume.config(text=v)

    def reset(self, event):
        """По клику переводит окно в первоначальное состояние, обнуляя всю информацию."""
        self.clear_entries()
        self.deactivate_entries()
        self.clear_labels(param_lst)
        self.clear_labels(result_lst)

    def draw_picture(self):
        """Выводит в отдельном окне изображение фигуры."""
        obj.draw()

    def exit_out(self):
        """Завершает работу программы."""
        self.window.destroy()


if __name__ == '__main__':
    window = tk.Tk()
    app = Main(window)
    window.mainloop()
