from lxml import etree

class SvgTextModifier:
    def __init__(self, svg_content):
        self.svg_content = svg_content
        self.tree = etree.fromstring(svg_content.encode('utf-8'))
        self.ns = {'svg': 'http://www.w3.org/2000/svg'}
        self.text_elements = self.tree.findall('.//svg:text', namespaces=self.ns)

    def get_texts(self):
        texts = []
        for text in self.text_elements:
            tspan_elements = text.findall('.//svg:tspan', namespaces=self.ns)
            if not tspan_elements:
                text_content = text.text.strip() if text.text else ''
                if text_content:  # Ignorar textos vacíos
                    texts.append(text_content)
            else:
                for tspan in tspan_elements:
                    tspan_content = tspan.text.strip() if tspan.text else ''
                    if tspan_content:  # Ignorar textos vacíos
                        texts.append(tspan_content)
        return list(set(texts))  # Return unique texts

    def modify_text(self, text_replacements):
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
    