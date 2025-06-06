"""  
Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición, casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias para poder realizar las siguientes actividades:
-   a. eliminar el nodo que contiene la información de Linterna Verde;
-   b. mostrar el año de aparición de Wolverine;
-   c. cambiar la casa de Dr. Strange a Marvel;
-   d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”;
-   e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
-   f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
-   g. mostrar toda la información de Flash y Star-Lord;
-   h. listar los superhéroes que comienzan con la letra B, M y S;
-   i. determinar cuántos superhéroes hay de cada casa de comic.
"""

from list_ import List

superheroes = List([
    {"name": "Linterna Verde", "alias": "Green Lantern", "real_name": "Hal Jordan", "short_bio": "Un héroe con anillo de poder", "first_appearance": 1959, "comic_house": "DC"},
    {"name": "Wolverine", "alias": "Logan", "real_name": "James Howlett", "short_bio": "Héroe con garras de adamantium", "first_appearance": 1974, "comic_house": "Marvel"},
    {"name": "Dr Strange", "alias": "Doctor Strange", "real_name": "Stephen Strange", "short_bio": "Hechicero supremo de Marvel", "first_appearance": 1963, "comic_house": "Marvel"},
    {"name": "Capitana Marvel", "alias": "Carol Danvers", "real_name": "", "short_bio": "", "first_appearance": 1968, "comic_house": "Marvel"},
    {"name": "Mujer Maravilla", "alias": "", "real_name": "", "short_bio": "", "first_appearance": 1941, "comic_house": "DC"},
    {"name": "Flash", "alias": "", "real_name": "", "short_bio": "", "first_appearance": 1940, "comic_house": "DC"},
    {"name": "Star-Lord", "alias": "", "real_name": "", "short_bio": "", "first_appearance": 1976, "comic_house": 'Marvel'},
])

def linterna_verde(lista: List) -> List:
    """
    Elimina el nodo que contiene la información de Linterna Verde.
    """
    return lista.delete_value('Linterna Verde', 'name')

def año_wolverine(lista: List) -> str:
    """
    Muestra el año de aparición de Wolverine.
    """
    index = lista.search('Wolverine', 'name')
    if index is not None:
        return lista[index].first_appearance
    else:
        return 'Wolverine no está en la lista'

def Dr_Strange(lista: List) -> str:
    """
    Cambia la casa de Dr. Strange a Marvel.
    """
    index = lista.search('Dr Strange', 'name')
    if index is not None:
        lista[index].comic_house = 'Marvel'
        return f"Dr. Strange ahora pertenece a {lista[index].comic_house}"
    else:
        return 'Dr. Strange no está en la lista'
    
def Traje_Armadura(lista: List) -> List:
    """
    Muestra el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”.
    """
    result = List()
    for hero in lista:
        if 'traje' in hero.short_bio.lower() or 'armadura' in hero.short_bio.lower():
            result.append(hero.name)
    return result

def antes1963(lista: List) -> List:
    """
    Muestra el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963.
    """
    result = List()
    for hero in lista:
        if hero.first_appearance < 1963:
            result.append(f"{hero.name} - {hero.comic_house}")
    return result

def CapitanaMarvel_WonderWoman(lista: List) -> List:
    """
    Muestra la casa a la que pertenece Capitana Marvel y Mujer Maravilla.
    """
    result = List()
    for hero in lista:
        if hero.name in ['Capitana Marvel', 'Mujer Maravilla']:
            result.append(f"{hero.name} - {hero.comic_house}")
    return result

def Flash_StarLord(lista: List) -> List:
    """
    Muestra toda la información de Flash y Star-Lord.
    """
    result = List()
    for hero in lista:
        if hero.name in ['Flash', 'Star-Lord']:
            result.append(hero)
    return result

def B_M_S(lista: List) -> List:
    """
    Lista los superhéroes que comienzan con la letra B, M y S.
    """
    result = List()
    for hero in lista:
        if hero.name[0] in ['B', 'M', 'S']:
            result.append(hero.name)
    return result

def MCU_DCU(lista: List) -> dict:
    """
    Determina cuántos superhéroes hay de cada casa de comic.
    """
    count = {'Marvel': 0, 'DC': 0}
    for hero in lista:
        if hero.comic_house in count:
            count[hero.comic_house] += 1
    return count

print("- " * 50) 
linterna_verde(superheroes)
print("- " * 50) 
año_wolverine(superheroes)
print("- " * 50)
print(Dr_Strange(superheroes))
print("- " * 50)
print(Traje_Armadura(superheroes))
print("- " * 50)
print(antes1963(superheroes))
print("- " * 50)
print(CapitanaMarvel_WonderWoman(superheroes))
print("- " * 50)
print(Flash_StarLord(superheroes))
print("- " * 50)
print(B_M_S(superheroes))
print("- " * 50)
print(MCU_DCU(superheroes))
print("- " * 50)




