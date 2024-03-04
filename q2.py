from abc import ABC, abstractmethod


class ILog(ABC):
    @abstractmethod
    def registrar(self, msg: str):
        pass

# Implementações de logs
class LogArquivo(ILog):
    def registrar(self, msg: str):
        print(f"Registrando no arquivo: {msg}")

class LogConsole(ILog):
    def registrar(self, msg: str):
        print(f"Registrando no console: {msg}")

class LogBancoDeDados(ILog):
    def registrar(self, msg: str):
        print(f"Registrando no banco de dados: {msg}")

# Factory Method para criação de objetos de log
class LogFactory(ABC):
    @abstractmethod
    def criar_log(self) -> ILog:
        pass

# Implementações Factory 
class LogArquivoFactory(LogFactory):
    def criar_log(self) -> ILog:
        return LogArquivo()

class LogConsoleFactory(LogFactory):
    def criar_log(self) -> ILog:
        return LogConsole()

class LogBancoDeDadosFactory(LogFactory):
    def criar_log(self) -> ILog:
        return LogBancoDeDados()

# Demonstra como o cliente pode usar o Factory 
factory = LogArquivoFactory()
log = factory.criar_log()
log.registrar("Mensagem de log no arquivo")
