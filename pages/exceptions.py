
class ElementNotFound(Exception):
    """Это исключение необходимо для абстракции NoSuchElementException."""
    
    def __init__(self, message: str):
        """Этот метод инициализирует экземпляр исключения. Он принимает сообщение об ошибке и хранит его внутри переменной экземпляра."""
        super().__init__(message)
        self.message = message 