import streamlit as st
from streamlit_option_menu import option_menu
import pags.collectionSpider, pags.profileSpider

st.set_page_config(
    page_title="Keras"
)

class MultiApp:
    def __init__(self) -> None:
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Data",
                options=["Profile Spider", "Collection Spider"],
                default_index=1,
                styles={
                "container": {"padding": "4!important","background-color":'black'},
                "icon": {"color": "white", "font-size": "23px"}, 
                "nav-link": {"color":"white","font-size": "18px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21", "font-size": "18px"},
                }
            )  
        if app == "Profile Spider":
            pags.profileSpider.app()  
        if app == "Collection Spider":
            pags.collectionSpider.app()

    run()      