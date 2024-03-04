from abc import ABC, abstractmethod

# Interface comum para os produtos
class Botao(ABC):
    @abstractmethod
    def clicar(self):
        pass

class Janela(ABC):
    @abstractmethod
    def abrir(self):
        pass

class Cursor(ABC):
    @abstractmethod
    def mover(self):
        pass

class Select(ABC):
    @abstractmethod
    def selecionar(self):
        pass

class Input(ABC):
    @abstractmethod
    def receber_entrada(self):
        pass

class AbstractFactoryUI(ABC):
    @abstractmethod
    def criar_botao(self) -> Botao:
        pass

    @abstractmethod
    def criar_janela(self) -> Janela:
        pass

    @abstractmethod
    def criar_cursor(self) -> Cursor:
        pass

    @abstractmethod
    def criar_select(self) -> Select:
        pass

    @abstractmethod
    def criar_input(self) -> Input:
        pass

# Implementações W e MAC
class FabricaWindows(AbstractFactoryUI):
    def criar_botao(self) -> Botao:
        return BotaoWindows()

    def criar_janela(self) -> Janela:
        return JanelaWindows()

    def criar_cursor(self) -> Cursor:
        return CursorWindows()

    def criar_select(self) -> Select:
        return SelectWindows()

    def criar_input(self) -> Input:
        return InputWindows()

class FabricaMacOS(AbstractFactoryUI):
    def criar_botao(self) -> Botao:
        return BotaoMacOS()

    def criar_janela(self) -> Janela:
        return JanelaMacOS()

    def criar_cursor(self) -> Cursor:
        return CursorMacOS()

    def criar_select(self) -> Select:
        return SelectMacOS()

    def criar_input(self) -> Input:
        return InputMacOS()

# Implementações W
class BotaoWindows(Botao):
    def clicar(self):
        print("Botão do Windows foi clicado")

class JanelaWindows(Janela):
    def abrir(self):
        print("Janela do Windows foi aberta")

class CursorWindows(Cursor):
    def mover(self):
        print("Cursor do Windows está se movendo")

class SelectWindows(Select):
    def selecionar(self):
        print("Seleção no Windows")

class InputWindows(Input):
    def receber_entrada(self):
        print("Recebendo entrada no Windows")

# Implementações Mac
class BotaoMacOS(Botao):
    def clicar(self):
        print("Botão do macOS foi clicado")

class JanelaMacOS(Janela):
    def abrir(self):
        print("Janela do macOS foi aberta")

class CursorMacOS(Cursor):
    def mover(self):
        print("Cursor do macOS está se movendo")

class SelectMacOS(Select):
    def selecionar(self):
        print("Seleção no macOS")

class InputMacOS(Input):
    def receber_entrada(self):
        print("Recebendo entrada no macOS")

# Demonstra como o código cliente pode utilizar a fábrica para criar produtos compatíveis com o sistema operacional em uso
def usar_fabrica(ui_factory: AbstractFactoryUI):
    botao = ui_factory.criar_botao()
    janela = ui_factory.criar_janela()
    cursor = ui_factory.criar_cursor()
    select = ui_factory.criar_select()
    entrada = ui_factory.criar_input()

    botao.clicar()
    janela.abrir()
    cursor.mover()
    select.selecionar()
    entrada.receber_entrada()
    
# Exemplo Windows
print("Usando a fábrica Windows:")
usar_fabrica(FabricaWindows())

# Exemplo macOS
print("\nUsando a fábrica macOS:")
usar_fabrica(FabricaMacOS())
