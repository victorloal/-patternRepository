from PyQt5 import QtGui, QtSvg
import os

class ImageHandler:
    def __init__(self, base_path):
        """
        Initializes the ImageHandler with the base path for images.

        Args:
            base_path (str): The base directory path where SVG files are stored.
        """
        self.base_path = base_path

    def load_image(self, image_type):
        """
        Loads an image from the base path and returns a QPixmap object.

        Args:
            image_type (str): The type of image to load (used to form the SVG filename).

        Returns:
            QtGui.QPixmap: The QPixmap object containing the rendered image.
        """
        svg_path = os.path.join(self.base_path, f"diagramas.svg/{image_type}.svg")
        return self._get_pixmap_from_svg(svg_path)

    def _get_pixmap_from_svg(self, svg_path):
        """
        Renders an SVG image to a QPixmap object with the SVG's original size.

        Args:
            svg_path (str): The path to the SVG file.

        Returns:
            QtGui.QPixmap: The QPixmap object containing the rendered image.
        """
        # Create an SVG renderer
        svg_renderer = QtSvg.QSvgRenderer(svg_path)

        if not svg_renderer.isValid():
            print(f"Error: SVG file '{svg_path}' is invalid or could not be loaded.")
            return QtGui.QPixmap()  # Return an empty QPixmap

        # Get the size of the SVG
        size = svg_renderer.defaultSize()  # Get the original size of the SVG

        # Create QPixmap with the SVG's original size
        pixmap = QtGui.QPixmap(size)
        pixmap.fill(QtGui.QColor(0, 0, 0, 0))  # Fill with transparent color

        # Create a QPainter to render the SVG onto the QPixmap
        painter = QtGui.QPainter(pixmap)
        svg_renderer.render(painter)
        painter.end()

        return pixmap