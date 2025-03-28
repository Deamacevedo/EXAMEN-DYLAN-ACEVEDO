# Music Artist Management System

## Description

This project is a Python-based system designed to manage information about musical artists, countries, and genres, with detailed report generation.

## Problem Statement

The music industry requires an efficient way to organize and manage artists, their country of origin, and their musical genres. Currently, keeping track of artists, their debut years, and associated albums is challenging without a structured system. This project aims to centralize all this information, allowing users to register, modify, and analyze musical data efficiently.

## Technologies & Tools

- **Python 3**: Core programming language for development.
- **JSON**: Used for data storage and persistence.

## Features

### **Artist Management**

- Complete registration of musical artists.
- Storage of detailed information:
  - Artist name
  - Country of origin
  - Music genre
  - Debut year
  - Albums and certifications
- Functionalities:
  - Add, edit, and delete artists.
  - View a detailed list of registered artists.

### **Country Management**

- Register and manage artists' countries of origin.
- Functionalities:
  - Add, edit, and delete countries.
  - Display all registered countries.

### **Music Genre Management**

- Register and manage musical genres associated with artists.
- Functionalities:
  - Add, edit, and delete genres.
  - Display available genres.

### **Reports & Queries**

- **Artists active in the last 10 years**.
- **Artists by country and time range** (e.g., artists from the UK between 1960-1970).
- **Number of artists per musical genre** (e.g., Rock/Pop).
- Data is organized into clear and structured reports.

## System Structure Overview

- **Artists**: Dictionary containing name, country, genre, debut year, and albums.
- **Countries**: Dictionary with country names and codes.
- **Genres**: Dictionary with genre names and descriptions.

## Technical Considerations

- **Persistence**: Data is stored and managed using JSON files.
- **Modularity**: The system is organized into modular functions for artist, country, and genre management.
- **Validation**: Ensures unique artist names and proper data integrity before processing records.

## Requirements

- Python 3.x
- JSON library for data handling
- GitHub for version control

## Best Practices

- Use modular functions for better code clarity and reusability.
- Implement clear and descriptive variable and function names.
- Validate user input to prevent errors and ensure data integrity.

## Example Execution

```
"""
Bienvenido al portal usuario
1.Agregar Artista
2.Editar Artista
3.Eliminar Artista
4.Editar País
5.Eliminar País
6.Editar genero
7.Eliminar genero
8.Reporte: Artistas Últimos 10 Años
9.Reporte: Número de Artistas por Año
10.Reporte: Unidades Certificadas en 2023
11.Salir
"""

```



## Authors

- Developed by **Dylan Acevedo**

