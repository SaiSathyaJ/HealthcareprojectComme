import logging

class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename=r"C:\Users\Lenovo\PycharmProjects\HealthcareprojectComm\Logs\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

        logge=logging.getLogger()
        logge.setLevel(logging.INFO)

        logge.info("Hello, World!")
        return logge

