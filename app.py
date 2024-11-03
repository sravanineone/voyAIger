# voyAIger
# Import packages and modules | External
import streamlit as st

# Import packages and modules | Internal
from voyAIger_package import config as cfg

# Function: main
def main() -> None:
    # Set header and logo images
    st.logo("images/voyAIger_header.png", icon_image="images/voyAIger_logo.png")

    # Initialize the session variables
    
    # Set navigation pages
    home_page = st.Page(page="nav_pages/home.py", title="Home", icon=":material/home:")
    account_page = st.Page(page="nav_pages/account.py", title="Account", icon=":material/account_circle:")
    travel_page = st.Page(page="nav_pages/travel.py", title="Travel", icon=":material/map:")
    voyaige_page = st.Page(page="nav_pages/voyaige.py", title="voyAIge", icon=":material/smart_toy:")

    # Enable sidebar navigation menu
    sidebar_navigation_menu = st.navigation(pages=[home_page, account_page, travel_page, voyaige_page], position="sidebar")
    sidebar_navigation_menu.run()

# Main handler
if __name__ == '__main__':
    main()
