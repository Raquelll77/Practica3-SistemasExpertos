import flet as ft

def main(page: ft.Page):
    page.window.width =360
    page.window.height =640
    page.padding = 0  
    page.spacing = 0  
    page.window.resizable = False 
    page.update()
    page.bgcolor = ft.colors.GREY_300  # Simula el fondo de una barra de estado

    # Elementos de la barra de notificaciones
    puntitos = ft.Text("····", size=30, weight=ft.FontWeight.BOLD, color="white")
    movistar = ft.Text("movistar", size=12, color="white")
    iconoWifi = ft.Icon(name=ft.icons.WIFI, size=16, color="white")
    hora = ft.Text("06:45 PM", size=12, color="white")
    iconoCarga = ft.Icon(name=ft.icons.BATTERY_5_BAR_ROUNDED, size=20, color="white", rotate=ft.Rotate(angle=1.5708))

    #PARTE 2 DEL HEADER
    iconoView = ft.Icon(name=ft.icons.REMOVE_RED_EYE_OUTLINED, size=35, color="white")
    textHeader = ft.Text("Explore", size=25, color="white")
    iconoCamara = ft.Icon(name=ft.icons.VIDEO_CAMERA_FRONT_ROUNDED, size=35, color="white")

    # Sección 1: "Movistar" con puntos e ícono WiFi
    seccion_izquierda = ft.Row(
        controls=[puntitos, movistar, iconoWifi],
        alignment=ft.MainAxisAlignment.START,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=1
    )

    # Sección 2: Hora al centro
    seccion_centro = ft.Row(
        controls=[hora],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Sección 3: Ícono de batería a la derecha
    seccion_derecha = ft.Row(
        controls=[iconoCarga],
        alignment=ft.MainAxisAlignment.END,
        vertical_alignment=ft.CrossAxisAlignment.CENTER
    )

    # Fila principal con las tres secciones
    fila_notificacion = ft.Row(
        controls=[
            ft.Container(content=seccion_izquierda, expand=1, alignment=ft.alignment.center_left),
            ft.Container(content=seccion_centro, expand=1, alignment=ft.alignment.center),
            ft.Container(content=seccion_derecha, expand=1, alignment=ft.alignment.center_right),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        
    )

    fila2_header = ft.Row(
        controls= [
            ft.Container(content=iconoView),
            ft.Container(content = textHeader),
            ft.Container(content=iconoCamara)       
        ],
        alignment= ft.MainAxisAlignment.SPACE_BETWEEN
    )

    headerContainer = ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(content=fila_notificacion),
                ft.Container(content=fila2_header)
            ],
            spacing=0
        ),
        bgcolor="#20C997", 
        padding=ft.padding.only(top=0, right=10, bottom=10, left=10) ,  # Espaciado interno opcional
    )

    #body

    def button_clicked(e):
        t.value = f"Textboxes values are:  '{textInput}'."
        page.update()
    
    t = ft.Text()

    textInput = ft.TextField(label="Search people or tags", bgcolor="white", border_width=0, prefix_icon=ft.Icon(ft.Icons.SEARCH))

    textoCard1 = ft.Text("Popular Now", color="black")
    textoCard2 = ft.Text("On the Rise", color="black")

    iconoCard1 = ft.Icon(name =ft.icons.STAR_HALF_ROUNDED, size=60, color="yellow")
    iconoCard2 = ft.Icon(name = ft.icons.ARROW_UPWARD_OUTLINED, size=60, color="blue")

    acciones = ft.Container(
        content= ft.Column(
            controls= [
                ft.Container(content=iconoCard1),
                ft.Container(content=textoCard1)
            ]
        )
    )

    card_style = {
        "width": 160,  # Ancho de cada tarjeta
        "height": 90,  # Alto de cada tarjeta
        "bgcolor": "white",  # Fondo blanco
        "border_radius": 5,  # Bordes redondeados
        "padding": 0,  # Espaciado interno
        "alignment": ft.alignment.center  # Alinear contenido al centro
    }

    # Tarjeta 1: "Popular Now"
    card1 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(name=ft.icons.STAR, size=40, color="orange"),
                ft.Text("Popular Now", size=18, weight=ft.FontWeight.BOLD, color="black")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        **card_style
    )

    # Tarjeta 2: "On the Rise"
    card2 = ft.Container(
        content=ft.Column(
            controls=[
                ft.Icon(name=ft.icons.ARROW_UPWARD, size=40, color="blue"),
                ft.Text("On the Rise", size=18, weight=ft.FontWeight.BOLD, color="black")
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        ),
        **card_style
    )



    # Contenedor principal con las tarjetas en una fila
    card_row = ft.Row(
        controls=[card1, card2],
      #  alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        spacing=1,  # Espacio entre las tarjetas
    )

    acciones = ft.Container(content=card_row, padding=0)


    imagen = ft.Image(
        src="https://cdn-icons-png.flaticon.com/512/12355/12355749.png",
        width=60,  # Ajustar tamaño
        height=60
    )

    imagen2 = ft.Image(
        src="https://cdn-icons-png.flaticon.com/512/6381/6381807.png",
        width=60,  # Ajustar tamaño
        height=60
    )

    imagen3 = ft.Image(
        src="https://cdn-icons-png.flaticon.com/512/3529/3529417.png",
        width=60,  # Ajustar tamaño
        height=60
    )

    imagen4 = ft.Image(
        src="https://cdn-icons-png.flaticon.com/512/14705/14705555.png",
        width=60,  # Ajustar tamaño
        height=60
    )



    targeta1 = ft.Container(
        content= ft.Column(
            controls= [
                ft.Row(
                    controls=[
                        imagen,
                        ft.Text("Comedy", size=22, weight=ft.FontWeight.W_500, color="white")]
                )
            ]
        ),
        bgcolor="pink",
        padding=5,
        border_radius=5
    )

    targeta2 = ft.Container(
        content= ft.Column(
            controls= [
                ft.Row(
                    controls=[
                        imagen2,
                        ft.Text("Art and Experimental", size=22, weight=ft.FontWeight.W_500, color="white")]
                )
            ]
        ),
        bgcolor="orange",
        padding=5,
        border_radius=5
    )

    targeta3 = ft.Container(
        content= ft.Column(
            controls= [
                ft.Row(
                    controls=[
                        imagen3,
                        ft.Text("Scary", size=22, weight=ft.FontWeight.W_500, color="white")]
                )
            ]
        ),
        bgcolor="black",
        padding=5,
        border_radius=5
    )

    targeta4 = ft.Container(
        content= ft.Column(
            controls= [
                ft.Row(
                    controls=[
                        imagen4,
                        ft.Text("Cats", size=22, weight=ft.FontWeight.W_500, color="white")]
                )
            ]
        ),
        bgcolor="blue",
        padding=5,
        border_radius=5
    )



    bodyContainer = ft.Container(
        content= ft.Column(
            controls= [
                ft.Container(content=textInput),
                ft.Container(content=acciones),
                ft.Container(content=
                     ft.Row(controls= [ft.Text("Channels", color="black", size=12)],
                        alignment= ft.MainAxisAlignment.CENTER
                     )
                ),
                ft.Container(content=targeta1),
                ft.Container(content=targeta2),
                ft.Container(content=targeta3),
                ft.Container(content=targeta4)
            ],
            alignment= ft.MainAxisAlignment.CENTER
        ),
        padding=10,
        
    )
    

    page.add(headerContainer, bodyContainer)

ft.app(target=main, view=ft.FLET_APP)
