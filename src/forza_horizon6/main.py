from forza_horizon6.core.game import Game


if __name__ == "__main__":
    game = Game()
    game.bootstrap()
    game.run_demo_loop(ticks=5)
