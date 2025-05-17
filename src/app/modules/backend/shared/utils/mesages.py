class SuccessCrudMessage:
    @staticmethod
    def create() -> str:
        return f"El recurso fue creado correctamente"

    @staticmethod
    def get() -> str:
        return f"El recurso fue consultado correctamente"

    @staticmethod
    def all() -> str:
        return f"Los recursos fueron consultados correctamente"

    @staticmethod
    def update() -> str:
        return f"El recurso fue actualizado correctamente"

    @staticmethod
    def delete() -> str:
        return f"El recurso fue eliminado"

    @staticmethod
    def custom(detail:str, name:str) -> str:
        return f"{detail}: {name}"


class ErrorCrudMessage:
    @staticmethod
    def create() -> str:
        return f"¡Error! Hubo un error al crear el recurso"

    @staticmethod
    def get() -> str:
        return f"¡Error! Hubo un error al leer el recurso"

    @staticmethod
    def all() -> str:
        return f"¡Error! NO se pueden leer los recursos"

    @staticmethod
    def update() -> str:
        return f"¡Error! Hubo un error al actualizar el recurso"

    @staticmethod
    def delete() -> str:
        return f"¡Error! Hubo un error al eliminar el recurso"

    @staticmethod
    def record_not_found()->str:
        return f"El recurso solicitado no existe"

    @staticmethod
    def custom_error(detail:str, name:str) -> str:
        return f"{detail}: {name}"

