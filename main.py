import flet as ft


# COLORES

PINK = "#E8C5CC"
CREAM = "#F8F4EF"
BROWN = "#352B2B"
WHITE = "#FFFFFF"


# PRODUCTOS

products = [
    {
        "name": "Vinyl Ink",
        "brand": "Maybelline",
        "category": "Makeup",
        "price": "$14.00",
        "description": "Labial líquido de larga duración con acabado brillante.",
        "malls": "Multiplaza, Albrook Mall y Metromall",
        "image": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=500"
    },
    {
        "name": "Soft Pinch Blush",
        "brand": "Rare Beauty",
        "category": "Makeup",
        "price": "$25.00",
        "description": "Rubor líquido de textura ligera y color intenso.",
        "malls": "Multiplaza y Albrook Mall",
        "image": "https://images.unsplash.com/photo-1599733589046-833f2d6a7e8c?w=500"
    },
    {
        "name": "Samba OG",
        "brand": "Adidas",
        "category": "Shoes",
        "price": "$85.00",
        "description": "Zapatillas clásicas de Adidas que combinan con diferentes estilos.",
        "malls": "Multiplaza, Albrook Mall, Metromall y AltaPlaza",
        "image": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500"
    },
    {
        "name": "Oversized Blazer",
        "brand": "Zara",
        "category": "Clothing",
        "price": "$45.00",
        "description": "Blazer de corte amplio para crear outfits elegantes y casuales.",
        "malls": "Multiplaza, Albrook Mall y AltaPlaza",
        "image": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=500"
    },
    {
        "name": "Lip Gloss",
        "brand": "Maybelline",
        "category": "Makeup",
        "price": "$10.00",
        "description": "Brillo labial para dar luminosidad e hidratación a los labios.",
        "malls": "Multiplaza, Albrook Mall y Metromall",
        "image": "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=500"
    },
    {
        "name": "Air Force 1",
        "brand": "Nike",
        "category": "Shoes",
        "price": "$90.00",
        "description": "Zapatillas icónicas de Nike con un diseño clásico y versátil.",
        "malls": "Multiplaza, Albrook Mall y Metromall",
        "image": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500"
    },
    {
        "name": "Shoulder Bag",
        "brand": "Zara",
        "category": "Accessories",
        "price": "$30.00",
        "description": "Bolso de hombro ideal para complementar outfits diarios.",
        "malls": "Multiplaza, Albrook Mall y AltaPlaza",
        "image": "https://images.unsplash.com/photo-1584917865442-de89df76afd3?w=500"
    },
    {
        "name": "Stan Smith",
        "brand": "Adidas",
        "category": "Shoes",
        "price": "$80.00",
        "description": "Zapatillas minimalistas con un diseño sencillo y atemporal.",
        "malls": "Multiplaza, Albrook Mall y Metromall",
        "image": "https://images.unsplash.com/photo-1525966222134-fcfa99b8ae77?w=500"
    },
    {
        "name": "Classic Handbag",
        "brand": "Zara",
        "category": "Accessories",
        "price": "$35.00",
        "description": "Bolso clásico que puede utilizarse en ocasiones casuales o elegantes.",
        "malls": "Multiplaza, Albrook Mall y AltaPlaza",
        "image": "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=500"
    },
    {
        "name": "Fit Me Foundation",
        "brand": "Maybelline",
        "category": "Makeup",
        "price": "$13.00",
        "description": "Base de maquillaje ligera con acabado natural.",
        "malls": "Multiplaza, Albrook Mall y Metromall",
        "image": "https://images.unsplash.com/photo-1631214540242-2d8e1e7e3c6d?w=500"
    },
    {
        "name": "Basic T-Shirt",
        "brand": "Zara",
        "category": "Clothing",
        "price": "$20.00",
        "description": "Camiseta básica fácil de combinar con diferentes prendas.",
        "malls": "Multiplaza, Albrook Mall y Metromall",
        "image": "https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=500"
    },
    {
        "name": "Crossbody Bag",
        "brand": "Zara",
        "category": "Accessories",
        "price": "$28.00",
        "description": "Bolso cruzado práctico para llevar tus objetos personales.",
        "malls": "Multiplaza, Albrook Mall y AltaPlaza",
        "image": "https://images.unsplash.com/photo-1548036328-c9fa89d128fa?w=500"
    },
    {
        "name": "Lipstick",
        "brand": "Maybelline",
        "category": "Makeup",
        "price": "$12.00",
        "description": "Labial clásico disponible en diferentes tonos y acabados.",
        "malls": "Multiplaza, Albrook Mall y Metromall",
        "image": "https://images.unsplash.com/photo-1586495777744-4413f21062fa?w=500"
    }
]


# TENDENCIAS

trends = [
    {
        "name": "Burgundy Outfits",
        "description": "La tendencia burgundy utiliza tonos vino y rojo oscuro. Se puede combinar con negro, beige, gris y blanco."
    },
    {
        "name": "Chocolate Brown",
        "description": "Consiste en utilizar diferentes tonos marrones para crear outfits elegantes y fáciles de combinar."
    },
    {
        "name": "Balletcore",
        "description": "Estilo inspirado en el ballet. Incluye prendas delicadas, tonos suaves, lazos, faldas y bailarinas."
    },
    {
        "name": "Oversized Clothing",
        "description": "Consiste en usar prendas de corte amplio, como camisetas grandes, blazers y pantalones holgados."
    },
    {
        "name": "Minimalist Accessories",
        "description": "Accesorios sencillos y delicados que complementan un outfit sin hacerlo demasiado llamativo."
    }
]


# BEAUTY

beauty = [
    {
        "name": "Clean Girl Makeup",
        "description": "Maquillaje de apariencia natural que utiliza tonos suaves, cejas peinadas y acabados luminosos."
    },
    {
        "name": "Cherry Makeup",
        "description": "Maquillaje inspirado en los tonos cereza, con labios y mejillas en tonos rojizos o rosados."
    },
    {
        "name": "Lip Products",
        "description": "Incluye gloss, lip oils y labiales que ayudan a dar color y brillo a los labios."
    },
    {
        "name": "Blush Trends",
        "description": "Diferentes formas de aplicar rubor para complementar el maquillaje y darle color a las mejillas."
    },
    {
        "name": "Skincare",
        "description": "Rutinas de cuidado de la piel que incluyen limpieza, hidratación y protección solar."
    }
]


# CENTROS COMERCIALES

malls = [
    {
        "name": "Multiplaza Panamá",
        "description": "Centro comercial con diferentes tiendas de moda, accesorios y belleza.",
        "url": "https://www.google.com/maps/search/?api=1&query=Multiplaza+Panama"
    },
    {
        "name": "Albrook Mall",
        "description": "Uno de los centros comerciales más grandes de Panamá, con variedad de tiendas.",
        "url": "https://www.google.com/maps/search/?api=1&query=Albrook+Mall+Panama"
    },
    {
        "name": "Metromall",
        "description": "Centro comercial con tiendas de ropa, calzado y productos de belleza.",
        "url": "https://www.google.com/maps/search/?api=1&query=Metromall+Panama"
    },
    {
        "name": "AltaPlaza Mall",
        "description": "Centro comercial con tiendas de moda, restaurantes y entretenimiento.",
        "url": "https://www.google.com/maps/search/?api=1&query=AltaPlaza+Mall+Panama"
    },
    {
        "name": "Soho Mall",
        "description": "Centro comercial ubicado en el área de Obarrio, con diferentes establecimientos.",
        "url": "https://www.google.com/maps/search/?api=1&query=Soho+Mall+Panama"
    }
]


def main(page: ft.Page):

    page.title = "Fashion Finder"
    page.bgcolor = CREAM
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO

    # CONTENEDOR PRINCIPAL

    content = ft.Column(
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
        expand=True
    )

    # TITULOS

    def make_title(text):
        return ft.Text(
            text,
            size=27,
            weight=ft.FontWeight.BOLD,
            color=BROWN,
            text_align=ft.TextAlign.CENTER
        )

    # TARJETAS DE PRODUCTOS

    def product_card(product):

        details = ft.Container(
            visible=False,
            bgcolor=CREAM,
            padding=10,
            border_radius=10,
            content=ft.Column(
                [
                    ft.Text(
                        product["description"],
                        color=BROWN,
                        size=14,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        "Marca: " + product["brand"] +
                        "\nPrecio de ejemplo: " + product["price"] +
                        "\nCategoría: " + product["category"] +
                        "\nTiendas donde puedes consultar: " + product["malls"],
                        color=BROWN,
                        size=13,
                        text_align=ft.TextAlign.CENTER
                    )
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8
            )
        )

        def toggle_details(e):
            details.visible = not details.visible
            page.update()

        return ft.Container(
            width=190,
            bgcolor=WHITE,
            padding=12,
            border_radius=15,
            content=ft.Column(
                [
                    ft.Image(
                        src=product["image"],
                        width=160,
                        height=145,
                        fit=ft.BoxFit.COVER
                    ),
                    ft.Text(
                        product["name"],
                        size=16,
                        weight=ft.FontWeight.BOLD,
                        color=BROWN,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        product["brand"],
                        color=BROWN,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Text(
                        product["price"],
                        color=BROWN,
                        weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Button(
                        "Ver detalles",
                        bgcolor=PINK,
                        color=BROWN,
                        on_click=toggle_details
                    ),
                    details
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=8
            )
        )

    # TARJETAS DE TENDENCIAS Y BEAUTY

    def information_card(item):

        details = ft.Container(
            visible=False,
            bgcolor=CREAM,
            padding=12,
            border_radius=10,
            content=ft.Text(
                item["description"],
                color=BROWN,
                size=14,
                text_align=ft.TextAlign.CENTER
            )
        )

        def toggle_details(e):
            details.visible = not details.visible
            page.update()

        return ft.Container(
            width=220,
            bgcolor=WHITE,
            padding=18,
            border_radius=15,
            content=ft.Column(
                [
                    ft.Text(
                        item["name"],
                        size=18,
                        weight=ft.FontWeight.BOLD,
                        color=BROWN,
                        text_align=ft.TextAlign.CENTER
                    ),
                    ft.Button(
                        "Conocer más",
                        bgcolor=PINK,
                        color=BROWN,
                        on_click=toggle_details
                    ),
                    details
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=12
            )
        )

    # INICIO

    def show_home(e=None):

        content.controls.clear()

        content.controls.extend([
            ft.Text(
                "FASHION FINDER",
                size=35,
                weight=ft.FontWeight.BOLD,
                color=BROWN,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Text(
                "Discover your style",
                size=18,
                italic=True,
                color=BROWN,
                text_align=ft.TextAlign.CENTER
            ),
            ft.Image(
                src="https://images.unsplash.com/photo-1483985988355-763728e1935b?w=1000",
                width=650,
                height=300,
                fit=ft.BoxFit.COVER
            ),
            ft.Text(
                "Explore fashion, beauty and the latest trends.",
                size=17,
                color=BROWN,
                text_align=ft.TextAlign.CENTER
            )
        ])

        page.update()

    # PRODUCTOS

    def show_products(e=None):

        content.controls.clear()

        search = ft.TextField(
            label="Search products",
            width=350,
            bgcolor=WHITE,
            border_color=PINK,
            text_align=ft.TextAlign.CENTER
        )

        category = ft.Dropdown(
            label="Category",
            width=350,
            value="All",
            options=[
                ft.dropdown.Option("All"),
                ft.dropdown.Option("Makeup"),
                ft.dropdown.Option("Shoes"),
                ft.dropdown.Option("Clothing"),
                ft.dropdown.Option("Accessories")
            ],
            border_color=PINK
        )

        product_list = ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            run_spacing=15
        )

        def filter_products(e=None):

            product_list.controls.clear()

            text = search.value.lower() if search.value else ""
            selected = category.value

            for product in products:

                matches_text = (
                    text in product["name"].lower()
                    or text in product["brand"].lower()
                    or text in product["category"].lower()
                )

                matches_category = (
                    selected == "All"
                    or product["category"] == selected
                )

                if matches_text and matches_category:
                    product_list.controls.append(product_card(product))

            if len(product_list.controls) == 0:
                product_list.controls.append(
                    ft.Text(
                        "No products found.",
                        color=BROWN,
                        text_align=ft.TextAlign.CENTER
                    )
                )

            page.update()

        search.on_change = filter_products
        category.on_change = filter_products

        content.controls.extend([
            make_title("PRODUCTS"),
            search,
            category,
            product_list
        ])

        filter_products()
        page.update()

    # TENDENCIAS

    def show_trends(e=None):

        content.controls.clear()

        cards = ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            run_spacing=15
        )

        for trend in trends:
            cards.controls.append(information_card(trend))

        content.controls.extend([
            make_title("FASHION TRENDS"),
            ft.Text(
                "Discover the latest fashion styles.",
                color=BROWN,
                size=16,
                text_align=ft.TextAlign.CENTER
            ),
            cards
        ])

        page.update()

    # BEAUTY

    def show_beauty(e=None):

        content.controls.clear()

        cards = ft.Row(
            wrap=True,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15,
            run_spacing=15
        )

        for item in beauty:
            cards.controls.append(information_card(item))

        content.controls.extend([
            make_title("BEAUTY"),
            ft.Text(
                "Explore makeup and skincare trends.",
                color=BROWN,
                size=16,
                text_align=ft.TextAlign.CENTER
            ),
            cards
        ])

        page.update()

    # UBICACIONES

    def show_stores(e=None):

        content.controls.clear()

        cards = ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=15
        )

        for mall in malls:

            cards.controls.append(
                ft.Container(
                    width=500,
                    bgcolor=WHITE,
                    padding=18,
                    border_radius=15,
                    content=ft.Column(
                        [
                            ft.Text(
                                mall["name"],
                                size=19,
                                weight=ft.FontWeight.BOLD,
                                color=BROWN,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Text(
                                mall["description"],
                                color=BROWN,
                                text_align=ft.TextAlign.CENTER
                            ),
                            ft.Button(
                                "Ver ubicación en Google Maps",
                                bgcolor=PINK,
                                color=BROWN,
                                action=ft.OpenUrl(
                                    url=mall["url"],
                                    target=ft.UrlTarget.BLANK
                                )
                            )
                        ],
                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        spacing=10
                    )
                )
            )

        content.controls.extend([
            make_title("STORE LOCATIONS"),
            ft.Text(
                "Find shopping malls in Panama.",
                color=BROWN,
                size=16,
                text_align=ft.TextAlign.CENTER
            ),
            cards
        ])

        page.update()

    # NAVEGACIÓN

    navigation = ft.Row(
        [
            ft.Button(
                "HOME",
                on_click=show_home,
                bgcolor=PINK,
                color=BROWN
            ),
            ft.Button(
                "PRODUCTS",
                on_click=show_products,
                bgcolor=PINK,
                color=BROWN
            ),
            ft.Button(
                "TRENDS",
                on_click=show_trends,
                bgcolor=PINK,
                color=BROWN
            ),
            ft.Button(
                "BEAUTY",
                on_click=show_beauty,
                bgcolor=PINK,
                color=BROWN
            ),
            ft.Button(
                "STORES",
                on_click=show_stores,
                bgcolor=PINK,
                color=BROWN
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        wrap=True,
        spacing=8
    )

    # MOSTRAR TODO CENTRADO

    page.add(
        ft.Column(
            [
                navigation,
                content
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=25,
            expand=True
        )
    )

    show_home()


ft.run(main)