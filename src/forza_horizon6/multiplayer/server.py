from dataclasses import dataclass, field


@dataclass
class MultiplayerServer:
    max_players: int
    players: list[str] = field(default_factory=list)

    def connect(self, player_name: str) -> bool:
        if len(self.players) >= self.max_players:
            return False
        self.players.append(player_name)
        return True
