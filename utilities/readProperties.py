import configparser

config = configparser.RawConfigParser()
config.read(r"C:\Users\Lenovo\PycharmProjects\HealthcareprojectComm\Configurations\config.ini")


class ReadConfig():
    @staticmethod
    def getApplicationURL():
        URL = config.get('common','baseURL')
        return URL

    @staticmethod
    def getUseremail():
        username = config.get('common','useremail')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common','password')
        return password