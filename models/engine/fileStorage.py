#!/usr/bin/python3
"""
importamos las librerias para crear un motor de
almacenamiento, el cual se hara en un archivo json
"""
import json
from os.path import exists
from os import stat


class FileStorage:
    """
    Esta clase contiene los atributos y metodos necesarios
    para crear un motor de almacenamiento a través de un
    archivo json
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        retorna el atributo de clase __objects,
        el cual es un objeto de tipo dict
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                diccionario = json.load(f)
                return diccionario
        else:
            dic = {}
            with open(self.__file_path, 'w') as f:
                diccionario = json.dump(dic, f)
                return diccionario

    def new(self, obj):
        """
        crea el nuevo objeto para almacenar
        """
        dic = self.all()
        name = obj['usuario']
        dic[name] = obj
        FileStorage.__objects = dic

    def save(self):
        """
        serializa __objects y lo almacena en
        un archivo .json
        """
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """deserializa y guarda en __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = classes[jo[key]["__class__"]](**jo[key])
        except:
            pass

    def delete(self, obj=None):
        """elimina un registro dentro del file.json"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]
