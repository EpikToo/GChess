from ninja_extra import api_controller, http_get
from .services import ChessAnalyzer


@api_controller("/chess")
class ChessAPI:
    def __init__(self):
        self.analyzer = ChessAnalyzer()

    @http_get("/analyze")
    async def analyze_position(self, fen: str):
        analysis = await self.analyzer.analyze_position(fen)
        return {
            "score": analysis.score,
            "best_move": analysis.best_move,
            "is_mate": analysis.is_mate
        }