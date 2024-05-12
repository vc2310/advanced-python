from ..core.bot import Bot


class RigelBot(Bot):
    """rigel bot"""

    name = "Rigel"

    def run(self) -> None:
        """run"""
        msg = "Rigel is running"
        self.logger.info(msg)
        print(msg)
