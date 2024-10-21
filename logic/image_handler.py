from PyQt5 import QtGui, QtSvg
import os

class ImageHandler:
    """
    A class to handle loading and rendering images from SVG and DIA files.

    Attributes:
        base_path (str): The base directory path where SVG and DIA files are stored.
    """

    def __init__(self, base_path):
        """
        Initializes the ImageHandler with the base path for images.

        Args:
            base_path (str): The base directory path where SVG files are stored.
        """
        self.base_path = base_path

    def load_image(self, image_type):
        """
        Loads an SVG image from the base path and returns a QPixmap object.

        Args:
            image_type (str): The type of image to load (used to form the SVG filename).

        Returns:
            QtGui.QPixmap: The QPixmap object containing the rendered image, or None if the image cannot be loaded.
        """
        svg_path = os.path.join(self.base_path, f"diagramas.svg/{image_type}.svg")
        return self._get_pixmap_from_svg(svg_path)
    
    def load_dia(self, image_type):
        """
        Loads a DIA image from the base path and returns the path to the DIA file.

        Args:
            image_type (str): The type of image to load (used to form the DIA filename).

        Returns:
            str: The path to the DIA file.
        """
        dia_path = os.path.join(self.base_path, f"diagramas.dia/{image_type}.dia")
        return dia_path

    def get_path_images(self, image_type):
        """
        Gets the file path for an SVG image.

        Args:
            image_type (str): The type of image to load (used to form the SVG filename).

        Returns:
            str: The full path to the SVG file.
        """
        return os.path.join(self.base_path, f"diagramas.svg/{image_type}.svg")

    def get_path_dia(self, image_type):
        """
        Gets the file path for a DIA image.

        Args:
            image_type (str): The type of image to load (used to form the DIA filename).

        Returns:
            str: The full path to the DIA file.
        """
        return os.path.join(self.base_path, f"diagramas.dia/{image_type}.dia")
    
    def _get_pixmap_from_svg(self, svg_path):
        """
        Renders an SVG image to a QPixmap object with the SVG's original size.

        Args:
            svg_path (str): The path to the SVG file.

        Returns:
            QtGui.QPixmap: The QPixmap object containing the rendered image, or None if the SVG file is invalid or cannot be loaded.
        """
        if not os.path.exists(svg_path):
            return None  
        svg_renderer = QtSvg.QSvgRenderer(svg_path)
        if not svg_renderer.isValid():
            return None  
        size = svg_renderer.defaultSize() 
        pixmap = QtGui.QPixmap(size)
        pixmap.fill(QtGui.QColor(0, 0, 0, 0)) 
        painter = QtGui.QPainter(pixmap)
        svg_renderer.render(painter)
        painter.end()
        return pixmap
