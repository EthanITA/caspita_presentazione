"""
PROBLEMA:
    Da una folder di immagini serve un json con questo tipo di formato per un sito web:
    [ # pagine, un numero indefinito di elementi
        [ # colonne, 3 elementi
            [ # righe, 2 elementi
                { # prodotto
                    name: str,
                    description:str,
                    path: str,
                    price:int
                },
                {...}
            ],
            [...],
            [...]
        ]
        ...
    ]
    in altre parole, ogni pagina ha 6 prodotti, con 3 colonne e 2 righe. Ogni prodotto ha certi campi
    (che verrano aggiunti altri)

    In piu, il nome di ogni file immagine .jpg/.jpeg/.png saranno cosi formattati:
        name,price
        es. Detersivo per piatti, 3.99.png

    La descrizione, invece, sarà contenuta in un file .txt,
    dove il nome del file sarà uguale al nome del prodotto associato
"""
import json
import os
import re


def parse_to_dict(folder):
    """
    Parso i file come dizionari sfruttando la lista ordinata + regex, il dict è di questo formato:
        {
            name:{
                "name":name,
                "description":description,
                "price":price,
                "path":path
            }
            ...
        }
    :param folder:
    :return:
    """
    price_regex = "[0-9]+[.][0-9][0-9]"
    image_ext_regex = "(png|jpg|jpeg)"
    product_name_regex = "[a-zA-Z0-9]+"
    separator = "[,]"
    image_regex = f"{product_name_regex}(.)*{separator}(.)*{price_regex}[.]{image_ext_regex}"

    images = {}
    for file in sorted(os.listdir(folder)):
        namefile, extension = os.path.splitext(file)
        if os.path.isfile(os.path.join(folder, file)) and re.search(image_regex, file) is not None:
            name, price = namefile.strip().split(",")
            description_file = os.path.join(folder, f"{name}.txt")
            images[name] = {
                "name": name,
                "path": os.path.join("".join((namefile, extension))),
                "price": '{:.2f}'.format(float(price)),
                "description": " ".join(
                    map(str.strip, open(description_file).readlines())) if os.path.exists(description_file) else ""
            }
    return images


def build_page(keys, dictionary):
    def encode(i, j):
        return i + j * 2

    return [
        [
            {
                "name": dictionary[key]["name"],
                "path": dictionary[key]["path"],
                "price": dictionary[key]["price"],
                "description": dictionary[key]["description"]
            } for row in range(2)
            for key in (keys[encode(row, col)],)
        ] for col in range(3)
    ]


def solve(folder: str):
    dict_products = parse_to_dict(folder)
    products_name = list(dict_products.keys())
    result_array = [build_page(products_name[page * 6:page * 6 + 6], dict_products) for page in
                    range(len(products_name) // 6)]

    n_products_excess = len(products_name) - 6 * len(result_array)
    n_products_to_fill = 6 - n_products_excess
    if n_products_excess > 0:
        if len(products_name) >= 6:
            result_array.append(build_page(products_name[-n_products_excess:] + products_name[:n_products_to_fill],
                                           dict_products))
        else:
            result_array.append(build_page(
                products_name[-n_products_excess:] + [products_name[i % len(products_name)] for i in
                                                      range(n_products_to_fill)], dict_products))

    return json.dumps(result_array)


if __name__ == '__main__':
    working_proj_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
    print(solve("/home/marco/Documents/projects/porcari/negozio/presentazione/public/products"))