from lxml import etree

class SvgTextModifier:
    """
    A class to modify text elements in an SVG content string.

    Attributes:
        svg_content (str): The original SVG content as a string.
        tree (lxml.etree.Element): The parsed SVG content as an XML tree.
        ns (dict): A dictionary containing the SVG namespace.
        text_elements (list): A list of text elements found in the SVG.
    """

    def __init__(self, svg_content):
        """
        Initializes the SvgTextModifier with the SVG content.

        Args:
            svg_content (str): The original SVG content as a string.
        """
        self.svg_content = svg_content
        self.tree = etree.fromstring(svg_content.encode('utf-8'))
        self.ns = {'svg': 'http://www.w3.org/2000/svg'}
        self.text_elements = self.tree.findall('.//svg:text', namespaces=self.ns)

    def get_texts(self):
        """
        Retrieves all unique text content from the SVG.

        Returns:
            list: A list of unique text strings found in the SVG.
        """
        texts = []
        for text in self.text_elements:
            tspan_elements = text.findall('.//svg:tspan', namespaces=self.ns)
            if not tspan_elements:
                text_content = text.text.strip() if text.text else ''
                if text_content:  
                    texts.append(text_content)
            else:
                for tspan in tspan_elements:
                    tspan_content = tspan.text.strip() if tspan.text else ''
                    if tspan_content:  
                        texts.append(tspan_content)
        return list(set(texts))  

    def modify_text(self, text_replacements):
        """
        Modifies the text content in the SVG based on provided replacements.

        Args:
            text_replacements (dict): A dictionary mapping original text to new text.

        Returns:
            str: The modified SVG content as a string.
        """
        for text in self.text_elements:
            tspan_elements = text.findall('.//svg:tspan', namespaces=self.ns)
            if not tspan_elements:
                original_text = text.text.strip() if text.text else ''
                if original_text in text_replacements:
                    text.text = text_replacements[original_text]
            else:
                for tspan in tspan_elements:
                    original_text = tspan.text.strip() if tspan.text else ''
                    if original_text in text_replacements:
                        tspan.text = text_replacements[original_text]
        return etree.tostring(self.tree, encoding='unicode')
