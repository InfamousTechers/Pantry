from unicodedata import category
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.responsivelayout import MDResponsiveLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList, OneLineAvatarIconListItem, ImageLeftWidget, IconLeftWidget
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window

from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from datetime import datetime

Window.size = (400, 700)

colors = {
    "Pink": {
        "200": "#f4c2c2",
        "500": "#f4c2c2",
        "700": "#f4c2c2"
    },
    "Teal": {
        "200": "#212121",
        "500": "#212121",
        "700": "#212121",
    },
    "Red": {
        "200": "#C25554",
        "500": "#C25554",
        "700": "#C25554",
    },
    "Light": {
        "StatusBar": "#f4c2c2",
        "AppBar": "#202020",
        "Background": "#FFFFFF",
        "CardsDialogs": "#FFFFFF",
        "FlatButtonDown": "#CCCCCC",
    },
    "Brand": {
        "StatusBar": "#464d99",
        "AppBar": "#21263b",
        "Background": "#040817",
        "CardsDialogs": "#3d476b",
        "FlatButtonDown": "#CCCCCC"
    }
}

KV = '''
<CommonComponentLabel>
    halign: "center"


<MobileView>
    MDNavigationLayout:
        MDScreenManager:
            MDScreen:
                MDBoxLayout:
                    orientation: "vertical"
                    id: box

                    MDTopAppBar:
                        title: "Pantry"
                        right_action_items: [["home", lambda x: app.shelf()],["cart", lambda x: app.cart()],]
                        left_action_items: [["cupboard", lambda x: nav_drawer.set_state("open")]]
                        elevation: 4

                    MDBoxLayout:
                        id: "screen"

                    MDFloatingActionButton:
                        icon: 'plus'
                        on_release: app.add_category() #functionality to be added later
                        elevation_normal: 12
                        pos_hint: {'x': .8, 'y':.05}
        
        MDNavigationDrawer:
            id: nav_drawer
            close_on_click: True

            ContentNavigationDrawer:
                id: content_drawer
                orientation: 'vertical'
                padding: "5dp"
                spacing: "5dp"

                AnchorLayout:
                    anchor_x: "left"
                    size_hint_y: None
                    height: avatar.height

                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "56dp", "56dp"
                        source: "cupboard.png"

                MDLabel:
                    text: "Patry"
                    font_style: "Button"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "brandon.m.paahla@gmail.com"
                    font_style: "Caption"
                    size_hint_y: None
                    height: self.texture_size[1]

                ScrollView:

                    Card:
                        source:'cooking.png'
                        text:"Groceries"
                        size_hint: None, None
                        # size: ("20dp", "20dp")
                        on_release:lambda x: print("Im touched")

                    # OneLineAvatarIconListItem:
                    #     ImageLeftWidget:
                    #         source:'cooking.png'
                    #         text:"Groceries"
                    #         on_release:lambda x: self.show_groceries()

                    # OneLineAvatarIconListItem:
                    #     ImageLeftWidget:
                    #         source:'fitness.png'
                    #         text:"Gym supplies"
                    #         on_release:lambda x: print("Click 2")

                    # OneLineAvatarIconListItem:
                    #     ImageLeftWidget:
                    #         source:'toiletries.png'
                    #         text:"Toiletries"
                    #         on_release:lambda x: print("Click 2")

                    # OneLineAvatarIconListItem:
                    #     ImageLeftWidget:
                    #         source:'fruits.png'
                    #         text:"Fruits"
                    #         on_release:lambda x: print("Click 2")
    
<TabletView>
    CommonComponentLabel:
        text: "Table"


<DesktopView>
    CommonComponentLabel:
        text: "Desktop"


ResponsiveView:
'''

class CommonComponentLabel(MDLabel):
    pass


class DialogContent(MDBoxLayout):
    """OPENS A DIALOG BOX THAT GETS THE TASK FROM THE USER"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_save(self, instance, value, date_range):
        """This functions gets the date from the date picker and converts its it a
        more friendly form then changes the date label on the dialog to that"""
        pass


class ContentNavigationDrawer(MDBoxLayout):
    pass


class MobileView(MDScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TabletView(MDScreen):
    pass


class DesktopView(MDScreen):
    pass


class ResponsiveView(MDResponsiveLayout, MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.mobile_view = MobileView()
        self.tablet_view = TabletView()
        self.desktop_view = DesktopView()


class Pantry(MDApp):
    dialog = None
    theme_light = True

    def toggle_theme(self):
        pass

    def build(self):
        self.theme_cls.colors = colors
        self.theme_cls.primary_palette = "Pink"
        return Builder.load_string(KV)

    def cart(self):
        print("cart pressed")

    def shelf(self):
        print("Home pressed")

    def add_groceries(self):
        print("adding groceries")

    def add_category(self):
        # if not self.dialog:
        #     self.dialog = MDDialog(
        #         title="Add Iterm",
        #         type="custom",
        #         content_cls=DialogContent(),
        #     )
        # self.dialog.open()
        print("Adding category")


Pantry().run()
