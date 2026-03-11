# golfstore

Aplicación web desarrollada con Python y Django como proyecto final del curso de desarrollo web con Django.

El objetivo del proyecto es simular una tienda online de artículos de golf, donde se pueden gestionar productos, categorías y usuarios, implementando las principales funcionalidades del framework Django siguiendo el patrón de arquitectura MVT (Model - View - Template).

FUNCIONALIDADES PRINCIPALES:

- Gestión de Productos (CRUD completo)

El sistema permite administrar productos de la tienda mediante operaciones CRUD:

Crear nuevos productos

Visualizar la lista de productos disponibles

Editar información de productos existentes

Eliminar productos

Cada producto incluye:

Nombre

Marca

Precio

Descripción

Imagen del producto

Subcategoría asociada

- Sistema de Categorías y Subcategorías

Los productos se organizan en una estructura jerárquica:

Categorías principales

Palos

Indumentaria

Subcategorías

Ejemplos:

Drivers

Hierros

Putters

Polos

Zapatos

Accesorios

Esto permite organizar mejor los productos dentro de la tienda.

- Búsqueda de productos

La aplicación incluye un formulario de búsqueda que permite consultar la base de datos y filtrar productos por nombre.

El sistema muestra dinámicamente los resultados coincidentes.

- Sistema de autenticación de usuarios

Se implementa el sistema de autenticación provisto por Django:

Registro de nuevos usuarios

Login

Logout

- Perfil de usuario

Los usuarios autenticados pueden visualizar información básica de su cuenta.

Interfaz responsive

- El sitio utiliza Bootstrap para lograr un diseño moderno y adaptable a diferentes dispositivos.

Incluye:

Navbar responsive con menú hamburguesa

Tarjetas (cards) para mostrar productos

Formularios estilizados

Layout limpio y organizado

- Página About

- La aplicación incluye una página About donde se describe el propósito del proyecto y su autor.

Tecnologías utilizadas

Python

Django

SQLite

Bootstrap

HTML

CSS