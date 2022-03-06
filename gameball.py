# ايمپورت شده براي انتخاب مکان گزينه ها وامتياز ان ها
import random
# ايمپورت شده براي زماني که گزينه انتخاب ميشود و ان سياه ميشود و يک ثانيه روي صفحه ميماند
import time
# ايمپورت شده براي بدست اوردن حالت هاي ممکن
from itertools import permutations
# ايمپورت شده براي دسترسي به فايل ها و انتخاب فايل
import os
# ايمپورت شده براي تبديل مقدار هاي گرفته شده از محيط گرافيکي
import re
#  ايمپورت شده براي تبديل مقدار هاي گرفته شده از محيط گرافيکي
import string
# ايمپورت شده براي تشکيل محيط گرافيکي
# براي باز شدن صفحه با حالت ماکسيمم
from kivy import Config
# براي حرکت مهره در راستاي خط
from kivy.clock import Clock
# براي منع باز کردن صفحه به صورت فول اسکرين
from kivy.core.window import Window
# براي رنگ دکمه ها وامتياز ها ومهره هاووو
from kivy.graphics.context_instructions import Color
# براي کشيدن دايره ومستطيل خز
from kivy.graphics.vertex_instructions import Line, Ellipse, Rectangle
# براي اجراي برنامه
from kivy.app import App
# براي چينش صفحه
from kivy.uix.boxlayout import BoxLayout
# براي قرار دادن دکمه در صفحه
from kivy.uix.button import Button
# براي خواندن استرينگ مربوط به فايل kv
from kivy.lang import Builder
# براي قراردادن نوشته ها در صفحه
from kivy.uix.label import Label
# براي اعلام برنده در پايان بازي و گرفتن مکان امتياز ها
from kivy.uix.popup import Popup
# براي اجراي هر اسکرين
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
# براي گرفتن متن از کاربر
from kivy.uix.textinput import TextInput
# براي اجراي فر با اعداد اعشاري
from numpy.ma import arange

# مقدار ال در اين ذخيره ميشود
l = 1
# حرکات در اين ذخيره ميشوند
trak = []
# انتخاب نوبت توسط اين تعويض وانتخاب ميشود
com = True
# برچسب هاي روي نقاط
label = []
# مقدار انتخاب شده شده توسط کاربر
choose = 0
# گزينه هاي انتخاب داخل  اين ليست است
but = []
# نقاط درون اين ليست جاي ميگيرد
point = []
# کليد هاي گزينه هاي انتخاب درون اين ليست قرار ميگيرد
bu = []
# نقاط داده شده توسط کاربر ومقدار امتياز در اين ليست قرار ميگيرد
point_me = []
# مکان هاي نقاط که توسط کاربر داده شده است وارد اين ليست ميشود
index_me = []
# براي فرق دادن وقتي اولين با کاربر شروع مي کنيم يا کامپيوتر
a = 1
# براي فرق دادن وقتي اولين با کاربر شروع مي کنيم يا کامپيوتر
b = 1
# براي الگوريتم است و فقط يک با ر تکرار ميشود
turn = 1
# مکان هاي گزينه ها در اين ذخيره ميشوند
rand_save = []


# براي اجراي هر اسکرين وترتيبقرار گرفتن صفحات وارجاع صفحه اي به صفحه ديگر
class ScreenManagement(ScreenManager):
    # براي چينش صفحات
    def __init__(self, **kwargs):
        # ارث بري براي شنا ساندن تابع به عنوان ترتيب دهنده اسکرين ها
        super(ScreenManagement, self).__init__(**kwargs)


# اجراي فايل kvدر داخل اسکريپت
# <Page1Screen> تنظيم تصوير زمينه روي صفحه اول
# <Page2Screen> تنظيم تصوير زمينه روي صفحه دوم
# <Page3Screen> تنظيم تصوير زمينه و گرفتن فايل
h = '''

#:import C kivy.utils.get_color_from_hex

<Page1Screen>:
    id: my_widget
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "Elegant_Background6.jpg"



<Page2Screen>:
    canvas.before:
        Rectangle:
            pos: self.pos
            size: self.size
            source: "137362.jpg"
<Page3Screen>:
    id: my_widget

    FileChooserListView:
        id: filechooser
        path: {}
        on_selection: my_widget.selected(filechooser.selection)
    Button
        text: "open"
        size_hint_y:0.1
        background_down: '137362.jpg'
        background_normal: '137362.jpg'
        border: (2, 2, 2, 2)
        on_release: my_widget.open(filechooser.path, filechooser.selection)
'''.format('"' + os.getcwd().replace(r"\ "[0], r'\\') + '"')
# اجراي فايل kv
Builder.load_string(h)


# صفحه انتخاب فايل
class Page3Screen(BoxLayout, Screen):
    # تابع مقدار دهي
    def __init__(self, **kwargs):
        # ارث بري براي طبقه بندي صفحه
        super(Page3Screen, self).__init__(**kwargs)
        # گرفتن مقدار ال حرکات ونوبت
        global l, trak, com
        # صفحه به صورت عمودي ميشود
        self.orientation = 'vertical'

    # وقتي فايل را انتخاب ميکنيد صدا زده شده و ان را اپن ميکند
    def open(self, path, filename):
        # گرفتن مقدار ال حرکات ونوبت
        global com, l, trak
        # فايل را اپن ميکند
        with open(os.path.join(path, filename[0])) as f:
            # محتواي فايل را مي خواند و اعداد را ميابد
            resl1 = re.findall('\d+', f.read())
            # ليستي براي گرفتن اعداد تعريف ميکنيم
            resl = []
            # اعداد را وارد ليستي ميکند
            for u in resl1:
                # اعداد را  وارد ليست ميکنيم
                resl.append(int(u))
            # عدد اول lاست
            l = resl[0]
            # lرا حذف مي کنيم
            resl.remove(resl[0])
            # وبقيه اعداد حرکات هستند
            trak = resl
            # نوبت کامپيوتر نميباشدبنابر اين مقدار فالس است
            com = False
        # به صفحه اول ارجاع داده ميشود
        self.manager.current = 'page1'

    # فايل انتخاب شده را پرينت ميکند
    def selected(self, filename):
        # فايل انتخاب شده را پرينت ميکند
        print("selected: %s" % filename[0])


# صفحه اصلي بازي
class Page2Screen(Screen):
    # تابع مقدار دهي
    def __init__(self, **kwargs):
        # ارث بري براي ارتباط با اسکرين ها
        super(Page2Screen, self).__init__(**kwargs)
        # گرفتن مقدار ال وحرکات ونوبت و انتخاب کاربر وگزينه هاي انتخاب وامتيازات
        global l, trak, com, label, choose, but, point
        # دکمه استارت ايجاد ميشود
        self.button = Button(text='start', on_press=self.start, pos_hint={'top': 0.3, 'right': 0.55}, size=(50, 50),
                             size_hint_y=0.1, size_hint_x=0.1,
                             background_normal='137362.jpg')
        # اضافه کردن دکمه به صفحه
        self.add_widget(self.button)
        # نوشته ها وخز ومهره ها نشان داده ميشوند
        with self.canvas:
            # رنگ خط مشخص ميشود
            Color(1, 0.5, 0, 1, mode='rgba')
            # خط تشکيل ميشود
            Line(points=(100, 350, 1250, 350), width=10)
            # رنگ خط مشخص ميشود
            Color(1, 0, 1, .5, mode='rgba')
            # خط تشکيل ميشود
            Line(points=(100, 350, 1250, 350))
            # رنگ نقطه ها مشخص   ميشود
            Color(0.5568627450980392, 0.26666666666666666, 0.6784313725490196, 1, mode='rgba')

            # برچسبها ايجاد ميشوند
            # برچسب کاربر
            self.label1 = Label(text='me: ', pos=(100, 650), size=(20, 20), font_size=36)
            # برچسب امتياز کاربر
            self.label2 = Label(text='0', pos=(150, 650), size=(20, 20), font_size=36)
            # برچسب کامپيوتر
            self.label3 = Label(text='computer:', pos=(1150, 650), size=(20, 20), font_size=36)
            # امتياز کامپيوتر
            self.label4 = Label(text='0', pos=(1260, 650), size=(20, 20), font_size=36)
            # برچسب ال
            self.label10 = Label(text='L: ', pos=(82, 550), size=(20, 20), font_size=36)
            # طول ال
            self.label20 = Label(text='-', pos=(150, 550), size=(20, 20), font_size=36)
            # برچسب حرکات
            self.label30 = Label(text='actions:', pos=(1120, 550), size=(20, 20), font_size=36)
            # مقدار حرکات
            self.label40 = Label(text='-', pos=(1260, 550), size=(20, 20), font_size=36)
            # برچسب نوبت
            self.label11 = Label(text='turn: ', pos=(100, 450), size=(20, 20), font_size=36)
            # نمايش نوبت کاربر يا کامپيوتر
            self.label22 = Label(text='-', pos=(210, 450), size=(20, 20), font_size=36)
            # برچسب حرکت انجام شده
            self.label33 = Label(text='action:', pos=(1120, 450), size=(20, 20), font_size=36)
            # مقدار حرکتي که انجام شده
            self.label44 = Label(text='-', pos=(1260, 450), size=(20, 20), font_size=36)

    # دکمه ها و امتياز ها نشانداده ميشوند
    def start(self, c):
        # گرفتن مقادير نوبت ونقاطي که کاربر به برنامه داده است
        global com, point_me, index_me
        # مقدار lوارد کلاس ميشود
        self.l = l
        # همچنين حرکت ها مقداردهي ميشوند
        # بخاطر تاثيري که ليست ها بر هم دارند بايد کپي انها وارد ليست شود
        # حرکاتي که در صفحه اول گرفته شده به ليست مخصوص حرکات کاربر داده ميشود
        self.trak_me = trak.copy()
        # حرکاتي که در صفحه اول گرفته شده به ليست مخصوص حرکات کامپيوتر داده ميشود
        self.trak_com = trak.copy()
        # کليد شروع را حذف ميکند
        self.remove_widget(self.button)
        # اگر کاربر نقاطي وارد نکرده باشد
        if len(point_me) == 0:
            # امتياز ها به طور رندوم انتخاب ميشوند
            rando = [y for y in range(100, 1150)]
            # اعدادي که روي خط سفيد هستند حذف ميشوند
            s = [range(int(((1150 / self.l) * i) + 100 - 23), int(((1150 / self.l) * i) + 100 + 23)) for i in
                 range(1, self.l)]
            print(s)
            # براي حذف نقاطي که رئي خز افتادند
            # رنج هاي مد نظر از ليست اس بيرون مي ايند
            for t in s:
                # متغيري که اعداد در رنج را ميپيمايد
                for r in t:
                    # تا پايان خط تمام نقاطي که روي خط مي افتند را حذف ميکند
                    if r < 1150:
                        # اعداد حذف ميشوند
                        rando.remove(r)
            # حذف روي هم افتادگي ها و انتخاب مکان ومقدار امتياز
            for i in range(int(self.l / 2)):
                # به طور رندوم عددي از ليست انتخاب ميشود
                rand = random.choice(rando)
                # اگر روي هم بيفتند حذف ميشوند
                for rs in rand_save:
                    # تا زماني که نقطه مطلوب انتخاب نشود از وايل خارج نميشود
                    while rand in range(rs - 15, rs + 15):
                        print(314663413641, 1)
                        # نقطه ديگري انتخاب ميشود
                        rand = random.choice(rando)
                # مقدار هارا ذخيره ميکنند
                rand_save.append(rand)
                # روي صفحه ال ومقدار دهي ميشوندactions 
                with self.canvas:
                    # نمايش ال در صفحه
                    self.label20.text = str(self.l)
                    # نمايش حرکات در صفحه
                    self.label40.text = str(self.trak_me)
                    # مقدار امتياز ها
                    po = random.randint(-20, 20)
                    # رنگ گزينه ها
                    Color(0.5568627450980392, 0.26666666666666666, 0.6784313725490196, 1, mode='rgba')
                    # ايجاد گزينه ها
                    point.append(Rectangle(pos=(rand, 340), size=(20, 20)))
                    # ايجاد برچسب مقدار امتياز روي گزينه
                    label.append(Label(text=str(po), pos=(rand, 340), size=(20, 20)))
                    # خط کشي خط
                    for i in range(1, self.l):
                        # خطي هايي کشيده ميشود که تمام خط را به اندازه ال تقسيم کند
                        Line(points=(int(((1150 / self.l) * i) + 100), 360, int(((1150 / self.l) * i) + 100), 340),
                             size=(25, 25), width=3)
            print(rand_save)
        # اگر گزينه ها را خودتان وارد کنيد وارد الس ميشويد
        else:
            # روي صفحه ال ومقدار دهي ميشوندactions
            # مقدار ال روي صفحه نشان داده ميشود
            self.label20.text = str(self.l)
            # حرکات روي صفحه نشان داده ميشود
            self.label40.text = str(self.trak_me)
            # ايجاد امتياز ها
            with self.canvas:
                print(index_me, point_me)
                # مقدار هاي داده شده توسط کاربر
                for im, p in zip(index_me, point_me):
                    # رنگ امتياز ها
                    Color(0.5568627450980392, 0.26666666666666666, 0.6784313725490196, 1, mode='rgba')
                    print(index_me, point_me, 123456789)
                    # ايجاد امتياز
                    point.append(Rectangle(pos=(int(((1150 / self.l) * im) + 100), 340), size=(20, 20)))
                    # ايجاد برچسب مقدار امتياز روي گزينه
                    label.append(Label(text=str(p), pos=(int(((1150 / self.l) * im) + 100), 340), size=(20, 20)))
                # خط کشي خط
                for il in range(1, self.l):
                    # خطي هايي کشيده ميشود که تمام خط را به اندازه ال تقسيم کند
                    Line(points=(int(((1150 / self.l) * il) + 100), 360, int(((1150 / self.l) * il) + 100), 340),
                         size=(25, 25), width=3)
        # مهره ها
        with self.canvas:
            # مهره من
            Color(0, 0, 1, 1, mode='rgba')
            self.e = Ellipse(pos=(50, 350), size=(25, 25))
            # مهره کامپيوتر
            Color(1, 0, 0, 1, mode='rgba')
            self.e2 = Ellipse(pos=(50, 320), size=(25, 25))
        # انتخاب نوبت
        # اگر نوبت را براي  کاربر انتخاب کرديد ايف اجرا ميشود
        if com == False:
            # نوبت من است
            self.f()
        # اگر نوبت را براي کامپيوتر اجرا کرده ايد ايف اجرا  ميشود
        if com == True:
            # نوبت کامپوتر است
            self.g()

    # نوبت من
    def f(self):
        # گرفتن مقادير نوبت و کليد انتخاب ها وحرکات
        global com, bu, trak
        # پايان بازي
        if self.e2.pos[0] >= 1200:
            # ترتيب دهنده صفحه
            content = BoxLayout(orientation='vertical')
            # اعلام برنده يا بازنده
            # اگر شما برنده شديد
            if int(self.label2.text) >= int(self.label4.text):
                content.add_widget(Label(text='you win', font_size=72))
            # اگر کامپيوتر برنده شد
            else:
                content.add_widget(Label(text='you lose', font_size=72))
            # کليد خروج نمايش داده ميشود
            button12 = Button(text='quit', background_normal='back.jpg')
            # بازدن دکمه از برنامه خارج ميشويد
            button12.bind(on_press=quit)
            # مرتب کننده دکمه ها
            options = BoxLayout(size=(100, 100))
            # برچسب ها
            # برچسب کاربر
            self.lab = Label(text='you: ' + self.label2.text, font_size=32)
            # اضافه کردن ان به باکس
            options.add_widget(self.lab)
            # برچسب کامپيوتر
            self.lab2 = Label(text='computer: ' + self.label4.text, font_size=32)
            # اضافه کردن ان به باکس
            options.add_widget(self.lab2)
            # براي تنظيم فاصله
            self.lab3 = Label(text='')
            # اضافه کردن ان به باکس
            content.add_widget(self.lab3)
            # اضافه کردن ان به باکس اصلي
            content.add_widget(options)
            # براي تنظيم فاصله
            self.lab3 = Label(text='')
            # اضافه کردن ان به باکس
            content.add_widget(self.lab3)
            # اضافه کردن ان به باکس
            content.add_widget(button12)
            # popupباز ميشود
            popup = Popup(title='game',
                          content=content,
                          size_hint=(None, None),
                          size=(500, 500),
                          background='137362.jpg'
                          ).open()
            # براي خروج از بازي
            return 1
        # نوبت نمايش داده ميشود
        self.label22.text = 'me'
        # حرکت ها اپديت ميشوند اگر همه حرکات انجام شده باشد
        if len(self.trak_me) == 0:
            # براي تاثير نگزاشتن ليست ها برهم از کپي استفاده شده است
            self.trak_me = trak.copy()
        print(self.trak_me, trak)
        # ايجاد گزينه
        for i in self.trak_me:
            # ويت براي گرافيک کار
            with self.canvas:
                # رنگ گزينه ها
                Color(1, 1, 1, 0.75, mode='rgba')
                # اگر اولين نوبت با کاربر باشد
                if self.e2.pos[0] == 50:
                    # گزينه ها  نمايش داده ميشوند
                    but.append(Ellipse(pos=(int(((1150 / self.l) * i) + 100), 338), size=(25, 25)))
                # اگر اولين نوبت براي کامپيوتر باشد
                elif self.e2.pos[0] != 50:
                    # گزينه ها  نمايش داده ميشوند
                    self.e3 = Ellipse(pos=(int(((1150 / self.l) * i) + self.e2.pos[0]), 338), size=(25, 25))
                    # اگر در انتهاي خط باشيم
                    if self.e3.pos[0] > 1350:
                        # کمي نزديک تر ميشود تا در صفحه باشد
                        self.e3 = Ellipse(pos=(1350, 338), size=(25, 25))
                    # در ليستي زخيره ميشود
                    but.append(self.e3)
            # ايجاد  دکمه براي انتخاب گزينه وقي  اولين نوبت براي کاربر باشد
            if self.e2.pos[0] == 50:
                # دکمه اي ايجاد ميشود که با زدن ان  مقداري به تابعي داده ميشود
                bu.append(Button(text='[color=#000000]' + str(i) + '  [/color]', size=(25, 25), size_hint_y=0.04,
                                 size_hint_x=0.025,
                                 background_color=(0, 0, 0, 0),
                                 pos=(int(((1150 / self.l) * i) + 100), 336), markup=True))
            # ايجاد  دکمه براي انتخاب گزينه وقي  اولين نوبت براي کامپيوتر باشد
            elif self.e2.pos[0] != 50:
                # دکمه اي ايجاد ميشود که با زدن ان  مقداري به تابعي داده ميشود
                self.butt = Button(text='[color=#000000]' + str(i) + '  [/color]', size=(25, 25), size_hint_y=0.04,
                                   size_hint_x=0.025,
                                   background_color=(0, 0, 0, 0),
                                   pos=(int((((1150 / self.l) * i)) + self.e2.pos[0]), 336), markup=True)
                # اگر در انتهاي خط باشيم
                if self.butt.pos[0] > 1350:
                    self.butt = Button(text='[color=#000000]' + str(i) + '  [/color]', size=(25, 25), size_hint_y=0.04,
                                       size_hint_x=0.025,
                                       background_color=(0, 0, 0, 0),
                                       pos=(1350, 336), markup=True)
                # در ليستي زخيره ميشود مقدارها
                bu.append(self.butt)
            # دادن دستور وقتي گزينه انتخاب شد
            bu[-1].fbind('on_press', self.clock, i)
            # کليد ها را در صفحه نمايش ميدهد
            self.add_widget(bu[-1])

    # وقتي نوبت کامپيوتر است
    def g(self):
        # گرفتن مقادير نوبت حرکات
        global com, trak, turn
        # نمايش نوبت
        self.label22.text = 'computer'
        # اپديت حرکت ها
        if len(self.trak_com) == 0:
            # حرکات دوباره شارژ ميشوند
            self.trak_com = trak.copy()
        # ليستي که بر حرص کردن شاخه هاي اصلي به کار ميرود
        self.win = [0 for i in range(len(self.trak_com))]
        # با پايان بازي ايف اجرا مي شود
        if self.e.pos[0] >= 1239:
            # ترتيب دهنده صفحه
            content = BoxLayout(orientation='vertical')
            # اعلام برنده يا بازنده
            # اگر شما برنده شديد
            if int(self.label2.text) >= int(self.label4.text):
                # برچسب شما برده شديد
                content.add_widget(Label(text='you win', font_size=72))
            # اگر کامپيوتر برنده شد
            else:
                # برچسب شما برنده شديد
                content.add_widget(Label(text='you lose', font_size=72))
            # دکمه خروج
            button12 = Button(text='quit', background_normal='back.jpg')
            # بازدن دکمه از برنامه خارج ميشويد
            button12.bind(on_press=quit)
            # مرتب کننده دکمه ها
            options = BoxLayout(size=(100, 100))
            # برچسب ها
            # برچسب کاربر
            self.lab = Label(text='you: ' + self.label2.text, font_size=32)
            # اضافه کردن ان به باکس
            options.add_widget(self.lab)
            # برچسب کامپيوتر
            self.lab2 = Label(text='computer: ' + self.label4.text, font_size=32)
            # اضافه کردن ان به باکس
            options.add_widget(self.lab2)
            # براي  تنظيم فاصله
            self.lab3 = Label(text='')
            # اضافه کردن ان به باکس
            content.add_widget(self.lab3)
            # اضافه کردن ان به باکس اصلي
            content.add_widget(options)
            # براي تنظيم فاصله
            self.lab3 = Label(text='')
            # اضافه کردن ان به باکس
            content.add_widget(self.lab3)
            # اضافه کردن ان به باکس
            content.add_widget(button12)
            # اجرايpopup
            popup = Popup(title='game',
                          content=content,
                          size_hint=(None, None),
                          size=(500, 500),
                          background='137362.jpg'
                          ).open()
            # براي پايان بازي
            return 1
        # اين ايف فقط اولين بار اجرا ميشود وديگر اجرا نميشود

        if turn == 1:
            # کامپيوتر ليستي از حرکت ها  ايجاد ميکند که در ان تا ته خط رفته است
            # به دست اورد ن حداکثر حرکاتي که در خط به دون اپديت مي تواند برود
            self.tra = (trak.copy()) * 2
            print('yes')
            # به دست اوردن جمع ليست حرکات تا اخر خط
            w = sum(self.tra)
            # به دست اوردن نسبت خط  و حداکثر حرکتي که که بدون اپديت شدن مي تواند برود
            self.xp = int(self.l / w) + 1
            # اگر دقيقا با رسيدن به پايان خط حرکات تمام ميشود
            if self.l % w == 0:
                # اگر دقيقا با رسيدن به پايان خط حرکات تمام ميشود ترا دو برابر ميشود اما با کم کردن از ايکس پي يک برابر ميشود
                self.xp -= 1
            # اگر جمع حرکات  از نصف ال کمتر باشد
            elif self.l - w <= w / 2:
                # از ضريب يکي کم ميکنيم
                self.xp -= 1
                # ضريب را ضرب در حرکات ميکنيم تا  جايي که  بدون اپديت سپري شود
                self.tra *= self.xp
                # حرکات را تا جايي که به اخر خط برسد به ليست اضافه ميکنيم
                self.tra.extend(trak)
            # اگر هيچ يک درست نبودند
            else:
                # حرکات تا جايي که به اخر خط برسند به ليست اضافه ميشوند
                self.tra *= self.xp
            # اگر حرکت اول را کاربر رفنه باشديکي از حرکات بايد حذف شود
            # حرکات را تبديل به ست ميکنيم
            se = set(trak)
            # حرکات را تبديل به ست ميکنيم
            se2 = set(self.trak_me.copy())
            # تفاوت هايشان يا به عبارتي حرکت هاي انجام شده را استخراج ميکنيم
            for t in se.difference(se2):
                # حرکت ها را حذف ميکنيم
                self.tra.remove(t)
            # به اين معني است که ديگر اجرا نخواهد شد
            turn = 2
        print(self.tra, 100)
        # ليست حالت ها را تعريف ميکنيم
        Permutation = []
        # به دست اوردن حالت هاي ممکن خام
        Pu = permutations(self.tra)
        print(1)
        '''for u in Pu:
            y=1
            for j in u:
                if sum(u[:y])>=self.l:
                    i=list(u)
                    i.remove(u[y:])
                    Permutation.append(i)
                    break'''
        # تبديل به ليست ميکنيم
        for h in Pu:
            # وارد ليست ميشود
            Permutation.append(h)

        # Permutation.extend(Pu)
        print(2)
        # حذف حالت هاي غير ممکن
        for t in Permutation:
            # حرکت هاي کامپيوتر به دست ميايد
            f = t[::2]
            # ليستي تعريف ميکنيم
            h = []
            # تبديل تاپل به ليست
            for ip in f:
                # اضاف کرد به ليست
                h.append(ip)
            # تکرار به اندازه اي که به اخر خط برسد
            for poi in range(self.xp * 2):
                # حرکت هايي که با قي مانده است وارد هيف ميشود
                if len(h) < len(trak):
                    # اگر حرکت ها ي باقيمانده مطابق با حرکت هاي نکرده نباشد از حالت هاي ممکن حذف ميشود
                    if sorted(h) != sorted(self.trak_com) and len(h) != 0:
                        print('new delete3')
                        # جاگزاري صفر به جاي حالت
                        Permutation.insert(Permutation.index(t), 0)
                        # حذف حالت
                        Permutation.remove(t)
                        # شکستن حلقه
                        break
                    # به دست اوردن حرکت هاي کامپيوتر
                    f = t[1::2]
                    # ليستي تعريف ميکنيم
                    h1 = []
                    # تبديل به ليست
                    for ip in f:
                        # اضاف کرد به ليست
                        h1.append(ip)
                    # تکرار به اندازه اي که به اخر خط برسد
                    for pou in range(self.xp * 2):
                        # حرکت هايي که با قي مانده است وارد هيف ميشود
                        if len(h1) < len(trak):
                            # اگر حرکت ها ي باقيمانده مطابق با حرکت هاي نکرده نباشد از حالت هاي ممکن حذف ميشود
                            if sorted(h1) != sorted(self.trak_me) and len(h1) != 0:
                                print('new delete4')
                                # جاگزاري صفر به جاي حالت
                                Permutation.insert(Permutation.index(t), 0)
                                # حذف حالت
                                Permutation.remove(t)
                            # شکستن حلقه فر
                            break
                        # انتخاب حرکت ها از ليست به اندازه حرکت هاي داده شده
                        k = h1[-len(trak):].copy()
                        # حذف حرکت هايي که از ليست اصلي انتخاب شده بودند
                        for u in k:
                            # حذف
                            h1.remove(u)

                        print(h1, k, self.trak_me)
                        # ازمودن مطابق بودن يا نبودن حرکات در ليست خالت ها و حرکات اصلي
                        if sorted(trak) != sorted(k):
                            print('new delete2')

                            # جاگزاري صفر به جاي حالت
                            Permutation.insert(Permutation.index(t), 0)
                            # حذف حالت
                            Permutation.remove(t)
                            # شکستن حلقه فر
                            break
                    # شکستن حلقه فر اصلي براي اينکه حالت ها به پايان رسيده
                    break
                # انتخاب حرکت ها از ليست به اندازه حرکت هاي داده شده
                k = h[-len(trak):].copy()
                # حذف حرکت هايي که از ليست اصلي انتخاب شده بودند
                for u in k:
                    # حذف
                    h.remove(u)
                print(t, f, h, k, self.trak_com, 1.2)
                # ازمودن مطابق بودن يا نبودن حرکات در ليست خالت ها و حرکات اصلي
                if sorted(trak) != sorted(k):
                    print('new delete1')

                    # جاگزاري صفر به جاي حالت
                    Permutation.insert(Permutation.index(t), 0)
                    # حذف حالت
                    Permutation.remove(t)
                    # شکستن حلقه فر
                    break

                '''for j in t[::-1]:
                    if j in [self.tra[-len(trak) * i] for i in range(1, int(len(self.tra) / len(trak)) + 1)]:
                        ui += j
                        if ui != sum(trak):
                            print('new delete')
                            Permutation.insert(Permutation.index(t), 0)
                            Permutation.remove(t)
                            break
                        ui = 0
                    else:
                        ui += j'''
        print(Permutation, 666)
        # پياده سازي الگوريتم
        for tr in Permutation:
            # اگر حرکت اول باشد جايگاه 50 ميشود اما اگر حرکت اول نباشد مطابق با بازي حرکت از انجا شروع ميشود
            if self.e.pos[0] == 50:
                # مکان کاربر به 50 انتقال ميابد
                self.me_pos = 50
                # مکان کامپيوتر به 50 انتقال ميابد
                self.computer_pos = 50
            # حرکت اول را کاربر انجام داده است
            else:
                # حرکت ها مطابق بازي چيده ميشوند
                self.me_pos = self.e.pos[0]
                # حرکت ها مطابق بازي چيده ميشوند
                self.computer_pos = self.e2.pos[0]
            # امتيازها هر  بار اپديت ميشوند
            self.computer_point = 0
            # امتيازها هر  بار اپديت ميشوند
            self.me_point = 0
            # به علت حذف حالت ها وتبديل به صفر اين حالت ها ناديده گرفته ميشود
            if tr != 0:
                # مقداري به جاي ايندکس جون ايندکس به خاطره  اعداد متشابه درست عمل نميکند
                q = 0
                # فر براي هر حرکت
                for h in tr:
                    print(self.trak_com, 2)
                    print(h, tr, 45)
                    # حرکت هاي کامپيوتر
                    if q % 2 == 0:
                        # ذخيره حرکت
                        self.p123 = h
                        print(q, 23)
                        # به معناي يک مکان جلو رفتن
                        q += 1
                        print(self.computer_pos, self.me_pos)
                        #  بريک ميکند اگر به ته خط رسيد
                        if self.computer_pos >= 1249:
                            # مقاديري که اضافه هستند را پاک ميکند
                            Permutation[Permutation.index(tr)] = tr[:q]
                            # وحلقه را قطع ميکند
                            break
                        #  بريک ميکند اگر به ته خط رسيد
                        if self.me_pos >= 1249:
                            # مقاديري که اضافه هستند را پاک ميکند
                            Permutation[Permutation.index(tr)] = tr[:q - 1]
                            # وحلقه را قطع ميکند
                            break
                        # اگر اولين نوبت براي کامپيوتر باشد
                        if self.me_pos == 50:
                            # مکان کامپيوتر مشخص ميشود
                            self.computer_pos = int(((1150 / self.l) * h) + 100)
                        # اگر اولين نوبت براي کاربر باشد
                        elif self.me_pos != 50:
                            # مکان کامپيوتر مشخص ميود
                            self.computer_pos = int(((1150 / self.l) * h) + self.me_pos)
                        # اضافه کردن امتياز هاي به دست اورده
                        for i, o in zip(point, label):
                            # امتياز هاي داخل ناحيه را در نظر ميگيرد
                            if i.pos[0] in arange(self.me_pos, self.computer_pos, ):
                                # اگر امتياز داده شده نبود
                                if o.text != '':
                                    # امتياز  نقطه را به امتياز کاپيوتر اضافه ميکند
                                    print(o.text,121212)
                                    self.computer_point += int(o.text)

                        print(self.computer_point)
                    # نوبت کاربر است
                    elif q % 2 == 1:
                        print(q, 32)
                        # به معناي يک مکان جلو رفتن
                        q += 1
                        # وقتي به ته خط برسد
                        if self.me_pos >= 1249:
                            # مقاديري که اضافه هستند را پاک ميکند
                            Permutation[Permutation.index(tr)] = tr[:q - 1]
                            # وحلقه را قطع ميکند
                            break
                        # وقتي به ته خط برسد 
                        if self.computer_pos >= 1249:
                            # مقاديري که اضافه هستند را پاک ميکند
                            Permutation[Permutation.index(tr)] = tr[:q - 1]
                            # وحلقه را قطع ميکند
                            break
                        # اگر اولين نوبت براي کامپيوتر باشد 
                        if self.computer_pos == 0:
                            # مکان کاربر مشخص ميشود
                            self.me_pos = int(((1150 / self.l) * h) + 100)
                        elif self.computer_pos != 0:
                            # مکان کاربر مشخص ميشود
                            self.me_pos = int(((1150 / self.l) * h) + self.computer_pos)
                        # اضافه کردن امتياز هاي به دست اورده
                        for i, o in zip(point, label):
                            # امتياز هاي داخل ناحيه را در نظر ميگيرد
                            if i.pos[0] in arange(self.computer_pos, self.me_pos, ):
                                # امتياز  نقطه را به امتياز  کابر اضافه ميکند
                                print(o.text,121212)
                                self.me_point += int(o.text)

                        print(self.me_point)
                    # بر اساس الگوريتم اگر ايف درست شود در واقع شاخه قطع ميشود
                    # ودرواقع ليست از موارد ممکن حذف ميشود
                    if self.computer_point <= self.me_point:
                        print(3, q, len(tr))
                        # بايد هم کامپيوتر وهم حرکت کاربر رفته باشد مگر اينکه اخرين حرکت باشد
                        if q % 2 == 0 or len(tr) - q == 0:
                            print(2.2)
                            try:
                                print(h, tr)
                                # جايگزاري حالت به جاي صفر
                                Permutation.insert(Permutation.index(tr), 0)
                                print(Permutation, 55555555555)
                                # حذف حالت
                                Permutation.remove(tr)
                            # ارور احتمالي براي نبودن حالت در ليست به خاطر تکرار اين کد
                            except ValueError:
                                print('error')
                            break
        # حذف صفر هايي که در اثر حذف حالت به وجود امده اند
        while 0 in Permutation:
            print('finish')
            # حذف صفر
            Permutation.remove(0)
        # حذف حالتهاي تکراري
        Po = set(Permutation)
        # پاکسازي ليست
        Permutation.clear()
        # اضافه کردن دوباره حالت ها بدون تکرار حالت
        for ji in Po:
            # افزودن يه ليست
            Permutation.append(ji)
        # حالا به شاخه هاي اصلي ميرسيم که باتوجه به الگوريتم شاخه اي که داراي ماکسيمم حالت برد باشد انتخاب وبقيه رد ميشوند
        for you in Permutation:
            print(self.trak_com, Permutation, you)
            try:
                # اولين حرکت را از ليست انتخاب ميکنيم چون اولين حرکت  در ليست را کامپيوتر ميرود
                rt = self.trak_com.index(you[0])
                # به حالت هاي برد اضافه ميشويد
                self.win[rt] += 1
                print(self.win, 2222222222222222)
            # ارور احتمالي براي نبودن حالت در ليست به خاطر تکرار اين کد
            except ValueError:
                print('not in list')
            # براي زماني که باخت کامپيوتر حتمي است
            except IndexError:
                # تعداد حالت برد صفر است
                self.win = [0]
        # بيشترين حالت برد را انتخاب ميکند
        e = max(self.win)
        # جايگاه ان را که با جايگاه حرکات متناسب است حرکت را انتخاب ميکنند
        # جايگاه بيشترين حالت برد را گيدا ميکند
        u = self.win.index(e)
        # حرکت مربوز به بيشترين حالت برد را انتخاب ميکند
        self.q = self.trak_com[u]
        print(self.trak_com, 4)
        # به تابع زير ميقرستد
        self.clock_computer(self.q)

    # حرکت انتخاب شده به اين ارسال ميشود
    def clock_computer(self, c):
        print(self.tra, self.trak_com, 1111111111111111)
        # حرکت در صفحه نمايش داده ميشود
        self.label44.text = str(c)
        # حرکت ازليست حرکات حذف ميشود
        if c in self.tra:
            # حذف حرکت
            self.trak_com.remove(c)
        # حذف حرکت از ليست مربوط به الگوريتم
        self.tra.remove(c)
        # دايره اي سياه که نشان دهنده انتخاب است نمايش داده ميشود
        with self.canvas:
            # رنگ دايره نشاندهنده انتخاب
            Color(0, 0, 0, 1)
            # اگر اولين حرکت را کاپيوتر انجام داده باشد
            if self.e.pos[0] == 50:
                # دايره سياهي به مدت يک ثانيه نمايش داده ميشود
                self.k1 = Ellipse(pos=(int(((1150 / self.l) * c) + 100), 338), size=(25, 25))
            # اگر نه
            else:
                # دايره سياهي به مدت يک ثانيه نمايش داده ميشود
                self.k1 = Ellipse(pos=(int(((1150 / self.l) * c) + self.e.pos[0]), 338), size=(25, 25))
        # اضافه کردن امتياز کسب شده
        self.x1 = self.e2.pos[0]
        # اگر اولين حرکت را کاپيوتر انجام داده باشد
        if self.e.pos[0] == 50:
            # در نظر گرفتن  نقطه ها در ناحيه حرکت
            for i, o in zip(point, label):
                # در نظر گرفتن امتياز ها
                if i.pos[0] in arange(self.x1, ((1150 / self.l) * c) + 100):
                    print(o.text, 44445)
                    # نقاط را پاک ميکند
                    self.canvas.remove(i)
                    # اگر قبلا داده نشده باشند
                    if o.text != '':
                        # به امتيازهاي کامپيوتر اضافه ميشود
                        self.label4.text = str(int(self.label4.text) + int(o.text))
                    # امتياز انها پاکميشود
                    o.text = ''
        else:
            # در نظر گرفتن  نقطه ها در ناحيه حرکت
            for i, o in zip(point, label):
                # در نظر گرفتن امتياز ها
                if i.pos[0] in arange(self.e.pos[0], (((1150 / self.l) * c) + self.e.pos[0])):
                    # نقاط را پاک ميکند
                    self.canvas.remove(i)
                    # اگر قبلا داده نشده باشند
                    if o.text != '':
                        # به امتيازهاي کامپيوتر اضافه ميشود
                        self.label4.text = str(int(self.label4.text) + int(o.text))
                    # امتياز انها پاکميشود
                    o.text = ''
        # براي اينکه تابع قرار است هرثانيه صدا زده شود و فقط يک بار دايره سياه بايد حذف شود بنابر اين متغيري تعريف ميکنيم
        self.qlo = 1
        # براي اينکه تابع قرار است هرثانيه صدا زده شود وفقط يک بار بايد حذف اتفاق بيفتد بنابر اين متغيري تعريف ميکنيم
        self.op = 1
        # هر ثانيه دف مورد صدا زده ميشود و حرکت اتفاق مي افتد
        self.clok1 = Clock.schedule_interval(self.anim_computer, 1.0 / 60.0)

    # اين براي حرکت در راستاي خط در هر ثانيه صدا زده ميشود
    def anim_computer(self, c):
        global b, but, bu
        # نمايش دايره سياه
        if self.qlo == 1:
            # يک ثانيه براي نمايش
            time.sleep(1)
            # مقدار جديد براي اينکه دوباره اجرا نشود
            self.qlo = 2
        # براي اينکه دوباره اجرا نشود
        if self.op == 1:
            # مقدار جديد براي اينکه دوباره اجرا نشود
            self.op = 2
            # حذف دايره
            self.canvas.remove(self.k1)
        # ذخيره مکان کامپيوتر براي حرکت  چون بايد هر بار اپديت شود
        x = self.e2.pos[0]
        # حرکت مهره در راستاي خط
        if x != (int(((1150 / self.l) * self.q) + self.e.pos[0])) and self.e.pos[0] != 50:
            # حرکت درخط
            self.e2.pos = (x + 1, 338)
        # حرکت مهره در راستاي خط
        if x != (int((((1150 / self.l) * self.q)) + 100)) and self.e.pos[0] == 50:
            # حرکت درخط
            self.e2.pos = (x + 1, 338)
        # به نقطه هدف ريسد
        if x == (int((((1150 / self.l) * self.q)) + 100)) and a == 1:
            # توقف تکرار تابع
            self.clok1.cancel()
            # تغيير مقدار به خاطر  بعضي حالات خاص  در شرط ها که باعث صحيح شدن انها ميشد
            b = 2
            # نوبت کاربراست
            self.f()
        # به نقطه هدف ريسد
        if x == (int(((1150 / self.l) * self.q) + self.e.pos[0])) and self.e.pos[0] != 50:
            # توقف تکرار تابع
            self.clok1.cancel()
            # تغيير مقدار به خاطر  بعضي حالات خاص  در شرط ها که باعث صحيح شدن انها ميشد
            b = 2
            # نوبت کاربر است
            self.f()

    # حرکت انتخاب شده به اين ارسال ميشود 
    def clock(self, c, f):
        # گرفتن حرکت انتخاب شده توسط کاربر
        global choose
        choose = c
        # حرکت در صفحه نمايش داده ميشود
        self.label44.text = str(choose)
        print(54)
        # حرکت ازليست حرکات حذف ميشود
        self.trak_me.remove(choose)
        try:
            # حذف حرکت از ليست حرکات  مربوط الگوريتم
            self.tra.remove(choose)
            print(choose, 33333333333333)
        # ارور هاي احتمالي که ممکن است رخ دهد
        except AttributeError:
            pass
        # ارور هاي احتمالي که ممکن است رخ دهد
        except ValueError:
            pass
        # گزينه ها حذف ميشود
        for y in but:
            # حذف گزينه ها
            self.canvas.remove(y)
        # حذف کليد  گزينه ها
        for x in bu:
            # حذف کليد
            self.remove_widget(x)

        # دايره اي سياه که نشان دهنده انتخاب است نمايش داده ميشود
        with self.canvas:
            # رنگ دايره سياه
            Color(0, 0, 0, 1)
            # اگر اولين حرکت را کاربر کرد هباشد
            if self.e2.pos[0] == 50:
                # دايره اي سياه نمايش ميدهد
                self.k = Ellipse(pos=(int(((1150 / self.l) * choose) + 100), 338), size=(25, 25))
            else:
                # دايره اي سياه نمايش ميدهد
                self.k = Ellipse(pos=(int(((1150 / self.l) * choose) + self.e2.pos[0]), 338), size=(25, 25))
        # اضافه کردن امتياز کسب شده
        # زخيره مکان کاربر
        self.x1 = self.e.pos[0]
        # اگر اولين حرکت را کاربر کرده باشد
        if self.e2.pos[0] == 50:
            # در نظر گرفتن نقطه ها
            for i, o in zip(point, label):
                # در نظر گرفتن امتياز ها در ناحيه حرکت
                if i.pos[0] in arange(self.x1, ((1150 / self.l) * choose) + 100):
                    # حذف نقطه ها
                    self.canvas.remove(i)
                    print('1381')
                    # اگر قبلا انتخاب نشده باشد
                    if o.text != '':
                        # امتياز در نظر گرفته شده را به امتياز کاربر مي افزايد
                        self.label2.text = str(int(self.label2.text) + int(o.text))
                    # امتياز ان را پاک ميکند
                    o.text = ''
        else:
            # در نظر گرفتن نقطه ها
            for i, o in zip(point, label):
                # در نظر گرفتن امتياز ها در ناحيه حرکت
                if i.pos[0] in arange(self.e2.pos[0], (((1150 / self.l) * choose) + self.e2.pos[0])):
                    # حذف نقطه ها
                    self.canvas.remove(i)
                    # اگر قبلا انتخاب نشده باشد
                    if o.text != '':
                        # امتياز در نظر گرفته شده را به امتياز کاربر مي افزايد
                        self.label2.text = str(int(self.label2.text) + int(o.text))
                    # امتياز ان را پاک ميکند
                    o.text = ''
        # براي اينکه تابع قرار است هرثانيه صدا زده شود و فقط يک بار دايره سياه بايد حذف شود بنابر اين متغيري تعريف ميکنيم
        self.ql = 1
        # براي اينکه تابع قرار است هرثانيه صدا زده شود وفقط يک بار بايد حذف اتفاق بيفتد بنابر اين متغيري تعريف ميکنيم
        self.ki = 1
        # در هر ثانيه صدا زده ميشود
        self.clok = Clock.schedule_interval(self.anim, 1.0 / 60.0)

    # براي حرکت مهر ها است
    def anim(self, c):
        # گرفتن مقادير نوبت گزينه ها وکليد ها
        global com, bu, but, a
        # ثانيه دايره سياه را نشان ميدهد
        if self.ql == 1:
            # يک ثانيه براي نمايش
            time.sleep(1)
            # مقدار جديد براي اينکه دوباره اجرا نشود
            self.ql = 2
        # براي اينکه دوباره اجرا نشود
        if self.ki == 1:
            # مقدار جديد براي اينکه دوباره اجرا نشود
            self.ki = 2
            # حذف دايره
            self.canvas.remove(self.k)
        # حرکت مهره در خط
        # زخيره مکان کاربر براي حرکت
        x = self.e.pos[0]
        # حرکت مهره در راستاي خط
        if x != (int(((1150 / self.l) * choose) + self.e2.pos[0])) and self.e2.pos[0] != 50:
            # حرکت درخط
            self.e.pos = (x + 1, 338)
        # حرکت مهره در راستاي خط
        if x != (int(((1150 / self.l) * choose) + 100)) and self.e2.pos[0] == 50:
            # حرکت درخط
            self.e.pos = (x + 1, 338)
        # ايستادن مهره در نقطه مورد نظر
        if x == (int(((1150 / self.l) * choose) + 100)) and a == 1 and self.e2.pos[0] == 50:
            # توقف تکرار تابع
            self.clok.cancel()
            # تغيير مقدار به خاطر  بعضي حالات خاص  در شرط ها که باعث صحيح شدن انها ميشد
            a = 2
            # ارجاع نوبت به کامپيوتر
            self.g()
        if x == (int(((1150 / self.l) * choose) + self.e2.pos[0])) and self.e2.pos[0] != 50:
            # توقف تکرار تابع
            self.clok.cancel()
            # تغيير مقدار به خاطر  بعضي حالات خاص  در شرط ها که باعث صحيح شدن انها ميشد
            a = 2
            # ارجاع نوبت به کامپيوتر
            self.g()


# صفحه گرفتن اطلاعات
class Page1Screen(Screen):
    # تابع مقدار دهي
    def __init__(self, **kwargs):
        # براي ارتباط با اسکرين ها
        super(Page1Screen, self).__init__(**kwargs)
        # گرفتن مقدار ال وحرکات
        global l, trak
        # ساخت برچسب ها براي گرفتن اطلاعات
        # برچسب  گرفتن مقدار ال
        self.label2 = Label(text='enter a value for L:', font_size=36, pos_hint={'top': 1.3, 'right': 0.65})
        # اضافه کردن ان به باکس
        self.add_widget(self.label2)
        # گرفتن ال
        self.text1 = TextInput(text='L', multiline=False, size_hint_y=None, size_hint_x=None,
                               background_color=(0, 0, 0, 1), pos_hint={'top': 0.83, 'right': 0.365}, font_size=28,
                               size=(100, 50), background_normal='white', foreground_color=(1, 1, 1, 1))
        # اضافه کردن ان به باکس
        self.add_widget(self.text1)
        # برچسب  گرفتن حرکات
        self.label3 = Label(text='      enter list iterable:', font_size=36, pos_hint={'top': 1.3, 'right': 1.12})
        # اضافه کردن ان به باکس
        self.add_widget(self.label3)
        # گرفتن حرکات
        self.text2 = TextInput(text='0,0,0', multiline=False, size_hint_y=None, size_hint_x=None,
                               background_color=(0, 0, 0, 1), pos_hint={'top': 0.83, 'right': 0.925}, font_size=28,
                               size=(200, 50), background_normal='white', foreground_color=(1, 1, 1, 1))
        # اضافه کردن ان به باکس
        self.add_widget(self.text2)
        # برچسب انتخاب فايل
        self.label3 = Label(text='or choose file:', font_size=36, pos_hint={'top': 1.15, 'right': 0.9})
        # اضافه کردن ان به باکس
        self.add_widget(self.label3)
        # کليد انتخاب فايل
        self.button = Button(text='browser...', on_press=lambda a: self.screen_transition2(),
                             pos_hint={'top': 0.7, 'right': 0.6}, size_hint_y=0.1, size_hint_x=0.1,
                             background_normal='137362.jpg')
        # اضافه کردن ان به باکس
        self.add_widget(self.button)
        # کليد انتخاب نوبت براي کاربر
        self.button = Button(text='me', on_release=lambda a: self.iter1(),
                             pos_hint={'top': 0.35, 'right': 0.8}, size_hint_y=0.1, size_hint_x=0.1,
                             background_normal='137362.jpg')
        # اضافه کردن ان به باکس
        self.add_widget(self.button)
        # کليد انتخاب نوبت براي  کامپيوتر
        self.button = Button(text='computer', on_press=lambda a: self.screen_transition1(),
                             pos_hint={'top': 0.35, 'right': 0.4}, size_hint_y=0.1,
                             size_hint_x=0.1, background_normal='137362.jpg')
        # اضافه کردن ان به باکس
        self.add_widget(self.button)
        # برچسب انتخاب فايل
        self.label3 = Label(text='Which one do you start it:', font_size=36, pos_hint={'top': 0.97, 'right': 0.7})
        # اضافه کردن ان به باکس
        self.add_widget(self.label3)
        # براي تنظيم فاصله
        self.lab3 = Label(text='')
        # کليد  دادن  نقطه ها
        self.button = Button(text='enter points', on_press=lambda a: self.pop(),
                             pos_hint={'top': 0.2, 'right': 0.65}, size_hint_y=0.1,
                             size_hint_x=0.2, background_normal='137362.jpg')
        # اضافه کردن ان به باکس
        self.add_widget(self.button)

    # popup براي گرفتن مکان و امتياز نقاط
    def pop(self):
        # نظم دهنده به اشکال
        content = BoxLayout(orientation='vertical')
        # گرافيک خاص
        self.textinput1 = TextInput(text='6,-2\n3,2', background_normal='137362.jpg', size=(477, 400),
                                    size_hint=(None, None))
        # اضافه کردن ان به باکس
        content.add_widget(self.textinput1)
        # کليد ها براي لغو و ذخيره
        button_confirm = Button(text='save', size=(240, 100), size_hint=(None, None), background_normal='137362.jpg')
        # به تابع سيو ارجاع داده ميشود
        button_confirm.bind(on_press=self.save)
        # کليد لغو
        button_cancel = Button(text='Cancel', size=(237, 100), size_hint=(None, None), background_normal='137362.jpg')
        # به تابع کنسل ارجاع داده ميشود
        button_cancel.bind(on_press=self.cancel)
        # ايجاد باکس لايت براي  سازماندهي دکمه ها ووو
        options = BoxLayout()
        # اضافه کردن ان به باکس
        options.add_widget(button_cancel)
        # اضافه کردن ان به باکس
        options.add_widget(button_confirm)
        # اضافه کردن ان به باکس
        content.add_widget(options)
        # اجراي popup
        self.popup = Popup(title='game',
                           content=content,
                           size_hint=(None, None),
                           size=(500, 500),
                           background='137362.jpg'
                           )
        # اجراي popup
        self.popup.open()

    # لغو ذخيره نقاط
    def cancel(self, c):
        # بستن popup
        self.popup.dismiss()

    # ذخيره نقاط 
    def save(self, c):
        # استفاده از اين متغير ها براي زخيره امتياز ها ونقطه ها
        global point_me, index_me
        # گرفتن متن
        Dmin = self.textinput1.text.split()
        # ايجاد ليست براي جداسازي اعداد
        res = []
        # تبديل متن به اعداد
        for Dm in Dmin:
            # حذف کاما
            Dmin = Dm.replace(',', ' ')
            # پيدا کردن واضافه کردن اعداد
            res.append(re.findall('-?\d*', Dmin))
        print(res, 88888888)
        # ذخيره در مکان ها و امتيازات
        for j in res:
            # حذف اسپيس
            j.remove('')
            # حذف اسپيس
            j.remove('')
            # فر براي دسته بندي امتيازات ومکان ها
            for u in j:
                # عدد اول در ليست مکان است
                if j[0] == u:
                    # ذخيره در مکان ها
                    index_me.append(int(u))
                    print(u, 12345678910)
                # عدد دوم در ليست امتياز است
                if j[1] == u:
                    # ذخيره در امتيازات
                    point_me.append(int(u))
                    print(u, 1234567891)
        # حذف حالت هاي خاص که موجب اشتباه ميشود مانند 1و1
        for i, o in zip(index_me, point_me):
            # براي مثال 1و1
            if i == o:
                # اگر تعداد ان در مکان ها بيشتر از يک بود
                if index_me.count(i) != 1:
                    # حذف از مکان
                    index_me.remove(i)
                    # حذف از امتياز
                    point_me.remove(o)
        # خروج
        self.popup.dismiss()

    # ذخيره ال و حرکات وانتخاب نوبت 
    def iter1(self):
        # گرفتن مقادير ال حرکات ونوبت
        global l, trak, com
        # اگر فايل وارد نشده باشد شرط اجرا ميشود
        if self.text2.text != '0,0,0':
            # تبديل متن به اعداد
            self.text2.text = self.text2.text.replace(',', ' , ')
            # جداسازي اعداد
            res = re.sub('[' + string.punctuation + ']', '', self.text2.text).split()
            # ذخيره سازي
            for i in res:
                # اضافه کردن
                trak.append(int(i))
            # ذخيره ال
            l = int(self.text1.text)
        # نوبت براي کاربر ذخيره شد
        com = False
        # به صفحه بازي ارجاع داده ميشود
        self.manager.current = 'page2'

    # ذخيره ال و حرکات وانتخاب نوبت
    def screen_transition1(self):
        # گرفتن مقادير نوبت وال
        global com, l
        # اگر فايل وارد نشده باشد شرط اجرا ميشود
        if self.text2.text != '0,0,0':
            # تبديل متن به اعداد
            self.text2.text = self.text2.text.replace(',', ' , ')
            # جداسازي اعداد
            res = re.sub('[' + string.punctuation + ']', '', self.text2.text).split()
            # ذخيره سازي
            for i in res:
                # اضافه کردن اعداد
                trak.append(int(i))
            # ذخيره ال
            l = int(self.text1.text)
        # نوبت براي کاربر ذخيره شد
        com = True
        # به صفحه بازي ارجاع داده ميشود
        self.manager.current = 'page2'

    # ارجاع به صفحه انتخاب فايل
    def screen_transition2(self):
        # ارجاع به صفحه انتخاب فايل
        self.manager.current = 'page3'


# کلاس اجراي بازي
class Project(App):
    def build(self):
        # Window.clearcolor = (0.8549019607843137,0.9686274509803922, 0.6509803921568628,1)
        # حالت فول اسکرين نباشد و ترتيب صفحات بطور مطلوب باشد
        Window.fullscreen = False
        # رفتن به صفحات بعد حالت خاصينداشته باشد
        sm = ScreenManagement(transition=NoTransition())
        # بارگزاري صفحه گرفتن اطلاعات
        sm.add_widget(Page1Screen(name="page1"))
        # بارگزاري صفحه اصلي
        sm.add_widget(Page2Screen(name='page2'))
        # بارگزاري صفحه انتخاب فايل
        sm.add_widget(Page3Screen(name="page3"))

        return sm


if __name__ == "__main__":
    # صفحه در حالت ماکسيمم تنظيم باشد
    Config.set('graphics', 'resizable', True)
    # اجراي برنامه
    Project().run()
