from pygame import *
import inspect


class WPButton:
    def __init__(self, surface, x, y, w, h, text, text_font, command):
        self.surface = surface
        # главные параметры
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text

        self.getname = ""

        self.command = command

        self.click = 0

        self.text_font = text_font

        self.rect = (self.x, self.y, self.w, self.h)
        self.mpos = mouse.get_pos()

        # второстепенные параметры
        self.button_color = (0, 100, 255)
        self.hover_button_color = (0, 50, 127)
        self.roundness = 0

        # Параметры текста

        self.font_size = 20
        self.text_color = (255, 255, 255)
        try:
            self.tfont = font.Font(self.text_font, self.font_size)
        except:
            self.tfont = font.SysFont(self.text_font, self.font_size)
        self.fontRender = self.tfont.render(self.text, True, self.text_color)

    def setRectProperties(self, new_button_color, new_hover_button_color, new_roundness):
        # установка новых параметров
        self.button_color = new_button_color
        self.hover_button_color = new_hover_button_color
        self.roundness = new_roundness

    def setColor(self, new_button_color):
        self.button_color = new_button_color

    def setHoverColor(self, new_hower_button_color):
        self.hover_button_color = new_hower_button_color

    def setRoundness(self, new_roundness):
        self.roundness = new_roundness

    def setPosition(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def setSize(self, new_w, new_h):
        self.w = new_w
        self.h = new_h

    def setPositionX(self, new_x):
        self.x = new_x

    def setPositionY(self, new_y):
        self.y = new_y

    def setTextProperties(self, new_text, new_text_font, new_font_size, new_text_color):
        self.text = new_text
        self.text_font = new_text_font
        self.font_size = new_font_size
        self.text_color = new_text_color

    def setText(self, new_text):
        self.text = new_text

    def setFont(self, new_text_font):
        self.text_font = new_text_font

    def setFontSize(self, new_font_size):
        self.font_size = new_font_size

    def setTextColor(self, new_text_color):
        self.text_color = new_text_color

    def getRect(self):
        return [self.x, self.y, self.w, self.h]

    def getColor(self):
        return self.button_color

    def getPosition(self):
        return [self.x, self.y]

    def getPositionX(self):
        return self.x

    def getPositionY(self):
        return self.y

    def getRoundness(self):
        return self.roundness

    def getHoverColor(self):
        return self.hover_button_color

    def getTextFont(self):
        return self.text_font

    def getTextSize(self):
        return self.font_size

    def getTextColor(self):
        return self.text_color

    def drawButton(self, click_variable):
        self.rect = (self.x, self.y, self.w, self.h)


        self.mpos = mouse.get_pos()
        if (self.x <= self.mpos[0] <= self.x + self.w) and (self.y <= self.mpos[1] <= self.y + self.h):
            draw.rect(self.surface, self.hover_button_color, self.rect, 0, self.roundness)
            if click_variable == True:
                self.getname = ""
                try:
                    for i in inspect.currentframe().f_back.f_locals.items():
                        if id(self) == id(i[1]):
                            self.getname += i[0]
                    self.command(name=self.getname)
                except:
                    self.command()

        else:
            draw.rect(self.surface, self.button_color, self.rect, 0, self.roundness)

        self.surface.blit(self.fontRender, (
            self.x + self.w / 2 - self.fontRender.get_rect()[2] / 2,
            self.y + self.h / 2 - self.fontRender.get_rect()[3] / 2,
        ))
