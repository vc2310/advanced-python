from ..core.bot import Bot


class BetelgeuseBot(Bot):
    """betelgeuse bot"""

    name = "Betelgeuse"

    def run(self) -> None:
        """run"""
        msg = "Betelgeuse is running"
        self.logger.info(msg)
        print(msg)
