class Configuracao:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Configuracao, cls).__new__(cls)
      
            cls._instance.tema = "claro"
            cls._instance.idioma = "portugues"
            cls._instance.tamanho_fonte = 12
        return cls._instance

# Demonstra o uso da classe singleton Configuracao
config = Configuracao()
print(f'Tema: {config.tema}, Idioma: {config.idioma}, Tamanho da Fonte: {config.tamanho_fonte}')

# Modifica as configurações usando a instância singleton
config.tema = "escuro"
config.idioma = "ingles"
config.tamanho_fonte = 14

# Acessa as configurações modificadas
print(f'Tema: {config.tema}, Idioma: {config.idioma}, Tamanho da Fonte: {config.tamanho_fonte}')
