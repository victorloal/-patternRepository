import json
import os
import shutil

import numpy as np

from logic.image_handler import ImageHandler

class PatternRepository:
    """
    A class to manage pattern data in a repository.

    Attributes:
        repo_path (str): The path to the repository where pattern data is stored.
    """

    def __init__(self, config_path='config.json'):
        """
        Initializes the PatternRepository instance by loading the repository path
        from the configuration file. If the configuration file or repository 
        does not exist, appropriate actions are taken.

        Args:
            config_path (str): The path to the configuration file.
        """
        self.config_path = config_path
        self.repo_path = self._load_repo_path()

        if not os.path.exists(self.repo_path):
            print('Repository not found ... creating repository')
            os.makedirs(self.repo_path)

    def _load_repo_path(self):
        """
        Loads the repository path from the configuration file.

        Returns:
            str: The path to the repository.
        """
        try:
            with open(self.config_path, 'r') as file:
                config = json.load(file)
                return config.get('repo_path', '')
        except FileNotFoundError:
            print('Configuration file not found.')
            return ''
        
    def get_pattern_data_by_name(self, pattern_name):
        """
        Retrieves the complete data of a pattern by its name.

        Args:
            pattern_name (str): The name of the pattern to retrieve.

        Returns:
            dict or None: The pattern data if found, otherwise None.
        """
        pattern_name = pattern_name.lower()

        for directory in self._list_directories():
            data_file = os.path.join(self.repo_path, directory, 'data.json')
            if os.path.exists(data_file):
                with open(data_file, 'r') as file:
                    pattern_data = json.load(file)
                    if pattern_data.get('Name', '').lower() == pattern_name:
                        images = self.__get_image_by_pattern_name(pattern_data.get('Name', ''))
                        return pattern_data, images
        
        # Return None if no pattern matches
        return None
    
    def get_path_images_by_name(self, pattern_name):
        """
        Retrieves the complete data of a pattern by its name.

        Args:
            pattern_name (str): The name of the pattern to retrieve.

        Returns:
            dict or None: The pattern data if found, otherwise None.
        """
        pattern_name = pattern_name.lower()

        for directory in self._list_directories():
            data_file = os.path.join(self.repo_path, directory, 'data.json')
            if os.path.exists(data_file):
                with open(data_file, 'r') as file:
                    pattern_data = json.load(file)
                    if pattern_data.get('Name', '').lower() == pattern_name:
                        images = self.__get_path_image_by_pattern_name(pattern_data.get('Name', ''))
                        return images
        
        # Return None if no pattern matches
        return None
    
    def __get_path_image_by_pattern_name(self, pattern_name):
        imageHandler = ImageHandler(f"{self.repo_path}/{pattern_name}")
        #devolver las imagenes en un diccionario
        images = {}
        images["template"] = imageHandler.get_path_images("template")
        images["scopeModel"] = imageHandler.get_path_images("scopeModel")
        images["structureModel"] = imageHandler.get_path_images("structureModel")
        images["behaviorModel"] = imageHandler.get_path_images("behaviorModel")
        
        return images
        
    def __get_image_by_pattern_name(self, pattern_name):
        imageHandler = ImageHandler(f"{self.repo_path}/{pattern_name}")
        #devolver las imagenes en un diccionario
        images = {}
        images["template"] = imageHandler.load_image("template")
        images["scopeModel"] = imageHandler.load_image("scopeModel")
        images["structureModel"] = imageHandler.load_image("structureModel")
        images["behaviorModel"] = imageHandler.load_image("behaviorModel")
        
        return images
        
        
        
    def search_pattern_by_name(self, pattern_name):
        """
        Searches for a specific pattern by name and returns results sorted by similarity.

        Args:
            pattern_name (str): The exact name of the pattern to search for.

        Returns:
            list: A list of dictionaries containing the pattern data sorted by similarity.
        """
        pattern_name = pattern_name.lower()
        results = []

        for directory in self._list_directories():
            data_file = os.path.join(self.repo_path, directory, 'data.json')
            if os.path.exists(data_file):
                with open(data_file, 'r') as file:
                    pattern_data = json.load(file)
                    name = pattern_data.get('Name', '')
                    similarity = self._levenshtein_distance(pattern_name, name.lower())
                    results.append({
                        'Name': name,
                        'Description': pattern_data.get('Description', ''),
                        'Similarity': similarity
                    })

        # Sort results by similarity (lower is more similar)
        results.sort(key=lambda x: x['Similarity'])
        return results
    
    def _levenshtein_distance(self, s1, s2):
        """
        Computes the Levenshtein distance between two strings.

        Args:
            s1 (str): The first string.
            s2 (str): The second string.

        Returns:
            int: The Levenshtein distance between the two strings.
        """
        if len(s1) < len(s2):
            return self._levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = np.arange(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = np.zeros(len(s2) + 1)
            current_row[0] = i + 1
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row[j + 1] = min(insertions, deletions, substitutions)
            previous_row = current_row

        return int(previous_row[-1])
        
    def search(self, search_text, search_by_name=False, search_by_roles=False, search_by_dominio=False):
        """
        Searches for patterns in the repository based on the provided criteria.

        Args:
            search_text (str): The text to search for within the pattern data.
            search_by_name (bool): If True, search by pattern name.
            search_by_roles (bool): If True, search by pattern roles.
            search_by_dominio (bool): If True, search by pattern domains.

        Returns:
            list: A list of dictionaries containing the search results. Each dictionary 
                  contains 'Name', 'Description', and 'Match' keys where 'Match' indicates 
                  whether the pattern matched the search criteria.
        """
        search_text = search_text.lower()
        results = []

        for directory in self._list_directories():
            data_file = os.path.join(self.repo_path, directory, 'data.json')
            if os.path.exists(data_file):
                with open(data_file, 'r') as file:
                    pattern_data = json.load(file)
                    match = self._is_match(pattern_data, search_text, search_by_name, search_by_roles, search_by_dominio)
                    results.append({
                        'Name': pattern_data.get('Name', ''),
                        'Description': pattern_data.get('Description', ''),
                        'Match': match
                    })

        results.sort(key=lambda x: not x['Match'])
        return results

    def _list_directories(self):
        """
        Lists directories in the repository.

        Returns:
            list: A list of directory names in the repository.
        """
        names = os.listdir(self.repo_path)
        return [name for name in names if os.path.isdir(os.path.join(self.repo_path, name)) and not name.startswith('.')]

    def _is_match(self, pattern_data, search_text, search_by_name, search_by_roles, search_by_dominio):
        """
        Checks if the pattern data matches the search criteria.

        Args:
            pattern_data (dict): The pattern data to check.
            search_text (str): The text to search for.
            search_by_name (bool): If True, check the pattern name.
            search_by_roles (bool): If True, check the pattern roles.
            search_by_dominio (bool): If True, check the pattern domains.

        Returns:
            bool: True if the pattern data matches the search criteria, False otherwise.
        """
        match = False
        if search_by_name and search_text in pattern_data.get('Name', '').lower():
            match = True
        if search_by_roles and any(search_text in role.lower() for role in pattern_data.get('Roles', [])):
            match = True
        if search_by_dominio and search_text in pattern_data.get('Domains', []):
            match = True
        return match
    
    def get_domains(self):
        with open(f"{self.repo_path}/Domains.json") as file:
            data = json.load(file)
            return data
        
    def add_domain(self,name, requirements = []):
        try:
            with open(f"{self.repo_path}/Domains.json", "r") as file:
                data = json.load(file) 
                data["Domains"][name] = requirements
            with open(f"{self.repo_path}/Domains.json", "w") as file:
                json.dump(data, file)
        except:
            return False, "Error al guardar el dominio"
        
    def set_domain(self,name, domains = []):
        with open(f"{self.repo_path}/{name}/data.json","w") as file:
            data = json.load(file)
            data["Domains"] = domains
            
    
    def get_knowUses(self):
        with open(f"{self.repo_path}/KnownUses.json") as file:
            data = json.load(file)
            return data
            
    def set_knowUses(self,name,uses = []):
        with open (f"{self.repo_path}/KnownUses.json") as file:
            data = json.load(file)
            for use in uses:
                flat = False
                for key in data["Uses"]:
                    if use == key:
                        flat = True
                        data["Uses"][key].append(name)
                if not flat:
                    data["Uses"][use].append(name)
        with open(f"{self.repo_path}/KnownUses.json", "w") as file:
            json.dump(data, file)
                   
    def get_requirements(self):
        all_requirements = []
        with open(f"{self.repo_path}/Domains.json") as file:
            data = json.load(file)

            # Recorrer cada dominio en el diccionario
            for domain, requirements in data["Domains"].items():
                # Añadir los requisitos a la lista de todos los requisitos
                for requirement in requirements:
                    # verificar si el requisito ya esta en la lista
                    if requirement not in all_requirements:
                        all_requirements.append(requirement)
                
        return all_requirements
    
    def delete_requirement(self,domain_delete, requirement_delete):
        with open(f"{self.repo_path}/Domains.json") as file:
            data = json.load(file)
            for domain, requirements in data["Domains"].items():
                if domain_delete == domain:
                    if requirement_delete in requirements:
                        requirements.remove(requirement_delete)
        with open(f"{self.repo_path}/Domains.json", "w") as file:
            json.dump(data, file)
    def append_requirement(self,domain, requirement):
        with open(f"{self.repo_path}/Domains.json") as file:
            data = json.load(file)
            data["Domains"][domain].append(requirement)
        with open(f"{self.repo_path}/Domains.json", "w") as file:
            json.dump(data, file)
        
        
    def new_pattern(self, pattern_data, images_path):
        self.__crear_directorio(pattern_data)
        self.__save_pattern_data(pattern_data)
        self.__save_images(pattern_data,images_path)
        pass
    
    def append_data(self,name_pattern,data,key):
        with open(f"{self.repo_path}/{name_pattern}/data.json") as file:
            file = json.load(file)
            file[key] = data
        with open(f"{self.repo_path}/{name_pattern}/data.json", "w") as f:
            json.dump(file, f)
    
    def __save_images(self,pattern_data, images_path = {}):
        try:
            print("pattern_data")
            new_directory = os.path.join(self.repo_path, pattern_data['Name'])
            print("images_path")
            shutil.copy(images_path["behaviorModelDia"], f"{new_directory}/diagramas.dia/behaviorModel.dia")
            shutil.copy(images_path["scopeModelDia"], f"{new_directory}/diagramas.dia/scopeModel.dia")
            shutil.copy(images_path["structureModelDia"], f"{new_directory}/diagramas.dia/structureModel.dia")
            shutil.copy(images_path["templateDia"], f"{new_directory}/diagramas.dia/template.dia")
            
            shutil.copy(images_path["behaviorModelSVG"], f"{new_directory}/diagramas.svg/behaviorModel.svg")
            shutil.copy(images_path["scopeModelSVG"], f"{new_directory}/diagramas.svg/scopeModel.svg")
            shutil.copy(images_path["structureModelSVG"], f"{new_directory}/diagramas.svg/structureModel.svg")
            shutil.copy(images_path["templateSVG"], f"{new_directory}/diagramas.svg/template.svg")
            
        except Exception as e:
            error = f"Error al guardar las imagenes: {e}"
            print(error)
            return False, error
            
    def __save_pattern_data(self, pattern_data):
        # Guardar los datos del patrón en un archivo JSON
        data_file = os.path.join(self.repo_path, pattern_data['Name'], 'data.json')
        with open(data_file, 'w') as file:
            json.dump(pattern_data, file, indent=4)
            
            
    def __crear_directorio(self,pattern_data):
            # Crear un nuevo directorio en el repositorio
            new_directory = os.path.join(self.repo_path, pattern_data['Name'])
            # Verificar si el directorio ya existe
            if os.path.exists(new_directory):
                error = 'El directorio ya existe'
                return False, error
            os.makedirs(new_directory)
            os.mkdir(f"{new_directory}/diagramas.dia")
            os.mkdir(f"{new_directory}/diagramas.svg")
            
            return new_directory

