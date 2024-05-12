from ..core.bot import Bot


class BellatrixBot(Bot):
    """bellatrix bot"""

    name = "Bellatrix"

    def run(self) -> None:
        """run"""
        msg = "Bellatrix is running"
        self.logger.info(msg)
        print(msg)
