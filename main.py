import kivy
kivy.require("1.9.1")
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty, NumericProperty, StringProperty, BooleanProperty
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.scrollview import ScrollView
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.label import Label
import xml.etree.ElementTree as ET
from kivy.effects.scroll import ScrollEffect

from calculate import calculate

current_god = ''
skills_num = 0
skills_with_states = []
double_diamonds = False
special_int_input = False
god_class = ""

def elements_number(lista):
    number = 0
    for i in lista:
        number = number + 1
    return number

def approximate_number_to_int(number):
        if number - int(number) >= 0.5:
            number = int(number) + 1
            return number
        elif number - int(number) < 0.5:
            number = int(number)
            return number

def editar_numero_de_imagen(palabra_a_editar, nuevo_indice):
        nueva_palabra = ""
        numero_de_caracteres = 0
        numero_de_caracter = 1
        for j in palabra_a_editar:
            if numero_de_caracter != 13:
                nueva_palabra = nueva_palabra + j
            if numero_de_caracter == 13:
                nueva_palabra = nueva_palabra + nuevo_indice
                nueva_palabra = nueva_palabra + ".png"
                return nueva_palabra
            numero_de_caracter = numero_de_caracter + 1

class Info_Screen(Screen):
    pass

cidh_mode = 0
class Main_Screen(Screen):
    def turn_off_cidh_and_go(self):
        global cidh_mode
        cidh_mode = 0
        self.manager.get_screen("class selection").check_cidh_mode()
        self.manager.current = "class selection"
    def turn_on_cidh_and_go(self):
        global cidh_mode
        cidh_mode = 1
        self.manager.get_screen("class selection").check_cidh_mode()
        self.manager.current = "class selection"

class god_info_Screen(Screen):
    helptext = StringProperty('')
    toScreen = StringProperty('')
    def update_text(self):
        global current_god
        current_info_screen = "%s info" % (current_god)
        filename = current_god + ".txt"
        f = open(filename, "r")
        self.helptext = f.read()

        if current_god == "fafnir" or current_god == "terra":
            self.toScreen = current_god
        else:
            self.toScreen = "normal god screen"

class ClickableImage(ButtonBehavior, Image):
    pass

class Class_Selection_Screen(Screen):
    guardian_btn = ObjectProperty
    hunter_btn = ObjectProperty
    warrior_btn = ObjectProperty
    mage_btn = ObjectProperty
    assassin_btn = ObjectProperty

    def initialize_next_screen_and_go(self, class_selected):
        global god_class
        god_class = class_selected
        options = { "guardian": 0 , "hunter": 1, "warrior": 2,
                    "mage": 3, "assassin": 4 }
        self.manager.get_screen("god selection screen").initialize(options[class_selected])
        self.manager.current = "god selection screen"
    def check_cidh_mode(self):
        global cidh_mode
        if cidh_mode == 1:
            self.guardian_btn.opacity = 0.3
            self.guardian_btn.disabled = True
            self.hunter_btn.opacity = 0.3
            self.hunter_btn.disabled = True
            self.warrior_btn.opacity = 0.3
            self.warrior_btn.disabled = True
            self.mage_btn.opacity = 0.3
            self.mage_btn.disabled = True
            self.assassin_btn.opacity = 1
            self.assassin_btn.disabled = False
        else:
            self.guardian_btn.opacity = 1
            self.guardian_btn.disabled = False
            self.hunter_btn.opacity = 1
            self.hunter_btn.disabled = False
            self.warrior_btn.opacity = 1
            self.warrior_btn.disabled = False
            self.mage_btn.opacity = 1
            self.mage_btn.disabled = False
            self.assassin_btn.opacity = 1
            self.assassin_btn.disabled = False
    def reset_pages_and_go_back(self):
        global classes_pages_numbers
        classes_pages_numbers = [1, 1, 1, 1, 1]
        self.manager.current = "main screen"
            
        
class_option_number = 0
classes_pages_numbers = [1, 1, 1, 1, 1]
class God_Selection_Screen(Screen):
    next_button = ObjectProperty()
    previous_button = ObjectProperty()

    guardians = [ "ares", "artio", "athena", "bacchus", "cabrakan",
                   "cerberus", "fafnir", "ganesha", "geb",
                   "khepri", "kumbhakarna", "kuzenbo", "sobek", "sylvanus",
                   "terra", "xing-tian", "ymir" ]
    hunters = [ "ah-muzen-cab", "anhur", "apollo", "artemis", "cernunnos",
                 "chernobog", "chiron", "cupid", "hachiman",
                 "hou-yi", "izanami", "jing-wei", "medusa", "neith",
                 "rama", "skadi", "ullr", "xbalanque" ]
    warriors = [ "achilles", "amaterasu", "bellona", "chaac", "cu-chulainn",
                  "erlang-shen", "guan-yu", "hercules", "nike",
                  "odin", "osiris", "sun-wukong", "tyr", "vamana" ]
    mages = [ "agni", "ah-puch", "anubis", "ao-kuang", "aphrodite",
               "baron-samedi", "change", "chronos", "discordia",
               "freya", "hades", "he-bo", "hel", "isis",
               "janus", "kukulkan", "nox", "nu-wa",
               "poseidon", "ra", "raijin", "scylla", "sol",
               "the-morrigan", "thoth", "vulcan", "zeus",
               "zhong-kui" ]
    assassins = [ "arachne", "awilix", "bakasura", "bastet", "camazotz",
                   "da-ji", "fenrir", "hun-batz", "kali",
                   "loki", "mercury", "ne-zha", "nemesis", "pele",
                   "ratatoskr", "ravana", "serqet", "susano",
                   "thanatos", "thor" ]
    deleter_assassins = [ "loki", "nothing", "nothing",
                          "nothing", "nothing", "nothing",
                          "nothing", "nothing", "nothing" ]

    button_positions = [ [0.123, 0.7], [0.391, 0.7], [0.659, 0.7],
                         [0.123, 0.508], [0.391, 0.508], [0.659, 0.508],
                         [0.123, 0.316], [0.391, 0.316], [0.659, 0.316] ]
    
    list_of_lists = [guardians, hunters, warriors, mages, assassins,
                     deleter_assassins]

    btn1 = ClickableImage(pos_hint = { "x": button_positions[0][0] , "y": button_positions[0][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn2 = ClickableImage(pos_hint = { "x": button_positions[1][0] , "y": button_positions[1][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn3 = ClickableImage(pos_hint = { "x": button_positions[2][0] , "y": button_positions[2][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn4 = ClickableImage(pos_hint = { "x": button_positions[3][0] , "y": button_positions[3][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn5 = ClickableImage(pos_hint = { "x": button_positions[4][0] , "y": button_positions[4][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn6 = ClickableImage(pos_hint = { "x": button_positions[5][0] , "y": button_positions[5][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn7 = ClickableImage(pos_hint = { "x": button_positions[6][0] , "y": button_positions[6][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn8 = ClickableImage(pos_hint = { "x": button_positions[7][0] , "y": button_positions[7][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn9 = ClickableImage(pos_hint = { "x": button_positions[8][0] , "y": button_positions[8][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

    initialized = False

    def initialize(self, option):
        global classes_pages_numbers
        
        global cidh_mode
        if option == 4 and cidh_mode == 1:
            option = 5
        
        selected_list = self.list_of_lists[option]
        if option == 5:
            page_number = 1
        else:
            page_number = classes_pages_numbers[option]
        elements_number = 0
        
        global class_option_number
        class_option_number = option
        
        for x in selected_list:
            elements_number = elements_number + 1

        number_of_pages = elements_number/9 + 1
        if elements_number == 9 or elements_number == 18 or elements_number == 27 or elements_number == 36 or elements_number == 45:
            number_of_pages = number_of_pages - 1
            
        if self.initialized == False:
            layout = FloatLayout()
            i = 0
            page_number = 1
            for button in self.buttons:
                if i == 9:
                    break
                button.source = selected_list[i] + ".png"
                button.name = selected_list[i]
                button.bind(on_press=self.go_to_god_or_combo)
                layout.add_widget(button)
                i = i + 1
            self.add_widget(layout)
            self.initialized = True
        elif self.initialized == True:
            if page_number == 1:
                i = 8
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god_or_combo)
                    if i == 0:
                        break
                    i = i - 1
            if page_number == 2:
                i = 17
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god_or_combo)
                    if i == 9:
                        break
                    i = i - 1
            if page_number == 3:
                i = 26
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god_or_combo)
                    if i == 18:
                        break
                    i = i - 1
            if page_number == 4:
                i = 35
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god_or_combo)
                    if i == 27:
                        break
                    i = i - 1

        if page_number == 1:
            self.previous_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.previous_button.pos_hint = { "x": 0.0 , "y": 0.0 }
        if page_number == number_of_pages:
            self.next_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.next_button.pos_hint = { "x": 0.8 , "y": 0.0 }
                
    def go_to_god_or_combo(self, btn):
        if btn.name != "nothing":
            global current_god
            current_god = btn.name
            global cidh_mode
            if ((current_god == "fafnir" or current_god == "terra") and
                 cidh_mode == 0):
                self.manager.get_screen("god info screen").update_text()
                self.manager.current = current_god
            elif ((current_god != "fafnir" and current_god != "terra") and
                   cidh_mode == 0):
                self.manager.get_screen("normal god screen").initialize()
                self.manager.current = "normal god screen"
            elif ((current_god != "fafnir" and current_god != "terra") and
                   cidh_mode == 1):
                self.manager.get_screen("combo screen").initialize()
                self.manager.current = "combo screen"

    def next_page(self):
        global classes_pages_numbers
        global class_option_number
        classes_pages_numbers[class_option_number] = classes_pages_numbers[class_option_number] + 1
        self.initialize(class_option_number)

    def previous_page(self):
        global classes_pages_numbers
        global class_option_number
        classes_pages_numbers[class_option_number] = classes_pages_numbers[class_option_number] - 1
        self.initialize(class_option_number)
        
    def change_global_variables(self, name, sk_num, sk_states, double_state, special_input):
        global current_god
        global skills_num
        global skills_with_states
        global double_diamonds
        global special_int_input
        current_god = name
        skills_num = sk_num
        skills_with_states = sk_states
        double_diamonds = double_state
        special_int_input = special_input

selected_combo = 0
class Combo_Screen(Screen):
    combos_number = { "loki": 2 }
    initialized = 0
    def initialize(self):
        if self.initialized == 0:
            global current_god
            self.rows_number = self.combos_number[current_god]
    
            layout = FloatLayout()
            scroll = ScrollView(size_hint=(0.9, 0.75), pos_hint={"x": 0.05, "y": 0.1},
                                    effect_cls = ScrollEffect)
            grid = GridLayout( size_hint = (1,None), col_default_width = 50, row_default_height = 100,
                                   cols = 1, rows = self.rows_number )
            self.buttons = []
            for i in range(0, self.rows_number):
                current_picture = current_god + "_combo_" + str(i + 1) + ".png"
                self.buttons.append(ClickableImage( size_hint=(1,1), pos_hint={"x":0.0, "y":0.0},
                                                    source=current_picture, id=str(i+1)))
                self.buttons[i].bind(on_press=self.select_combo_and_go)
                grid.add_widget(self.buttons[i])

            grid.bind(minimum_height=grid.setter('height'))

            scroll.add_widget(grid)
            layout.add_widget(scroll)
            self.add_widget(layout)

    def select_combo_and_go(self, btn_object):
        global selected_combo
        selected_combo = btn_object.id
        self.manager.get_screen("build screen").reset_items_to_zero()
        self.manager.get_screen("ranks screen").initialize()
        self.manager.current = "ranks screen"

class Ranks_Screen(Screen):
    initialized = 0
    images = []
    ranks = { "loki_1": [1, 2, 3, 3, 4, 3, 3, 2, 4, 3, 2, 2, 4, 2, 1, 1, 4, 1, 1, 4],
              "loki_2": [1, 2, 3, 2, 4, 2, 2, 1, 4, 2, 1, 1, 4, 1, 3, 3, 4, 3, 3, 4] }
    
    def initialize(self):
        if self.initialized == 0:
            global current_god
            global selected_combo
    
            layout = FloatLayout()
            self.add_widget(layout)
            
            scroll = ScrollView(size_hint=(0.9, 0.6), pos_hint={"x": 0.05, "y": 0.25}, effect_cls = ScrollEffect)
            self.children[0].add_widget(scroll)
            
            grid = GridLayout( size_hint = (1,None), col_default_width = 50, row_default_height = 100, cols = 4, rows = 10)
            grid.bind(minimum_height=grid.setter('height'))
            self.children[0].children[0].add_widget(grid)
            
            self.put_items_in_the_grid()

            self.initialized = 1
            
        elif self.initialized == 1:
            self.children[0].children[0].children[0].clear_widgets()
            self.images = []
            self.put_items_in_the_grid()

    def put_items_in_the_grid(self):
        j = -1
        l = 9
        global current_god
        global selected_combo
        for i in range(0, 40):
                if i/2 == i/2.0:
                    for k in range(0, 10):
                        if i == [0,4,8,12,16,20,24,28,32,36][k]:
                            current_picture = str([1,2,3,4,5,6,7,8,9,10][k]) + ".png"
                            break
                        elif i == [2,6,10,14,18,22,26,30,34,38][k]:
                            current_picture = str([11,12,13,14,15,16,17,18,19,20][k]) + ".png"
                            break
                elif i/2 != i/2.0:
                    for k in range(0, 10):
                        if i == [1,5,9,13,17,21,25,29,33,37][k]:
                            j = j + 1
                            current_picture = current_god + "_sk_" + str(self.ranks[current_god + "_" + str(selected_combo)][j]) + ".png"
                            break
                        elif i == [3,7,11,15,19,23,27,31,35,39][k]:
                            l = l + 1
                            current_picture = current_god + "_sk_" + str(self.ranks[current_god + "_" + str(selected_combo)][l]) + ".png"
                            break
                            
                self.images.append(Image( size_hint=(1,1), pos_hint={"x":0.0, "y":0.0},
                                          source=current_picture, keep_ratio=False,
                                          allow_strech=True ))
                self.children[0].children[0].children[0].add_widget(self.images[i])

    def reset_screen_and_go_back(self):
        self.children[0].children[0].children[0].clear_widgets()
        self.images = []
        self.manager.current = "combo screen"

class Item():
    name_id = ""
    power = 0
    cost = 0

    power2 = 0
    mana = 0
    power_states = []
    mana_states = []
    ba_flat_buff = 0
    ba_flat_buff_states = []
    mana_to_power_percent = []
    can_change = []
    mana_to_power_percent = 0
    mages_blessing_buff = 0
    hydras_multiplier_buff = 0
    hydras_affected_bas = 0
    hydras_affected_bas_states = []
    heartseeker_buff = 0
    heartseeker_states = []
    crusher_flat_buff = 0
    crusher_buff_based_on_power = 0
    poly_buff_based_on_power = 0
    polys_affected_bas = 0
    polys_affected_bas_states = []
    p_prot = 0
    p_prot_states = []
    power_per_charge = 0
    mana_per_charge = 0
    penetration = 0
    penetration_states = []
    percent_penetration = 0
    percent_penetration_protections_scaling = []
    max_percent_penetration = 0
    executioner_reduction = 0
    qins_bonus = 0
    qins_health_scaling = []
    qins_max_bonus = 0
    crit_chance = 0
    crit_chance_states = []
    malice_bonus = 0
    scs_bonus = 0
    aura_penetration = 0
    
    state = 1
    max_state = 1
    
    def __init__(self, name_id_p, power_p, cost_p):
        self.name_id = name_id_p
        self.power = power_p
        self.cost = cost_p
    def update_power(self):
        self.power = self.power_states[self.state - 1]
    def update_mana(self):
        self.mana = self.mana_states[self.state - 1]
    def update_mana_to_power_percent(self):
        self.mana_to_power_percent = self.mana_to_power_percent_states[self.state - 1]
    def update_ba_flat_buff(self):
        self.ba_flat_buff = self.ba_flat_buff_states[self.state - 1]
    def update_hydras_affected_bas(self):
        self.hydras_affected_bas = self.hydras_affected_bas_states[self.state - 1]
    def update_heartseeker_buff(self):
        self.heartseeker_buff = self.heartseeker_buff_states[self.state - 1]
    def update_polys_affected_bas(self):
        self.polys_affected_bas = self.polys_affected_bas_states[self.state - 1]
    def update_p_prot(self):
        self.p_prot = self.p_prot_states[self.state - 1]
    def update_penetration(self):
        self.penetration = self.penetration_states[self.state - 1]
    def update_crit_chance(self):
        self.crit_chance = self.crit_chance_states[self.state - 1]

attackers_blessing = Item("x_sta1_1", 20, 700)
attackers_blessing.power2 = 25
attackers_blessing.max_state = 2
attackers_blessing.penetration_states = [0, 10]
attackers_blessing.can_change = ["penetration"]
mages_blessing = Item("x_sta2", 0, 700)
mages_blessing.mages_blessing_buff = 25
hunters_blessing = Item("x_sta3_1", 0, 700)
hunters_blessing.ba_flat_buff = 15
hunters_blessing.max_state = 2
hunters_blessing.ba_flat_buff_states = [15, 30]
hunters_blessing.can_change = ["ba_flat_buff"]

mask = Item("x_mas1", 0, 500)
    #fighters_mask = Item("x_mas1", 20, 1200)
    #fighters_mask.power2 = 50
messengers_mask = Item("x_mas3", 10, 1200)
messengers_mask.power2 = 30
    #rangdas_mask = Item("x_mas3", 35, 2500)
    #rangdas_mask.power2 = 70
    #rangdas_mask.ability_damage_buff = 0.15
    #rangdas_mask.basic_attacks_buff_based_on_power = 0.2
bumbas_mask = Item("x_mas5", 20, 2500)
bumbas_mask.power2 = 50
bumbas_mask.total_damage_debuff = 0.1
lonos_mask = Item("x_mas6", 0, 2300)
lonos_mask.total_damage_debuff = 0.2

    #potion_of_physical_might = Item("p_pot1", 30, 500)
    #potion_of_physical_might.ability_damage_buff_based_on_power = 0.15
    #potion_of_magical_might = Item("m_pot1", 60, 500)
    #elixir_of_power = Item("x_eli1", 0, 3000)
    #elixir_of_power.power_buff_percent = 0.25
    #damage_camp_buff = Item("x_buf1", 5, 0)
    #damage_camp_buff.power2 = 10
    #damage_camp_buff.total_damage_buff_percent = 0.2
    #attack_speed_camp_buff = Item("x_buf2", 0, 0)
    #attack_speed_camp_buff.physical_basic_attacks_buff = 12
    #attack_speed_camp_buff.magical_basic_attacks_buff = 15
    #shadow_of_apophis = Item("x_buf3", 30, 0)
    #shadow_of_apophis.power2 = 50
    #fire_giants_might = Item("x_buf4", 50, 0)
    #fire_giants_might.power2 = 70


breastplate = Item("d_bre1", 0, 600)
breastplate.p_prot = 20
silver_breastplate = Item("d_bre2", 0, 1050)
silver_breastplate.mana = 200
silver_breastplate.p_prot = 35
hide_of_the_nemean_lion = Item("d_bre3", 0, 2200)
hide_of_the_nemean_lion.mana = 200
hide_of_the_nemean_lion.p_prot = 70
breastplate_of_valor = Item("d_bre4", 0, 2300)
breastplate_of_valor.mana = 300
breastplate_of_valor.p_prot = 65
spectral_armor = Item("d_bre5", 0, 2100)
spectral_armor.mana = 300
spectral_armor.p_prot = 60

cloak = Item("d_clo1", 0, 650)
cloak.p_prot = 10
cloak_of_concentration = Item("d_clo2", 0, 1500)
cloak_of_concentration.p_prot = 30
spirit_robe = Item("d_clo3", 0, 2500)
spirit_robe.p_prot = 40
mantle_of_discord = Item("d_clo4", 0, 2900)
mantle_of_discord.p_prot = 60
clerics_cloak = Item("d_clo5", 0, 1150)
clerics_cloak.p_prot = 10
magis_cloak = Item("d_clo6", 0, 2150)
magis_cloak.p_prot = 15
armored_cloak = Item("d_clo7", 0, 1550)
armored_cloak.mana = 125
armored_cloak.p_prot = 25
hide_of_the_urchin = Item("d_clo8", 0, 2450)
hide_of_the_urchin.mana = 250
hide_of_the_urchin.p_prot = 30
hide_of_the_urchin.can_change = ["p_prot"]
hide_of_the_urchin.p_prot_states = [30, 51]
hide_of_the_urchin.max_state = 2

gauntlet_of_thebes = Item("d_glo1", 0, 2400)
gauntlet_of_thebes.can_change = ["p_prot"]
gauntlet_of_thebes.p_prot_states = [0, 60]
gauntlet_of_thebes.max_state = 2

iron_mail = Item("d_mai1", 0, 650)
iron_mail.p_prot = 10
steel_mail = Item("d_mai2", 0, 1400)
steel_mail.p_prot = 20
sovereignty = Item("d_mai3", 0, 2100)
sovereignty.p_prot = 60
mystical_mail = Item("d_mai4", 0, 2700)
mystical_mail.p_prot = 40
midgardian_mail = Item("d_mai5", 0, 2300)
midgardian_mail.p_prot = 40
emperors_armor = Item("d_mai6", 0, 2000)
emperors_armor.p_prot = 40
    

acorn_of_swiftness = Item("p_aco1", 10, 900)
acorn_of_yggdrasil = Item("p_aco2", 50, 1600)

combat_boots = Item("p_boo1", 10, 900)
    #combat_boots.movement_speed = 0.12
warrior_tabi = Item("p_boo2", 40, 1600)
    #warrior_tabi.movement_speed = 0.18
ninja_tabi = Item("p_boo3", 20, 1550)
ninja_tabi.mana = 100
    #ninja_tabi.movement_speed = 0.18
reinforced_greaves = Item("p_boo4", 10, 1550)
    #reinforced_greaves.movement_speed = 0.18
talaria_boots = Item("p_boo5", 20, 1600)
    #talaria_boots.movement_speed = 0.25

morningstar = Item("p_mor1", 10, 550)
charged_morningstar = Item("p_mor2", 20, 1200)
charged_morningstar.mana = 150
transcendence = Item("p_mor3", 35, 2600)
transcendence.mana = 300
transcendence.mana_per_charge = 15
transcendence.mana_to_power_percent = 0.03
transcendence.max_state = 4
transcendence.mana_states = [300, (300 + transcendence.mana_per_charge * 20), (300 + transcendence.mana_per_charge * 40), (300 + transcendence.mana_per_charge * 50)]
transcendence.can_change = ["mana"]
hydras_star = Item("p_mor4", 20, 1200)
hydras_star.hydras_multiplier_buff = 1.1
hydras_star.hydras_affected_bas = 0
hydras_star.can_change = ["hydras_affected_bas"]
hydras_star.max_state = 4
hydras_star.hydras_affected_bas_states = [0, 1, 2, 3]
hydras_lament = Item("p_mor5", 40, 2150)
hydras_lament.hydras_multiplier_buff = 1.5
hydras_lament.hydras_affected_bas = 0
hydras_lament.can_change = ["hydras_affected_bas"]
hydras_lament.max_state = 4
hydras_lament.hydras_affected_bas_states = [0, 1, 2, 3]
    
mace = Item("p_mac1", 15, 700)
heavy_mace = Item("p_mac2", 25, 1550)
heavy_mace.penetration = 10
brawlers_beat_stick = Item("p_mac3", 40, 2350)
brawlers_beat_stick.penetration = 15
jotunns_wrath = Item("p_mac4", 40, 2350)
jotunns_wrath.mana = 150
jotunns_wrath.penetration = 10
the_crusher = Item("p_mac5", 30, 2400)
the_crusher.crusher_flat_buff = 20
the_crusher.crusher_buff_based_on_power = 0.15
the_crusher.penetration = 15
warriors_bane = Item("p_mac6", 20, 1500)
warriors_bane.percent_penetration = 0.15
titans_bane = Item("p_mac7", 30, 2300)
titans_bane.percent_penetration = 0.15
titans_bane.percent_penetration_protections_scaling = [65, 200]
titans_bane.max_percent_penetration = 0.4

balanced_blade = Item("p_lig1", 15, 1250)
the_executioner = Item("p_lig2", 30, 2350)
the_executioner.executioner_reduction = 0.12
qins_sais = Item("p_lig3", 40, 2700)
qins_sais.qins_bonus = 0.03
qins_sais.qins_health_scaling = [2000, 2750]
qins_sais.qins_max_bonus = 0.05

hidden_dagger = Item("p_hid1", 10, 700)
hidden_dagger.crit_chance = 0.05
short_sword = Item("p_hid2", 20, 1500)
short_sword.crit_chance = 0.1
deathbringer = Item("p_hid3", 40, 3000)
deathbringer.crit_chance = 0.25
deathbringer.db_crit_bonus = 0.3
rage = Item("p_hid4", 20, 2400)
rage.crit_chance = 0.3
rage.can_change = ["crit_chance"]
rage.crit_chance_states = [0.3, 0.32, 0.34, 0.36, 0.38, 0.4]
malice = Item("p_hid5", 40, 3000)
malice.crit_chance = 0.25
malice.malice_bonus = 0.35

shuriken = Item("p_shu1", 10, 650)
eight_pointed_shuriken = Item("p_shu2", 15, 1500)
eight_pointed_shuriken.crit_chance = 0.1
poisoned_star = Item("p_shu3", 20, 2400)
poisoned_star.crit_chance = 0.2
wind_demon = Item("p_shu4", 30, 2700)
wind_demon.crit_chance = 0.2

spiked_gauntlet = Item("p_spi1", 5, 600)
cursed_gauntlet = Item("p_spi2", 20, 1400)
devourers_gauntlet = Item("p_spi3", 30, 2300)
devourers_gauntlet.power_per_charge = 0.5
devourers_gauntlet.max_state = 4
devourers_gauntlet.power_states = [30, (30 + devourers_gauntlet.power_per_charge * 25),
                                       (30 + devourers_gauntlet.power_per_charge * 50), (30 + devourers_gauntlet.power_per_charge * 70)]
devourers_gauntlet.can_change = ["power"]
bloodforge = Item("p_spi4", 75, 2800)
bound_gauntlet = Item("p_spi5", 15, 1050)
bound_gauntlet.mana = 75
soul_eater = Item("p_spi6", 40, 2300)
soul_eater.mana = 200
soul_eater.max_state = 2
soul_eater.power_states = [40, 60]
soul_eater.can_change = ["power"]

katana = Item("p_kat1", 10, 700)
    #katana.movement_speed = 0.05
thousand_fold_blade = Item("p_kat2", 20, 1300)
    #thousand_fold_blade.movement_speed = 0.08
hastened_katana = Item("p_kat3", 25, 2200)
    #hastened_katana.movement_speed = 0.1
heartseeker = Item("p_kat4", 30, 2300)
heartseeker.mana = 200
    #heartseeker.movement_speed = 0.1
heartseeker.max_state = 2
heartseeker.heartseeker_buff = 0.0
heartseeker.heartseeker_buff_states = [0.0, 0.8]
heartseeker.can_change = ["heartseeker_buff"]
stone_cutting_sword = Item("p_kat5", 50, 2500)
stone_cutting_sword.scs_bonus = 10
    #stone_cutting_sword.movement_speed = 0.1
masamune = Item("p_kat6", 50, 2500)
    #masamune.movement_speed = 0.1
golden_blade = Item("p_kat7", 30, 2200)

round_shield = Item("p_rou1", 10, 650)
round_shield.p_prot = 5
spiked_shield = Item("p_rou2", 20, 1600)
spiked_shield.p_prot = 30
spiked_shield.aura_penetration = 8
void_shield = Item("p_rou3", 20, 2600)
void_shield.p_prot = 50
void_shield.aura_penetration = 20
tower_shield = Item("p_rou4", 20, 1150)
tower_shield.p_prot = 15
shifters_shield = Item("p_rou5", 70, 2400)
shifters_shield.p_prot = 15
shifters_shield.can_change = ["power", "p_prot"]
shifters_shield.max_state = 2
shifters_shield.power_states = [70, 35] 
shifters_shield.p_prot_states = [15, 50]
gladiators_shield = Item("p_rou6", 20, 1700)
gladiators_shield.p_prot = 30
berserkers_shield = Item("p_rou7", 25, 1050)
berserkers_shield.p_prot = 15

enchanted_buckler = Item("p_enc1", 10, 650)
warded_shield = Item("p_enc2", 15, 1400)
runic_shield = Item("p_enc3", 35, 2150)
ancile = Item("p_enc4", 40, 2000)

hunters_bow = Item("p_bow1", 10, 1200)
atalantas_bow = Item("p_bow2", 30, 2200)
silverbranch_bow = Item("p_bow3", 20, 2200)

cudgel = Item("p_cud1", 5, 650)
heavy_hammer = Item("p_cud2", 20, 1350)
frostbound_hammer = Item("p_cud3", 25, 2300)
runeforged_hammer = Item("p_cud4", 40, 2300)
runeforged_hammer.runeforged_bonus = 0.15
shillelagh = Item("p_cud5", 10, 1500)
shillelagh.mana = 100
blackthorn_hammer = Item("p_cud6", 25, 2200)
blackthorn_hammer.mana = 200
    

magic_shoes = Item("m_sho1", 20, 900)
shoes_of_the_magi = Item("m_sho2", 55, 1600)
shoes_of_focus = Item("m_sho3", 55, 1550)
shoes_of_focus.mana = 250
reinforced_shoes = Item("m_sho4", 20, 1550)
travelers_shoes = Item("m_sho5", 25, 1600)

spellbook = Item("m_spe1", 20, 650)
book_of_souls = Item("m_spe2", 65, 1350)
book_of_souls.mana = 125
book_of_thoth = Item("m_spe3", 80, 2800)
book_of_thoth.mana = 250
book_of_thoth.mana_per_charge = 10
book_of_thoth.mana_to_power_percent = 0.03
book_of_thoth.max_state = 4
book_of_thoth.mana_states = [250, (250 + book_of_thoth.mana_per_charge * 25),
                                 (250 + book_of_thoth.mana_per_charge * 50), (250 + book_of_thoth.mana_per_charge * 75)]
book_of_thoth.mana_to_power_percent_states = [0.03, 0.03, 0.03, 0.05]
book_of_thoth.can_change = ["mana", "mana_to_power_percent"]
polynomicon = Item("m_spe4", 75, 2300)
polynomicon.mana = 300
polynomicon.poly_buff_based_on_power = 0.75
polynomicon.polys_affected_bas = 0
polynomicon.max_state = 4
polynomicon.polys_affected_bas_states = [0, 1, 2, 3]
polynomicon.can_change = ["polys_affected_bas"]
    #polynomicon.lifesteal = 0.12
soul_reaver = Item("m_spe5", 130, 2750)
soul_reaver.mana = 300
book_of_the_dead = Item("m_spe6", 100, 2600)
book_of_the_dead.mana = 200

magic_focus = Item("m_foc1", 25, 650)
enchanted_spear = Item("m_foc2", 30, 1400)
divine_ruin = Item("m_foc3", 80, 2300)
spear_of_the_magus = Item("m_foc4", 65, 2300)
spear_of_desolation = Item("m_foc5", 100, 2600)
spell_focus = Item("m_foc6", 45, 1500)
obsidian_shard = Item("m_foc7", 60, 2150)
    
uncommon_staff = Item("m_unc1", 15, 650)
fortified_scepter = Item("m_unc2", 50, 1350)
gem_of_isolation = Item("m_unc3", 90, 2700)
ethereal_staff = Item("m_unc4", 90, 2700)
rod_of_healing = Item("m_unc5", 45, 1500)
rod_of_asclepius = Item("m_unc6", 90, 2600)
sorcerers_staff = Item("m_unc7", 30, 1350)
sorcerers_staff.mana = 100
warlocks_staff = Item("m_unc8", 65, 2650)
warlocks_staff.mana = 200
warlocks_staff.power_per_charge = 0.5
warlocks_staff.max_state = 4
warlocks_staff.power_states = [65, (65 + warlocks_staff.power_per_charge * 40),
                                   (65 + warlocks_staff.power_per_charge * 80), (65 + warlocks_staff.power_per_charge * 100)]
warlocks_staff.can_change = ["power"]

tiny_trinket = Item("m_tin1", 20, 550)
    #tiny_trinket.lifesteal = 0.06
talon_trinket = Item("m_tin2", 60, 1400)
talon_trinket.mana = 100
    #talon_trinket.lifesteal = 0.08
bancrofts_talon = Item("m_tin3", 100, 2500)
bancrofts_talon.mana = 150
    #bancrofts_talon.lifesteal = 0.15
bancrofts_talon.max_state = 4
bancrofts_talon.power_states = [ 100, 125, 150, 200 ]
bancrofts_talon.can_change = ["power"]
typhons_fang = Item("m_tin4", 80, 2800)
typhons_fang.mana = 200
    #typhons_fang.lifesteal = 0.1
enchanted_trinket = Item("m_tin5", 30, 1100)
    #enchanted_trinket.lifesteal = 0.12
soul_gem = Item("m_tin6", 65, 2300)
    #soul_gem.lifesteal = 0.12
    #soul_gem.max_state = 2
    #soul_gem.extra_power_based_damage_percent = 0.3
pythagorems_piece = Item("m_tin7", 70, 2300)
    #pythagorems_piece.lifesteal = 0.24

lost_artifact = Item("m_los1", 20, 550)
restored_artifact = Item("m_los2", 50, 1600)
rod_of_tahuti = Item("m_los3", 150, 300)
chronos_pendant = Item("m_los4", 90, 2800)
doom_orb = Item("m_los5", 70, 1700)
doom_orb.mana = 200
    

emerald_ring = Item("m_eme1", 20, 600)
enchanted_ring = Item("m_eme2", 45, 1200)
demonic_grip = Item("m_eme3", 65, 2150)
hastened_ring = Item("m_eme4", 50, 2300)
shamans_ring = Item("m_eme5", 100, 2400)
    #shamans_ring.max_state = 2
telkhines_ring = Item("m_eme6", 90, 2700)
    #telkhines_ring.basic_attacks_buff = 10
    #telkhines_ring.basic_attacks_buff_based_on_power = 0.1

imperial_helmet = Item("m_imp1", 10, 600)
jade_mountain_helm = Item("m_imp2", 20, 1200)
celestial_legion_helm = Item("m_imp3", 60, 2050)
jade_emperors_crown = Item("m_imp4", 20, 2150)
lotus_crown = Item("m_imp5", 30, 2050)
dinasty_plate_helm = Item("m_imp6", 45, 1700)

druid_stone = Item("m_dru1", 10, 600)
ward_stone = Item("m_dru2", 20, 1350)
void_stone = Item("m_dru3", 20, 2150)
sages_stone = Item("m_dru4", 40, 1400)
stone_of_fal = Item("m_dru5", 70, 2300)
stone_of_binding = Item("m_dru6", 20, 1700)

nothing = Item("nothing", 0, 0)

item_objects = { "nothing.png": nothing,
                     "item_x_sta1_1.png": attackers_blessing, "item_x_sta2.png": mages_blessing,
                     "item_x_sta3_1.png": hunters_blessing,
                     #"item_x_mas1.png": fighters_mask, "item_x_mas2.png": messengers_mask,
                     #"item_x_mas3.png": rangdas_mask, "item_x_mas4.png": lonos_mask,
                     #"item_x_mas5.png": bumbas_mask,

                     #"item_p_pot1.png": potion_of_physical_might, "item_m_pot1.png": potion_of_magical_might,
                     #"item_x_eli1.png": elixir_of_power, "item_x_buf1.png": damage_camp_buff,
                     #"item_x_buf2.png": attack_speed_camp_buff, "item_x_buf3.png": shadow_of_apophis,
                     #"item_x_buf4.png": fire_giants_might,

                     "item_d_bre1.png": breastplate, "item_d_bre2.png": silver_breastplate,
                     "item_d_bre3.png": hide_of_the_nemean_lion, "item_d_bre4.png": breastplate_of_valor,
                     "item_d_bre5.png": spectral_armor,
                     "item_d_clo1.png": cloak, "item_d_clo2.png": cloak_of_concentration,
                     "item_d_clo3.png": spirit_robe, "item_d_clo4.png": mantle_of_discord,
                     "item_d_clo5.png": clerics_cloak, "item_d_clo6.png": magis_cloak,
                     "item_d_clo7.png": armored_cloak, "item_d_clo8_1.png": hide_of_the_urchin,
                     "item_d_glo1_1.png": gauntlet_of_thebes,
                     "item_d_mai1.png": iron_mail, "item_d_mai2.png": steel_mail,
                     "item_d_mai3.png": sovereignty, "item_d_mai4.png": mystical_mail,
                     "item_d_mai5.png": midgardian_mail, "item_d_mai6.png": emperors_armor,

                     "item_p_aco1.png": acorn_of_swiftness, "item_p_aco2.png": acorn_of_yggdrasil,
                     "item_p_boo1.png": combat_boots, "item_p_boo2.png": warrior_tabi,
                     "item_p_boo3.png": ninja_tabi, "item_p_boo4.png": reinforced_greaves,
                     "item_p_boo5.png": talaria_boots,
                     "item_p_mor1.png": morningstar, "item_p_mor2.png": charged_morningstar,
                     "item_p_mor3_1.png": transcendence, "item_p_mor4_1.png": hydras_star,
                     "item_p_mor5_1.png": hydras_lament,
                     "item_p_mac1.png": mace, "item_p_mac2.png": heavy_mace,
                     "item_p_mac3.png": brawlers_beat_stick, "item_p_mac4.png": jotunns_wrath,
                     "item_p_mac5.png": the_crusher, "item_p_mac6.png": warriors_bane,
                     "item_p_mac7.png": titans_bane,
                     "item_p_lig1.png": balanced_blade, "item_p_lig2.png": the_executioner,
                     "item_p_lig3.png": qins_sais,
                     "item_p_hid1.png": hidden_dagger, "item_p_hid2.png": short_sword,
                     "item_p_hid3.png": deathbringer, "item_p_hid4.png": rage,
                     "item_p_hid5.png": malice,
                     "item_p_shu1.png": shuriken, "item_p_shu2.png": eight_pointed_shuriken,
                     "item_p_shu3.png": poisoned_star, "item_p_shu4.png": wind_demon,
                     "item_p_spi1.png": spiked_gauntlet, "item_p_spi2.png": cursed_gauntlet,
                     "item_p_spi3_1.png": devourers_gauntlet, "item_p_spi4.png": bloodforge,
                     "item_p_spi5.png": bound_gauntlet,  "item_p_spi6_1.png": soul_eater,
                     "item_p_kat1.png": katana, "item_p_kat2.png": thousand_fold_blade,
                     "item_p_kat3.png": hastened_katana, "item_p_kat4_1.png": heartseeker,
                     "item_p_kat5.png": stone_cutting_sword, "item_p_kat6.png": masamune,
                     "item_p_kat7.png": golden_blade,
                     "item_p_rou1.png": round_shield, "item_p_rou2.png": spiked_shield,
                     "item_p_rou3.png": void_shield, "item_p_rou4.png": tower_shield,
                     "item_p_rou5_1.png": shifters_shield, "item_p_rou6.png": gladiators_shield,
                     "item_p_rou7.png": berserkers_shield,
                     "item_p_enc1.png": enchanted_buckler, "item_p_enc2.png": warded_shield,
                     "item_p_enc3.png": runic_shield, "item_p_enc4.png": ancile,
                     "item_p_bow1.png": hunters_bow, "item_p_bow2.png": atalantas_bow,
                     "item_p_bow3.png": silverbranch_bow,
                     "item_p_cud1.png": cudgel, "item_p_cud2.png": heavy_hammer,
                     "item_p_cud3.png": frostbound_hammer, "item_p_cud4.png": runeforged_hammer,
                     "item_p_cud5.png": shillelagh, "item_p_cud6.png": blackthorn_hammer,
                     
                     "item_m_sho1.png": magic_shoes, "item_m_sho2.png": shoes_of_the_magi,
                     "item_m_sho3.png": shoes_of_focus, "item_m_sho4.png": reinforced_shoes,
                     "item_m_sho5.png": travelers_shoes,
                     "item_m_spe1.png": spellbook, "item_m_spe2.png": book_of_souls,
                     "item_m_spe3_1.png": book_of_thoth, "item_m_spe4_1.png": polynomicon,
                     "item_m_spe5.png": soul_reaver, "item_m_spe6.png": book_of_the_dead,
                     "item_m_foc1.png": magic_focus, "item_m_foc2.png": enchanted_spear,
                     "item_m_foc3.png": divine_ruin, "item_m_foc4.png": spear_of_the_magus,
                     "item_m_foc5.png": spear_of_desolation, "item_m_foc6.png": spell_focus,
                     "item_m_foc7.png": obsidian_shard,
                     "item_m_unc1.png": uncommon_staff, "item_m_unc2.png": fortified_scepter,
                     "item_m_unc3.png": gem_of_isolation, "item_m_unc4.png": ethereal_staff,
                     "item_m_unc5.png": rod_of_healing, "item_m_unc6.png": rod_of_asclepius,
                     "item_m_unc7.png": sorcerers_staff, "item_m_unc8_1.png": warlocks_staff,
                     "item_m_tin1.png": tiny_trinket, "item_m_tin2.png": talon_trinket,
                     "item_m_tin3_1.png": bancrofts_talon, "item_m_tin4.png": typhons_fang,
                     "item_m_tin5.png": enchanted_trinket, "item_m_tin6_1.png": soul_gem,
                     "item_m_tin7.png": pythagorems_piece,
                     "item_m_los1.png": lost_artifact, "item_m_los2.png": restored_artifact,
                     "item_m_los3.png": rod_of_tahuti, "item_m_los4.png": chronos_pendant,
                     "item_m_los5.png": doom_orb,
                     "item_m_eme1.png": emerald_ring, "item_m_eme2.png": enchanted_ring,
                     "item_m_eme3.png": demonic_grip, "item_m_eme4.png": hastened_ring,
                     "item_m_eme5_1.png": shamans_ring, "item_m_eme6.png": telkhines_ring,
                     "item_m_imp1.png": imperial_helmet, "item_m_imp2.png": jade_mountain_helm,
                     "item_m_imp3.png": celestial_legion_helm, "item_m_imp4.png": jade_emperors_crown,
                     "item_m_imp5.png": lotus_crown, "item_m_imp6.png": dinasty_plate_helm,
                     "item_m_dru1.png": druid_stone, "item_m_dru2.png": ward_stone,
                     "item_m_dru3.png": void_stone, "item_m_dru4.png": sages_stone,
                     "item_m_dru5.png": stone_of_fal, "item_m_dru6.png": stone_of_binding }

items_trees = { "d_bre2": ["item_d_bre1.png", "item_d_bre2.png"],
                "d_bre3": ["item_d_bre1.png", "item_d_bre2.png", "item_d_bre3.png"],
                "d_bre4": ["item_d_bre1.png", "item_d_bre2.png", "item_d_bre4.png"],
                "d_bre5": ["item_d_bre1.png", "item_d_bre2.png", "item_d_bre5.png"],
                "d_clo2": ["item_d_clo1.png", "item_d_clo2.png"],
                "d_clo3": ["item_d_clo1.png", "item_d_clo2.png", "item_d_clo3.png"],
                "d_clo4": ["item_d_clo1.png", "item_d_clo2.png", "item_d_clo4.png"],
                "d_clo5": ["item_d_clo1.png", "item_d_clo5.png"],
                "d_clo6": ["item_d_clo1.png", "item_d_clo5.png", "item_d_clo6.png"],
                "d_clo7": ["item_d_clo1.png", "item_d_clo7.png"],
                "d_clo8": ["item_d_clo1.png", "item_d_clo7.png", "item_d_clo8_1.png"],
                "d_mai2": ["item_d_mai1.png", "item_d_mai2.png"],
                "d_mai3": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai3.png"],
                "d_mai4": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai4.png"],
                "d_mai5": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai5.png"],
                "d_mai6": ["item_d_mai1.png", "item_d_mai2.png", "item_d_mai6.png"],
                "p_aco2": ["item_p_aco1.png", "item_p_aco2.png"],
                "p_boo2": ["item_p_boo1.png", "item_p_boo2.png"],
                "p_boo3": ["item_p_boo1.png", "item_p_boo3.png"],
                "p_boo4": ["item_p_boo1.png", "item_p_boo4.png"],
                "p_boo5": ["item_p_boo1.png", "item_p_boo5.png"],
                "p_mor2": ["item_p_mor1.png", "item_p_mor2.png"],
                "p_mor3": ["item_p_mor1.png", "item_p_mor2.png", "item_p_mor3_1.png"],
                "p_mor4": ["item_p_mor1.png", "item_p_mor4_1.png"],
                "p_mor5": ["item_p_mor1.png", "item_p_mor4_1.png", "item_p_mor5_1.png"],
                "p_mac2": ["item_p_mac1.png", "item_p_mac2.png"],
                "p_mac3": ["item_p_mac1.png", "item_p_mac2.png", "item_p_mac3.png"],
                "p_mac4": ["item_p_mac1.png", "item_p_mac2.png", "item_p_mac4.png"],
                "p_mac5": ["item_p_mac1.png", "item_p_mac2.png", "item_p_mac5.png"],
                "p_mac6": ["item_p_mac1.png", "item_p_mac6.png"],
                "p_mac7": ["item_p_mac1.png", "item_p_mac6.png", "item_p_mac7.png"],
                "p_lig2": ["item_p_lig1.png", "item_p_lig2.png"],
                "p_lig3": ["item_p_lig1.png", "item_p_lig3.png"],
                "p_hid2": ["item_p_hid1.png", "item_p_hid2.png"],
                "p_hid3": ["item_p_hid1.png", "item_p_hid2.png", "item_p_hid3.png"],
                "p_hid4": ["item_p_hid1.png", "item_p_hid2.png", "item_p_hid4.png"],
                "p_hid5": ["item_p_hid1.png", "item_p_hid2.png", "item_p_hid5.png"],
                "p_shu2": ["item_p_shu1.png", "item_p_shu2.png"],
                "p_shu3": ["item_p_shu1.png", "item_p_shu2.png", "item_p_shu3.png"],
                "p_shu4": ["item_p_shu1.png", "item_p_shu2.png", "item_p_shu4.png"],
                "p_spi2": ["item_p_spi1.png", "item_p_spi2.png"],
                "p_spi3": ["item_p_spi1.png", "item_p_spi2.png", "item_p_spi3_1.png"],
                "p_spi4": ["item_p_spi1.png", "item_p_spi2.png", "item_p_spi4.png"],
                "p_spi5": ["item_p_spi1.png", "item_p_spi5.png"],
                "p_spi6": ["item_p_spi1.png", "item_p_spi5.png", "item_p_spi6_1.png"],
                "p_kat2": ["item_p_kat1.png", "item_p_kat2.png"],
                "p_kat3": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat3.png"],
                "p_kat4": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat4_1.png"],
                "p_kat5": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat5.png"],
                "p_kat6": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat6.png"],
                "p_kat7": ["item_p_kat1.png", "item_p_kat2.png", "item_p_kat7.png"],
                "p_rou2": ["item_p_rou1.png", "item_p_rou2.png"],
                "p_rou3": ["item_p_rou1.png", "item_p_rou2.png", "item_p_rou3.png"],
                "p_rou4": ["item_p_rou1.png", "item_p_rou4.png"],
                "p_rou5": ["item_p_rou1.png", "item_p_rou4.png", "item_p_rou5_1.png"],
                "p_rou6": ["item_p_rou1.png", "item_p_rou6.png"],
                "p_rou7": ["item_p_rou1.png", "item_p_rou7.png"],
                "p_enc2": ["item_p_enc1.png", "item_p_enc2.png"],
                "p_enc3": ["item_p_enc1.png", "item_p_enc2.png", "item_p_enc3.png"],
                "p_enc4": ["item_p_enc1.png", "item_p_enc4.png"],
                "p_bow2": ["item_p_bow1.png", "item_p_bow2.png"],
                "p_bow3": ["item_p_bow1.png", "item_p_bow3.png"],
                "p_cud2": ["item_p_cud1.png", "item_p_cud2.png"],
                "p_cud3": ["item_p_cud1.png", "item_p_cud2.png", "item_p_cud3.png"],
                "p_cud4": ["item_p_cud1.png", "item_p_cud2.png", "item_p_cud4.png"],
                "p_cud5": ["item_p_cud1.png", "item_p_cud5.png"],
                "p_cud6": ["item_p_cud1.png", "item_p_cud5.png", "item_p_cud6.png"],
                "m_sho2": ["item_m_sho1.png", "item_m_sho2.png"],
                "m_sho3": ["item_m_sho1.png", "item_m_sho3.png"],
                "m_sho4": ["item_m_sho1.png", "item_m_sho4.png"],
                "m_sho5": ["item_m_sho1.png", "item_m_sho5.png"],
                "m_spe2": ["item_m_spe1.png", "item_m_spe2.png"],
                "m_spe3": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe3.png"],
                "m_spe4": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe4.png"],
                "m_spe5": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe5.png"],
                "m_spe6": ["item_m_spe1.png", "item_m_spe2.png", "item_m_spe6.png"],
                "m_foc2": ["item_m_foc1.png", "item_m_foc2.png"],
                "m_foc3": ["item_m_foc1.png", "item_m_foc2.png", "item_m_foc3.png"],
                "m_foc4": ["item_m_foc1.png", "item_m_foc2.png", "item_m_foc4.png"],
                "m_foc5": ["item_m_foc1.png", "item_m_foc2.png", "item_m_foc5.png"],
                "m_foc6": ["item_m_foc1.png", "item_m_foc6.png"],
                "m_foc7": ["item_m_foc1.png", "item_m_foc6.png", "item_m_foc7.png"],
                "m_unc2": ["item_m_unc1.png", "item_m_unc2.png"],
                "m_unc3": ["item_m_unc1.png", "item_m_unc2.png", "item_m_unc3.png"],
                "m_unc4": ["item_m_unc1.png", "item_m_unc2.png", "item_m_unc4.png"],
                "m_unc5": ["item_m_unc1.png", "item_m_unc5.png"],
                "m_unc6": ["item_m_unc1.png", "item_m_unc5.png", "item_m_unc6.png"],
                "m_unc7": ["item_m_unc1.png", "item_m_unc7.png"],
                "m_unc8": ["item_m_unc1.png", "item_m_unc7.png", "item_m_unc8_1.png"],
                "m_tin2": ["item_m_tin1.png", "item_m_tin2.png"],
                "m_tin3": ["item_m_tin1.png", "item_m_tin2.png", "item_m_tin3_1.png"],
                "m_tin4": ["item_m_tin1.png", "item_m_tin2.png", "item_m_tin4.png"],
                "m_tin5": ["item_m_tin1.png", "item_m_tin5.png"],
                "m_tin6": ["item_m_tin1.png", "item_m_tin6_1.png"],
                "m_tin7": ["item_m_tin1.png", "item_m_tin7.png"],
                "m_los2": ["item_m_los1.png", "item_m_los2.png"],
                "m_los3": ["item_m_los1.png", "item_m_los2.png", "item_m_los3.png"],
                "m_los4": ["item_m_los1.png", "item_m_los2.png", "item_m_los4.png"],
                "m_los5": ["item_m_los1.png", "item_m_los5.png"],
                "m_eme2": ["item_m_eme1.png", "item_m_eme2.png"],
                "m_eme3": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme3.png"],
                "m_eme4": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme4.png"],
                "m_eme5": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme5_1.png"],
                "m_eme6": ["item_m_eme1.png", "item_m_eme2.png", "item_m_eme6.png"],
                "m_imp2": ["item_m_imp1.png", "item_m_imp2.png"],
                "m_imp3": ["item_m_imp1.png", "item_m_imp2.png", "item_m_imp3.png"],
                "m_imp4": ["item_m_imp1.png", "item_m_imp2.png", "item_m_imp4.png"],
                "m_imp5": ["item_m_imp1.png", "item_m_imp2.png", "item_m_imp5.png"],
                "m_imp6": ["item_m_imp1.png", "item_m_imp6.png"],
                "m_dru2": ["item_m_dru1.png", "item_m_dru2.png"],
                "m_dru3": ["item_m_dru1.png", "item_m_dru2.png", "item_m_dru3.png"],
                "m_dru4": ["item_m_dru1.png", "item_m_dru4.png"],
                "m_dru5": ["item_m_dru1.png", "item_m_dru4.png", "item_m_dru5.png"],
                "m_dru6": ["item_m_dru1.png", "item_m_dru6.png"],
                "x_mas3": ["item_x_mas1.png", "item_x_mas3.png"],
                "x_mas5": ["item_x_mas1.png", "item_x_mas3.png", "item_x_mas5.png"],
                "x_mas6": ["item_x_mas1.png", "item_x_mas6.png"]}
                

class Build_Screen(Screen):
    slot1 = ObjectProperty()
    slot2 = ObjectProperty()
    slot3 = ObjectProperty()
    slot4 = ObjectProperty()
    slot5 = ObjectProperty()
    slot6 = ObjectProperty()

    list_of_slots = [slot1, slot2, slot3,
                     slot4, slot5, slot6]

    total_damage_label = ObjectProperty()
    total_power_label = ObjectProperty()
    total_gold_label = ObjectProperty()
    total_mana_label = ObjectProperty()

    remove_item = ObjectProperty()
    edit_item = ObjectProperty()

    background1 = ObjectProperty()
    background2 = ObjectProperty()

    def select_item_slot_and_do_something(self, slot_number):
        global current_item_slot
        current_item_slot = slot_number
        list_of_slots = [self.slot1, self.slot2, self.slot3,
                         self.slot4, self.slot5, self.slot6]

        if self.remove_mode_state == 1:
            if list_of_slots[current_item_slot - 1].source != "nothing.png":
                self.quitar_item()
            elif list_of_slots[current_item_slot - 1].source == "nothing.png":
                self.toggle_remove_mode()
        elif self.edit_mode_state == 1:
            self.editar_item()
        else:
            self.initialize_screen2_and_go() 

    def quitar_item(self):
        global current_item_slot
        global selected_objects
        if current_item_slot == 1:
            self.slot1.source = "1st.png"
            selected_objects[0] = nothing
        if current_item_slot == 2:
            self.slot2.source = "2nd.png"
            selected_objects[1] = nothing
        if current_item_slot == 3:
            self.slot3.source = "3rd.png"
            selected_objects[2] = nothing
        if current_item_slot == 4:
            self.slot4.source = "4th.png"
            selected_objects[3] = nothing
        if current_item_slot == 5:
            self.slot5.source = "5th.png"
            selected_objects[4] = nothing
        if current_item_slot == 6:
            self.slot6.source = "6th.png"
            selected_objects[5] = nothing
        global selected_items 
        selected_items = [self.slot1.source, self.slot2.source, self.slot3.source,
                          self.slot4.source, self.slot5.source, self.slot6.source]
        self.update_labels()

    def editar_item(self):
        global current_item_slot
        global selected_objects
        if current_item_slot == 1:
            if selected_objects[0].max_state != 1:
                selected_objects[0].state = selected_objects[0].state + 1
                if selected_objects[0].state > selected_objects[0].max_state:
                    selected_objects[0].state = 1
                self.slot1.source = self.editar_numero_de_imagen(self.slot1.source, str(selected_objects[0].state))
        if current_item_slot == 2:
            if selected_objects[1].max_state != 1:
                selected_objects[1].state = selected_objects[1].state + 1
                if selected_objects[1].state > selected_objects[1].max_state:
                    selected_objects[1].state = 1
                self.slot2.source = self.editar_numero_de_imagen(self.slot2.source, str(selected_objects[1].state))
        if current_item_slot == 3:
            if selected_objects[2].max_state != 1:
                selected_objects[2].state = selected_objects[2].state + 1
                if selected_objects[2].state > selected_objects[2].max_state:
                    selected_objects[2].state = 1
                self.slot3.source = self.editar_numero_de_imagen(self.slot3.source, str(selected_objects[2].state))
        if current_item_slot == 4:
            if selected_objects[3].max_state != 1:
                selected_objects[3].state = selected_objects[3].state + 1
                if selected_objects[3].state > selected_objects[3].max_state:
                    selected_objects[3].state = 1
                self.slot4.source = self.editar_numero_de_imagen(self.slot4.source, str(selected_objects[3].state))
        if current_item_slot == 5:
            if selected_objects[4].max_state != 1:
                selected_objects[4].state = selected_objects[4].state + 1
                if selected_objects[4].state > selected_objects[4].max_state:
                    selected_objects[4].state = 1
                self.slot5.source = self.editar_numero_de_imagen(self.slot5.source, str(selected_objects[4].state))
        if current_item_slot == 6:
            if selected_objects[5].max_state != 1:
                selected_objects[5].state = selected_objects[5].state + 1
                if selected_objects[5].state > selected_objects[5].max_state:
                    selected_objects[5].state = 1
                self.slot6.source = self.editar_numero_de_imagen(self.slot6.source, str(selected_objects[5].state))

        self.update_labels()

    def initialize_screen2_and_go(self):
        self.manager.get_screen("items screen 2").initialize()
        self.manager.current = "items screen 2"

    def editar_numero_de_imagen(self, palabra_a_editar, nuevo_indice):
        nueva_palabra = ""
        numero_de_caracteres = 0
        numero_de_caracter = 1
        for j in palabra_a_editar:
            if numero_de_caracter != 13:
                nueva_palabra = nueva_palabra + j
            if numero_de_caracter == 13:
                nueva_palabra = nueva_palabra + nuevo_indice
                nueva_palabra = nueva_palabra + ".png"
                return nueva_palabra
            numero_de_caracter = numero_de_caracter + 1

    def reset_items_to_zero(self):
        self.slot1.source = "1st.png"
        self.slot2.source = "2nd.png"
        self.slot3.source = "3rd.png"
        self.slot4.source = "4th.png"
        self.slot5.source = "5th.png"
        self.slot6.source = "6th.png"
        global selected_items
        selected_items = ["a", "a", "a",
                          "a", "a", "a"]
        global selected_objects
        selected_objects = [Item("", 0, 0), Item("", 0, 0), Item("", 0, 0),
                            Item("", 0, 0), Item("", 0, 0), Item("", 0, 0)]
        self.update_labels()

    
    def update_items(self):
        global current_item_slot
        global selected_item_picture
        global selected_objects
        global item_objects
        
        slots = [self.slot1, self.slot2, self.slot3,
                 self.slot4, self.slot5, self.slot6]
        
        for i in range(1, 7):
            if current_item_slot == i:
                slots[i-1].source = selected_item_picture
                selected_objects[i-1] = item_objects[selected_item_picture]

        global selected_items
        selected_items = [self.slot1.source, self.slot2.source, self.slot3.source,
                          self.slot4.source, self.slot5.source, self.slot6.source]

    item1_saved_state = 1
    item2_saved_state = 1
    item3_saved_state = 1
    item4_saved_state = 1
    item5_saved_state = 1
    item6_saved_state = 1
    total_power = 0
    mana_to_power_percent = 0
    initialized = 0
    
    def update_labels(self):
        global selected_objects
        item1 = selected_objects[0]
        item2 = selected_objects[1]
        item3 = selected_objects[2]
        item4 = selected_objects[3]
        item5 = selected_objects[4]
        item6 = selected_objects[5]
        items = [item1, item2, item3, item4, item5, item6]

        global god_class

        items_saved_states = [self.item1_saved_state, self.item2_saved_state,
                              self.item3_saved_state, self.item4_saved_state,
                              self.item5_saved_state, self.item6_saved_state]

        item1_power = 0
        item2_power = 0
        item3_power = 0
        item4_power = 0
        item5_power = 0
        item6_power = 0
        items_power = [item1_power, item2_power, item3_power,
                       item4_power, item5_power, item6_power]

        for i in range(0, 6):
            if items[i].state != items_saved_states[i]:
                items_saved_states[i] = items[i].state
                for changeable in items[i].can_change:
                    if changeable == "power":
                        items[i].update_power()
                    if changeable == "mana":
                        items[i].update_mana()
                    if changeable == "mana_to_power_percent":
                        items[i].update_mana_to_power_percent()
                    if changeable == "ba_flat_buff":
                        items[i].update_ba_flat_buff()
                    if changeable == "hydras_affected_bas":
                        items[i].update_hydras_affected_bas()
                    if changeable == "heartseeker_buff":
                        items[i].update_heartseeker_buff()
                    if changeable == "polys_affected_bas":
                        items[i].update_polys_affected_bas()
                    if changeable == "p_prot":
                        items[i].update_p_prot()
            if items[i].power2 != 0 and (god_class=="mage" or god_class=="guardian"):
                items_power[i] = items[i].power2
            else:
                items_power[i] = items[i].power

        selected_objects[0] = item1
        selected_objects[1] = item2
        selected_objects[2] = item3
        selected_objects[3] = item4
        selected_objects[4] = item5
        selected_objects[5] = item6

        global base_mana
        global mana_per_level
        global base_p_prot
        global p_prot_per_level
        global god_level

        total_ba_flat_buff = item1.ba_flat_buff + item2.ba_flat_buff + item3.ba_flat_buff + item4.ba_flat_buff + item5.ba_flat_buff + item6.ba_flat_buff
        global ba_flat_buff
        ba_flat_buff = total_ba_flat_buff

        total_mages_blessing_buff = item1.mages_blessing_buff + item2.mages_blessing_buff + item3.mages_blessing_buff + item4.mages_blessing_buff + item5.mages_blessing_buff + item6.mages_blessing_buff
        global mages_blessing_buff
        mages_blessing_buff = total_mages_blessing_buff

        total_hydras_multiplier_buff = item1.hydras_multiplier_buff + item2.hydras_multiplier_buff + item3.hydras_multiplier_buff + item4.hydras_multiplier_buff + item5.hydras_multiplier_buff + item6.hydras_multiplier_buff
        global hydras_multiplier_buff
        hydras_multiplier_buff = total_hydras_multiplier_buff

        total_hydras_affected_bas = item1.hydras_affected_bas + item2.hydras_affected_bas + item3.hydras_affected_bas + item4.hydras_affected_bas + item5.hydras_affected_bas + item6.hydras_affected_bas
        global hydras_affected_bas
        hydras_affected_bas = total_hydras_affected_bas

        total_heartseeker_buff = item1.heartseeker_buff + item2.heartseeker_buff + item3.heartseeker_buff + item4.heartseeker_buff + item5.heartseeker_buff + item6.heartseeker_buff
        global heartseeker_buff
        heartseeker_buff = total_heartseeker_buff

        total_crusher_flat_buff = item1.crusher_flat_buff + item2.crusher_flat_buff + item3.crusher_flat_buff + item4.crusher_flat_buff + item5.crusher_flat_buff + item6.crusher_flat_buff
        global crusher_flat_buff
        crusher_flat_buff = total_crusher_flat_buff

        total_crusher_buff_based_on_power = item1.crusher_buff_based_on_power + item2.crusher_buff_based_on_power + item3.crusher_buff_based_on_power + item4.crusher_buff_based_on_power + item5.crusher_buff_based_on_power + item6.crusher_buff_based_on_power
        global crusher_buff_based_on_power
        crusher_buff_based_on_power = total_crusher_buff_based_on_power

        total_poly_buff_based_on_power = item1.poly_buff_based_on_power + item2.poly_buff_based_on_power + item3.poly_buff_based_on_power + item4.poly_buff_based_on_power + item5.poly_buff_based_on_power + item6.poly_buff_based_on_power
        global poly_buff_based_on_power
        poly_buff_based_on_power = total_poly_buff_based_on_power

        total_polys_affected_bas = item1.polys_affected_bas + item2.polys_affected_bas + item3.polys_affected_bas + item4.polys_affected_bas + item5.polys_affected_bas + item6.polys_affected_bas
        global polys_affected_bas
        polys_affected_bas = total_polys_affected_bas

    remove_mode_state = 0
    edit_mode_state = 0
    def toggle_remove_mode(self):
        remove_states = ["interface_remove_item.png", "interface_remove_item_2.png"]
        edit_states = ["interface_edit_item.png", "interface_edit_item_2.png"]
        if self.remove_mode_state == 0:
            self.remove_mode_state = 1
            self.edit_mode_state = 0
            self.remove_item.source = remove_states[self.remove_mode_state]
            self.edit_item.source = edit_states[self.edit_mode_state]
        elif self.remove_mode_state == 1:
            self.remove_mode_state = 0
            self.remove_item.source = remove_states[self.remove_mode_state]
            
        if self.remove_mode_state == 1 or self.edit_mode_state == 1:
            self.background1.source = "color_golden.png"
        elif self.remove_mode_state == 0 and self.edit_mode_state == 0:
            self.background1.source = "color_gray.png"

    def toggle_edit_mode(self):
        edit_states = ["interface_edit_item.png", "interface_edit_item_2.png"]
        remove_states = ["interface_remove_item.png", "interface_remove_item_2.png"]
        if self.edit_mode_state == 0:
            self.edit_mode_state = 1
            self.remove_mode_state = 0
            self.edit_item.source = edit_states[self.edit_mode_state]
            self.remove_item.source = remove_states[self.remove_mode_state]
        elif self.edit_mode_state == 1:
            self.edit_mode_state = 0
            self.edit_item.source = edit_states[self.edit_mode_state]
        if self.remove_mode_state == 1 or self.edit_mode_state == 1:
            self.background1.source = "color_golden.png"
        elif self.remove_mode_state == 0 and self.edit_mode_state == 0:
            self.background1.source = "color_gray.png"

target_god_class = ""
class Target_Class_Screen(Screen):
    guardian_btn = ObjectProperty
    hunter_btn = ObjectProperty
    warrior_btn = ObjectProperty
    mage_btn = ObjectProperty
    assassin_btn = ObjectProperty

    def initialize_next_screen_and_go(self, class_selected):
        global target_god_class
        target_god_class = class_selected
        options = { "guardian": 0 , "hunter": 1, "warrior": 2,
                    "mage": 3, "assassin": 4 }
        self.manager.get_screen("target god selection screen").initialize(options[class_selected])
        self.manager.current = "target god selection screen"
    def check_cidh_mode(self):
        global cidh_mode
        if cidh_mode == 1:
            self.guardian_btn.opacity = 0.3
            self.guardian_btn.disabled = True
            self.hunter_btn.opacity = 0.3
            self.hunter_btn.disabled = True
            self.warrior_btn.opacity = 0.3
            self.warrior_btn.disabled = True
            self.mage_btn.opacity = 0.3
            self.mage_btn.disabled = True
            self.assassin_btn.opacity = 1
            self.assassin_btn.disabled = False
        else:
            self.guardian_btn.opacity = 1
            self.guardian_btn.disabled = False
            self.hunter_btn.opacity = 1
            self.hunter_btn.disabled = False
            self.warrior_btn.opacity = 1
            self.warrior_btn.disabled = False
            self.mage_btn.opacity = 1
            self.mage_btn.disabled = False
            self.assassin_btn.opacity = 1
            self.assassin_btn.disabled = False
    def reset_pages_and_go_back(self):
        global target_classes_pages_numbers
        target_classes_pages_numbers = [1, 1, 1, 1, 1]
        self.manager.current = "build screen"

target_class_option_number = 0
target_classes_pages_numbers = [1, 1, 1, 1, 1]
target_god = ""
class Target_God_Selection_Screen(Screen):

    next_button = ObjectProperty()
    previous_button = ObjectProperty()

    guardians = [ "ares", "artio", "athena", "bacchus", "cabrakan",
                   "cerberus", "fafnir", "ganesha", "geb",
                   "khepri", "kumbhakarna", "kuzenbo", "sobek", "sylvanus",
                   "terra", "xing-tian", "ymir" ]
    hunters = [ "ah-muzen-cab", "anhur", "apollo", "artemis", "cernunnos",
                 "chernobog", "chiron", "cupid", "hachiman",
                 "hou-yi", "izanami", "jing-wei", "medusa", "neith",
                 "rama", "skadi", "ullr", "xbalanque" ]
    warriors = [ "achilles", "amaterasu", "bellona", "chaac", "cu-chulainn",
                  "erlang-shen", "guan-yu", "hercules", "nike",
                  "odin", "osiris", "sun-wukong", "tyr", "vamana" ]
    mages = [ "agni", "ah-puch", "anubis", "ao-kuang", "aphrodite",
               "baron-samedi", "change", "chronos", "discordia",
               "freya", "hades", "he-bo", "hel", "isis",
               "janus", "kukulkan", "nox", "nu-wa",
               "poseidon", "ra", "raijin", "scylla", "sol",
               "the-morrigan", "thoth", "vulcan", "zeus",
               "zhong-kui" ]
    assassins = [ "arachne", "awilix", "bakasura", "bastet", "camazotz",
                   "da-ji", "fenrir", "hun-batz", "kali",
                   "loki", "mercury", "ne-zha", "nemesis", "pele",
                   "ratatoskr", "ravana", "serqet", "susano",
                   "thanatos", "thor" ]

    button_positions = [ [0.123, 0.7], [0.391, 0.7], [0.659, 0.7],
                         [0.123, 0.508], [0.391, 0.508], [0.659, 0.508],
                         [0.123, 0.316], [0.391, 0.316], [0.659, 0.316] ]
    
    list_of_lists = [guardians, hunters, warriors, mages, assassins]

    btn1 = ClickableImage(pos_hint = { "x": button_positions[0][0] , "y": button_positions[0][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn2 = ClickableImage(pos_hint = { "x": button_positions[1][0] , "y": button_positions[1][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn3 = ClickableImage(pos_hint = { "x": button_positions[2][0] , "y": button_positions[2][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn4 = ClickableImage(pos_hint = { "x": button_positions[3][0] , "y": button_positions[3][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn5 = ClickableImage(pos_hint = { "x": button_positions[4][0] , "y": button_positions[4][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn6 = ClickableImage(pos_hint = { "x": button_positions[5][0] , "y": button_positions[5][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn7 = ClickableImage(pos_hint = { "x": button_positions[6][0] , "y": button_positions[6][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn8 = ClickableImage(pos_hint = { "x": button_positions[7][0] , "y": button_positions[7][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    btn9 = ClickableImage(pos_hint = { "x": button_positions[8][0] , "y": button_positions[8][1] }, source = "nothing.png",
                          size_hint = (0.218, 0.142), keep_ratio = False, allow_stretch = True)
    
    buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

    initialized = False

    def initialize(self, option):
        global target_classes_pages_numbers
        selected_list = self.list_of_lists[option]
        page_number = target_classes_pages_numbers[option]
        elements_number = 0
        
        global target_class_option_number
        target_class_option_number = option
        
        for x in selected_list:
            elements_number = elements_number + 1

        number_of_pages = elements_number/9 + 1
        if elements_number == 18 or elements_number == 27 or elements_number == 36 or elements_number == 45:
            number_of_pages = number_of_pages - 1
            
        if self.initialized == False:
            layout = FloatLayout()
            i = 0
            page_number = 1
            for button in self.buttons:
                if i == 9:
                    break
                button.source = selected_list[i] + ".png"
                button.name = selected_list[i]
                button.bind(on_press=self.go_to_god)
                layout.add_widget(button)
                i = i + 1
            self.add_widget(layout)
            self.initialized = True
        elif self.initialized == True:
            if page_number == 1:
                i = 8
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 0:
                        break
                    i = i - 1
            if page_number == 2:
                i = 17
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 9:
                        break
                    i = i - 1
            if page_number == 3:
                i = 26
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 18:
                        break
                    i = i - 1
            if page_number == 4:
                i = 35
                for button in self.children[0].children:
                    if i > (elements_number - 1):
                        button.source = "nothing.png"
                        button.name = "nothing"
                    else:
                        button.source = selected_list[i] + ".png"
                        button.name = selected_list[i]
                        button.bind(on_press=self.go_to_god)
                    if i == 27:
                        break
                    i = i - 1

        if page_number == 1:
            self.previous_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.previous_button.pos_hint = { "x": 0.0 , "y": 0.0 }
        if page_number == number_of_pages:
            self.next_button.pos_hint = { "x": 1.5 , "y": 1.5 }
        else:
            self.next_button.pos_hint = { "x": 0.8 , "y": 0.0 }
                
    def go_to_god(self, btn):
        if btn.name != "nothing":
            global target_god
            target_god = btn.name
            self.manager.get_screen("cidh final screen").initialize()
            self.manager.current = "cidh final screen"

    def next_page(self):
        global target_classes_pages_numbers
        global target_class_option_number
        target_classes_pages_numbers[target_class_option_number] = target_classes_pages_numbers[target_class_option_number] + 1
        self.initialize(target_class_option_number)

    def previous_page(self):
        global target_classes_pages_numbers
        global target_class_option_number
        target_classes_pages_numbers[target_class_option_number] = target_classes_pages_numbers[target_class_option_number] - 1
        self.initialize(target_class_option_number)
        
    def change_global_variables(self, name, sk_num, sk_states, double_state, special_input):
        global current_god
        global skills_num
        global skills_with_states
        global double_diamonds
        global special_int_input
        current_god = name
        skills_num = sk_num
        skills_with_states = sk_states
        double_diamonds = double_state
        special_int_input = special_input

class CIDH_Final_Screen(Screen):
    player_god_btn = ObjectProperty
    target_god_btn = ObjectProperty
    player_lvl_img = ObjectProperty
    target_lvl_img = ObjectProperty
    item1_img = ObjectProperty
    item2_img = ObjectProperty
    item3_img = ObjectProperty
    item4_img = ObjectProperty
    item5_img = ObjectProperty
    item6_img = ObjectProperty
    cidh_answer_img = ObjectProperty
    edit_item = ObjectProperty

    player_god = ""
    target_god = ""
    player_lvl = 0
    target_lvl = 0

    skills_levels = ["i don't exist", 0, 0, 0, 0]

    sk1_bs = 0
    sk1_ps = 0
    sk1_bs2 = 0
    sk1_ps2 = 0
    sk2_bs = 0
    sk2_ps = 0
    sk2_bs2 = 0
    sk2_ps2 = 0
    sk3_bs = 0
    sk3_ps = 0
    sk3_bs2 = 0
    sk3_ps2 = 0
    sk4_bs = 0
    sk4_ps = 0
    sk4_bs2 = 0
    sk4_ps2 = 0

    base_ba_d_simple = 0
    base_ba_d_per_level = 0.0
    base_ba_d_power_multiplier = 0
    ba_progression = []

    base_p_prot = 0
    p_prot_per_level = 0.0
    base_mana = 0
    mana_per_level = 0

    final_build = []#[obj1, obj2, obj3, obj4, obj5, obj6]
    current_build = [nothing, nothing, nothing, nothing, nothing, nothing]
    building_order = []#[[], [], [], [], [], []]
    current_slot = 1
    current_tree_item = 1
    finished_build = False
    

    target_base_health = 0
    target_health_per_level = 0
    target_base_p_prot = 0.0
    target_p_prot_per_level = 0.0
    target_base_m_prot = 0.0
    target_m_prot_per_level = 0.0

    edit_mode = False
    
    def initialize(self):
        global current_god
        self.player_god_btn.source = current_god + ".png"
        global target_god
        self.target_god_btn.source = target_god + ".png"
        self.player_lvl_img.source = "1.png"
        self.target_lvl_img.source = "1.png"
        self.cidh_answer_img.source = "cidh_answer_no.png"

        ranks = self.manager.get_screen("ranks screen").ranks
        global selected_combo
        i = current_god + "_" + selected_combo
        skill_to_upgrade = ranks[i][self.player_lvl - 1]
        self.skills_levels[skill_to_upgrade] = self.skills_levels[skill_to_upgrade] + 1

        self.player_god = current_god
        self.target_god = target_god
        self.player_lvl = 0
        self.target_lvl = 0
        self.final_build = []
        self.building_order = []
        self.current_slot = 1
        self.current_tree_item = 1
        self.finished_build = False
        self.current_build = [nothing, nothing, nothing, nothing, nothing, nothing]
        self.skills_levels = ["i don't exist", 0, 0, 0, 0]

        global selected_objects
        global item_trees
        i = -1
        for item in selected_objects:
            if item.name_id != "" and item.name_id != "nothing":
                self.final_build.append(item)
                self.building_order.append([])
                i = i + 1
                j = 0
                finished_tree = False
                while finished_tree == False:
                    try:
                        self.building_order[i].append(items_trees[item.name_id][j])
                    except:
                        self.building_order[i].append(("item_" + item.name_id + ".png"))
                        break
                    
                    if elements_number(items_trees[item.name_id]) == (j + 1):
                        finished_tree = True
                    else:
                        j = j + 1
            
        print "final_build:"
        for i in self.final_build:
            print i.name_id
        print "-------------"
            
        print "current_build:"
        print self.current_build
        print "-------------"
        
        print "building_order:"
        print self.building_order
        print "-------------"

        tree = ET.parse("gods.xml")
        raet = tree.getroot()
        for god in raet.findall("god"):
            if god.get("name") == target_god:
                self.target_base_health = int(god.find("base_health").text)
                self.target_health_per_level = int(god.find("health_per_level").text)
                self.target_base_p_prot = int(god.find("base_p_prot").text)
                self.target_p_prot_per_level = float(god.find("p_prot_per_level").text)
                self.targeT_base_m_prot = int(god.find("base_m_prot").text)
                self.target_m_prot_per_level = float(god.find("m_prot_per_level").text)
                break

        for god in raet.findall("god"):
            if god.get("name") == current_god:
                if current_god == "anhur":
                    self.sk1_bs = string_with_commas_to_list(god.find("sk1bs").text, True)
                else:
                    self.sk1_bs = string_with_commas_to_list(god.find("sk1bs").text, False)
                if current_god == "hachiman":
                    self.sk1_ps = string_with_commas_to_list(god.find("sk1ps").text, False)
                else:
                    self.sk1_ps = float(god.find("sk1ps").text)
                self.sk1_bs2 = string_with_commas_to_list(god.find("sk1bs2").text, False)
                self.sk1_ps2 = float(god.find("sk1ps2").text)

                if current_god == "hou-yi" or current_god == "skadi":
                    self.sk2_bs = string_with_commas_to_list(god.find("sk2bs").text, True)
                else:
                    self.sk2_bs = string_with_commas_to_list(god.find("sk2bs").text, False)
                self.sk2_ps = float(god.find("sk2ps").text)
                if current_god == "skadi":
                    self.sk2_bs2 = string_with_commas_to_list(god.find("sk2bs2").text, True)
                else:
                    self.sk2_bs2 = string_with_commas_to_list(god.find("sk2bs2").text, False)
                self.sk2_ps2 = float(god.find("sk2ps2").text)
                
                self.sk3_bs = string_with_commas_to_list(god.find("sk3bs").text, False)
                self.sk3_ps = float(god.find("sk3ps").text)
                if current_god == "isis":
                    self.sk3_bs2 = string_with_commas_to_list(god.find("sk3bs2").text, True)
                else:
                    self.sk3_bs2 = string_with_commas_to_list(god.find("sk3bs2").text, False)
                self.sk3_ps2 = float(god.find("sk3ps2").text)
                
                if current_god == "nemesis":
                    self.sk4_bs = string_with_commas_to_list(god.find("sk4bs").text, True)
                else:
                    self.sk4_bs = string_with_commas_to_list(god.find("sk4bs").text, False)
                self.sk4_ps = float(god.find("sk4ps").text)
                self.sk4_bs2 = string_with_commas_to_list(god.find("sk4bs2").text, False)
                self.sk4_ps2 = float(god.find("sk4ps2").text)

                self.base_ba_d_simple = int(god.find("base_ba_d_simple").text)
                self.base_ba_d_per_level = float(god.find("base_ba_d_per_level").text)
                self.base_ba_d_power_multiplier = float(god.find("base_ba_d_power_multiplier").text)
                self.ba_progression = string_with_commas_to_list(god.find("ba_progression").text, True)

                self.base_p_prot = int(god.find("base_p_prot").text)
                self.p_prot_per_level = float(god.find("p_prot_per_level").text)
                self.base_mana = int(god.find("base_mana").text)
                self.mana_per_level = int(god.find("mana_per_level").text)
                
                break
            
        self.level_up_player()
        self.level_up_target()
        
        
    def level_up_player(self):
        ranks = self.manager.get_screen("ranks screen").ranks
        if self.player_lvl == 20:
            return
        self.player_lvl = self.player_lvl + 1
        self.player_lvl_img.source = str(self.player_lvl) + ".png"

        global selected_combo
        i = current_god + "_" + selected_combo
        skill_to_upgrade = ranks[i][self.player_lvl - 1]
        self.skills_levels[skill_to_upgrade] = self.skills_levels[skill_to_upgrade] + 1

        self.check_if_icdh()

    def level_up_target(self):
        if self.target_lvl == 20:
            return
        self.target_lvl = self.target_lvl + 1
        self.target_lvl_img.source = str(self.target_lvl) + ".png"

        self.check_if_icdh()

    def build_up(self):
        if self.finished_build == True:
            return
        
        slot = self.current_slot
        item = self.current_tree_item

        buttons_list = [self.item1_img, self.item2_img, self.item3_img,
                        self.item4_img, self.item5_img, self.item6_img]
        current_build = self.current_build

        buttons_list[slot - 1].source = self.building_order[slot - 1][item - 1]
        global item_objects
        current_build[slot - 1] = item_objects[self.building_order[slot - 1][item - 1]]

        item = item + 1
        if elements_number(self.building_order[slot - 1]) < item:
            slot = slot + 1
            item = 1

        if elements_number(self.building_order) < slot:
            self.finished_build = True

        self.current_slot = slot
        self.current_tree_item = item
        
        self.check_if_icdh()

    def check_if_icdh(self):
        print self.skills_levels
        
        sk1_bs = self.sk1_bs
        sk1_ps = self.sk1_ps
        sk1_bs2 = self.sk1_bs2
        sk1_ps2 = self.sk1_ps2
        sk2_bs = self.sk2_bs
        sk2_ps = self.sk2_ps
        sk2_bs2 = self.sk2_bs2
        sk2_ps2 = self.sk2_ps2
        sk3_bs = self.sk3_bs
        sk3_ps = self.sk3_ps
        sk3_bs2 = self.sk3_bs2
        sk3_ps2 = self.sk3_ps2
        sk4_bs = self.sk4_bs
        sk4_ps = self.sk4_ps
        sk4_bs2 = self.sk4_bs2
        sk4_ps2 = self.sk4_ps2

        target_base_health = self.target_base_health
        target_health_per_level = self.target_health_per_level
        target_base_p_prot = self.target_base_p_prot
        target_p_prot_per_level = self.target_p_prot_per_level
        target_base_m_prot = self.target_base_m_prot
        target_m_prot_per_level = self.target_m_prot_per_level
        target_lvl = self.target_lvl

        target_health = target_base_health + target_health_per_level * target_lvl
        target_p_prot = target_base_p_prot + target_p_prot_per_level * target_lvl
        target_m_prot = target_base_m_prot + target_m_prot_per_level * target_lvl
        
        mages_starter = False
        hunters_starter = False
        hydras_1 = False
        hydras_2 = False
        heartseek = False
        crusher = False
        warrior_bane = False
        titan_bane = False
        execut = False
        qins = False
        deathbring = False
        malice = False
        poison_star = False
        stone_cuttng_sword = False
        void_shld = False
        frostbnd_hammer = False
        runeforgd_hammer = False

        total_power = 0
        total_mana = self.base_mana + self.mana_per_level * self.player_lvl
        total_mana_to_power_percent = 0.0
        total_crit_chance = 0
        p_percent_penetration = 0
        flat_penetration = 0

        mages_blessing_buff = 0
        hunters_blessing_buff = 0
        hydras_buff = 1
        heartseeker_buff = 0
        crusher_flat_buff = 0
        crusher_power_buff = 0
        p_percent_penetration = 0
        executioner_reduction = 0
        qins_bonus = 0
        p_void_shield_reduction = 0
        p_flat_reduction = 0
        crit_multiplier = 2
        
        items = self.current_build
        for i in range(0, 6):
            if items[i].name_id == "x_sta2":
                mages_blessing_buff = mages_blessing.mages_blessing_buff
            if items[i].name_id == "x_sta3":
                hunters_blessing_buff = hunters_blessing.ba_flat_buff
            if items[i].name_id == "p_mor4":
                hydras_buff = hydras_star.hydras_multiplier_buff
            if items[i].name_id == "p_mor5":
                hydras_buff = hydras_lament.hydras_multiplier_buff
            if items[i].name_id == "p_kat4" and items[i].state != 1:
                heartseeker_buff = heartseeker.heartseeker_buff_states[heartseeker.state - 1]
            if items[i].name_id == "p_mac5":
                crusher_flat_buff = the_crusher.crusher_flat_buff
                crusher_power_buff = the_crusher.crusher_buff_based_on_power
            if items[i].name_id == "p_mac6":
                p_percent_penetration = warriors_bane.percent_penetration
            if items[i].name_id == "p_mac7":
                p_percent_penetration = titans_bane.percent_penetration
                if target_p_prot > titans_bane.percent_penetration_protections_scaling[0]:
                    p_percent_penetration_per_protection = (titans_bane.max_percent_penetration - titans_bane.percent_penetration)/(titans_bane.percent_penetration_protections_scaling[1] - titans_bane.percent_penetration_protections_scaling[0])
                    p_percent_penetration = p_percent_penetration + p_percent_penetration_per_protection * (target_p_prot - titans_bane.percent_penetration_protections_scaling[0])
            if items[i].name_id == "p_lig2":
                executioner_reduction = the_executioner.executioner_reduction
            if items[i].name_id == "p_lig3":
                qins_bonus = qins_sais.qins_bonus
                if target_health > qins_sais.qins_health_scaling[0]:
                    qins_bonus_per_health_unit = (qins_sais.qins_max_bonus - qins_sais.qins_bonus)/(qins_sais.qins_health_scaling[1] - qins_sais.qins_health_scaling[0])
                    qins_bonus = qins_bonus + qins_bonus_per_health_unit * (target_health - qins_sais.qins_health_scaling[0]) 
            if items[i].name_id == "p_hid3":    
                crit_multiplier = 2 + deathbringer.db_crit_bonus
            if items[i].name_id == "p_hid5":    
                malice = True                   #
            if items[i].name_id == "p_shu3":
                poison_star = True              #
            if items[i].name_id == "p_kat5":
                p_flat_reduction = stone_cutting_sword.scs_bonus
            if items[i].name_id == "p_rou3":
                p_void_shield_reduction = void_shield.aura_penetration
            if items[i].name_id == "p_cud3":
                frostbnd_hammer = True          #
            if items[i].name_id == "p_cud4":
                runeforgd_hammer = True         #
                
            if items[i].power2 != 0 and (god_class=="mage" or god_class=="guardian"):
                total_power = total_power + items[i].power2
            else:
                total_power = total_power + items[i].power 
                
            total_mana = total_mana + items[i].mana
            total_mana_to_power_percent = total_mana_to_power_percent + items[i].mana_to_power_percent
            total_crit_chance = total_crit_chance + items[i].crit_chance
            if items[i].name_id == "x_sta1":
                flat_penetration = flat_penetration + items[i].penetration_states[items[i].state - 1]
            else:
                flat_penetration = flat_penetration + items[i].penetration
            
        if flat_penetration > 50:
            flat_penetration = 50
        
        total_power = total_power + total_mana_to_power_percent * total_mana

        print "-------------------"
        print "Power:"
        print total_power 
        
        global selected_combo
        if self.player_god == "loki":

            print "Percent penetration:"
            print p_percent_penetration
            print "Flat penetration:"
            print flat_penetration
                
            if int(selected_combo) == 1:

                if self.player_lvl < 5:
                    self.cidh_answer_img.source = "cidh_answer_no.png"
                    return
                
                sk4d = sk4_bs[self.skills_levels[4] - 1] + sk4_ps * total_power
                prot_after_pen = target_p_prot - p_void_shield_reduction
                prot_after_pen = prot_after_pen * (1 - p_percent_penetration)
                prot_after_pen = prot_after_pen - flat_penetration
                sk4d = approximate_number_to_int((sk4d * (1 - ( prot_after_pen / (prot_after_pen + 100)))))
                
                mages_blessing_damage_1 = approximate_number_to_int(mages_blessing_buff * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                heartseeker_dmg = heartseeker_buff * total_power
                heartseeker_dmg = approximate_number_to_int(heartseeker_dmg * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                crusher_damage_1 = crusher_flat_buff + crusher_power_buff * total_power
                crusher_damage_1 = approximate_number_to_int(crusher_damage_1 * (1 - ( prot_after_pen / (prot_after_pen + 100))))
                    
                ba_1_dmg = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + total_power + hunters_blessing_buff) * 1.2 * hydras_buff
                ba_1_dmg = approximate_number_to_int(ba_1_dmg * (1 - ( prot_after_pen / (prot_after_pen + 100))))
                ba_1_dmg_crit = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + total_power + hunters_blessing_buff) * 1.2 * hydras_buff * crit_multiplier
                ba_1_dmg_crit = approximate_number_to_int(ba_1_dmg_crit * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                sais_dmg_1 = target_health * qins_bonus
                sais_dmg_1 = approximate_number_to_int(sais_dmg_1 * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                    
                sk3d = sk3_bs[self.skills_levels[3] - 1] + sk3_ps * total_power
                prot_after_pen = target_p_prot * (1 - executioner_reduction)
                prot_after_pen = prot_after_pen - p_void_shield_reduction - p_flat_reduction
                prot_after_pen = prot_after_pen * (1 - p_percent_penetration)
                prot_after_pen = prot_after_pen - flat_penetration
                sk3d = approximate_number_to_int(sk3d * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                mages_blessing_damage_2 = approximate_number_to_int(mages_blessing_buff * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                crusher_damage_2 = crusher_flat_buff + crusher_power_buff * total_power
                crusher_damage_2 = approximate_number_to_int(crusher_damage_2 * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                ba_2_dmg = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + total_power + hunters_blessing_buff) * 1.2 * hydras_buff
                ba_2_dmg = approximate_number_to_int(ba_2_dmg * (1 - ( prot_after_pen / (prot_after_pen + 100))))
                ba_2_dmg_crit = (self.base_ba_d_simple + self.base_ba_d_per_level * self.player_lvl + total_power + hunters_blessing_buff) * 1.2 * hydras_buff * crit_multiplier
                print self.base_ba_d_simple
                print self.base_ba_d_per_level
                print self.player_lvl
                print total_power
                print hunters_blessing_buff
                print hydras_buff
                print crit_multiplier

                ba_2_dmg_crit = approximate_number_to_int(ba_2_dmg_crit * (1 - ( prot_after_pen / (prot_after_pen + 100))))


                sais_dmg_2 = target_health * qins_bonus
                sais_dmg_2 = approximate_number_to_int(sais_dmg_2 * (1 - ( prot_after_pen / (prot_after_pen + 100))))

                total_dmg = sk4d + mages_blessing_damage_1 + heartseeker_dmg + crusher_damage_1 + ba_1_dmg + sais_dmg_1 + sk3d + mages_blessing_damage_2 + crusher_damage_2 + ba_2_dmg + sais_dmg_2
                
                print "Final, real damage:"
                print total_dmg
                print "Target health:"
                print target_health
                print "Target protections:"
                print target_p_prot
                print "Total crit chance:"
                print total_crit_chance

                if total_dmg > target_health:
                    self.cidh_answer_img.source = "cidh_answer_yes.png"
                else:
                    if total_crit_chance != 0.0:
                        delete_probability = 0.0
                        total_dmg = total_dmg - ba_1_dmg + ba_1_dmg_crit
                        if total_dmg > target_health:
                            event_probability = 100 * (1.0 - total_crit_chance) * total_crit_chance
                            delete_probability = delete_probability + event_probability

                        total_dmg = total_dmg + ba_1_dmg - ba_1_dmg_crit             
                        total_dmg = total_dmg - ba_2_dmg + ba_2_dmg_crit
                        if total_dmg > target_health:
                            event_probability = 100 * total_crit_chance * (1.0 - total_crit_chance)
                            delete_probability = delete_probability + event_probability

                        total_dmg = total_dmg + ba_2_dmg - ba_2_dmg_crit             
                        total_dmg = total_dmg - ba_1_dmg - ba_2_dmg + ba_1_dmg_crit + ba_2_dmg_crit
                        if total_dmg > target_health:
                            event_probability = 100 * total_crit_chance * total_crit_chance
                            delete_probability = delete_probability + event_probability

                        if delete_probability == 0.0:
                            print "gg 0"
                            self.cidh_answer_img.source = "cidh_answer_no.png"
                        else:
                            print "Delete probability:"
                            print delete_probability
                            self.cidh_answer_img.source = "cidh_answer_crit_" + str(approximate_number_to_int(delete_probability)) + ".png"
                            
                    else:
                        self.cidh_answer_img.source = "cidh_answer_no.png"
                
        #global selected_items
        #global selected_objects
        #for obj in selected_objects:
        #    print obj.name_id

    def toggle_edit_mode(self):
        if self.edit_mode == False:
            self.edit_mode = True
            self.edit_item.source = "interface_edit_item_2.png"
        else:
            self.edit_mode = False
            self.edit_item.source = "interface_edit_item.png"

    def upgrade_item_or_do_nothing(self, item_number):
        i = item_number - 1
        if self.edit_mode == True:
            if self.current_build[i].max_state != 1 and (self.current_build[i].state < self.current_build[i].max_state):
                self.current_build[i].state = self.current_build[i].state + 1
                if self.current_build[i].name_id == "x_sta1_1":
                    self.current_build[i].update_penetration()
                if self.current_build[i].name_id == "x_sta3_1":
                    self.current_build[i].update_ba_flat_buff()
                if self.current_build[i].name_id == "p_hid4":
                    self.current_build[i].update_crit_chance()
                if self.current_build[i].name_id == "p_spi3":
                    self.current_build[i].update_power()
                if self.current_build[i].name_id == "p_spi6":
                    self.current_build[i].update_power()
                if self.current_build[i].name_id == "p_kat4":
                    self.current_build[i].update_heartseeker_buff()
                if self.current_build[i].name_id == "p_mor3":
                    self.current_build[i].update_mana()
                if i == 0:
                    self.item1_img.source = editar_numero_de_imagen(self.item1_img.source, str(self.current_build[i].state))
                elif i == 1:
                    self.item2_img.source = editar_numero_de_imagen(self.item2_img.source, str(self.current_build[i].state))
                elif i == 2:
                    self.item3_img.source = editar_numero_de_imagen(self.item3_img.source, str(self.current_build[i].state))
                elif i == 3:
                    self.item4_img.source = editar_numero_de_imagen(self.item4_img.source, str(self.current_build[i].state))
                elif i == 4:
                    self.item5_img.source = editar_numero_de_imagen(self.item5_img.source, str(self.current_build[i].state))
                elif i == 5:
                    self.item6_img.source = editar_numero_de_imagen(self.item6_img.source, str(self.current_build[i].state))
                self.check_if_icdh()
        else:
            self.build_up()
                
def string_with_commas_to_list(string, float_or_int):
        string_to_use = string + ","
        the_list = []
        current_number_list = []
        current_number = 0
        number = 0
        j = ""
        if float_or_int == False:
            for char in string_to_use:
                if char == " ":
                    pass
                elif char != ',':
                    number = int(char)
                    current_number_list.append(number)
                elif char == ',':
                    for n in current_number_list:
                        i = str(n)
                        j = j + i
                    current_number = int(j)
                    j = ""
                    the_list.append(current_number)
                    current_number_list = []
            return the_list
        elif float_or_int == True:
            for char in string_to_use:
                if char == " ":
                    pass
                elif char != ',':
                    if char != '.':
                        number = int(char)
                        current_number_list.append(number)
                    elif char == '.':
                        current_number_list.append(char)
                elif char == ',':
                    for n in current_number_list:
                        i = str(n)
                        j = j + i
                    current_number = float(j)
                    j = ""
                    the_list.append(current_number)
                    current_number_list = []
            return the_list

ba_flat_buff = 0
mages_blessing_buff = 0
hydras_multiplier_buff = 0
hydras_affected_bas = 0
heartseeker_buff = 0
crusher_flat_buff = 0
crusher_buff_based_on_power = 0
poly_buff_based_on_power = 0
polys_affected_bas = 0
class Normal_God_Screen(Screen):
    floatlayout = ObjectProperty
    god_big_image = ObjectProperty
    total_damage_label = ObjectProperty
    three_inputs_widget = ObjectProperty
    n_skills_hud = ObjectProperty
    n_diamonds_hud = ObjectProperty
    calculate_button = ObjectProperty
    special_input_widget = ObjectProperty

    toScreen = StringProperty('')

    info_active = StringProperty('')

    state_sk1a = 0

    def import_power_from_items(self, value):
        self.three_inputs_widget.int_input_2.int_input_textinput.text = str(value)
        self.three_inputs_widget.int_input_2.int_input_num = int(value)

    def string_to_list(self, string):
        the_list = []
        for char in string:
            number = int(char)
            the_list.append(number)
        return the_list

    def string_with_commas_to_list(self, string, float_or_int):
        string_to_use = string + ","
        the_list = []
        current_number_list = []
        current_number = 0
        number = 0
        j = ""
        if float_or_int == False:
            for char in string_to_use:
                if char == " ":
                    pass
                elif char != ',':
                    number = int(char)
                    current_number_list.append(number)
                elif char == ',':
                    for n in current_number_list:
                        i = str(n)
                        j = j + i
                    current_number = int(j)
                    j = ""
                    the_list.append(current_number)
                    current_number_list = []
            return the_list
        elif float_or_int == True:
            for char in string_to_use:
                if char == " ":
                    pass
                elif char != ',':
                    if char != '.':
                        number = int(char)
                        current_number_list.append(number)
                    elif char == '.':
                        current_number_list.append(char)
                elif char == ',':
                    for n in current_number_list:
                        i = str(n)
                        j = j + i
                    current_number = float(j)
                    j = ""
                    the_list.append(current_number)
                    current_number_list = []
            return the_list

    def initialize(self):
        global current_god
        global skills_num
        global skills_with_states
        global double_diamonds
        global special_int_input

        tree = ET.parse("gods.xml")
        raet = tree.getroot()
        for god in raet.findall("god"):
            if god.get("name") == current_god:
                skills_num = int(god.find("number_of_abilities").text)
                skills_with_states = self.string_to_list(god.find("diamond_states").text)
                double_diamonds = bool(int(god.find("double_diamonds").text))
                special_int_input = bool(int(god.find("special_input").text))

        self.manager.get_screen("god info screen").update_text()

        self.info_active = "god info screen"
        god_without_info_screen = ["sylvanus", "apollo", "artemis",
                                   "osiris", "ravana",
                                   "aphrodite", "change", "chronos",
                                   "he-bo", "hel", "scylla",
                                   "loki", "mercury", "serqet",
                                   "thanatos"]
        for k in god_without_info_screen:
            if current_god == k:
                self.info_active = "normal god screen"
        
        self.god_big_image.source = current_god + "2.png"


        guardians = [ "ares", "artio", "athena", "bacchus", "cabrakan",
                       "cerberus", "fafnir", "ganesha", "geb",
                       "khepri", "kumbhakarna", "kuzenbo", "sobek", "sylvanus",
                       "terra", "xing-tian", "ymir" ]


        hunters = [ "ah-muzen-cab", "anhur", "apollo", "artemis", "cernunnos",
                     "chernobog", "chiron", "cupid", "hachiman",
                     "hou-yi", "izanami", "jing-wei", "medusa", "neith",
                     "rama", "skadi", "ullr", "xbalanque" ]


        warriors = [ "achilles", "amaterasu", "bellona", "chaac", "cu-chulainn",
                      "erlang-shen", "guan-yu", "hercules", "nike",
                      "odin", "osiris", "sun-wukong", "tyr", "vamana" ]


        mages = [ "agni", "ah-puch", "anubis", "ao-kuang", "aphrodite",
                   "baron-samedi", "change", "chronos", "discordia",
                   "freya", "hades", "he-bo", "hel", "isis",
                   "janus", "kukulkan", "nox", "nu-wa",
                   "poseidon", "ra", "raijin", "scylla", "sol",
                   "the-morrigan", "thoth", "vulcan", "zeus",
                   "zhong-kui" ]


        assassins = [ "arachne", "awilix", "bakasura", "bastet", "camazotz",
                       "da-ji", "fenrir", "hun-batz", "kali",
                       "loki", "mercury", "ne-zha", "nemesis", "pele",
                       "ratatoskr", "ravana", "serqet", "susano",
                       "thanatos", "thor" ]

        global god_class

        for god in guardians:
            if current_god == god:
                god_class = "guardian"
        for god in hunters:
            if current_god == god:
                god_class = "hunter"
        for god in warriors:
            if current_god == god:
                god_class = "warrior"
        for god in mages:
            if current_god == god:
                god_class = "mage"
        for god in assassins:
            if current_god == god:
                god_class = "assassin"

        if double_diamonds == False:
            three_inputs_height = 0.4
            hud_height = 0.1
            diamonds_a_height = 0.3
            if special_int_input == False:
                calculate_button_pos = { "x": 0.35 , "y": 0.59 }
                damage_label_pos = { "x": 0.5 , "y": 0.73 }
                self.special_input_widget.pos_hint = { "x": 1.5 , "y": 1.5 }
            if special_int_input == True:
                calculate_button_pos = { "x": 0.45 , "y": 0.59 }
                damage_label_pos = { "x": 0.6 , "y": 0.73 }
                self.special_input_widget.pos_hint = { "x": 0.15 , "y": 0.56 }
                
        if double_diamonds == True:
            hud_height = 0.18
            three_inputs_height = 0.5
            calculate_button_pos = { "x": 0.12 , "y": 0.68 }
            damage_label_pos = { "x": 0.7, "y": 0.72 }
            diamonds_a_height = 0.392
            self.special_input_widget.pos_hint = { "x": 1.5 , "y": 1.5 }

        if current_god == "cu-chulainn":
            self.special_input_widget.pos_hint = { "x": 0.285 , "y": 0.373 }
            calculate_button_pos = { "x": 0.12 , "y": 0.7 }
            damage_label_pos = { "x": 0.7, "y": 0.74 }
            three_inputs_height = 0.52

        gods_without_diamonds = ["khepri", "sylvanus", "apollo",
                                 "artemis", "izanami", "osiris",
                                 "ao-kuang", "aphrodite", "change",
                                 "chronos", "he-bo", "scylla",
                                 "arachne", "bakasura", "bastet",
                                 "loki", "mercury", "ravana",
                                 "serqet", "thanatos"]
        for l in gods_without_diamonds:
            if current_god == l:
                hud_height = 0.15

        if current_god == "athena":
            self.special_input_widget.title = "P. bas:"
        if current_god == "anhur" or current_god == "cernunnos":
            self.special_input_widget.title = "Sk1 bas:"
        if current_god == "chernobog":
            self.special_input_widget.title = "P. ticks:"
        if current_god == "chiron":
            self.special_input_widget.title = "Sk3 bas:"
        if current_god == "cupid":
            self.special_input_widget.title = "P. stacks:"
        if current_god == "hachiman":
            self.special_input_widget.title = "Sk1 bas:"
        if current_god == "izanami":
            self.special_input_widget.title = "Sk1 bas:"
        if current_god == "jing-wei":
            self.special_input_widget.title = "Sk2 bas:"
        if current_god == "skadi":
            self.special_input_widget.title = "K. basics:"
        if current_god == "xbalanque":
            self.special_input_widget.title = "Sk1 bas:"
        if current_god == "guan-yu":
            self.special_input_widget.title = "H. att:"
        if current_god == "cu-chulainn":
            self.special_input_widget.title = ""
        if current_god == "sun-wukong":
            self.special_input_widget.title = "Pet bas:"
        if current_god == "vamana":
            self.special_input_widget.title = "Ult bas:"
        if current_god == "ao-kuang":
            self.special_input_widget.title = "Melee dra:"
        if current_god == "baron-samedi":
            self.special_input_widget.title = "Ult ticks:"
        if current_god == "discordia":
            self.special_input_widget.title = "Minor ticks:"
        if current_god == "freya":
            self.special_input_widget.title = "Sk2 bas:"
        if current_god == "nu-wa":
            self.special_input_widget.title = "C.S. bas:"
        if current_god == "poseidon":
            self.special_input_widget.title = "Sk1 ticks"
        if current_god == "vulcan":
            self.special_input_widget.title = "C. attacks:"
        if current_god == "arachne":
            self.special_input_widget.title = "W. ticks:"
        if current_god == "bakasura":
            self.special_input_widget.title = "Ult ticks:"
        if current_god == "bastet":
            self.special_input_widget.title = "C. ticks:"
        if current_god == "ne-zha":
            self.special_input_widget.title = "Sk1 ticks:"
        if current_god == "pele":
            self.special_input_widget.title = "Sk3 ticks:"

        self.total_damage_label.text = "Damage: 0"

        self.n_skills_hud.skill_1_level_num = 1
        self.n_skills_hud.skill_2_level_num = 1
        self.n_skills_hud.skill_3_level_num = 1
        self.n_skills_hud.skill_4_level_num = 1

        self.n_skills_hud.skill_1_points = "sk_l_1.jpg"
        self.n_skills_hud.skill_2_points = "sk_l_1.jpg"
        self.n_skills_hud.skill_3_points = "sk_l_1.jpg"
        self.n_skills_hud.skill_4_points = "sk_l_1.jpg"
            
        self.n_diamonds_hud.state_sk1a = 0
        self.n_diamonds_hud.state_sk2a = 0
        self.n_diamonds_hud.state_sk3a = 0
        self.n_diamonds_hud.state_sk4a = 0
        self.n_diamonds_hud.state_sk1b = 0
        self.n_diamonds_hud.state_sk2b = 0
        self.n_diamonds_hud.state_sk3b = 0
        self.n_diamonds_hud.state_sk4b = 0

        self.n_diamonds_hud.picture_1a = ''
        self.n_diamonds_hud.picture_2a = ''
        self.n_diamonds_hud.picture_3a = ''
        self.n_diamonds_hud.picture_4a = ''
        self.n_diamonds_hud.picture_1b = ''
        self.n_diamonds_hud.picture_2b = ''
        self.n_diamonds_hud.picture_3b = ''
        self.n_diamonds_hud.picture_4b = ''

        if skills_num == 2:

            self.three_inputs_widget.pos_hint = { "x": 0.15, "y": three_inputs_height }
            self.calculate_button.pos_hint = calculate_button_pos
            self.total_damage_label.pos_hint = damage_label_pos

            self.n_skills_hud.size_hint = 0.45 , 0.172
            self.n_skills_hud.pos_hint = { "x": 0.275 , "y": hud_height }
            self.n_skills_hud.picture_1 = current_god + "_sk_1.png"
            self.n_skills_hud.picture_2 = current_god + "_sk_2.png"
            
            self.n_skills_hud.size1a = 0.444 , 0.756
            self.n_skills_hud.pos1a = { "x": 0.0 , "y": 0.244 }
            self.n_skills_hud.size1b = 0.444 , 0.215
            self.n_skills_hud.pos1b = { "x": 0.0 , "y": 0.0 }
            
            self.n_skills_hud.size2a = 0.444 , 0.756
            self.n_skills_hud.pos2a = { "x": 0.555 , "y": 0.244 }
            self.n_skills_hud.size2b = 0.444 , 0.215
            self.n_skills_hud.pos2b = { "x": 0.555 , "y": 0.0 }

            self.n_skills_hud.size3a = 0.0 , 0.0
            self.n_skills_hud.size3b = 0.0 , 0.0

            self.n_skills_hud.size4a = 0.0 , 0.0
            self.n_skills_hud.size4b = 0.0 , 0.0

            self.n_diamonds_hud.pos1a = { "x": 0.335 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos2a = { "x": 0.585 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos1b = { "x": 0.335 , "y": 0.1 }
            self.n_diamonds_hud.pos2b = { "x": 0.585 , "y": 0.1 }

            self.n_diamonds_hud.size1a = 0.08, 0.045
            self.n_diamonds_hud.size2a = 0.08, 0.045
            self.n_diamonds_hud.size1b = 0.08, 0.045
            self.n_diamonds_hud.size2b = 0.08, 0.045
            
            self.n_diamonds_hud.size3a = 0.0 , 0.0
            self.n_diamonds_hud.size4a = 0.0 , 0.0
            self.n_diamonds_hud.size3b = 0.0 , 0.0
            self.n_diamonds_hud.size4b = 0.0 , 0.0

            if double_diamonds == False:                  
                d_index = 2
                self.n_diamonds_hud.picture_1b = "nothing.png"
                self.n_diamonds_hud.size1b = 0.0 , 0.0
                self.n_diamonds_hud.picture_2b = "nothing.png"
                self.n_diamonds_hud.size2b = 0.0 , 0.0
            if double_diamonds == True:
                d_index = 4

            self.n_diamonds_hud.picture_3a = "nothing.png"
            self.n_diamonds_hud.size4a = 0.0 , 0.0
            self.n_diamonds_hud.picture_3b = "nothing.png"
            self.n_diamonds_hud.size4b = 0.0 , 0.0
            self.n_diamonds_hud.picture_4a = "nothing.png"
            self.n_diamonds_hud.size4a = 0.0 , 0.0
            self.n_diamonds_hud.picture_4b = "nothing.png"
            self.n_diamonds_hud.size4b = 0.0 , 0.0

            i = 0
            while d_index > 0:
                if skills_with_states[i] == 0:
                    if i == 0:
                        self.n_diamonds_hud.picture_1a = "nothing.png"
                        self.n_diamonds_hud.size1a = 0.0 , 0.0
                    if i == 1:
                        self.n_diamonds_hud.picture_2a = "nothing.png"
                        self.n_diamonds_hud.size2a = 0.0 , 0.0
                    if i == 2:
                        self.n_diamonds_hud.picture_1b = "nothing.png"
                        self.n_diamonds_hud.size1b = 0.0 , 0.0
                    if i == 3:
                        self.n_diamonds_hud.picture_2b = "nothing.png"
                        self.n_diamonds_hud.size2b = 0.0 , 0.0
                        
                if skills_with_states[i] != 0:
                    if i == 0:
                        self.n_diamonds_hud.picture_1a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 1:
                        self.n_diamonds_hud.picture_2a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 2:
                        self.n_diamonds_hud.picture_1b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 3:
                        self.n_diamonds_hud.picture_2b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                d_index = d_index - 1
                i = i + 1

        if skills_num == 3:

            self.three_inputs_widget.pos_hint = { "x": 0.15, "y": three_inputs_height }
            self.calculate_button.pos_hint = calculate_button_pos
            self.total_damage_label.pos_hint = damage_label_pos

            self.n_skills_hud.size_hint = 0.7 , 0.172
            self.n_skills_hud.pos_hint = { "x": 0.15 , "y": hud_height }
            self.n_skills_hud.picture_1 = current_god + "_sk_1.png"
            self.n_skills_hud.picture_2 = current_god + "_sk_2.png"
            self.n_skills_hud.picture_3 = current_god + "_sk_3.png"

            self.n_skills_hud.size1a = 0.286 , 0.756
            self.n_skills_hud.pos1a = { "x": 0.0 , "y": 0.244 }
            self.n_skills_hud.size1b = 0.286 , 0.215
            self.n_skills_hud.pos1b = { "x": 0.0 , "y": 0.0 }
            
            self.n_skills_hud.size2a = 0.286 , 0.756
            self.n_skills_hud.pos2a = { "x": 0.357 , "y": 0.244 }
            self.n_skills_hud.size2b = 0.286 , 0.215
            self.n_skills_hud.pos2b = { "x": 0.357 , "y": 0.0 }

            self.n_skills_hud.size3a = 0.286 , 0.756
            self.n_skills_hud.pos3a = { "x": 0.714 , "y": 0.244 }
            self.n_skills_hud.size3b = 0.286 , 0.215
            self.n_skills_hud.pos3b = { "x": 0.714 , "y": 0.0 }

            self.n_skills_hud.size4a = 0.0 , 0.0
            self.n_skills_hud.size4b = 0.0 , 0.0

            self.n_diamonds_hud.pos1a = { "x": 0.21 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos2a = { "x": 0.46 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos3a = { "x": 0.71 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos1b = { "x": 0.21 , "y": 0.1 }
            self.n_diamonds_hud.pos2b = { "x": 0.46 , "y": 0.1 }
            self.n_diamonds_hud.pos3b = { "x": 0.71 , "y": 0.1 }

            self.n_diamonds_hud.size1a = 0.08, 0.045
            self.n_diamonds_hud.size2a = 0.08, 0.045
            self.n_diamonds_hud.size3a = 0.08, 0.045
            self.n_diamonds_hud.size1b = 0.08, 0.045
            self.n_diamonds_hud.size2b = 0.08, 0.045
            self.n_diamonds_hud.size3b = 0.08, 0.045

            self.n_diamonds_hud.size3a = 0.08 , 0.045
            self.n_diamonds_hud.size3b = 0.08 , 0.045
            
            self.n_diamonds_hud.size4a = 0.0 , 0.0
            self.n_diamonds_hud.size4b = 0.0 , 0.0

            if double_diamonds == False:                  
                d_index = 3
                self.n_diamonds_hud.picture_1b = "nothing.png"
                self.n_diamonds_hud.size1b = 0.0 , 0.0
                self.n_diamonds_hud.picture_2b = "nothing.png"
                self.n_diamonds_hud.size2b = 0.0 , 0.0
                self.n_diamonds_hud.picture_3b = "nothing.png"
                self.n_diamonds_hud.size3b = 0.0 , 0.0
            if double_diamonds == True:
                d_index = 6

            self.n_diamonds_hud.picture_4a = "nothing.png"
            self.n_diamonds_hud.size4a = 0.0 , 0.0
            self.n_diamonds_hud.picture_4b = "nothing.png"
            self.n_diamonds_hud.size4b = 0.0 , 0.0

            i = 0
            while d_index > 0:
                if skills_with_states[i] == 0:
                    if i == 0:
                        self.n_diamonds_hud.picture_1a = "nothing.png"
                        self.n_diamonds_hud.size1a = 0.0 , 0.0
                    if i == 1:
                        self.n_diamonds_hud.picture_2a = "nothing.png"
                        self.n_diamonds_hud.size2a = 0.0 , 0.0
                    if i == 2:
                        self.n_diamonds_hud.picture_3a = "nothing.png"
                        self.n_diamonds_hud.size3a = 0.0 , 0.0
                    if i == 3:
                        self.n_diamonds_hud.picture_1b = "nothing.png"
                        self.n_diamonds_hud.size1b = 0.0 , 0.0
                    if i == 4:
                        self.n_diamonds_hud.picture_2b = "nothing.png"
                        self.n_diamonds_hud.size2b = 0.0 , 0.0
                    if i == 5:
                        self.n_diamonds_hud.picture_3b = "nothing.png"
                        self.n_diamonds_hud.size3b = 0.0 , 0.0
                if skills_with_states[i] != 0:
                    if i == 0:
                        self.n_diamonds_hud.picture_1a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 1:
                        self.n_diamonds_hud.picture_2a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 2:
                        self.n_diamonds_hud.picture_3a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 3:
                        self.n_diamonds_hud.picture_1b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 4:
                        self.n_diamonds_hud.picture_2b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 5:
                        self.n_diamonds_hud.picture_3b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                d_index = d_index - 1
                i = i + 1
            
        if skills_num == 4:

            self.three_inputs_widget.pos_hint = { "x": 0.15, "y": three_inputs_height }
            self.calculate_button.pos_hint = calculate_button_pos
            self.total_damage_label.pos_hint = damage_label_pos

            self.n_skills_hud.size_hint = 0.87 , 0.172
            self.n_skills_hud.pos_hint = { "x": 0.065 , "y": hud_height }
            self.n_skills_hud.picture_1 = current_god + "_sk_1.png"
            self.n_skills_hud.picture_2 = current_god + "_sk_2.png"
            self.n_skills_hud.picture_3 = current_god + "_sk_3.png"
            self.n_skills_hud.picture_4 = current_god + "_sk_4.png"

            self.n_skills_hud.size1a = 0.207 , 0.756
            self.n_skills_hud.pos1a = { "x": 0.0 , "y": 0.244 }
            self.n_skills_hud.size1b = 0.207 , 0.215
            self.n_skills_hud.pos1b = { "x": 0.0 , "y": 0.0 }
            
            self.n_skills_hud.size2a = 0.207 , 0.756
            self.n_skills_hud.pos2a = { "x": 0.264 , "y": 0.244 }
            self.n_skills_hud.size2b = 0.207 , 0.215
            self.n_skills_hud.pos2b = { "x": 0.264 , "y": 0.0 }

            self.n_skills_hud.size3a = 0.207 , 0.756
            self.n_skills_hud.pos3a = { "x": 0.528 , "y": 0.244 }
            self.n_skills_hud.size3b = 0.207 , 0.215
            self.n_skills_hud.pos3b = { "x": 0.528 , "y": 0.0 }

            self.n_skills_hud.size4a = 0.207 , 0.756
            self.n_skills_hud.pos4a = { "x": 0.792 , "y": 0.244 }
            self.n_skills_hud.size4b = 0.207 , 0.215
            self.n_skills_hud.pos4b = { "x": 0.792 , "y": 0.0 }

            self.n_diamonds_hud.pos1a = { "x": 0.115 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos2a = { "x": 0.345 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos3a = { "x": 0.575 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos4a = { "x": 0.805 , "y": diamonds_a_height }
            self.n_diamonds_hud.pos1b = { "x": 0.115 , "y": 0.1 }
            self.n_diamonds_hud.pos2b = { "x": 0.345 , "y": 0.1 }
            self.n_diamonds_hud.pos3b = { "x": 0.575 , "y": 0.1 }
            self.n_diamonds_hud.pos4b = { "x": 0.805 , "y": 0.1 }

            self.n_diamonds_hud.size1a = 0.08, 0.045
            self.n_diamonds_hud.size2a = 0.08, 0.045
            self.n_diamonds_hud.size3a = 0.08, 0.045
            self.n_diamonds_hud.size4a = 0.08, 0.045
            self.n_diamonds_hud.size1b = 0.08, 0.045
            self.n_diamonds_hud.size2b = 0.08, 0.045
            self.n_diamonds_hud.size3b = 0.08, 0.045
            self.n_diamonds_hud.size4b = 0.08, 0.045
            
            self.n_diamonds_hud.size3a = 0.08 , 0.045
            self.n_diamonds_hud.size4a = 0.08 , 0.045
            self.n_diamonds_hud.size3b = 0.08 , 0.045
            self.n_diamonds_hud.size4b = 0.08 , 0.045

            if double_diamonds == False:                  
                d_index = 4
                self.n_diamonds_hud.picture_1b = "nothing.png"
                self.n_diamonds_hud.size1b = 0.0 , 0.0
                self.n_diamonds_hud.picture_2b = "nothing.png"
                self.n_diamonds_hud.size2b = 0.0 , 0.0
                self.n_diamonds_hud.picture_3b = "nothing.png"
                self.n_diamonds_hud.size3b = 0.0 , 0.0
                self.n_diamonds_hud.picture_4b = "nothing.png"
                self.n_diamonds_hud.size4b = 0.0 , 0.0
            if double_diamonds == True:
                d_index = 8

            i = 0
            while d_index > 0:
                if skills_with_states[i] == 0:
                    if i == 0:
                        self.n_diamonds_hud.picture_1a = "nothing.png"
                        self.n_diamonds_hud.size1a = 0.0 , 0.0
                    if i == 1:
                        self.n_diamonds_hud.picture_2a = "nothing.png"
                        self.n_diamonds_hud.size2a = 0.0 , 0.0
                    if i == 2:
                        self.n_diamonds_hud.picture_3a = "nothing.png"
                        self.n_diamonds_hud.size3a = 0.0 , 0.0
                    if i == 3:
                        self.n_diamonds_hud.picture_4a = "nothing.png"
                        self.n_diamonds_hud.size4a = 0.0 , 0.0
                    if i == 4:
                        self.n_diamonds_hud.picture_1b = "nothing.png"
                        self.n_diamonds_hud.size1b = 0.0 , 0.0
                    if i == 5:
                        self.n_diamonds_hud.picture_2b = "nothing.png"
                        self.n_diamonds_hud.size2b = 0.0 , 0.0
                    if i == 6:
                        self.n_diamonds_hud.picture_3b = "nothing.png"
                        self.n_diamonds_hud.size3b = 0.0 , 0.0
                    if i == 7:
                        self.n_diamonds_hud.picture_4b = "nothing.png"
                        self.n_diamonds_hud.size4b = 0.0 , 0.0
                        
                if skills_with_states[i] != 0:
                    if i == 0:
                        self.n_diamonds_hud.picture_1a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 1:
                        self.n_diamonds_hud.picture_2a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 2:
                        self.n_diamonds_hud.picture_3a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 3:
                        self.n_diamonds_hud.picture_4a = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 4:
                        self.n_diamonds_hud.picture_1b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 5:
                        self.n_diamonds_hud.picture_2b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 6:
                        self.n_diamonds_hud.picture_3b = current_god + "_diamond_" + str(i + 1) + "_1.png"
                    if i == 7:
                        self.n_diamonds_hud.picture_4b = current_god + "_diamond_" + str(i + 1) + "_1.png"

                d_index = d_index - 1
                i = i + 1
                
        tree = ET.parse("gods.xml")
        raet = tree.getroot()
        for god in raet.findall("god"):
            if god.get("name") == current_god:
                if current_god == "anhur":
                    self.sk1_bs = self.string_with_commas_to_list(god.find("sk1bs").text, True)
                else:
                    self.sk1_bs = self.string_with_commas_to_list(god.find("sk1bs").text, False)
                if current_god == "hachiman":
                    self.sk1_ps = self.string_with_commas_to_list(god.find("sk1ps").text, False)
                else:
                    self.sk1_ps = float(god.find("sk1ps").text)
                self.sk1_bs2 = self.string_with_commas_to_list(god.find("sk1bs2").text, False)
                self.sk1_ps2 = float(god.find("sk1ps2").text)

                if current_god == "hou-yi" or current_god == "skadi":
                    self.sk2_bs = self.string_with_commas_to_list(god.find("sk2bs").text, True)
                else:
                    self.sk2_bs = self.string_with_commas_to_list(god.find("sk2bs").text, False)
                self.sk2_ps = float(god.find("sk2ps").text)
                if current_god == "skadi":
                    self.sk2_bs2 = self.string_with_commas_to_list(god.find("sk2bs2").text, True)
                else:
                    self.sk2_bs2 = self.string_with_commas_to_list(god.find("sk2bs2").text, False)
                self.sk2_ps2 = float(god.find("sk2ps2").text)
                
                self.sk3_bs = self.string_with_commas_to_list(god.find("sk3bs").text, False)
                self.sk3_ps = float(god.find("sk3ps").text)
                if current_god == "isis":
                    self.sk3_bs2 = self.string_with_commas_to_list(god.find("sk3bs2").text, True)
                else:
                    self.sk3_bs2 = self.string_with_commas_to_list(god.find("sk3bs2").text, False)
                self.sk3_ps2 = float(god.find("sk3ps2").text)
                
                if current_god == "nemesis":
                    self.sk4_bs = self.string_with_commas_to_list(god.find("sk4bs").text, True)
                else:
                    self.sk4_bs = self.string_with_commas_to_list(god.find("sk4bs").text, False)
                self.sk4_ps = float(god.find("sk4ps").text)
                self.sk4_bs2 = self.string_with_commas_to_list(god.find("sk4bs2").text, False)
                self.sk4_ps2 = float(god.find("sk4ps2").text)

                self.base_ba_d_simple = int(god.find("base_ba_d_simple").text)
                self.base_ba_d_per_level = float(god.find("base_ba_d_per_level").text)
                self.base_ba_d_power_multiplier = float(god.find("base_ba_d_power_multiplier").text)
                self.ba_progression = self.string_with_commas_to_list(god.find("ba_progression").text, True)
            
                self.base_mana = int(god.find("base_mana").text)
                self.mana_per_level = int(god.find("mana_per_level").text)
                self.base_p_prot = int(god.find("base_p_prot").text)
                self.p_prot_per_level = float(god.find("p_prot_per_level").text)
            
        global base_mana
        global mana_per_level
        base_mana = self.base_mana
        mana_per_level = self.mana_per_level
        global base_p_prot
        global p_prot_per_level
        base_p_prot = self.base_p_prot
        p_prot_per_level = self.p_prot_per_level
                                               
    def back_screen(self):
        self.manager.current = "guardian selection"

    ba_n = 0

    def prepare_paramatres_for_calculate_and_then_calculate(self):
        global current_god

        sk_states = [self.n_diamonds_hud.state_sk1a, self.n_diamonds_hud.state_sk2a,
                     self.n_diamonds_hud.state_sk3a, self.n_diamonds_hud.state_sk4a,
                     self.n_diamonds_hud.state_sk1b, self.n_diamonds_hud.state_sk2b,
                     self.n_diamonds_hud.state_sk3b, self.n_diamonds_hud.state_sk4b]

        skills_levels = [self.n_skills_hud.skill_1_level_num, self.n_skills_hud.skill_2_level_num,
                         self.n_skills_hud.skill_3_level_num, self.n_skills_hud.skill_4_level_num]

        sk1_info = [self.sk1_bs, self.sk1_ps, self.sk1_bs2, self.sk1_ps2]
        sk2_info = [self.sk2_bs, self.sk2_ps, self.sk2_bs2, self.sk2_ps2]
        sk3_info = [self.sk3_bs, self.sk3_ps, self.sk3_bs2, self.sk3_ps2]
        sk4_info = [self.sk4_bs, self.sk4_ps, self.sk4_bs2, self.sk4_ps2]

        ba_info = [self.base_ba_d_simple, self.base_ba_d_per_level,
                   self.base_ba_d_power_multiplier, self.ba_progression]

        inputs = [self.three_inputs_widget.int_input_1.int_input_num,
                  self.three_inputs_widget.int_input_2.int_input_num,
                  self.three_inputs_widget.int_input_3.int_input_num,
                  self.special_input_widget.int_input_num]

        global ba_flat_buff
        global hydras_multiplier_buff
        global hydras_affected_bas
        global heartseeker_buff
        global poly_buff_based_on_power
        global polys_affected_bas
        global mages_blessing_buff
        global crusher_flat_buff
        global crusher_buff_based_on_power
        global skills_num

        values = calculate(current_god, sk_states, skills_levels, sk1_info, sk2_info, sk3_info, sk4_info,
                         ba_info, inputs, ba_flat_buff, hydras_multiplier_buff, hydras_affected_bas,
                         heartseeker_buff, poly_buff_based_on_power, polys_affected_bas,
                         mages_blessing_buff, crusher_flat_buff, crusher_buff_based_on_power,
                         skills_num)

        self.total_damage_label.text = values[0]

        self.ba_n = values[1]

current_item_slot = 0
selected_items = ["a", "a", "a", "a", "a", "a", "a", "a", "a"]

selected_objects = [Item("", 0, 0), Item("", 0, 0), Item("", 0, 0),
                    Item("", 0, 0), Item("", 0, 0), Item("", 0, 0),
                    Item("", 0, 0), Item("", 0, 0), Item("", 0, 0)]
selected_item_picture = "a"

god_level = 0
base_mana = 0
mana_per_level = 0
base_p_prot = 0
p_prot_per_level = 0

class Items_Screen(Screen):
    slot1 = ObjectProperty()
    slot2 = ObjectProperty()
    slot3 = ObjectProperty()
    slot4 = ObjectProperty()
    slot5 = ObjectProperty()
    slot6 = ObjectProperty()
    #slot7 = ObjectProperty()
    #slot8 = ObjectProperty()
    #slot9 = ObjectProperty()

    list_of_slots = [slot1, slot2, slot3,
                     slot4, slot5, slot6]
                     #slot7, slot8, slot9]

    total_damage_label = ObjectProperty()
    total_power_label = ObjectProperty()
    total_gold_label = ObjectProperty()
    total_mana_label = ObjectProperty()

    remove_item = ObjectProperty()
    edit_item = ObjectProperty()

    background1 = ObjectProperty()
    background2 = ObjectProperty()

    def select_item_slot_and_do_something(self, slot_number):
        global current_item_slot
        current_item_slot = slot_number
        list_of_slots = [self.slot1, self.slot2, self.slot3,
                         self.slot4, self.slot5, self.slot6]
                         #self.slot7, self.slot8, self.slot9]

        if self.remove_mode_state == 1:
            if list_of_slots[current_item_slot - 1].source != "nothing.png":
                self.quitar_item()
            elif list_of_slots[current_item_slot - 1].source == "nothing.png":
                self.toggle_remove_mode()
        elif self.edit_mode_state == 1:
            self.editar_item()
        else:
            self.initialize_screen2_and_go() 

    def quitar_item(self):
        global current_item_slot
        global selected_objects
        if current_item_slot == 1:
            self.slot1.source = "nothing.png"
            selected_objects[0] = self.nothing
        if current_item_slot == 2:
            self.slot2.source = "nothing.png"
            selected_objects[1] = self.nothing
        if current_item_slot == 3:
            self.slot3.source = "nothing.png"
            selected_objects[2] = self.nothing
        if current_item_slot == 4:
            self.slot4.source = "nothing.png"
            selected_objects[3] = self.nothing
        if current_item_slot == 5:
            self.slot5.source = "nothing.png"
            selected_objects[4] = self.nothing
        if current_item_slot == 6:
            self.slot6.source = "nothing.png"
            selected_objects[5] = self.nothing
        #if current_item_slot == 7:
        #    self.slot7.source = "nothing.png"
        #    selected_objects[6] = self.nothing
        #if current_item_slot == 8:
        #    self.slot8.source = "nothing.png"
        #    selected_objects[7] = self.nothing
        #if current_item_slot == 9:
        #    self.slot9.source = "nothing.png"
        #    selected_objects[8] = self.nothing
        global selected_items 
        selected_items = [self.slot1.source, self.slot2.source, self.slot3.source,
                          self.slot4.source, self.slot5.source, self.slot6.source]
                          #self.slot7.source, self.slot8.source, self.slot9.source]
        self.update_labels()

    def editar_item(self):
        global current_item_slot
        global selected_objects
        if current_item_slot == 1:
            if selected_objects[0].max_state != 1:
                selected_objects[0].state = selected_objects[0].state + 1
                if selected_objects[0].state > selected_objects[0].max_state:
                    selected_objects[0].state = 1
                self.slot1.source = self.editar_numero_de_imagen(self.slot1.source, str(selected_objects[0].state))
        if current_item_slot == 2:
            if selected_objects[1].max_state != 1:
                selected_objects[1].state = selected_objects[1].state + 1
                if selected_objects[1].state > selected_objects[1].max_state:
                    selected_objects[1].state = 1
                self.slot2.source = self.editar_numero_de_imagen(self.slot2.source, str(selected_objects[1].state))
        if current_item_slot == 3:
            if selected_objects[2].max_state != 1:
                selected_objects[2].state = selected_objects[2].state + 1
                if selected_objects[2].state > selected_objects[2].max_state:
                    selected_objects[2].state = 1
                self.slot3.source = self.editar_numero_de_imagen(self.slot3.source, str(selected_objects[2].state))
        if current_item_slot == 4:
            if selected_objects[3].max_state != 1:
                selected_objects[3].state = selected_objects[3].state + 1
                if selected_objects[3].state > selected_objects[3].max_state:
                    selected_objects[3].state = 1
                self.slot4.source = self.editar_numero_de_imagen(self.slot4.source, str(selected_objects[3].state))
        if current_item_slot == 5:
            if selected_objects[4].max_state != 1:
                selected_objects[4].state = selected_objects[4].state + 1
                if selected_objects[4].state > selected_objects[4].max_state:
                    selected_objects[4].state = 1
                self.slot5.source = self.editar_numero_de_imagen(self.slot5.source, str(selected_objects[4].state))
        if current_item_slot == 6:
            if selected_objects[5].max_state != 1:
                selected_objects[5].state = selected_objects[5].state + 1
                if selected_objects[5].state > selected_objects[5].max_state:
                    selected_objects[5].state = 1
                self.slot6.source = self.editar_numero_de_imagen(self.slot6.source, str(selected_objects[5].state))

        self.update_labels()

    def initialize_screen2_and_go(self):
        self.manager.get_screen("items screen 2").initialize()
        self.manager.current = "items screen 2"

    def editar_numero_de_imagen(self, palabra_a_editar, nuevo_indice):
        nueva_palabra = ""
        numero_de_caracteres = 0
        numero_de_caracter = 1
        for j in palabra_a_editar:
            if numero_de_caracter != 13:
                nueva_palabra = nueva_palabra + j
            if numero_de_caracter == 13:
                nueva_palabra = nueva_palabra + nuevo_indice
                nueva_palabra = nueva_palabra + ".png"
                return nueva_palabra
            numero_de_caracter = numero_de_caracter + 1

    def reset_items_to_zero(self):
        self.slot1.source = "nothing.png"
        self.slot2.source = "nothing.png"
        self.slot3.source = "nothing.png"
        self.slot4.source = "nothing.png"
        self.slot5.source = "nothing.png"
        self.slot6.source = "nothing.png"
        global selected_items
        selected_items = ["a", "a", "a",
                          "a", "a", "a"]
        global selected_objects
        selected_objects = [Item("", 0, 0), Item("", 0, 0), Item("", 0, 0),
                            Item("", 0, 0), Item("", 0, 0), Item("", 0, 0)]
        self.update_labels()

    
    def update_items(self):
        global current_item_slot
        global selected_item_picture
        global selected_objects
        global item_objects

        slots = [self.slot1, self.slot2, self.slot3,
                 self.slot4, self.slot5, self.slot6]
        
        for i in range(1, 7):
            if current_item_slot == i:
                slots[i-1].source = selected_item_picture
                selected_objects[i-1] = item_objects[selected_item_picture]

        global selected_items
        selected_items = [self.slot1.source, self.slot2.source, self.slot3.source,
                          self.slot4.source, self.slot5.source, self.slot6.source]

    item1_saved_state = 1
    item2_saved_state = 1
    item3_saved_state = 1
    item4_saved_state = 1
    item5_saved_state = 1
    item6_saved_state = 1
    total_power = 0
    mana_to_power_percent = 0
    initialized = 0
    
    def update_labels(self):
        global selected_objects
        item1 = selected_objects[0]
        item2 = selected_objects[1]
        item3 = selected_objects[2]
        item4 = selected_objects[3]
        item5 = selected_objects[4]
        item6 = selected_objects[5]
        items = [item1, item2, item3, item4, item5, item6]

        global god_class

        items_saved_states = [self.item1_saved_state, self.item2_saved_state,
                              self.item3_saved_state, self.item4_saved_state,
                              self.item5_saved_state, self.item6_saved_state]

        item1_power = 0
        item2_power = 0
        item3_power = 0
        item4_power = 0
        item5_power = 0
        item6_power = 0
        items_power = [item1_power, item2_power, item3_power,
                       item4_power, item5_power, item6_power]

        for i in range(0, 6):
            if items[i].state != items_saved_states[i]:
                items_saved_states[i] = items[i].state
                for changeable in items[i].can_change:
                    if changeable == "power":
                        items[i].update_power()
                    if changeable == "mana":
                        items[i].update_mana()
                    if changeable == "mana_to_power_percent":
                        items[i].update_mana_to_power_percent()
                    if changeable == "ba_flat_buff":
                        items[i].update_ba_flat_buff()
                    if changeable == "hydras_affected_bas":
                        items[i].update_hydras_affected_bas()
                    if changeable == "heartseeker_buff":
                        items[i].update_heartseeker_buff()
                    if changeable == "polys_affected_bas":
                        items[i].update_polys_affected_bas()
                    if changeable == "p_prot":
                        items[i].update_p_prot()
            if items[i].power2 != 0 and (god_class=="mage" or god_class=="guardian"):
                items_power[i] = items[i].power2
            else:
                items_power[i] = items[i].power

        selected_objects[0] = item1
        selected_objects[1] = item2
        selected_objects[2] = item3
        selected_objects[3] = item4
        selected_objects[4] = item5
        selected_objects[5] = item6

        global base_mana
        global mana_per_level
        global base_p_prot
        global p_prot_per_level
        global god_level

        total_ba_flat_buff = item1.ba_flat_buff + item2.ba_flat_buff + item3.ba_flat_buff + item4.ba_flat_buff + item5.ba_flat_buff + item6.ba_flat_buff
        global ba_flat_buff
        ba_flat_buff = total_ba_flat_buff

        total_mages_blessing_buff = item1.mages_blessing_buff + item2.mages_blessing_buff + item3.mages_blessing_buff + item4.mages_blessing_buff + item5.mages_blessing_buff + item6.mages_blessing_buff
        global mages_blessing_buff
        mages_blessing_buff = total_mages_blessing_buff

        total_hydras_multiplier_buff = item1.hydras_multiplier_buff + item2.hydras_multiplier_buff + item3.hydras_multiplier_buff + item4.hydras_multiplier_buff + item5.hydras_multiplier_buff + item6.hydras_multiplier_buff
        global hydras_multiplier_buff
        hydras_multiplier_buff = total_hydras_multiplier_buff

        total_hydras_affected_bas = item1.hydras_affected_bas + item2.hydras_affected_bas + item3.hydras_affected_bas + item4.hydras_affected_bas + item5.hydras_affected_bas + item6.hydras_affected_bas
        global hydras_affected_bas
        hydras_affected_bas = total_hydras_affected_bas

        total_heartseeker_buff = item1.heartseeker_buff + item2.heartseeker_buff + item3.heartseeker_buff + item4.heartseeker_buff + item5.heartseeker_buff + item6.heartseeker_buff
        global heartseeker_buff
        heartseeker_buff = total_heartseeker_buff

        total_crusher_flat_buff = item1.crusher_flat_buff + item2.crusher_flat_buff + item3.crusher_flat_buff + item4.crusher_flat_buff + item5.crusher_flat_buff + item6.crusher_flat_buff
        global crusher_flat_buff
        crusher_flat_buff = total_crusher_flat_buff

        total_crusher_buff_based_on_power = item1.crusher_buff_based_on_power + item2.crusher_buff_based_on_power + item3.crusher_buff_based_on_power + item4.crusher_buff_based_on_power + item5.crusher_buff_based_on_power + item6.crusher_buff_based_on_power
        global crusher_buff_based_on_power
        crusher_buff_based_on_power = total_crusher_buff_based_on_power

        total_poly_buff_based_on_power = item1.poly_buff_based_on_power + item2.poly_buff_based_on_power + item3.poly_buff_based_on_power + item4.poly_buff_based_on_power + item5.poly_buff_based_on_power + item6.poly_buff_based_on_power
        global poly_buff_based_on_power
        poly_buff_based_on_power = total_poly_buff_based_on_power

        total_polys_affected_bas = item1.polys_affected_bas + item2.polys_affected_bas + item3.polys_affected_bas + item4.polys_affected_bas + item5.polys_affected_bas + item6.polys_affected_bas
        global polys_affected_bas
        polys_affected_bas = total_polys_affected_bas

        total_power = item1_power + item2_power + item3_power + item4_power + item5_power + item6_power
        total_cost = item1.cost + item2.cost + item3.cost + item4.cost + item5.cost + item6.cost
        total_mana = base_mana + mana_per_level * god_level + item1.mana + item2.mana + item3.mana + item4.mana + item5.mana + item6.mana
        total_mana_to_power_percent = item1.mana_to_power_percent + item2.mana_to_power_percent + item3.mana_to_power_percent + item4.mana_to_power_percent + item5.mana_to_power_percent + item6.mana_to_power_percent
        total_p_prot = base_p_prot + p_prot_per_level * god_level + item1.p_prot + item2.p_prot + item3.p_prot + item4.p_prot + item5.p_prot + item6.p_prot
        if total_p_prot > 325:
            total_p_prot = 325
        
        total_power = total_power + total_mana_to_power_percent * total_mana
        self.total_power = int(total_power)

        self.total_power_label.text = "Power: " + str(int(total_power))
        self.total_gold_label.text = "Gold required: " + str(int(total_cost))
        self.total_mana_label.text = "Mana: " + str(int(total_mana))

        if self.initialized == 0:
            total_p_prot_label = Label(text=("Physical protections: " + str(int(total_p_prot))),
                                       size_hint=(0.01, 0.01), pos_hint={"x": 0.5, "y": 0.25})
            flt = FloatLayout()
            flt.add_widget(total_p_prot_label)
            self.add_widget(flt)
            self.initialized = 1
        global current_god
        if current_god == "vamana":
            total_power = total_power + total_p_prot * 0.2
            self.total_power_label.text = "Power: " + str(int(total_power))
            self.children[0].children[0].text = "Physical protections: " + str(int(total_p_prot))
            self.children[0].children[0].pos_hint={"x": 0.5, "y": 0.25}
        else:
            self.children[0].children[0].pos_hint={"x": 1.5, "y": 1.5}

        self.manager.get_screen("normal god screen").import_power_from_items(int(total_power))

    remove_mode_state = 0
    edit_mode_state = 0

    def toggle_remove_mode(self):
        remove_states = ["interface_remove_item.png", "interface_remove_item_2.png"]
        edit_states = ["interface_edit_item.png", "interface_edit_item_2.png"]
        if self.remove_mode_state == 0:
            self.remove_mode_state = 1
            self.edit_mode_state = 0
            self.remove_item.source = remove_states[self.remove_mode_state]
            self.edit_item.source = edit_states[self.edit_mode_state]
        elif self.remove_mode_state == 1:
            self.remove_mode_state = 0
            self.remove_item.source = remove_states[self.remove_mode_state]
            
        if self.remove_mode_state == 1 or self.edit_mode_state == 1:
            self.background1.source = "color_golden.png"
            #self.background2.source = "color_golden.png"
        elif self.remove_mode_state == 0 and self.edit_mode_state == 0:
            self.background1.source = "color_gray.png"
            #self.background2.source = "color_gray.png"

    def toggle_edit_mode(self):
        edit_states = ["interface_edit_item.png", "interface_edit_item_2.png"]
        remove_states = ["interface_remove_item.png", "interface_remove_item_2.png"]
        if self.edit_mode_state == 0:
            self.edit_mode_state = 1
            self.remove_mode_state = 0
            self.edit_item.source = edit_states[self.edit_mode_state]
            self.remove_item.source = remove_states[self.remove_mode_state]
        elif self.edit_mode_state == 1:
            self.edit_mode_state = 0
            self.edit_item.source = edit_states[self.edit_mode_state]
        if self.remove_mode_state == 1 or self.edit_mode_state == 1:
            self.background1.source = "color_golden.png"
            #self.background2.source = "color_golden.png"
        elif self.remove_mode_state == 0 and self.edit_mode_state == 0:
            self.background1.source = "color_gray.png"
            #self.background2.source = "color_gray.png"

    def export_power_and_go_back(self):
        global current_god
        if current_god == "fafnir" or current_god == "terra":
            self.manager.get_screen(current_god).import_power_from_items(self.total_power)
            self.manager.current = current_god
        else:
            self.manager.get_screen("normal god screen").import_power_from_items(self.total_power)
            self.manager.current = "normal god screen"

class Items_Screen_2(Screen):
    god_class = ""

    guardian_gods = [ "ares", "artio", "athena", "bacchus", "cabrakan",
                      "cerberus", "fafnir", "ganesha", "geb", "khepri",
                      "kumbhakarna", "kuzenbo", "sobek", "sylvanus", "terra",
                      "xing-tian", "ymir"]

    hunter_gods = [ "ah-muzen-cab", "anhur", "apollo", "artemis", "cernunnos",
                      "chernobog", "chiron", "cupid", "hachiman", "hou-yi",
                      "izanami", "jing-wei", "medusa", "neith", "rama",
                      "skadi", "ullr", "xbalanque"]

    warrior_gods = [ "achilles", "amaterasu", "bellona", "chaac", "cu-chulainn",
                      "erlang-shen", "guan-yu", "hercules", "nike", "odin",
                      "osiris", "sun-wukong", "tyr", "vamana"]

    mage_gods = [ "agni", "ah-puch", "anubis", "ao-kuang", "aphrodite",
                 "baron-samedi", "change", "chronos", "discordia", "freya",
                 "hades", "he-bo", "hel", "isis", "janus",
                 "kukulkan", "nox", "nu-wa", "poseidon", "ra",
                 "raijin", "scylla", "sol", "the-morrigan", "thoth",
                 "vulcan", "zeus", "zhong-kui"]

    assassin_gods = [ "arachne", "awilix", "bakasura", "bastet", "camazotz",
                     "da-ji", "fenrir", "hun-batz", "kali", "loki",
                     "mercury", "ne-zha", "nemesis", "pele", "ratatoskr",
                     "ravana", "serqet", "susano", "thanatos", "thor"]

    warrior_items = [ "item_p_boo1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           "item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           "item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           "item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_kat1", "item_p_kat2", "nothing", "nothing",
                           "item_p_kat3", "item_p_kat4_1", "item_p_kat5", "item_p_kat6",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           "item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           "nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                           "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]

    assassin_items = [ "item_p_boo1", "item_x_sta1_1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           "item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           "item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           "item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_kat1", "item_p_kat2", "nothing", "nothing",
                           "item_p_kat3", "item_p_kat4_1", "item_p_kat5", "item_p_kat6",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           "item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           "nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_x_mas1", "item_x_mas3", "item_x_mas5", "item_x_mas6",
                           "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                           "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]

    hunter_items = [ "item_p_boo1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           "item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           "item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           "item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           "item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           "nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                           "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]

    guardian_items = [ "item_m_sho1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                          "item_m_sho2", "item_m_sho3", "item_m_sho4", "item_m_sho5",
                          "item_m_spe1", "item_m_spe2", "nothing", "nothing",
                          "item_m_spe3_1", "item_m_spe4_1", "item_m_spe5", "item_m_spe6",
                          "item_m_foc1", "item_m_foc2", "item_m_foc6", "nothing",
                          "item_m_foc3", "item_m_foc4", "item_m_foc5", "item_m_foc7",
                          "item_m_unc1", "item_m_unc2", "item_m_unc3", "item_m_unc4",
                          "item_m_unc5", "item_m_unc6", "item_m_unc7", "item_m_unc8_1",
                          "item_m_tin1", "item_m_tin2", "item_m_tin3_1", "item_m_tin4",
                          "nothing", "item_m_tin5", "item_m_tin6_1", "item_m_tin7",
                          "item_m_los1", "item_m_los2", "item_m_los3", "item_m_los4",
                          "nothing", "item_m_los5", "nothing", "nothing",
                          "item_m_eme1", "item_m_eme2", "nothing", "nothing",
                          "item_m_eme3", "item_m_eme4", "item_m_eme5_1", "item_m_eme6",
                          "item_m_imp1", "item_m_imp2", "nothing", "nothing",
                          "nothing", "item_m_imp3", "item_m_imp4", "item_m_imp5",
                          "nothing", "item_m_imp6", "nothing", "nothing",
                          "item_m_dru1", "item_m_dru2", "item_m_dru3", "nothing",
                          "nothing", "item_m_dru4", "item_m_dru5", "nothing",
                          "nothing", "item_m_dru6", "nothing", "nothing",
                          "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                          "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]

    mage_items = [ "item_m_sho1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                          "item_m_sho2", "item_m_sho3", "item_m_sho4", "item_m_sho5",
                          "item_m_spe1", "item_m_spe2", "nothing", "nothing",
                          "item_m_spe3_1", "item_m_spe4_1", "item_m_spe5", "item_m_spe6",
                          "item_m_foc1", "item_m_foc2", "item_m_foc6", "nothing",
                          "item_m_foc3", "item_m_foc4", "item_m_foc5", "item_m_foc7",
                          "item_m_unc1", "item_m_unc2", "item_m_unc3", "item_m_unc4",
                          "item_m_unc5", "item_m_unc6", "item_m_unc7", "item_m_unc8_1",
                          "item_m_tin1", "item_m_tin2", "item_m_tin3_1", "item_m_tin4",
                          "nothing", "item_m_tin5", "item_m_tin6_1", "item_m_tin7",
                          "item_m_los1", "item_m_los2", "item_m_los3", "item_m_los4",
                          "nothing", "item_m_los5", "nothing", "nothing",
                          "item_m_eme1", "item_m_eme2", "nothing", "nothing",
                          "item_m_eme3", "item_m_eme4", "item_m_eme5_1", "item_m_eme6",
                          "item_m_imp1", "item_m_imp2", "nothing", "nothing",
                          "nothing", "item_m_imp3", "item_m_imp4", "item_m_imp5",
                          "nothing", "item_m_imp6", "nothing", "nothing",
                          "item_m_dru1", "item_m_dru2", "item_m_dru3", "nothing",
                          "nothing", "item_m_dru4", "item_m_dru5", "nothing",
                          "nothing", "item_m_dru6", "nothing", "nothing",
                          "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                          "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]

    vamana_items = [ "item_p_boo1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                           "item_p_boo2", "item_p_boo3", "item_p_boo4", "item_p_boo5",
                           "item_p_mor1", "item_p_mor2", "item_p_mor3_1", "nothing",
                           "nothing", "item_p_mor4_1", "item_p_mor5_1", "nothing",
                           "item_p_mac1", "item_p_mac2", "item_p_mac6", "nothing",
                           "item_p_mac3", "item_p_mac4", "item_p_mac5", "item_p_mac7",
                           "item_p_lig1", "item_p_lig2", "item_p_lig3", "nothing",
                           "item_p_hid1", "item_p_hid2", "nothing", "nothing",
                           "item_p_hid3", "item_p_hid4", "item_p_hid5", "nothing",
                           "item_p_shu1", "item_p_shu2", "item_p_shu3", "item_p_shu4",
                           "item_p_spi1", "item_p_spi2", "item_p_spi3_1", "item_p_spi4",
                           "nothing", "item_p_spi5", "item_p_spi6_1", "nothing",
                           "item_p_kat1", "item_p_kat2", "nothing", "nothing",
                           "item_p_kat3", "item_p_kat4_1", "item_p_kat5", "item_p_kat6",
                           "item_p_rou1", "item_p_rou2", "item_p_rou3", "nothing",
                           "nothing", "item_p_rou4", "item_p_rou5_1", "nothing",
                           "nothing", "item_p_rou6", "nothing", "nothing",
                           "nothing", "item_p_rou7", "nothing", "nothing",
                           "item_p_enc1", "item_p_enc2", "item_p_enc3", "item_p_enc4",
                           "item_p_bow1", "item_p_bow2", "item_p_bow3", "nothing",
                           "item_p_cud1", "item_p_cud2", "item_p_cud3", "item_p_cud4",
                           "nothing", "item_p_cud5", "item_p_cud6", "nothing",
                           "item_d_bre1", "item_d_bre2", "nothing", "nothing",
                           "item_d_bre3", "item_d_bre4", "item_d_bre5", "nothing",
                           "item_d_clo1", "item_d_clo2", "item_d_clo3", "item_d_clo4",
                           "item_d_clo5", "item_d_clo6", "item_d_clo7", "item_d_clo8_1",
                           "item_d_glo1_1", "nothing", "nothing", "nothing",
                           "item_d_mai1", "item_d_mai2", "nothing", "nothing",
                           "item_d_mai3", "item_d_mai4", "item_d_mai5", "item_d_mai6"]

    ares_items = [ "item_m_sho1", "item_x_sta1", "item_x_sta2", "item_x_sta3_1",
                          "item_m_sho2", "item_m_sho3", "item_m_sho4", "item_m_sho5",
                          "item_m_spe1", "item_m_spe2", "nothing", "nothing",
                          "item_m_spe3_1", "item_m_spe4_1", "item_m_spe5", "item_m_spe6",
                          "item_m_foc1", "item_m_foc2", "item_m_foc6", "nothing",
                          "item_m_foc3", "item_m_foc4", "item_m_foc5", "item_m_foc7",
                          "item_m_unc1", "item_m_unc2", "item_m_unc3", "item_m_unc4",
                          "item_m_unc5", "item_m_unc6", "item_m_unc7", "item_m_unc8_1",
                          "item_m_tin1", "item_m_tin2", "item_m_tin3_1", "item_m_tin4",
                          "nothing", "item_m_tin5", "item_m_tin6_1", "item_m_tin7",
                          "item_m_los1", "item_m_los2", "item_m_los3", "item_m_los4",
                          "nothing", "item_m_los5", "nothing", "nothing",
                          "item_m_eme1", "item_m_eme2", "nothing", "nothing",
                          "item_m_eme3", "item_m_eme4", "item_m_eme5_1", "item_m_eme6",
                          "item_m_imp1", "item_m_imp2", "nothing", "nothing",
                          "nothing", "item_m_imp3", "item_m_imp4", "item_m_imp5",
                          "nothing", "item_m_imp6", "nothing", "nothing",
                          "item_m_dru1", "item_m_dru2", "item_m_dru3", "nothing",
                          "nothing", "item_m_dru4", "item_m_dru5", "nothing",
                          "nothing", "item_m_dru6", "nothing", "nothing",
                          "item_d_bre2", "item_d_bre3", "item_d_bre4", "item_d_bre5",
                          "item_d_clo7", "item_d_clo8_1", "nothing", "nothing"]

    def initialize(self):
        selected_list = []

        global cidh_mode
        if cidh_mode == 1:
            pass
        
        global current_god                   
        
        for god in self.guardian_gods:
            if current_god == god:
                self.god_class = "guardian"
        for god in self.hunter_gods:
            if current_god == god:
                self.god_class = "hunter"
        for god in self.warrior_gods:
            if current_god == god:
                self.god_class = "warrior"
        for god in self.mage_gods:
            if current_god == god:
                self.god_class = "mage"
        for god in self.assassin_gods:
            if current_god == god:
                self.god_class = "assassin"

        if current_god == "vamana":
            selected_list = self.vamana_items
        elif god_class == "warrior":
            selected_list = self.warrior_items
        elif god_class == "assassin":
            selected_list = self.assassin_items
        elif god_class == "hunter":
            selected_list = self.hunter_items
        elif god_class == "guardian":
            selected_list = self.guardian_items
        elif god_class == "mage":
            selected_list = self.mage_items
            
        elements_number = 0
        for image in selected_list:
            elements_number = elements_number + 1
            
        rows_number = elements_number / 4

        flt = FloatLayout()
        self.add_widget(flt)
        
        scroll = ScrollView( size_hint = (0.9, 0.8), pos_hint = { "x": 0.05, "y": 0.07 } )
        self.children[0].add_widget(scroll)
        
        grid = GridLayout( size_hint = (1,None), col_default_width = 50, row_default_height = 100, cols = 4, rows = rows_number )
        self.buttons = []
        picture = ""
        i = 0
        k = 0
        global selected_items                   
        for item in selected_list:              
            picture = item + ".png"                                              
            for h in selected_items:            
                if picture == h:                
                    picture = "nothing.png"     
                    break                       
            self.buttons.append(ClickableImage(source = picture))
            if item != "nothing":
                k = 1
            if item == "nothing" or picture == "nothing.png":
                k = 0
            if k == 1:
                self.buttons[i].bind(on_press=self.select_item_and_go_back)
            if k == 0:
                self.buttons[i].bind(on_press=self.do_nothing)
            grid.add_widget(self.buttons[i])
            i = i + 1
        grid.bind(minimum_height=grid.setter('height'))
        self.children[0].children[0].add_widget(grid)

    def do_nothing(self, j):
        pass

    def select_item_and_go_back(self, button_object):
        global cidh_mode
        global selected_item_picture
        if cidh_mode == 0:
            selected_item_picture = button_object.source
            self.manager.get_screen("items screen").update_items()
            self.manager.get_screen("items screen").update_labels()
            self.clean_screen()
            self.manager.current = "items screen"
        elif cidh_mode == 1:
            selected_item_picture = button_object.source
            self.manager.get_screen("build screen").update_items()
            self.manager.get_screen("build screen").update_labels()
            self.clean_screen()
            self.manager.current = "build screen"

    def clean_screen(self):
        for button in self.buttons:
            button.source = "nothing.png"
            button.bind(on_press=self.do_nothing)

    def clean_and_go_back(self):
        self.clean_screen()
        global cidh_mode
        if cidh_mode == 0:
            self.manager.current = "items screen"
        else:
            self.manager.current = "build screen"
            
            
class N_Diamonds_HUD(FloatLayout):

    state_ability_1a = ObjectProperty
    state_ability_2a = ObjectProperty
    state_ability_3a = ObjectProperty
    state_ability_4a = ObjectProperty
    state_ability_1b = ObjectProperty
    state_ability_2b = ObjectProperty
    state_ability_3b = ObjectProperty
    state_ability_4b = ObjectProperty

    state_sk1a = NumericProperty(0)
    state_sk2a = NumericProperty(0)
    state_sk3a = NumericProperty(0)
    state_sk4a = NumericProperty(0)
    state_sk1b = NumericProperty(0)
    state_sk2b = NumericProperty(0)
    state_sk3b = NumericProperty(0)
    state_sk4b = NumericProperty(0)

    def change_state_sk(self, index):
        global skills_num
        global skills_with_states
        global double_diamonds

        if skills_num == 2:
            if index == 0:
                state_sk1a = self.state_sk1a
                state_sk1a = state_sk1a + 1
                if state_sk1a == skills_with_states[index]:
                    state_sk1a = state_sk1a - skills_with_states[index]
                self.state_sk1a = state_sk1a
                for i in range(0, 8):
                    if state_sk1a == i:
                        self.picture_1a = current_god + "_diamond_1_" + str(i + 1) + ".png"
            if index == 1:
                state_sk2a = self.state_sk2a
                state_sk2a = state_sk2a + 1
                if state_sk2a == skills_with_states[index]:
                    state_sk2a = state_sk2a - skills_with_states[index]
                self.state_sk2a = state_sk2a
                for i in range(0, 8):
                    if state_sk2a == i:
                        self.picture_2a = current_god + "_diamond_2_" + str(i + 1) + ".png"
            if index == 4 and double_diamonds == True:
                state_sk1b = self.state_sk1b
                state_sk1b = state_sk1b + 1
                if state_sk1b == skills_with_states[2]:
                    state_sk1b = state_sk1b - skills_with_states[2]
                self.state_sk1b = state_sk1b
                for i in range(0, 8):
                    if state_sk1b == i:
                        self.picture_1b = current_god + "_diamond_3_" + str(i + 1) + ".png"
            if index == 5 and double_diamonds == True:
                state_sk2b = self.state_sk2b
                state_sk2b = state_sk2b + 1
                if state_sk2b == skills_with_states[3]:
                    state_sk2b = state_sk2b - skills_with_states[3]
                self.state_sk2b = state_sk2b
                for i in range(0, 8):
                    if state_sk2b == i:
                        self.picture_2b = current_god + "_diamond_4_" + str(i + 1) + ".png"

        if skills_num == 3:
            if index == 0:
                state_sk1a = self.state_sk1a
                state_sk1a = state_sk1a + 1
                if state_sk1a == skills_with_states[index]:
                    state_sk1a = state_sk1a - skills_with_states[index]
                self.state_sk1a = state_sk1a
                for i in range(0, 8):
                    if state_sk1a == i:
                        self.picture_1a = current_god + "_diamond_1_" + str(i + 1) + ".png"
            if index == 1:
                state_sk2a = self.state_sk2a
                state_sk2a = state_sk2a + 1
                if state_sk2a == skills_with_states[index]:
                    state_sk2a = state_sk2a - skills_with_states[index]
                self.state_sk2a = state_sk2a
                for i in range(0, 8):
                    if state_sk2a == i:
                        self.picture_2a = current_god + "_diamond_2_" + str(i + 1) + ".png"
            if index == 2:
                state_sk3a = self.state_sk3a
                state_sk3a = state_sk3a + 1
                if state_sk3a == skills_with_states[index]:
                    state_sk3a = state_sk3a - skills_with_states[index]
                self.state_sk3a = state_sk3a
                for i in range(0, 8):
                    if state_sk3a == i:
                        self.picture_3a = current_god + "_diamond_3_" + str(i + 1) + ".png"
            if index == 4:
                state_sk1b = self.state_sk1b
                state_sk1b = state_sk1b + 1
                if state_sk1b == skills_with_states[3]:
                    state_sk1b = state_sk1b - skills_with_states[3]
                self.state_sk1b = state_sk1b
                for i in range(0, 8):
                    if state_sk1b == i:
                        self.picture_1b = current_god + "_diamond_4_" + str(i + 1) + ".png"
            if index == 5 and double_diamonds == True:
                state_sk2b = self.state_sk2b
                state_sk2b = state_sk2b + 1
                if state_sk2b == skills_with_states[4]:
                    state_sk2b = state_sk2b - skills_with_states[4]
                self.state_sk2b = state_sk2b
                for i in range(0, 8):
                    if state_sk2b == i:
                        self.picture_2b = current_god + "_diamond_5_" + str(i + 1) + ".png"
            if index == 6 and double_diamonds == True:
                state_sk3b = self.state_sk3b
                state_sk3b = state_sk3b + 1
                if state_sk3b == skills_with_states[5]:
                    state_sk3b = state_sk3b - skills_with_states[5]
                self.state_sk3b = state_sk3b
                for i in range(0, 8):
                    if state_sk3b == i:
                        self.picture_3b = current_god + "_diamond_6_" + str(i + 1) + ".png"
            
        if skills_num == 4:
            if index == 0:
                state_sk1a = self.state_sk1a
                state_sk1a = state_sk1a + 1
                if state_sk1a == skills_with_states[index]:
                    state_sk1a = state_sk1a - skills_with_states[index]
                self.state_sk1a = state_sk1a
                for i in range(0, 8):
                    if state_sk1a == i:
                        self.picture_1a = current_god + "_diamond_1_" + str(i + 1) + ".png"
            if index == 1:
                state_sk2a = self.state_sk2a
                state_sk2a = state_sk2a + 1
                if state_sk2a == skills_with_states[index]:
                    state_sk2a = state_sk2a - skills_with_states[index]
                self.state_sk2a = state_sk2a
                for i in range(0, 8):
                    if state_sk2a == i:
                        self.picture_2a = current_god + "_diamond_2_" + str(i + 1) + ".png"
            if index == 2:
                state_sk3a = self.state_sk3a
                state_sk3a = state_sk3a + 1
                if state_sk3a == skills_with_states[index]:
                    state_sk3a = state_sk3a - skills_with_states[index]
                self.state_sk3a = state_sk3a
                for i in range(0, 8):
                    if state_sk3a == i:
                        self.picture_3a = current_god + "_diamond_3_" + str(i + 1) + ".png"
            if index == 3:
                state_sk4a = self.state_sk4a
                state_sk4a = state_sk4a + 1
                if state_sk4a == skills_with_states[index]:
                    state_sk4a = state_sk4a - skills_with_states[index]
                self.state_sk4a = state_sk4a
                for i in range(0, 8):
                    if state_sk4a == i:
                        self.picture_4a = current_god + "_diamond_4_" + str(i + 1) + ".png"
            if index == 4 and double_diamonds == True:
                state_sk1b = self.state_sk1b
                state_sk1b = state_sk1b + 1
                if state_sk1b == skills_with_states[index]:
                    state_sk1b = state_sk1b - skills_with_states[index]
                self.state_sk1b = state_sk1b
                for i in range(0, 8):
                    if state_sk1b == i:
                        self.picture_1b = current_god + "_diamond_5_" + str(i + 1) + ".png"
            if index == 5 and double_diamonds == True:
                state_sk2b = self.state_sk2b
                state_sk2b = state_sk2b + 1
                if state_sk2b == skills_with_states[index]:
                    state_sk2b = state_sk2b - skills_with_states[index]
                self.state_sk2b = state_sk2b
                for i in range(0, 8):
                    if state_sk2b == i:
                        self.picture_2b = current_god + "_diamond_6_" + str(i + 1) + ".png"
            if index == 6 and double_diamonds == True:
                state_sk3b = self.state_sk3b
                state_sk3b = state_sk3b + 1
                if state_sk3b == skills_with_states[index]:
                    state_sk3b = state_sk3b - skills_with_states[index]
                self.state_sk3b = state_sk3b
                for i in range(0, 8):
                    if state_sk3b == i:
                        self.picture_3b = current_god + "_diamond_7_" + str(i + 1) + ".png"
            if index == 7 and double_diamonds == True:
                state_sk4b = self.state_sk4b
                state_sk4b = state_sk4b + 1
                if state_sk4b == skills_with_states[index]:
                    state_sk4b = state_sk4b - skills_with_states[index]
                self.state_sk4b = state_sk4b
                for i in range(0, 8):
                    if state_sk4b == i:
                        self.picture_4b = current_god + "_diamond_8_" + str(i + 1) + ".png"

class N_Skills_HUD(FloatLayout):
    skill_1_level_image = ObjectProperty
    skill_1_level_num = 1

    skill_2_level_image = ObjectProperty
    skill_2_level_num = 1

    skill_3_level_image = ObjectProperty
    skill_3_level_num = 1

    skill_4_level_image = ObjectProperty
    skill_4_level_num = 1

    def level_up_skill_1(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk1_n = self.skill_1_level_num

        if sk1_n < 5:
            sk1_n = sk1_n + 1
            aumentado = True
        if sk1_n == 5 and aumentado == False:
            sk1_n = 0
        #self.skill_1_level_image.source = images[sk1_n]
        self.skill_1_points = images[sk1_n]
        self.skill_1_level_num = sk1_n
        self.skill_1_number = sk1_n

    def level_up_skill_2(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk2_n = self.skill_2_level_num

        if sk2_n < 5:
            sk2_n = sk2_n + 1
            aumentado = True
        if sk2_n == 5 and aumentado == False:
            sk2_n = 0
        #self.skill_2_level_image.source = images[sk2_n]
        self.skill_2_points = images[sk2_n]
        self.skill_2_level_num = sk2_n
        self.skill_2_number = sk2_n

    def level_up_skill_3(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk3_n = self.skill_3_level_num

        if sk3_n < 5:
            sk3_n = sk3_n + 1
            aumentado = True
        if sk3_n == 5 and aumentado == False:
            sk3_n = 0
        #self.skill_3_level_image.source = images[sk3_n]
        self.skill_3_points = images[sk3_n]
        self.skill_3_level_num = sk3_n
        self.skill_3_number = sk3_n

    def level_up_skill_4(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk4_n = self.skill_4_level_num

        if sk4_n < 5:
            sk4_n = sk4_n + 1
            aumentado = True
        if sk4_n == 5 and aumentado == False:
            sk4_n = 0
        #self.skill_4_level_image.source = images[sk4_n]
        self.skill_4_points = images[sk4_n]
        self.skill_4_level_num = sk4_n
        self.skill_4_number = sk4_n

class Fafnir_Screen(Screen):
    min_damage_label = ObjectProperty
    skills_hud = ObjectProperty

    state_ability_1_dwarf = ObjectProperty
    state_ability_2_dwarf = ObjectProperty
    state_ability_3_dwarf = ObjectProperty
    state_ability_1_dragon = ObjectProperty
    state_ability_2_dragon = ObjectProperty
    state_ability_3_dragon = ObjectProperty
    state_ability_4_dragon = ObjectProperty

    three_inputs_widget = ObjectProperty
    
    dragon_basic_attacks_input_widget = ObjectProperty

    min_damage = 0.0

    state_sk_1_dw = False
    state_sk_2_dw = False
    state_sk_3_dw = False
    state_sk_1_dr = False
    state_sk_2_dr = False
    state_sk_3_dr = False
    state_sk_4_dr = False

    def import_power_from_items(self, value):
        self.three_inputs_widget.int_input_2.int_input_textinput.text = str(value)
        self.three_inputs_widget.int_input_2.int_input_num = int(value)

    def change_state_sk_1_dw(self):
        state_sk_1_dw = self.state_sk_1_dw
        state_sk_1_dw = not(state_sk_1_dw)
        self.state_sk_1_dw = not(self.state_sk_1_dw)
        
        if state_sk_1_dw == False:
            self.state_ability_1_dwarf.source = "fafnir_sk_dwarf_off.png"
        if state_sk_1_dw == True:
            self.state_ability_1_dwarf.source = "fafnir_sk_dwarf_on.png"
        
    def change_state_sk_2_dw(self):
        state_sk_2_dw = self.state_sk_2_dw
        state_sk_2_dw = not(state_sk_2_dw)
        self.state_sk_2_dw = not(self.state_sk_2_dw)
        
        if state_sk_2_dw == False:
            self.state_ability_2_dwarf.source = "fafnir_sk_dwarf_off.png"
        if state_sk_2_dw == True:
            self.state_ability_2_dwarf.source = "fafnir_sk_dwarf_on.png"

    def change_state_sk_3_dw(self):
        state_sk_3_dw = self.state_sk_3_dw
        state_sk_3_dw = not(state_sk_3_dw)
        self.state_sk_3_dw = not(self.state_sk_3_dw)
        
        if state_sk_3_dw == False:
            self.state_ability_3_dwarf.source = "fafnir_sk_dwarf_off.png"
        if state_sk_3_dw == True:
            self.state_ability_3_dwarf.source = "fafnir_sk_dwarf_on.png"
            
    def change_state_sk_1_dr(self):
        state_sk_1_dr = self.state_sk_1_dr
        state_sk_1_dr = not(state_sk_1_dr)
        self.state_sk_1_dr = not(self.state_sk_1_dr)
        
        if state_sk_1_dr == False:
            self.state_ability_1_dragon.source = "fafnir_sk_dragon_off.png"
        if state_sk_1_dr == True:
            self.state_ability_1_dragon.source = "fafnir_sk_dragon_on.png"
            
    def change_state_sk_2_dr(self):
        state_sk_2_dr = self.state_sk_2_dr
        state_sk_2_dr = not(state_sk_2_dr)
        self.state_sk_2_dr = not(self.state_sk_2_dr)
        
        if state_sk_2_dr == False:
            self.state_ability_2_dragon.source = "fafnir_sk_dragon_off.png"
        if state_sk_2_dr == True:
            self.state_ability_2_dragon.source = "fafnir_sk_dragon_on.png"
            
    def change_state_sk_3_dr(self):
        state_sk_3_dr = self.state_sk_3_dr
        state_sk_3_dr = not(state_sk_3_dr)
        self.state_sk_3_dr = not(self.state_sk_3_dr)
        
        if state_sk_3_dr == False:
            self.state_ability_3_dragon.source = "fafnir_sk_dragon_off.png"
        if state_sk_3_dr == True:
            self.state_ability_3_dragon.source = "fafnir_sk_dragon_on.png"

    def change_state_sk_4_dr(self):
        state_sk_4_dr = self.state_sk_4_dr
        state_sk_4_dr = not(state_sk_4_dr)
        self.state_sk_4_dr = not(self.state_sk_4_dr)
        
        if state_sk_4_dr == False:
            self.state_ability_4_dragon.source = "fafnir_sk_dragon_off.png"
        if state_sk_4_dr == True:
            self.state_ability_4_dragon.source = "fafnir_sk_dragon_on.png"

    def calculate(self):
        sk1_l = self.skills_hud.skill_1_number
        sk2_l = self.skills_hud.skill_2_number
        sk3_l = self.skills_hud.skill_3_number
        sk4_l = self.skills_hud.skill_4_number

        sk1_dw_state = self.state_sk_1_dw
        sk2_dw_state = self.state_sk_2_dw
        sk3_dw_state = self.state_sk_3_dw
        sk1_dr_state = self.state_sk_1_dr
        sk2_dr_state = self.state_sk_2_dr
        sk3_dr_state = self.state_sk_3_dr
        sk4_dr_state = self.state_sk_4_dr
        
        ba_n = self.three_inputs_widget.int_input_1.int_input_num
        power = self.three_inputs_widget.int_input_2.int_input_num
        god_l = self.three_inputs_widget.int_input_3.int_input_num
        
        dr_ba_n = self.dragon_basic_attacks_input_widget.int_input_num
        
        sk1_dw_d = 0.0
        sk1_dr_d = 0.0
        sk2_dw_d = 0.0
        sk2_dr_d = 0.0
        sk3_dw_d = 0.0
        sk3_dr_d = 0.0
        sk4_d = 0.0
        dr_ba_totald = 0
        dw_ba_totald = 0

######## CHANGE THIS ###########################
        base_ba_d_simple = 37.0
        base_ba_d_per_level = 1.55
        base_ba_d_power_multiplier = 0.2
        ba_progression = [ 1, 1, 1 ]
        sk1_bs = [ 80, 125, 170, 215, 260 ]
        sk1_ps = 0.5
        sk1_bs2 = [ 150, 210, 270, 330, 390 ]
        sk1_ps2 = 0.75
        sk2_buff = [ 0.05, 0.1, 0.15, 0.2, 0.25 ]
        sk3_bs = [ 80, 120, 160, 200, 240 ]
        sk3_ps = 0.6
        sk3_bs2 = [ 120, 180, 240, 300, 360 ]
        sk3_ps2 = 0.9
        sk4_bs = [ 240, 300, 360, 420, 480 ]
        sk4_ps = 1.2
        sk4_bs2 = [ 20, 25, 30, 35, 40 ]
        sk4_ps2 = 0.1
################################################
        
        base_ba_d = float((base_ba_d_simple + base_ba_d_per_level * god_l) + base_ba_d_power_multiplier * power)
        base_dragon_ba_d = float(sk4_bs2[sk4_l - 1] + sk4_ps2 * power)

        if sk1_l != 0 and sk1_dw_state == True:
            sk1_dw_d = sk1_bs[sk1_l - 1] + power*sk1_ps
        if sk1_l != 0 and sk1_dr_state == True:
            sk1_dr_d = sk1_bs2[sk1_l - 1] + power*sk1_ps2
            
        if sk3_l != 0 and sk3_dw_state == True:
            sk3_dw_d = sk3_bs[sk3_l - 1] + power*sk3_ps
        if sk3_l != 0 and sk3_dr_state == True:
            sk3_dr_d = sk3_bs2[sk3_l - 1] + power*sk3_ps2

        if sk2_l != 0 and sk2_dw_state == True:
            sk2_dw_d = sk1_dw_d * sk2_buff[sk2_l - 1] + sk3_dw_d * sk2_buff[sk2_l - 1]
        if sk2_l != 0 and sk2_dr_state == True:
            sk2_dr_d = sk1_dr_d * sk2_buff[sk2_l - 1] + sk3_dr_d * sk2_buff[sk2_l - 1]

        if sk4_l != 0 and sk4_dr_state == True:
            sk4_d = sk4_bs[sk4_l - 1] + power * sk4_ps

        if ba_n != 0:
            index = 0
            while ba_n > 0:
                if index > 2:
                    index = index - 3
                current_basic_attack_damage = 0.0
                current_basic_attack_damage = float(base_ba_d*(ba_progression[index]))
                if sk2_l != 0 and sk2_dw_state == True:
                    current_basic_attack_damage = current_basic_attack_damage + current_basic_attack_damage * sk2_buff[sk2_l - 1]
                if current_basic_attack_damage - int(current_basic_attack_damage) >= 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage) + 1
                elif current_basic_attack_damage - int(current_basic_attack_damage) < 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage)
                dw_ba_totald = dw_ba_totald + current_basic_attack_damage
                index = index + 1
                ba_n = ba_n - 1

        if dr_ba_n != 0:
            while dr_ba_n > 0:
                current_ba_d = 0.0
                current_ba_d = float(base_dragon_ba_d)
                if sk2_l != 0 and sk2_dr_state == True:
                    current_ba_d = current_ba_d + current_ba_d * sk2_buff[sk2_l - 1]
                dr_ba_totald = dr_ba_totald + current_ba_d
                dr_ba_n = dr_ba_n - 1
        
        self.min_damage = sk1_dw_d + sk1_dr_d + sk2_dw_d + sk2_dr_d + sk3_dw_d + sk3_dr_d + sk4_d + dw_ba_totald + dr_ba_totald
        self.min_damage_label.text = "Damage: " + str(int(self.min_damage))

class Terra_Screen(Screen):
    total_damage_label = ObjectProperty
    skills_hud = ObjectProperty
    
    three_inputs_widget = ObjectProperty

    skill_5_level = ObjectProperty
    total_damage = 0.0

    skill_5_level_num = 1

    state_ability_1 = ObjectProperty
    state_ability_2a = ObjectProperty
    state_ability_2b = ObjectProperty

    state_sk1 = 0
    state_sk2a = 0
    state_sk2b = 0

    passive_basic_attacks_input_widget = ObjectProperty

    def import_power_from_items(self, value):
        self.three_inputs_widget.int_input_2.int_input_textinput.text = str(value)
        self.three_inputs_widget.int_input_2.int_input_num = int(value)

    def change_state_sk1(self):
        state_sk1 = self.state_sk1
        state_sk1 = state_sk1 + 1
        if state_sk1 == 2:
            state_sk1 = state_sk1 - 2
        self.state_sk1 = state_sk1
        
        if state_sk1 == 0:
            self.state_ability_1.source = "terra_sk_state_1-2.png"
        if state_sk1 == 1:
            self.state_ability_1.source = "terra_sk_state_1.png"

    def change_state_sk2a(self):
        state_sk2a = self.state_sk2a
        state_sk2a = state_sk2a + 1
        if state_sk2a == 3:
            state_sk2a = state_sk2a - 3
        self.state_sk2a = state_sk2a
        
        if state_sk2a == 0:
            self.state_ability_2a.source = "terra_sk_state_0.png"
        if state_sk2a == 1:
            self.state_ability_2a.source = "terra_sk_state_1-2.png"
            self.state_sk2b = 0
            self.state_ability_2b.source = "terra_sk_state_0.png"
        if state_sk2a == 2:
            self.state_ability_2a.source = "terra_sk_state_1.png"
            self.state_sk2b = 0
            self.state_ability_2b.source = "terra_sk_state_0.png"

    def change_state_sk2b(self):
        state_sk2b = self.state_sk2b
        state_sk2b = state_sk2b + 1
        if state_sk2b == 3:
            state_sk2b = state_sk2b - 3
        self.state_sk2b = state_sk2b
        
        if state_sk2b == 0:
            self.state_ability_2b.source = "terra_sk_state_0.png"
        if state_sk2b == 1:
            self.state_ability_2b.source = "terra_sk_state_1-2.png"
            self.state_sk2a = 0
            self.state_ability_2a.source = "terra_sk_state_0.png"
        if state_sk2b == 2:
            self.state_ability_2b.source = "terra_sk_state_1.png"
            self.state_sk2a = 0
            self.state_ability_2a.source = "terra_sk_state_0.png"

    def level_up_skill_5(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk5_n = self.skill_5_level_num

        if sk5_n < 5:
            sk5_n = sk5_n + 1
            aumentado = True
        if sk5_n == 5 and aumentado == False:
            sk5_n = 0
            
        self.skill_5_level.source = images[sk5_n]
        self.skill_5_level_num = sk5_n
        #self.skill_5_number = sk5_n
        

    def calculate(self):
        sk1_l = self.skills_hud.skill_1_number
        sk2_l = self.skills_hud.skill_2_number
        sk3_l = self.skills_hud.skill_4_number
        sk4_l = self.skill_5_level_num
        
        ba_n = self.three_inputs_widget.int_input_1.int_input_num
        power = self.three_inputs_widget.int_input_2.int_input_num
        god_l = self.three_inputs_widget.int_input_3.int_input_num
        
        pas_ba_n = self.passive_basic_attacks_input_widget.int_input_num

        sk1_d = 0.0
        sk2_d = 0.0
        sk3_d = 0.0
        sk4_d = 0.0
        ba_totald = 0
        pas_ba_totald = 0

        state_sk1 = self.state_sk1
        state_sk2a = self.state_sk2a
        state_sk2b = self.state_sk2b

######## CHANGE THIS ###########################
        base_ba_d_simple = 38.0
        base_ba_d_per_level = 1.55
        base_ba_d_power_multiplier = 0.2
        ba_progression = [ 1, 1, 1 ]
        sk0_bs = 7
        sk0_ps = 0.1
        sk1_bs = [ 60, 110, 160, 210, 260 ]
        sk1_ps = 0.3
        sk2_bs = [ 50, 85, 120, 155, 190 ]
        sk2_ps = 0.35
        sk2_bs2 = [ 60, 110, 160, 210, 260 ]
        sk2_ps2 = 0.35
        sk3_bs = [ 70, 100, 130, 170, 200 ]
        sk3_ps = 0.5
        sk3_bs2 = [ 10, 12, 14, 16, 18 ]
        sk3_ps2 = 0.05
        sk4_bs = [ 200, 250, 300, 350, 400 ]
        sk4_ps = 0.6
################################################

        
        
        base_ba_d = float((base_ba_d_simple + base_ba_d_per_level * god_l) + base_ba_d_power_multiplier * power)

        if sk1_l != 0 and state_sk1 == 0:
            sk1_d = sk1_bs[sk1_l - 1] + power * sk1_ps
        if sk1_l != 0 and state_sk1 == 1:
            sk1_d = sk1_bs[sk1_l - 1] * 2 + power * sk1_ps * 2

        if sk2_l != 0 and state_sk2a == 1:
            sk2_d = sk2_bs[sk2_l - 1] + power * sk2_ps
        if sk2_l != 0 and state_sk2a == 2:
            sk2_d = sk2_bs[sk2_l - 1] * 2 + power * sk2_ps * 2

        if sk2_l != 0 and state_sk2b == 1:
            sk2_d = sk2_bs2[sk2_l - 1] + power * sk2_ps2
        if sk2_l != 0 and state_sk2b == 2:
            sk2_d = sk2_bs2[sk2_l - 1] * 2 + power * sk2_ps2 * 2

        if sk3_l != 0:
            sk3_d = sk3_bs[sk3_l - 1] + power*sk3_ps
            sk3_d = sk3_d + sk3_bs2[sk3_l - 1] * 10 + power * sk3_ps2 * 10
        if sk4_l != 0:
            sk4_d = sk4_bs[sk4_l - 1] + power*sk4_ps
            
        if ba_n != 0:
            index = 0
            while ba_n > 0:
                if index > 2:
                    index = index - 3
                current_basic_attack_damage = 0.0
                current_basic_attack_damage = float(base_ba_d*(ba_progression[index]))
                if current_basic_attack_damage - int(current_basic_attack_damage) >= 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage) + 1
                elif current_basic_attack_damage - int(current_basic_attack_damage) < 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage)
                ba_totald = ba_totald + current_basic_attack_damage
                index = index + 1
                ba_n = ba_n - 1

        if pas_ba_n != 0:
            index = 0
            while pas_ba_n > 0:
                if index > 2:
                    index = index - 3
                current_basic_attack_damage = 0.0
                current_basic_attack_damage = float(base_ba_d*(ba_progression[index]))
                if current_basic_attack_damage - int(current_basic_attack_damage) >= 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage) + 1
                elif current_basic_attack_damage - int(current_basic_attack_damage) < 0.5:
                    current_basic_attack_damage = int(current_basic_attack_damage)
                pas_ba_totald = pas_ba_totald + current_basic_attack_damage + sk0_bs + power * sk0_ps
                index = index + 1
                pas_ba_n = pas_ba_n - 1
        
        self.total_damage = sk1_d + sk2_d + sk3_d + sk4_d + ba_totald + pas_ba_totald

        self.total_damage_label.text = "Damage: " + str(int(self.total_damage))

class ScrollableLabel(ScrollView):
    text = StringProperty('')

class Two_Skills_HUD(FloatLayout):
    skill_1_level_image = ObjectProperty
    skill_1_level_num = 1

    skill_2_level_image = ObjectProperty
    skill_2_level_num = 1

    skill_1_number = NumericProperty
    skill_2_number = NumericProperty

    def level_up_skill_1(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk1_n = self.skill_1_level_num

        if sk1_n < 5:
            sk1_n = sk1_n + 1
            aumentado = True
        if sk1_n == 5 and aumentado == False:
            sk1_n = 0
        self.skill_1_level_image.source = images[sk1_n]
        self.skill_1_level_num = sk1_n
        self.skill_1_number = sk1_n

    def level_up_skill_2(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk2_n = self.skill_2_level_num

        if sk2_n < 5:
            sk2_n = sk2_n + 1
            aumentado = True
        if sk2_n == 5 and aumentado == False:
            sk2_n = 0
        self.skill_2_level_image.source = images[sk2_n]
        self.skill_2_level_num = sk2_n
        self.skill_2_number = sk2_n

class Three_Skills_HUD(FloatLayout):
    skill_1_level_image = ObjectProperty
    skill_1_level_num = 1

    skill_2_level_image = ObjectProperty
    skill_2_level_num = 1

    skill_3_level_image = ObjectProperty
    skill_3_level_num = 1

    skill_1_number = NumericProperty
    skill_2_number = NumericProperty
    skill_3_number = NumericProperty

    def level_up_skill_1(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk1_n = self.skill_1_level_num

        if sk1_n < 5:
            sk1_n = sk1_n + 1
            aumentado = True
        if sk1_n == 5 and aumentado == False:
            sk1_n = 0
        self.skill_1_level_image.source = images[sk1_n]
        self.skill_1_level_num = sk1_n
        self.skill_1_number = sk1_n

    def level_up_skill_2(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk2_n = self.skill_2_level_num

        if sk2_n < 5:
            sk2_n = sk2_n + 1
            aumentado = True
        if sk2_n == 5 and aumentado == False:
            sk2_n = 0
        self.skill_2_level_image.source = images[sk2_n]
        self.skill_2_level_num = sk2_n
        self.skill_2_number = sk2_n

    def level_up_skill_3(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk3_n = self.skill_3_level_num

        if sk3_n < 5:
            sk3_n = sk3_n + 1
            aumentado = True
        if sk3_n == 5 and aumentado == False:
            sk3_n = 0
        self.skill_3_level_image.source = images[sk3_n]
        self.skill_3_level_num = sk3_n
        self.skill_3_number = sk3_n

class Four_Skills_HUD(FloatLayout):
    skill_1_level_image = ObjectProperty
    skill_1_level_num = 1

    skill_2_level_image = ObjectProperty
    skill_2_level_num = 1

    skill_3_level_image = ObjectProperty
    skill_3_level_num = 1

    skill_4_level_image = ObjectProperty
    skill_4_level_num = 1

    skill_1_number = NumericProperty
    skill_2_number = NumericProperty
    skill_3_number = NumericProperty
    skill_4_number = NumericProperty

    def level_up_skill_1(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk1_n = self.skill_1_level_num

        if sk1_n < 5:
            sk1_n = sk1_n + 1
            aumentado = True
        if sk1_n == 5 and aumentado == False:
            sk1_n = 0
        self.skill_1_level_image.source = images[sk1_n]
        self.skill_1_level_num = sk1_n
        self.skill_1_number = sk1_n

    def level_up_skill_2(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk2_n = self.skill_2_level_num

        if sk2_n < 5:
            sk2_n = sk2_n + 1
            aumentado = True
        if sk2_n == 5 and aumentado == False:
            sk2_n = 0
        self.skill_2_level_image.source = images[sk2_n]
        self.skill_2_level_num = sk2_n
        self.skill_2_number = sk2_n

    def level_up_skill_3(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk3_n = self.skill_3_level_num

        if sk3_n < 5:
            sk3_n = sk3_n + 1
            aumentado = True
        if sk3_n == 5 and aumentado == False:
            sk3_n = 0
        self.skill_3_level_image.source = images[sk3_n]
        self.skill_3_level_num = sk3_n
        self.skill_3_number = sk3_n

    def level_up_skill_4(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk4_n = self.skill_4_level_num

        if sk4_n < 5:
            sk4_n = sk4_n + 1
            aumentado = True
        if sk4_n == 5 and aumentado == False:
            sk4_n = 0
        self.skill_4_level_image.source = images[sk4_n]
        self.skill_4_level_num = sk4_n
        self.skill_4_number = sk4_n

class Four_Skills_Terra_HUD(FloatLayout):
    skill_1_level_image = ObjectProperty
    skill_1_level_num = 1

    skill_2_level_image = ObjectProperty
    skill_2_level_num = 1

    skill_4_level_image = ObjectProperty
    skill_4_level_num = 1

    skill_1_number = NumericProperty
    skill_2_number = NumericProperty
    skill_4_number = NumericProperty

    def level_up_skill_1(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk1_n = self.skill_1_level_num

        if sk1_n < 5:
            sk1_n = sk1_n + 1
            aumentado = True
        if sk1_n == 5 and aumentado == False:
            sk1_n = 0
        self.skill_1_level_image.source = images[sk1_n]
        self.skill_1_level_num = sk1_n
        self.skill_1_number = sk1_n

    def level_up_skill_2(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk2_n = self.skill_2_level_num

        if sk2_n < 5:
            sk2_n = sk2_n + 1
            aumentado = True
        if sk2_n == 5 and aumentado == False:
            sk2_n = 0
        self.skill_2_level_image.source = images[sk2_n]
        self.skill_2_level_num = sk2_n
        self.skill_2_number = sk2_n

    def level_up_skill_4(self):
        images = ["sk_l_0.jpg", "sk_l_1.jpg", "sk_l_2.jpg", "sk_l_3.jpg", "sk_l_4.jpg", "sk_l_5.jpg"]
        aumentado = False
        sk4_n = self.skill_4_level_num

        if sk4_n < 5:
            sk4_n = sk4_n + 1
            aumentado = True
        if sk4_n == 5 and aumentado == False:
            sk4_n = 0
        self.skill_4_level_image.source = images[sk4_n]
        self.skill_4_level_num = sk4_n
        self.skill_4_number = sk4_n

class BackButton(Button):
    pass

class God_Icon(ClickableImage):
    pass

class Three_Int_Inputs(FloatLayout):
    int_input_1 = ObjectProperty
    int_input_2 = ObjectProperty
    int_input_3 = ObjectProperty

class IntInput(FloatLayout):
    int_input_textinput = ObjectProperty
    int_input_num = NumericProperty
    existe_cero = BooleanProperty

    def save_int(self):
        if self.int_input_textinput.text != "" and int(self.int_input_textinput.text) != 0:
            self.int_input_num = int(self.int_input_textinput.text)
        elif self.int_input_textinput.text == "" and self.existe_cero == True:
            self.int_input_num = 0
        elif self.int_input_textinput.text == "" and self.existe_cero == False:
            self.int_input_num = 1
        elif int(self.int_input_textinput.text) == 0 and self.existe_cero == False:
            self.int_input_num = 1
        if self.title == "Lvl:":
            global god_level
            god_level = self.int_input_num
            

class God_BigImage(ClickableImage):
    pass

class CalculateButton(Button):
    pass

class DamageLabel(Label):
    pass

class ClickableDiamond(ClickableImage):
    pass

class sm(ScreenManager):
    pass
        
class DylanApp(App):
    def build(self):
        return sm()

if __name__ == "__main__":
    DylanApp().run()
