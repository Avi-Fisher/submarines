from submarines.board import count_remaining_ships, render_public


def print_status(state):
    have_shots = state["max_shots"] - state["shots_used"]
    live_ships = count_remaining_ships(state["n_ships"],state["shots_used"])

    print(f"you have now {have_shots} shots")
    print(f"and you have {live_ships} ships live")

    print(render_public(state["ships"],state["shots"]))























