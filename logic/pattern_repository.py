import json
import os

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
        
    def search_pattern_by_name(self, pattern_name):
        """
        Searches for a specific pattern by name.

        Args:
            pattern_name (str): The exact name of the pattern to search for.

        Returns:
            dict or None: The pattern data if found, otherwise None.
        """
        # List directories in the repository
        names = os.listdir(self.repo_path)
        directories = [name for name in names if os.path.isdir(os.path.join(self.repo_path, name)) and not name.startswith('.')]

        for directory in directories:
            data_file = os.path.join(self.repo_path, directory, 'data.json')
            if os.path.exists(data_file):
                with open(data_file, 'r') as file:
                    pattern_data = json.load(file)
                    if pattern_data.get('Name') == pattern_name:
                        return pattern_data
        
        # Return None if no pattern matches
        return None
        
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
