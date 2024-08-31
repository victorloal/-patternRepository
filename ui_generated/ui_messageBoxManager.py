from PyQt5 import QtWidgets

class MessageBoxManager:
    @staticmethod
    def show_info_message(parent, title, message):
        """
        Show an information message box.

        :param parent: Parent widget for the message box.
        :param title: Title of the message box.
        :param message: Message to display in the message box.
        """
        msg_box = QtWidgets.QMessageBox(parent)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    @staticmethod
    def show_warning_message(parent, title, message):
        """
        Show a warning message box.

        :param parent: Parent widget for the message box.
        :param title: Title of the message box.
        :param message: Message to display in the message box.
        """
        msg_box = QtWidgets.QMessageBox(parent)
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    @staticmethod
    def show_critical_message(parent, title, message):
        """
        Show a critical error message box.

        :param parent: Parent widget for the message box.
        :param title: Title of the message box.
        :param message: Message to display in the message box.
        """
        msg_box = QtWidgets.QMessageBox(parent)
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg_box.exec_()

    @staticmethod
    def show_question_message(parent, title, message, yes_text="Yes", no_text="No"):
        """
        Show a question message box.

        :param parent: Parent widget for the message box.
        :param title: Title of the message box.
        :param message: Message to display in the message box.
        :param yes_text: Text for the "Yes" button.
        :param no_text: Text for the "No" button.
        :return: True if the user clicked "Yes", False if the user clicked "No".
        """
        msg_box = QtWidgets.QMessageBox(parent)
        msg_box.setIcon(QtWidgets.QMessageBox.Question)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        msg_box.button(QtWidgets.QMessageBox.Yes).setText(yes_text)
        msg_box.button(QtWidgets.QMessageBox.No).setText(no_text)
        result = msg_box.exec_()==QtWidgets.QMessageBox.Yes
        return result

    @staticmethod
    def show_retry_ignore_message(parent, title, message):
        """
        Show a retry/ignore message box.

        :param parent: Parent widget for the message box.
        :param title: Title of the message box.
        :param message: Message to display in the message box.
        :return: QMessageBox.StandardButton indicating the user's choice.
        """
        msg_box = QtWidgets.QMessageBox(parent)
        msg_box.setIcon(QtWidgets.QMessageBox.Warning)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QtWidgets.QMessageBox.Retry | QtWidgets.QMessageBox.Ignore)
        result = msg_box.exec_()
        return result

    @staticmethod
    def show_custom_message(parent, title, message, icon_type, buttons):
        """
        Show a custom message box with specific icon and buttons.

        :param parent: Parent widget for the message box.
        :param title: Title of the message box.
        :param message: Message to display in the message box.
        :param icon_type: Type of icon (Information, Warning, Critical, Question).
        :param buttons: Set of buttons to display.
        :return: QMessageBox.StandardButton indicating the user's choice.
        """
        msg_box = QtWidgets.QMessageBox(parent)
        msg_box.setIcon(icon_type)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setStandardButtons(buttons)
        result = msg_box.exec_()
        return result