from abc import ABC, abstractmethod

class Renderizador(ABC):
    @abstractmethod
    def renderizar(self):
        pass

# Implementações renderização
class RenderizadorTexturas(Renderizador):
    def renderizar(self):
        print("Renderizando texturas")

class RenderizadorSombras(Renderizador):
    def renderizar(self):
        print("Renderizando sombras")

class RenderizadorModelos(Renderizador):
    def renderizar(self):
        print("Renderizando modelos")


class FabricaRenderizacao(ABC):
    @abstractmethod
    def criar_renderizador_texturas(self) -> Renderizador:
        pass

    @abstractmethod
    def criar_renderizador_sombras(self) -> Renderizador:
        pass

    @abstractmethod
    def criar_renderizador_modelos(self) -> Renderizador:
        pass

# Implementações concretas do Abstract Factory como Singleton
class FabricaOpenGL(FabricaRenderizacao):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(FabricaOpenGL, cls).__new__(cls)
        return cls._instance

    def criar_renderizador_texturas(self) -> Renderizador:
        return RenderizadorTexturas()

    def criar_renderizador_sombras(self) -> Renderizador:
        return RenderizadorSombras()

    def criar_renderizador_modelos(self) -> Renderizador:
        return RenderizadorModelos()

class FabricaDirectX(FabricaRenderizacao):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(FabricaDirectX, cls).__new__(cls)
        return cls._instance

    def criar_renderizador_texturas(self) -> Renderizador:
        return RenderizadorTexturas()

    def criar_renderizador_sombras(self) -> Renderizador:
        return RenderizadorSombras()

    def criar_renderizador_modelos(self) -> Renderizador:
        return RenderizadorModelos()

# Demonstra como o cliente pode usar os padrões combinados
fabrica_opengl = FabricaOpenGL()
renderizador_texturas_opengl = fabrica_opengl.criar_renderizador_texturas()
renderizador_texturas_opengl.renderizar()

fabrica_directx = FabricaDirectX()
renderizador_sombras_directx = fabrica_directx.criar_renderizador_sombras()
renderizador_sombras_directx.renderizar()
