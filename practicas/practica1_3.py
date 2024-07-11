# App en Lenguaje Flet

import flet as ft

# Crear la función main
def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.DARK
    page.update()

    # Función para crear un par de contenedor de imagen y contenedor de información
    def create_image_info_pair(image_url, info_text):
        image_container = ft.Container(
            bgcolor=ft.colors.BLUE,
            height=200,
            alignment=ft.alignment.center,
            content=ft.Image(
                src=image_url,
                scale=ft.Scale('0.5')
            )
        )

        info_container = ft.Container(
            bgcolor=ft.colors.ORANGE,
            height=50,
            alignment=ft.alignment.center,
            content=ft.Row(
                controls=[
                    ft.Text(info_text, color=ft.colors.BLACK)
                ]
            )
        )

        return ft.Column(
            controls=[
                image_container,
                info_container
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )

    # Crear pares de contenedor de imagen y contenedor de información
    image_info_pair_1 = create_image_info_pair(
        'https://img2.freepnges.com/20240204/ab/transparent-gotham-city-cartoon-of-batman-in-black-costume-with-1710887279786.webp',
        "Batman 1"
    )

    image_info_pair_2 = create_image_info_pair(
        'https://img2.freepnges.com/20240204/ab/transparent-gotham-city-cartoon-of-batman-in-black-costume-with-1710887279786.webp',
        "Batman 2"
    )

    image_info_pair_3 = create_image_info_pair(
        'https://img2.freepnges.com/20240204/ab/transparent-gotham-city-cartoon-of-batman-in-black-costume-with-1710887279786.webp',
        "Batman 3"
    )

    # Contenedor Principal
    main_layout = ft.Container(
        width=600,
        height=800,
        alignment=ft.alignment.center,
        border_radius=ft.border_radius.all(30),
        bgcolor=ft.colors.GREEN,
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        image_info_pair_1,
                        image_info_pair_2
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10
                ),
                image_info_pair_3
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=10
        )
    )

    page.add(main_layout)

# Mostrar App en el Desktop
ft.app(target=main)

# Mostrar en Web
# ft.app(target=main, view=ft.WEB_BROWSER)
