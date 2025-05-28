import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ecc import Ui_Dialog
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_gen_keys)
        self.ui.Sign.clicked.connect(self.call_api_sign)
        self.ui.Verify.clicked.connect(self.call_api_verify)

    def show_error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText(message)
        msg.exec_()

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5050/api/ecc/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(data["message"])
                msg.exec_()
            else:
                error_msg = response.json().get('error', 'Unknown error occurred')
                self.show_error(f"Error while calling API: {error_msg}")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Connection error: {str(e)}")

    def call_api_sign(self):
        url = "http://127.0.0.1:5050/api/ecc/sign"
        message = self.ui.plainTextEdit_3.toPlainText()
        if not message:
            self.show_error("Please enter a message to sign")
            return
            
        payload = {"message": message}
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.plainTextEdit_2.setPlainText(data["signature"])
                
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Signed Successfully")
                msg.exec_()
            else:
                error_msg = response.json().get('error', 'Unknown error occurred')
                self.show_error(f"Error while calling API: {error_msg}")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Connection error: {str(e)}")

    def call_api_verify(self):
        url = "http://127.0.0.1:5050/api/ecc/verify"
        message = self.ui.plainTextEdit_3.toPlainText()
        signature = self.ui.plainTextEdit_2.toPlainText()
        
        if not message or not signature:
            self.show_error("Both message and signature are required")
            return
            
        payload = {
            "message": message,
            "signature": signature
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                if data["is_verified"]:
                    msg.setText("Verified Successfully")
                else:
                    msg.setText("Verified Fail")
                msg.exec_()
            else:
                error_msg = response.json().get('error', 'Unknown error occurred')
                self.show_error(f"Error while calling API: {error_msg}")
        except requests.exceptions.RequestException as e:
            self.show_error(f"Connection error: {str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
