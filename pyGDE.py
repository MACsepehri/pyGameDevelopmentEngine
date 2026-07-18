"""
pyGDE (python game development engine)\n
Created by MACsepehri.\n
Version 1.0.0\n
MIT license\n
More info in github: https://github.com/MACsepehri/pyGameDevelopmentEngine
"""
# requierments : pygame
# use pip install pygame | pip3 install pygame
# main classes : 'Window' , 'Object' , 'Font' , 'Text'.

# requierments
import pygame
import sys
import os
import sqlite3
import mysql.connector
from mysql.connector import Error

# init of GDE
pygame.init()
pygame.mixer.init()
pygame.font.init()

# vars
keyboard = {
    'a': pygame.K_a,
    'b': pygame.K_b,
    'c': pygame.K_c,
    'd': pygame.K_d,
    'e': pygame.K_e,
    'f': pygame.K_f,
    'g': pygame.K_g,
    'h': pygame.K_h,
    'i': pygame.K_i,
    'j': pygame.K_j,
    'k': pygame.K_k,
    'l': pygame.K_l,
    'm': pygame.K_m,
    'n': pygame.K_n,
    'o': pygame.K_o,
    'p': pygame.K_p,
    'q': pygame.K_q,
    'r': pygame.K_r,
    's': pygame.K_s,
    't': pygame.K_t,
    'u': pygame.K_u,
    'v': pygame.K_v,
    'w': pygame.K_w,
    'x': pygame.K_x,
    'y': pygame.K_y,
    'z': pygame.K_z,
    '0': pygame.K_0,
    '1': pygame.K_1,
    '2': pygame.K_2,
    '3': pygame.K_3,
    '4': pygame.K_4,
    '5': pygame.K_5,
    '6': pygame.K_6,
    '7': pygame.K_7,
    '8': pygame.K_8,
    '9': pygame.K_9,
    'up': pygame.K_UP,
    'down': pygame.K_DOWN,
    'left': pygame.K_LEFT,
    'right': pygame.K_RIGHT,
    'space': pygame.K_SPACE,
    'enter': pygame.K_RETURN,
    'escape': pygame.K_ESCAPE,
    'backspace': pygame.K_BACKSPACE,
    'tab': pygame.K_TAB,
    'capslock': pygame.K_CAPSLOCK,
    'delete': pygame.K_DELETE,
    'insert': pygame.K_INSERT,
    'home': pygame.K_HOME,
    'end': pygame.K_END,
    'pageup': pygame.K_PAGEUP,
    'pagedown': pygame.K_PAGEDOWN,
    'pause': pygame.K_PAUSE,
    'scrollock': pygame.K_SCROLLOCK,
    'printscreen': pygame.K_PRINT,
    'sysreq': pygame.K_SYSREQ,
    'break': pygame.K_BREAK,
    'menu': pygame.K_MENU,
    'power': pygame.K_POWER,
    'euro': pygame.K_EURO,
    'clear': pygame.K_CLEAR,
    'numlock': pygame.K_NUMLOCK,
    'help': pygame.K_HELP,
    'lshift': pygame.K_LSHIFT,
    'rshift': pygame.K_RSHIFT,
    'lctrl': pygame.K_LCTRL,
    'rctrl': pygame.K_RCTRL,
    'lalt': pygame.K_LALT,
    'ralt': pygame.K_RALT,
    'lmeta': pygame.K_LMETA,
    'rmeta': pygame.K_RMETA,
    'lsuper': pygame.K_LSUPER,
    'rsuper': pygame.K_RSUPER,
    'mode': pygame.K_MODE,
    '`': pygame.K_BACKQUOTE,
    '-': pygame.K_MINUS,
    '=': pygame.K_EQUALS,
    '[': pygame.K_LEFTBRACKET,
    ']': pygame.K_RIGHTBRACKET,
    '\\': pygame.K_BACKSLASH,
    ';': pygame.K_SEMICOLON,
    "'": pygame.K_QUOTE,
    ',': pygame.K_COMMA,
    '.': pygame.K_PERIOD,
    '/': pygame.K_SLASH,
    'num0': pygame.K_KP_0,
    'num1': pygame.K_KP_1,
    'num2': pygame.K_KP_2,
    'num3': pygame.K_KP_3,
    'num4': pygame.K_KP_4,
    'num5': pygame.K_KP_5,
    'num6': pygame.K_KP_6,
    'num7': pygame.K_KP_7,
    'num8': pygame.K_KP_8,
    'num9': pygame.K_KP_9,
    'numperiod': pygame.K_KP_PERIOD,
    'numdivide': pygame.K_KP_DIVIDE,
    'nummultiply': pygame.K_KP_MULTIPLY,
    'numminus': pygame.K_KP_MINUS,
    'numplus': pygame.K_KP_PLUS,
    'numenter': pygame.K_KP_ENTER,
    'numequals': pygame.K_KP_EQUALS,
}
DEBUG = False
LOGGER = False

# object class
class Object:
    def __init__(self, x=0, y=0, win_object=None, outer=True):
        self.x = x
        self.y = y
        self.win_object = win_object
        self.move_condition = []
        self.obj_type = ""
        self.img_path = None
        self.width = 0
        self.height = 0
        self.outer = outer
        self.rect_color = (0, 0, 0)
        self.image = None
        self.rect = None
        self.circle_radius = 0
        self.circle_color = (0, 0, 0)
        self.circle_thickness = 0

    def render_image(self, img_path):
        self.img_path = img_path
        if not isinstance(self.img_path, str): raise ImageNotFound(f"'{self.img_path}' image path not found.")
        try:
            self.image = pygame.image.load(img_path)
            self.obj_type = "image"
            
            if not self.outer and self.win_object:
                img_rect = self.image.get_rect()
                win_rect = self.win_object.win.get_rect()
                
                if self.x < 0:
                    self.x = 0
                elif self.x + img_rect.width > win_rect.width:
                    self.x = win_rect.width - img_rect.width
                
                if self.y < 0:
                    self.y = 0
                elif self.y + img_rect.height > win_rect.height:
                    self.y = win_rect.height - img_rect.height
            
            self.win_object.win.blit(self.image, (self.x, self.y))
        except pygame.error: raise ImageNotFound(f"'{self.img_path}' image path not found.")
        
    def draw_circle(self, color, radius, thickness=0):
        self.obj_type = "circle"
        self.circle_radius = radius
        self.circle_thickness = thickness
        self.circle_color = color
        
        self.width = radius * 2
        self.height = radius * 2
        
        if not self.outer and self.win_object:
            win_rect = self.win_object.win.get_rect()
            
            if self.x - radius < 0:
                self.x = radius
            elif self.x + radius > win_rect.width:
                self.x = win_rect.width - radius
            
            if self.y - radius < 0:
                self.y = radius
            elif self.y + radius > win_rect.height:
                self.y = win_rect.height - radius
        
        pygame.draw.circle(self.win_object.win, self.circle_color, 
                        (int(self.x), int(self.y)), self.circle_radius, self.circle_thickness)

    def draw_rect(self, width, height, color):
        self.obj_type = "rect"
        self.width = width
        self.height = height
        self.rect_color = color
        
        if not self.outer and self.win_object:
            win_rect = self.win_object.win.get_rect()
            
            if self.x < 0:
                self.x = 0
            elif self.x + self.width > win_rect.width:
                self.x = win_rect.width - self.width
            
            if self.y < 0:
                self.y = 0
            elif self.y + self.height > win_rect.height:
                self.y = win_rect.height - self.height
        
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.win_object.win, self.rect_color, self.rect)
        
    def collision(self, obj: Object):
        if self.obj_type == "rect":
            rect1 = self.rect
            rect2 = obj.rect
            return rect1.colliderect(rect2)
        elif self.obj_type == "image":
            rect1 = self.image.get_rect()
            rect2 = obj.image.get_rect()
            return rect1.colliderect(rect2)
        else: 
            raise InvalidObjectType(f"'{self.obj_type}' is invalid.")

    def get_pos(self):
        return (self.x, self.y)
    
    def add_move_condition(self, key, direction, speed, callback_action=None):
        self.move_condition.append([key, direction, speed, callback_action])

    def callback_keyboard_action(self):
        keys = pygame.key.get_pressed()
        for condition in self.move_condition:
            if keys[condition[0]]:
                if condition[1] == "right":
                    self.x += condition[2]
                    if condition[3] is not None: 
                        condition[3]()
                elif condition[1] == "left":
                    self.x -= condition[2]
                    if condition[3] is not None: 
                        condition[3]()
                elif condition[1] == "up":
                    self.y -= condition[2]
                    if condition[3] is not None: 
                        condition[3]()
                elif condition[1] == "down":
                    self.y += condition[2]
                    if condition[3] is not None: 
                        condition[3]()

        if not self.outer and self.win_object:
            win_rect = self.win_object.win.get_rect()
            
            if self.obj_type == "rect":
                if self.x < 0:
                    self.x = 0
                elif self.x + self.width > win_rect.width:
                    self.x = win_rect.width - self.width
                
                if self.y < 0:
                    self.y = 0
                elif self.y + self.height > win_rect.height:
                    self.y = win_rect.height - self.height
                
                self.rect.x = self.x
                self.rect.y = self.y
                pygame.draw.rect(self.win_object.win, self.rect_color, self.rect)
            
            elif self.obj_type == "circle":
                if self.x - self.circle_radius < 0:
                    self.x = self.circle_radius
                elif self.x + self.circle_radius > win_rect.width:
                    self.x = win_rect.width - self.circle_radius
                
                if self.y - self.circle_radius < 0:
                    self.y = self.circle_radius
                elif self.y + self.circle_radius > win_rect.height:
                    self.y = win_rect.height - self.circle_radius
                
                pygame.draw.circle(self.win_object.win, self.circle_color, 
                                (int(self.x), int(self.y)), self.circle_radius, self.circle_thickness)
            
            elif self.obj_type == "image" and self.image:
                img_rect = self.image.get_rect()
                
                if self.x < 0:
                    self.x = 0
                elif self.x + img_rect.width > win_rect.width:
                    self.x = win_rect.width - img_rect.width
                
                if self.y < 0:
                    self.y = 0
                elif self.y + img_rect.height > win_rect.height:
                    self.y = win_rect.height - img_rect.height
                
                self.win_object.win.blit(self.image, (self.x, self.y))
        else:
            if self.obj_type == "rect":
                self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
                pygame.draw.rect(self.win_object.win, self.rect_color, self.rect)
            elif self.obj_type == "circle":
                pygame.draw.circle(self.win_object.win, self.circle_color, 
                                (int(self.x), int(self.y)), self.circle_radius, self.circle_thickness)
            elif self.obj_type == "image" and self.image:
                self.win_object.win.blit(self.image, (self.x, self.y))

# objects
class Button(Object):
    def __init__(self, x, y, width, height, font=None, text="", middle=False, text_color="white", button_color="black", hover_color=(21,21,21), image=None, r=5, win_object=None):
        super().__init__(x, y, win_object)
        if middle and win_object is not None:
            screen_width = win_object.size[0]
            x = (screen_width - width) // 2
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        try:
            if type(font[0]) == str and type(font[1]) == int: self.font = Font(font[0], font[1]).font()
            else: self.font = Font("system", 32).font()
        except:
            self.font = Font("system", 32).font()
        self.text_color = text_color
        self.button_color = button_color
        self.hover_color = hover_color
        self.clicked = False
        self.visible = True
        self.middle = middle
        if image != "":
            self.image = image
        else:
            self.image = None
        self.border_radius = r

    def draw(self):
        if not self.visible:
            return
        
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(self.win_object.win, self.hover_color, self.rect, border_radius=self.border_radius)
        else:
            pygame.draw.rect(self.win_object.win, self.button_color, self.rect, border_radius=self.border_radius)

        if self.image is not None:
            text_surface = self.image
        else:
            text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        self.win_object.win.blit(text_surface, text_rect)

    def is_clicked(self):
        if not self.visible:
            return
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()[0]
        if self.rect.collidepoint(mouse_x, mouse_y) and mouse_click:
            if not self.clicked:
                self.clicked = True
                return True
        else:
            self.clicked = False
        return False
    
    def hide(self):
        self.visible = False

    def show(self):
        self.visible = True

class Font:
    def __init__(self, font=None, size=32):
        if type(font) != str: raise InvalidFont(f"'{font}' is invalid by system.")
        if type(size) != int: raise InvalidFontSize(f"'{size}' must be integer, not {type(size)}")
        self.f = font
        self.size = size
        if font.lower() == "system": self.render_font = pygame.font.SysFont(None, self.size)
        else:
            try: self.render_font = pygame.font.Font(self.f, self.size)
            except FileNotFoundError: raise FontNotFound(f"'{font}' doesn't exist or wrong path given.")
    def font(self): return self.render_font

class Text(Object):
    def __init__(self, font, text, color, middle=False, x=0, y=0, win_object=None):
        self.x = x
        self.y = y
        self.font = font
        self.text = text
        self.color = color
        self.middle = middle
        super().__init__(self.x, self.y, win_object)
    
    def draw(self):
        text_object = self.font.font().render(self.text, True, self.color)
        if self.middle and self.win_object:
            text_rect = text_object.get_rect()
            win_rect = self.win_object.win.get_rect()
            text_rect.center = win_rect.center
            self.x = text_rect.x
            self.y = text_rect.y
        self.win_object.win.blit(text_object, (self.x, self.y))

# database
class mysql_database:
    def __init__(self, host, database, user, password, port=3306):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password,
                port=self.port
            )
            self.cursor = self.connection.cursor(dictionary=True)
            return True
        except Error as e:
            print(f"Connection error: {e}")
            return False
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def write(self, table, data):
        try:
            if not self.connection or not self.connection.is_connected():
                if not self.connect():
                    return False
            
            if 'id' in data:
                set_clause = ', '.join([f"{key} = %s" for key in data.keys() if key != 'id'])
                values = [data[key] for key in data.keys() if key != 'id']
                query = f"UPDATE {table} SET {set_clause} WHERE id = %s"
                values.append(data['id'])
                self.cursor.execute(query, tuple(values))
            else:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['%s'] * len(data))
                query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
                self.cursor.execute(query, tuple(data.values()))
            
            self.connection.commit()
            return True
            
        except Error as e:
            print(f"Write error: {e}")
            if self.connection:
                self.connection.rollback()
            return False
    
    def read(self, table, conditions=None):
        try:
            if not self.connection or not self.connection.is_connected():
                if not self.connect():
                    return []
            
            query = f"SELECT * FROM {table}"
            
            if conditions:
                where_clause = ' AND '.join([f"{key} = %s" for key in conditions.keys()])
                query += f" WHERE {where_clause}"
                self.cursor.execute(query, tuple(conditions.values()))
            else:
                self.cursor.execute(query)
            
            return self.cursor.fetchall()
            
        except Error as e:
            print(f"Read error: {e}")
            return []

class sqlite_database:
    def __init__(self, db_file):
        self.db_file = db_file
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = sqlite3.connect(self.db_file)
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            return True
        except sqlite3.Error as e:
            print(f"Connection error: {e}")
            return False
    
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def write(self, table, data):
        try:
            if not self.connection:
                if not self.connect():
                    return False
            
            if 'id' in data and self._record_exists(table, data['id']):
                set_clause = ', '.join([f"{key} = ?" for key in data.keys() if key != 'id'])
                values = [data[key] for key in data.keys() if key != 'id']
                query = f"UPDATE {table} SET {set_clause} WHERE id = ?"
                values.append(data['id'])
                self.cursor.execute(query, tuple(values))
            else:
                columns = ', '.join(data.keys())
                placeholders = ', '.join(['?'] * len(data))
                query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
                self.cursor.execute(query, tuple(data.values()))
            
            self.connection.commit()
            return True
            
        except sqlite3.Error as e:
            print(f"Write error: {e}")
            if self.connection:
                self.connection.rollback()
            return False
    
    def _record_exists(self, table, id_value):
        try:
            self.cursor.execute(f"SELECT id FROM {table} WHERE id = ?", (id_value,))
            return self.cursor.fetchone() is not None
        except:
            return False
    
    def read(self, table, conditions=None):
        try:
            if not self.connection:
                if not self.connect():
                    return []
            
            query = f"SELECT * FROM {table}"
            
            if conditions:
                where_clause = ' AND '.join([f"{key} = ?" for key in conditions.keys()])
                query += f" WHERE {where_clause}"
                self.cursor.execute(query, tuple(conditions.values()))
            else:
                self.cursor.execute(query)
            
            rows = self.cursor.fetchall()
            return [dict(row) for row in rows]
            
        except sqlite3.Error as e:
            print(f"Read error: {e}")
            return []

# raise
class IconNotFoundError(BaseException): pass
class ImageNotFound(BaseException): pass
class InvalidObjectType(BaseException): pass
class InvalidRgbColor(BaseException): pass
class InvalidTextColor(BaseException): pass
class InvalidColor(BaseException): pass
class InvalidCallbackFunction(BaseException): pass
class InvalidKey(BaseException): pass
class InvalidFont(BaseException): pass
class InvalidFontSize(BaseException): pass
class FontNotFound(BaseException): pass
class InvalidFpsType(BaseException): pass

# window object
class Window:
    def __init__(self, size=None, title="GDE", fps=60, fullscreen=False, icon=None):
        self.size = size
        self.displayInfo = pygame.display.Info()
        self.title = title
        self.fullscreen = fullscreen
        self.icon = icon
        self.fps = fps
        self.clock = pygame.time.Clock()
        if not isinstance(self.fps, int): raise InvalidFpsType(f"'{type(self.fps)}' is invalid type for fps.")
        if size == None:
            self.size = (self.displayInfo.current_w, self.displayInfo.current_h)
            self.win = pygame.display.set_mode(self.size)
        else: self.win = pygame.display.set_mode(self.size)
        if not isinstance(self.title, str): pygame.display.set_caption("GDE")
        else: pygame.display.set_caption(self.title)
        if not isinstance(self.icon, str): pass
        else:
            if not os.path.exists(self.icon): raise IconNotFoundError(f"'{self.icon}' Not found in the directory.")
            else: pygame.display.set_icon(pygame.image.load(self.icon))
        self.exit_event = None
        self.update_window_func = None

    def add_event_listener(self, event_type=None, func=None):
        if event_type == None or func == None: pass
        else:
            if event_type == "quit": self.exit_event = func
            else: pass

    def quit_game(self):
        if self.exit_event != None: self.exit_event()
        else: pass
        sys.exit()

    def update_window(self, func): self.update_window_func = func

    def fill_color(self, color):
        if isinstance(color, tuple):
            try: self.win.fill(color)
            except: raise InvalidRgbColor(f"'{color}' is invalid RGB.")
        elif isinstance(color, str):
            try: self.win.fill(color)
            except: raise InvalidTextColor(f"'{color}' is invalid text color.")
        else: raise InvalidColor(f"'{color}' is invaild (No RGB | Text).")

    def press_key(self, key, callback_func):
        keys = pygame.key.get_pressed()
        try:
            if keys[key]:
                try: callback_func()
                except: raise InvalidCallbackFunction(f"'{callback_func}' function object is invalid.")
        except: raise InvalidKey(f"'{key}' is invalid.")

    def delay(self, seconds): pygame.time.delay(int(seconds * 1000))

    def run(self):
        global DEBUG, LOGGER

        try:
            if DEBUG: open("window_object_debuger.log", "x")
        except: pass
        while True:
            for event in pygame.event.get():
                if DEBUG:
                    with open("window_object_debuger.log", "a") as file:
                        file.write(f"Event: {event}\n")
                if LOGGER: print(f"Event: {event}")
                if event.type == pygame.QUIT:
                    self.quit_game()

            if self.update_window_func != None: self.update_window_func()
            else: pass
            pygame.display.update()
            self.clock.tick(self.fps)
