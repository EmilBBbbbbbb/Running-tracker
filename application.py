import flet as ft
import os
import base64

from user_info.models.database import DATABASE_NAME, Session, create_db
from user_info.models.user import User

session = Session()

# Database creation
db_is_created: bool = os.path.exists(DATABASE_NAME)
if not db_is_created:
    create_db()
    user = User(name="User name", email='', password='', avatar='')
    session.add(user)
session.commit()


# Getting username
def get_username() -> str:
    name: str = ''
    for u in session.query(User):
        name = u.name

    return name


# Getting avatar
def get_avatar() -> str:
    for u in session.query(User):
        if u.avatar != '':
            return u.avatar
        else:
            return u.basic_avatar


def main(page: ft.Page):
    page.title = "Тренировки бега"
    page.theme_mode = 'light'
    page.window.height = 852
    page.window.width = 394
    page.window.resizable = False
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Receiving a picture
    def pick_result(e: ft.FilePickerResultEvent) -> None:
        path: str = ''
        if not e.files:
            pass
        else:
            for el in e.files:
                path = el.path

            # Converting an image to base64
            with open(path, 'rb') as img:
                ava_base64 = base64.b64encode(img.read()).decode('utf-8')
                users = session.query(User).all()
                for u in users:
                    u.avatar = ava_base64
        session.commit()

        # Avatar update
        user_avatar.image_src_base64 = get_avatar()
        page.update()

    # Start creating avatar block

    # BG ellipse
    ellipse = ft.Container(
        bgcolor='#EFEFEF',
        shape=ft.BoxShape.CIRCLE,
        height=520,
        width=520,
        margin=ft.Margin(-80, -146, 0, 0),

    )

    # User name
    user_name = ft.Text(value=get_username(),
                        color="black",
                        size=24,
                        weight=ft.FontWeight.W_100,
                        opacity=0.5,
                        font_family="Roboto")

    # User avatar
    user_avatar = ft.Container(image_src_base64=get_avatar(),
                               height=176,
                               width=176,
                               shape=ft.BoxShape.CIRCLE,
                               on_click=lambda _: pick_dialog.pick_files(allow_multiple=False))
    avatar_block = ft.Stack(
        [
            ellipse,
            ft.Column([ft.Container(content=user_avatar,
                                    height=278,
                                    width=374,
                                    alignment=ft.alignment.bottom_center),

                       ft.Container(content=user_name,
                                    height=30,
                                    width=374,
                                    alignment=ft.alignment.bottom_center)])

        ],
        width=520,
        height=520,
    )

    # End creating avatar block

    pick_dialog = ft.FilePicker(on_result=pick_result)
    page.overlay.append(pick_dialog)

    page.add(ft.Row([avatar_block], alignment=ft.MainAxisAlignment.CENTER))


ft.app(target=main)
