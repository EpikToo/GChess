from dataclasses import dataclass
import chess
import chess.engine
from pathlib import Path


@dataclass
class MoveAnalysis:
    score: float
    best_move: str | None
    is_mate: bool = False


class ChessAnalyzer:
    def __init__(self, depth: int = 20):
        self.depth = depth
        self.engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

    async def analyze_position(self, fen: str) -> MoveAnalysis:
        board = chess.Board(fen)

        result = await self.engine.analyse(
            board,
            chess.engine.Limit(depth=self.depth)
        )

        score = result["score"].white().score()
        best_move = result.get("pv")[0] if "pv" in result else None

        return MoveAnalysis(
            score=score if score else 0,
            best_move=best_move.uci() if best_move else None,
            is_mate=result["score"].is_mate()
        )

    def __del__(self):
        self.engine.quit()