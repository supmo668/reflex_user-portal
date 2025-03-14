import reflex_user_portal.config as CONFIG
import reflex as rx
import reflex_clerk as clerk

from reflex_user_portal.pages.landing import home, signin_page
from reflex_user_portal.pages.admin import admin_settings, users_table
from reflex_user_portal.pages.portal import about, profile, app_settings, overview
import reflex_user_portal.styles as styles

# Create app instance
app = rx.App(
    style=styles.base_style,
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&display=swap",
    ]
)

# Add pages
app.add_page(home, route="/", title="Home")

# Portal pages
app.add_page(overview)
app.add_page(users_table)
app.add_page(profile)
app.add_page(admin_settings)
app.add_page(about)
app.add_page(app_settings)

# sign-ins
app.add_page(signin_page, route="/sign-in")
app.add_page(signin_page, route="/sign-up")

clerk.install_pages(
    app,
    publishable_key=CONFIG.CLERK_PUBLISHABLE_KEY,
    signin_route="/sign-in",
    signup_route="/sign-up"
)