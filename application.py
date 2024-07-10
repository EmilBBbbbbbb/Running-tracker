import flet as ft
import os

from user_info.models.database import DATABASE_NAME, Session, create_db
from user_info.models.user import User

session = Session()

# Database creation
db_is_created: bool = os.path.exists(DATABASE_NAME)
if not db_is_created:
    create_db()
    user = User(name="User name", email='', password='')
    session.add(user)
session.commit()


# Getting username
def get_username() -> str:
    name: str = ''
    for u in session.query(User):
        name = u.name

    return name


def main(page: ft.Page):
    page.title = "Тренировки бега"
    page.theme_mode = 'light'
    page.window.height = 852
    page.window.width = 394
    # page.window_resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    ellipse = ft.Container(
        bgcolor='#E1E1E1',
        shape=ft.BoxShape.CIRCLE,
        height=520,
        width=520,
        margin=ft.Margin(-80, -146, 0, 0),

    )

    user_name = ft.Text(value=get_username(),
                        color="black",
                        size=24,
                        weight=ft.FontWeight.W_100,
                        opacity=0.5,
                        font_family="Roboto")

    avatar_block = ft.Stack(
        [
            ellipse,
            ft.Container(content=user_name,
                         height=300,
                         width=374,
                         alignment=ft.alignment.bottom_center)

        ],
        width=520,
        height=520,
    )
    page.add(ft.Row([avatar_block], alignment=ft.MainAxisAlignment.CENTER))


ft.app(target=main)
