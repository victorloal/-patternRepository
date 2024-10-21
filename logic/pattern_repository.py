import json
import os
import shutil
import numpy as np
from logic.image_handler import ImageHandler
from logic.UI.ui_dialogSettings import SelectDirectoryDialog
from PyQt5 import QtWidgets
class PatternRepository:
    """
    A class to manage pattern data in a repository.

    Attributes:
        repo_path (str): The path to the repository where pattern data is stored.
    """

    def __init__(self, config_path='config.json'):
        """
        Initializes the PatternRepository instance by loading the repository path
        from the configuration file. Creates the repository if it does not exist.

        Args:
            config_path (str): The path to the configuration file.
        """
        self.config_path = config_path
        self.repo_path = self._load_repo_path()

        if not os.path.exists(self.repo_path):
            self._create_repository() 
                
    def _create_repository(self):
        """
        Creates a new repository by selecting a directory.
        """
        dialog = SelectDirectoryDialog()
        dialog.exec_()
        if dialog.result() == QtWidgets.QDialog.Accepted:
            # buscar si el directorio tiene el archivo RepositoryData.json
            if not os.path.exists(f"{dialog.get_selected_directory()}/RepositoryData.json"):     
                self.repo_path = dialog.get_selected_directory()
                self._rewrite_config(self.repo_path)
                self._create_repository_data()
            else:
                self.repo_path = dialog.get_selected_directory()
                self._rewrite_config(self.repo_path)
            
    def _create_repository_data(self):
        """
        Creates the repository data file.
        """
        data = {
            "Domains": {},
            "DomainsWithPatterns": {},
            "RolwithPatterns": {},
            "Uses": {}
        }
        self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
        
    def _rewrite_config(self, repo_path):
        """
        Rewrites the configuration file with the new repository path.

        Args:
            repo_path (str): The new repository path.
        """
        with open(self.config_path, 'w') as file:
            json.dump({'repo_path': repo_path}, file)

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
        
    def _read_json_file(self, file_path):
        """
        Reads JSON data from a file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The JSON data.
        """
        with open(file_path, 'r') as file:
            return json.load(file)

    def _write_json_file(self, file_path, data):
        """
        Writes JSON data to a file.

        Args:
            file_path (str): The path to the JSON file.
            data (dict): The data to write.
        """
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def _get_pattern_data_file_path(self, pattern_name):
        """
        Gets the path to the data file of a given pattern.

        Args:
            pattern_name (str): The name of the pattern.

        Returns:
            str: The path to the pattern's data file.
        """
        return os.path.join(self.repo_path, pattern_name, 'data.json')

    def _list_directories(self):
        """
        Lists directories in the repository.

        Returns:
            list: A list of directory names in the repository.
        """
        return [name for name in os.listdir(self.repo_path)
                if os.path.isdir(os.path.join(self.repo_path, name)) and not name.startswith('.')]

    def get_pattern_data_by_name(self, pattern_name):
        """
        Retrieves the complete data of a pattern by its name.

        Args:
            pattern_name (str): The name of the pattern to retrieve.

        Returns:
            tuple: A tuple containing the pattern data and images if found, otherwise (None, None).
        """
        pattern_name = pattern_name.lower()

        for directory in self._list_directories():
            data_file = self._get_pattern_data_file_path(directory)
            if os.path.exists(data_file):
                pattern_data = self._read_json_file(data_file)
                if pattern_data.get('Name', '').lower() == pattern_name:
                    images = self.__get_path_image_by_pattern_name(pattern_data.get('Name', ''))
                    return pattern_data, images
                    
        
        return None, None
    
    
    
    def get_path_images_by_name(self, pattern_name):
        """
        Retrieves the image paths of a pattern by its name.

        Args:
            pattern_name (str): The name of the pattern to retrieve.

        Returns:
            dict or None: A dictionary with image paths if found, otherwise None.
        """
        pattern_name = pattern_name.lower()

        for directory in self._list_directories():
            data_file = self._get_pattern_data_file_path(directory)
            if os.path.exists(data_file):
                pattern_data = self._read_json_file(data_file)
                if pattern_data.get('Name', '').lower() == pattern_name:
                    images = self.__get_image_by_pattern_name(pattern_data.get('Name', ''))
                    return pattern_data, images
        
        return None
    
    def __get_path_image_by_pattern_name(self, pattern_name):
        """
        Retrieves the paths of images associated with a given pattern name.

        Args:
            pattern_name (str): The name of the pattern.

        Returns:
            dict: A dictionary containing paths to various image formats.
        """
        imageHandler = ImageHandler(f"{self.repo_path}/{pattern_name}")
        return {
            "templateSVG": imageHandler.get_path_images("template"),
            "scopeModelSVG": imageHandler.get_path_images("scopeModel"),
            "structureModelSVG": imageHandler.get_path_images("structureModel"),
            "behaviorModelSVG": imageHandler.get_path_images("behaviorModel"),
            "templateDIA": imageHandler.get_path_dia("template"),
            "scopeModelDIA": imageHandler.get_path_dia("scopeModel"),
            "structureModelDIA": imageHandler.get_path_dia("structureModel"),
            "behaviorModelDIA": imageHandler.get_path_dia("behaviorModel")
        }
        
    def __get_image_by_pattern_name(self, pattern_name):
        """
        Loads and returns the images associated with a given pattern name.

        Args:
            pattern_name (str): The name of the pattern.

        Returns:
            dict: A dictionary containing the loaded images.
        """
        imageHandler = ImageHandler(f"{self.repo_path}/{pattern_name}")
        return {
            "templateSVG": imageHandler.load_image("template"),
            "scopeModelSVG": imageHandler.load_image("scopeModel"),
            "structureModelSVG": imageHandler.load_image("structureModel"),
            "behaviorModelSVG": imageHandler.load_image("behaviorModel"),
            "templateDIA": imageHandler.load_dia("template"),
            "scopeModelDIA": imageHandler.load_dia("scopeModel"),
            "structureModelDIA": imageHandler.load_dia("structureModel"),
            "behaviorModelDIA": imageHandler.load_dia("behaviorModel")
        }
    
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
            data_file = self._get_pattern_data_file_path(directory)
            if os.path.exists(data_file):
                pattern_data = self._read_json_file(data_file)
                name = pattern_data.get('Name', '')
                similarity = self._levenshtein_distance(pattern_name, name.lower())
                results.append({
                    'Name': name,
                    'Description': pattern_data.get('Description', ''),
                    'Similarity': similarity
                })

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
        
        search_text = search_text.lower()
        results = []

        for directory in self._list_directories():
            data_file = self._get_pattern_data_file_path(directory)
            if os.path.exists(data_file):
                pattern_data = self._read_json_file(data_file)
                match = self._is_match(pattern_data, search_text, search_by_name, search_by_roles, search_by_dominio)
                results.append({
                    'Name': pattern_data.get('Name', ''),
                    'Description': pattern_data.get('Description', ''),
                    'Match': match
                })

        results.sort(key=lambda x: not x['Match'])
        return results

    def _is_match(self, pattern_data, search_text, search_by_name, search_by_roles, search_by_dominio):
        search_text = search_text.lower()
        match = 0
        
        # Buscar por nombre
        if search_by_name:
            similarity = self._levenshtein_distance(search_text, pattern_data["Name"].lower())
            if similarity == 0:
                match += 2
            elif similarity < 3:
                match += 1

        # Buscar por roles
        if search_by_roles:
            roles = self.get_roles()  
            if any(search_text in role.lower() for role in list(roles.keys())):  
                match += 1
                print("Match found in roles")

        # Buscar por dominio
        if search_by_dominio:
            domains = self.get_domainsWhitPatterns()  
            if any(search_text in domain.lower() for domain in list(domains.keys())):  
                match += 1
                print("Match found in domains")

        return match
        
    def get_domains(self):
        """
        Retrieves the domains from the repository data.

        Returns:
            dict: A dictionary of domains.
        """
        return self._read_json_file(f"{self.repo_path}/RepositoryData.json")["Domains"]
    
    def get_domainsWhitPatterns(self):
        """
        Retrieves the domains from the repository data.

        Returns:
            dict: A dictionary of domains.
        """
        return self._read_json_file(f"{self.repo_path}/RepositoryData.json")["DomainsWithPatterns"]
           
        
    def add_domain(self, name, requirements=[]):
        """
        Adds a new domain to the repository.

        Args:
            name (str): The name of the domain.
            requirements (list): A list of requirements for the domain.

        Returns:
            tuple: A tuple (success, message). Success is True if the operation was successful, otherwise False.
        """
        try:
            data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
            data["Domains"][name] = requirements
            self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
            return True, "Domain added successfully."
        except Exception as e:
            return False, f"Error adding domain: {e}"
        
    def get_roles(self):
        """
        Retrieves the roles from the repository data.

        Returns:
            dict: A dictionary of roles.
        """
        return self._read_json_file(f"{self.repo_path}/RepositoryData.json")["RolwithPatterns"]

        
    def add_roles(self, role, pattern):
        """
        Adds a pattern to a role in the repository.

        Args:
            role (str): The role to add the pattern to.
            pattern (str): The pattern to add.

        Returns:
            tuple: A tuple (success, message). Success is True if the operation was successful, otherwise False.
        """
        role = role.lower()
        data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
        if role not in data["RolwithPatterns"]:
            data["RolwithPatterns"][role] = [pattern]
        elif pattern not in data["RolwithPatterns"][role]:
            data["RolwithPatterns"][role].append(pattern)
        else:
            return False, "Pattern already exists in the role"
        self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
        return True, "Role updated successfully."
            
    def add_pattern_to_domain(self, domains, pattern):
        """
        Adds a pattern to a domain in the repository.

        Args:
            domains (list): A list of domains to add the pattern to.
            pattern (str): The pattern to add.

        Returns:
            tuple: A tuple (success, message). Success is True if the operation was successful, otherwise False.
        """
        data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
        #verificar si el patron ya esta en algun dominio
        for domain, patterns in data["DomainsWithPatterns"].items():
            if pattern in patterns:
                #si esta en algun dominio se elimina de data["DomainsWithPatterns"]
                patterns.remove(pattern)
                
        for domain in domains:
            if domain not in data["DomainsWithPatterns"]:
                data["DomainsWithPatterns"][domain] = [pattern]
            elif pattern not in data["DomainsWithPatterns"][domain]:
                data["DomainsWithPatterns"][domain].append(pattern)
        self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
        return True, "Domain updated successfully."
        
    def set_domain(self, name, domains=[]):
        """
        Sets the domains for a specific pattern.

        Args:
            name (str): The name of the pattern.
            domains (list): A list of domains to set.
        """
        data_file = self._get_pattern_data_file_path(name)
        pattern_data = self._read_json_file(data_file)
        pattern_data["Domains"] = domains
        self._write_json_file(data_file, pattern_data)
    
    def get_knowUses(self):
        """
        Retrieves the 'Uses' data from the repository data.

        Returns:
            dict: The 'Uses' data.
        """
        return self._read_json_file(f"{self.repo_path}/RepositoryData.json")["Uses"]
        
    def add_uses(self, name, uses=[]):
        """
        Adds uses to the repository.

        Args:
            name (str): The name to associate with the uses.
            uses (list): A list of uses to add.
        """
        data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
        for use in uses:
            if use not in data["Uses"]:
                data["Uses"][use] = [name]
            elif name not in data["Uses"][use]:
                data["Uses"][use].append(name)
        self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
                   
    def get_requirements(self):
        """"
        Retrieves all unique requirements from domains.

        Returns:
            list: A list of all unique requirements.
        """
        data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
        all_requirements = set()
        for requirements in data["Domains"].values():
            all_requirements.update(requirements)
        return list(all_requirements)
    
    def delete_requirement(self, domain_delete, requirement_delete):
        """
        Deletes a requirement from a domain.

        Args:
            domain_delete (str): The domain from which to delete the requirement.
            requirement_delete (str): The requirement to delete.
        """
        data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
        for pattern in data["DomainsWithPatterns"][domain_delete]:
            data_file = self._get_pattern_data_file_path(pattern)
            pattern_data = self._read_json_file(data_file)
            if requirement_delete in pattern_data["Domains"]["value"].keys():
                return False, "Requerimiento asociado al patron: "+pattern
        if domain_delete in data["Domains"]:
            requirements = data["Domains"][domain_delete]
            if requirement_delete in requirements:
                requirements.remove(requirement_delete)
        self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
            
    def append_requirement(self, domain, requirement):
        """
        Appends a requirement to a domain.

        Args:
            domain (str): The domain to which to append the requirement.
            requirement (str): The requirement to append.
        """
        data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
        data["Domains"].setdefault(domain, []).append(requirement)
        self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
        
    def new_pattern(self, pattern_data, images_path):
        """
        Adds a new pattern to the repository.

        Args:
            pattern_data (dict): The pattern data.
            images_path (dict): A dictionary with paths to the pattern images.
        """
        self.__create_directory(pattern_data)
        self.__save_pattern_data(pattern_data)
        self.__save_images(pattern_data, images_path)
    
    def update_data(self, name_pattern, data, key):
        """
        Updates a specific field in the pattern's data.

        Args:
            name_pattern (str): The name of the pattern.
            data (any): The new data to set.
            key (str): The key in the data to update.
        """
        data_file = self._get_pattern_data_file_path(name_pattern)
        pattern_data = self._read_json_file(data_file)
        pattern_data[key] = data
        self._write_json_file(data_file, pattern_data)
    
    def __save_images(self, pattern_data, images_path={}):
        """
        Saves images for a pattern.

        Args:
            pattern_data (dict): The pattern data.
            images_path (dict): A dictionary with paths to the images.
        """
        try:
            new_directory = os.path.join(self.repo_path, pattern_data['Name'])
            os.makedirs(f"{new_directory}/diagramas.dia", exist_ok=True)
            os.makedirs(f"{new_directory}/diagramas.svg", exist_ok=True)

            files_to_copy = [
                ("behaviorModelDia", f"{new_directory}/diagramas.dia/behaviorModel.dia"),
                ("scopeModelDia", f"{new_directory}/diagramas.dia/scopeModel.dia"),
                ("structureModelDia", f"{new_directory}/diagramas.dia/structureModel.dia"),
                ("templateDia", f"{new_directory}/diagramas.dia/template.dia"),
                ("behaviorModelSVG", f"{new_directory}/diagramas.svg/behaviorModel.svg"),
                ("scopeModelSVG", f"{new_directory}/diagramas.svg/scopeModel.svg"),
                ("structureModelSVG", f"{new_directory}/diagramas.svg/structureModel.svg"),
                ("templateSVG", f"{new_directory}/diagramas.svg/template.svg"),
            ]
            
            for key, dest in files_to_copy:
                src = images_path[key]

                # Verifica si el archivo de destino es el mismo que el de origen
                if os.path.exists(dest) and os.path.samefile(src, dest):
                    continue  # No hacer nada si son el mismo archivo
                
                # Copia el archivo (sobrescribiendo si ya existe)
                shutil.copy2(src, dest)
        
        except Exception as e:
            error = f"Error al guardar las imágenes: {e}"
            print(error)
            return False, error
            
    def __save_pattern_data(self, pattern_data):
        """
        Saves the pattern data to a JSON file.

        Args:
            pattern_data (dict): The pattern data.
        """
        data_file = os.path.join(self.repo_path, pattern_data['Name'], 'data.json')
        self._write_json_file(data_file, pattern_data)
            
    def __create_directory(self, pattern_data):
        """
        Creates a new directory for a pattern in the repository.

        Args:
            pattern_data (dict): The pattern data.
        
        Returns:
            str: The path to the newly created directory.
        """
        new_directory = os.path.join(self.repo_path, pattern_data['Name'])
        if os.path.exists(new_directory):
            return new_directory
        os.makedirs(new_directory)
        os.makedirs(f"{new_directory}/diagramas.dia")
        os.makedirs(f"{new_directory}/diagramas.svg")
        return new_directory

    def _read_json_file(self, file_path):
        """
        Reads a JSON file.

        Args:
            file_path (str): The path to the file.

        Returns:
            dict: The JSON content.
        """
        with open(file_path, 'r') as file:
            return json.load(file)
    
    def _write_json_file(self, file_path, data):
        """
        Writes data to a JSON file.

        Args:
            file_path (str): The path to the file.
            data (dict): The data to write.
        """
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
    
    def _get_pattern_data_file_path(self, name_pattern):
        """
        Gets the path to the pattern data file.

        Args:
            name_pattern (str): The name of the pattern.

        Returns:
            str: The path to the pattern data file.
        """
        return os.path.join(self.repo_path, name_pattern, 'data.json')

    def update_all_relatedPatterns(self, relatedPatterns, name_pattern):
        """
        Updates all related patterns for a given pattern.

        Args:
            relatedPatterns (list): A list of related pattern names.
            name_pattern (str): The name of the pattern to update.
        """
        for directory in self._list_directories():
            data_file = self._get_pattern_data_file_path(directory)
            pattern_data = self._read_json_file(data_file)
            if name_pattern in pattern_data["RelatedPatterns"]:
                pattern_data["RelatedPatterns"].remove(name_pattern)
            if directory in relatedPatterns:
                pattern_data["RelatedPatterns"].append(name_pattern)
            self._write_json_file(data_file, pattern_data)
            
    def delete_pattern(self, pattern_name):
        """
        Deletes a pattern from the repository.

        Args:
            pattern_name (str): The name of the pattern to delete.

        Returns:
            tuple: A tuple (success, message). Success is True if the operation was successful, otherwise False.
        """
        pattern_dir = os.path.join(self.repo_path, pattern_name)
        if os.path.exists(pattern_dir):
            shutil.rmtree(pattern_dir)
            data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
            for domain, patterns in data["DomainsWithPatterns"].items():
                if pattern_name in patterns:
                    patterns.remove(pattern_name)
            self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
            
            for role, patterns in data["RolwithPatterns"].items():
                if pattern_name in patterns:
                    patterns.remove(pattern_name)
            self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
            
            for use, patterns in data["Uses"].items():
                if pattern_name in patterns:
                    patterns.remove(pattern_name)
            self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
            
            for directory in self._list_directories():
                data_file = self._get_pattern_data_file_path(directory)
                pattern_data = self._read_json_file(data_file)
                if pattern_name in pattern_data["RelatedPatterns"]:
                    pattern_data["RelatedPatterns"].remove(pattern_name)
                self._write_json_file(data_file, pattern_data)
                
                
            for directory in self._list_directories():
                data_file = self._get_pattern_data_file_path(directory)
                pattern_data = self._read_json_file(data_file)
                if pattern_name in pattern_data["RelatedPatterns"]:
                    pattern_data["RelatedPatterns"].remove(pattern_name)
                self._write_json_file(data_file, pattern_data)
            
            return True, "Patrón eliminado exitosamente."
        return False, "Patrón no encontrado."
    
    def delete_domain(self, domain_name):
        """
        Deletes a domain from the repository.

        Args:
            domain_name (str): The name of the domain to delete.

        Returns:
            tuple: A tuple (success, message). Success is True if the operation was successful, otherwise False.
        """
        
        if domain_name in self.get_domainsWhitPatterns().keys() and len(self.get_domainsWhitPatterns()[domain_name]) > 0:
            return False, "Dominio asignado a los patrones: "+str(self.get_domainsWhitPatterns()[domain_name])
        try:
            data = self._read_json_file(f"{self.repo_path}/RepositoryData.json")
            if domain_name in data["Domains"]:
                del data["Domains"][domain_name]
                if domain_name in data["DomainsWithPatterns"]:
                    del data["DomainsWithPatterns"][domain_name]
                self._write_json_file(f"{self.repo_path}/RepositoryData.json", data)
                return True, "Dominio eliminado exitosamente."
            return False, "Dominio no encontrado."
        except Exception as e:
            return False, f"Error al eliminar dominio: {e}"
        
    def verifyRequirement(self, requirement):
        """
        Verifies if a requirement is associated with any pattern.

        Args:
            requirement (str): The requirement to check.

        Returns:
            bool: True if the requirement is found in any pattern, otherwise False.
        """
        for directory in self._list_directories():
            data_file = self._get_pattern_data_file_path(directory)
            pattern_data = self._read_json_file(data_file)
            if requirement in pattern_data["Domains"]["value"].keys():
                return True
        return False
    
    
    
    