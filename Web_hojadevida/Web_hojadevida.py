import reflex as rx

def navbar():
    return rx.hstack(
        rx.link("Informacion personal", href="/", margin_left="2rem",color="black", padding="0.5rem 1rem", border_radius="0.5rem", _hover={"color": "white", "bg": "#004d40"}),
        rx.divider(orientation="vertical", width="2px", margin_left="1rem",margin_right="1rem", bg="black",  ),
        rx.link("Experiencia", href="/experiencia", color="black", padding="0.5rem 1rem", border_radius="0.5rem", _hover={"color": "white", "bg": "#004d40"}),
        rx.divider(orientation="vertical", width="2px", margin_left="1rem", margin_right="1rem",bg="black",  ),        
        rx.link("Habilidades y Educación", href="/educacion", color="black", padding="0.5rem 1rem", border_radius="0.5rem", _hover={"color": "white", "bg": "#004d40"}),
        spacing="4",  
        padding="0.5rem", 
        bg="#E0E0E0",  
        color="black",  
        width="100%",  
        justify="start",  
        top="0",
        position="sticky",
        z_index="1000",
    )

def index():
    return rx.vstack(
        navbar(), 
        rx.heading("Informacion Personal",  margin_left="2.3rem", margin_top="2rem", font_family="IBM Plex Mono"),
        rx.divider( height="3px",width="90%", margin_left="2rem", margin_bottom="1rem",bg="#0da68c",  ),
        rx.hstack(
            rx.image(src="/foto.png", width="200px", height="auto", margin_left="3rem", border_radius="50%"),
            rx.vstack(
                rx.hstack(
                rx.avatar(src="/user.png", size="1"),
                rx.text("Nombre "),
                ),
                rx.divider( height="2px",width="90%",margin_left="2rem", margin_top="-0.8rem",bg="#004d40" ),
                
                rx.text("Juan Fernando Montoya", margin_left="3rem"),
                rx.hstack(
                rx.avatar(src="/suitcase.png", size="1"),
                rx.text("Profesión "),
                ),
                rx.divider( height="2px",width="90%",margin_left="2rem", margin_top="-0.8rem",bg="#004d40" ),
                rx.text("Estudiante en desarollo de software", margin_left="3rem"),
                rx.hstack(
                rx.avatar(src="/phone-call.png", size="1"),
                rx.text("Telefono "),
                ),
                rx.divider( height="2px",width="90%",margin_left="2rem", margin_top="-0.8rem",bg="#004d40" ),
                rx.text("+57 323 235 7586", margin_left="3rem"),
                rx.hstack(
                rx.avatar(src="/envelope.png", size="1"),
                rx.text("Email "),
                ),
                rx.divider( height="2px",width="90%",margin_left="2rem", margin_top="-0.8rem",bg="#004d40" ),
                rx.text("montoyajuan750@gmail.com", margin_left="3rem"),
                align_items="start",
                margin_left="1rem"
            ),
            rx.hstack(
            rx.vstack(
                rx.hstack(
                rx.avatar(src="/acerca.png", size="1"),
                rx.text("Sobre mi "),
                ),
                rx.divider( height="2px",margin_left="2rem", margin_top="-0.8rem",bg="#004d40", width="95%"),
                rx.text("Desarrollador de software altamente motivado y creativo, con una sólida base en python, React, JavaScript, Apasionado por aprender nuevas tecnologías y resolver desafíos complejos, me adapto rápidamente a diferentes entornos de trabajo y colaboro eficazmente en equipos multidisciplinarios. Mi responsabilidad y dedicación me han permitido entregar proyectos de alta calidad", margin_left="3rem"),
                align_items="start",
                width="80%",  
                margin_left="3rem",
            ),
            align_items="start",
            margin_top="2rem",
        ),
        

        margin_top="1.3rem",
        ),
        rx.hstack(
        rx.link(
            rx.avatar(src="/instagram.png", size="2"),
            href="https://www.instagram.com/_nand0.03/",
            is_external=True,  
            margin_left="4.5rem"), 

        rx.link(
            rx.avatar(src="/github.png", size="2"),
            href="https://github.com/nando0105",
            is_external=True,  
            margin_left="0.8rem"), 
        rx.link(
            rx.avatar(src="/linkedin.png", size="2"),
            href="https://www.linkedin.com/in/juan-fernando-montoya-22ba17186/",
            is_external=True,  
            margin_left="0.8rem"),
        ),       
        height="100vh",
        bg="#F5F5F5",
        color="black",  
        font_family="IBM Plex Mono",
    )

def experiencia():
    return rx.vstack(
        navbar(),  
        rx.heading("Experiencia",  margin_left="2.3rem", margin_top="2rem", font_family="IBM Plex Mono"),
        rx.divider( height="3px",width="90%", margin_left="2rem", margin_bottom="1rem",bg="#0da68c",  ),  
        height="100vh",
        bg="#F5F5F5",
        color="black",  
        font_family="IBM Plex Mono",
    )

def educacion():
    return rx.vstack(
        navbar(), 
        
        rx.heading("Habilidades y Educación", margin_left="2.3rem", margin_top="2rem", font_family="IBM Plex Mono"),
        rx.divider(height="3px", width="90%", margin_left="2rem", margin_bottom="1rem", bg="#0da68c"),
        rx.hstack(
            rx.tabs.root(
                rx.tabs.list(
                    rx.tabs.trigger("Habilidades Tecnicas", value="tab1", color="black", padding="0.5rem 1rem", border_radius="0.5rem", _hover={"color": "white", "bg": "#004d40"}, bg="#E0E0E0", margin="0.5rem"),
                    rx.tabs.trigger("Habilidades Blandas", value="tab2", color="black", padding="0.5rem 1rem", border_radius="0.5rem", _hover={"color": "white", "bg": "#004d40"}, bg="#E0E0E0", margin="0.5rem"),
                ),
                rx.tabs.content(
                    rx.hstack(
                        rx.vstack(
                        rx.text("Django", margin_left="3rem"),
                        rx.progress(value=30, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("GitHub", margin_left="3rem"),
                        rx.progress(value=15, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("SQL", margin_left="3rem"),
                        rx.progress(value=20, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("MySQL", margin_left="3rem"),
                        rx.progress(value=25, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("MongoDB", margin_left="3rem"),
                        rx.progress(value=33, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        width="100%",
                        ),
                        rx.vstack(
                        rx.text("Python", margin_left="3rem"),
                        rx.progress(value=35, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("JavaScript", margin_left="3rem"),
                        rx.progress(value=20, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("React", margin_left="3rem"),
                        rx.progress(value=28, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("HTML", margin_left="3rem"),
                        rx.progress(value=60, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        rx.text("CSS", margin_left="3rem"),
                        rx.progress(value=60, max=100, margin_left="3rem", color_scheme="jade", variant="classic", width="80%"),
                        width="100%",
                        ),
                        width="150%",
                        margin_top="1rem"
                    ),
                    value="tab1",
                ),
                rx.tabs.content(
                    rx.list(
                        rx.list_item("Comunicación Efectiva"),
                        rx.list_item("Trabajo en Equipo"),
                        rx.list_item("Resolución de Problemas"),
                        rx.list_item("Adaptabilidad"),
                        rx.list_item("Gestión del Tiempo"),
                        rx.list_item("Pensamiento Crítico"),
                        rx.list_item("Creatividad"),
                        rx.list_item("Empatía"),
                        rx.list_item("Liderazgo"),
                        rx.list_item("Aprendizaje Continuo"),
                        list_style_type="circle",
                        margin_top="1rem",
                    ),
                    margin_left="4rem",
                    spacing="2",
                    value="tab2",
                ),
                default_value="tab1",
                orientation="horizontal",
                margin_left="2rem",
            ),
        
            rx.vstack(
                rx.heading("Educación", margin_left="2.3rem", margin_top="2rem", font_family="IBM Plex Mono"),
                rx.divider(height="3px", width="70%", margin_left="2rem", margin_bottom="1rem", bg="#0da68c"),
                rx.text("Tecnologia en desarrollo de software", margin_left="3rem"),
                rx.text("Universidad del Valle", margin_left="3rem"),
                rx.text("2022 - Actualidad", margin_left="3rem"),
                rx.divider(height="2px", width="70%", margin_left="2rem", margin_bottom="1rem", bg="black"),
                rx.text("Bachiller Académico", margin_left="3rem"),
                rx.text("Institución Educativa Francisco Jose de Caldas", margin_left="3rem"),
                rx.text("2016 - 2021", margin_left="3rem"),
                
                margin_left="20%",
                width="100%",
            ),
            margin_bottom="2rem",
            width="100%",
        ),
        height="100vh",
        bg="#F5F5F5",
        color="black",
        font_family="IBM Plex Mono",
    )


app = rx.App()
app.add_page(index, title="Inicio")
app.add_page(experiencia, route="/experiencia", title="Experiencia")
app.add_page(educacion, route="/educacion", title="Habilidades y Educacion")

