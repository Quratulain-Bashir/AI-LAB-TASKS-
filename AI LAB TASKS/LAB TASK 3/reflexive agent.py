class ModelBasedReflexAgent:
    def __init__(self, desired_temperature: float = 22.0, hysteresis: float = 0.5) -> None:
        self.desired_temperature = desired_temperature
        self.hysteresis = hysteresis
        self.heater_state: dict[str, bool] = {}   # True => heater ON, False => heater OFF

    def set_desired(self, new_temp: float) -> None:
        """Update desired temperature for all rooms."""
        self.desired_temperature = new_temp

    def act(self, room: str, current_temperature: float) -> str:
        """
        Decide action for a given room based on current temperature and hysteresis.
        Returns one of: "Turn on heater", "Turn off heater", "No action".
        """
        prev_state = self.heater_state.get(room, False)  # default: heater off
        # Determine desired state using hysteresis
        if current_temperature < (self.desired_temperature - self.hysteresis):
            desired_state = True
        elif current_temperature > (self.desired_temperature + self.hysteresis):
            desired_state = False
        else:
            # inside deadband: keep previous state
            desired_state = prev_state

        if desired_state == prev_state:
            self.heater_state.setdefault(room, prev_state)
            return "No action"

        # state changed -> update and return action
        self.heater_state[room] = desired_state
        return "Turn on heater" if desired_state else "Turn off heater"


# Example usage / simple simulation
if __name__ == "__main__":
    agent = ModelBasedReflexAgent(desired_temperature=22.0, hysteresis=0.5)

    readings_round1 = {"Living Room": 18.0, "Bedroom": 22.0, "Kitchen": 20.0, "Bathroom": 24.0}
    for room, temp in readings_round1.items():
        print(f"{room}: {agent.act(room, temp)} (temp={temp}°C)")

    # next readings 
    readings_round2 = {"Living Room": 19.4, "Bedroom": 21.7, "Kitchen": 23.0, "Bathroom": 21.4}
    for room, temp in readings_round2.items():
        print(f"{room}: {agent.act(room, temp)} (temp={temp}°C)")

    # change desired
    agent.set_desired(21.0)
    readings_round3 = {"Living Room": 19.4, "Bedroom": 21.7, "Kitchen": 23.0, "Bathroom": 21.4}
    for room, temp in readings_round3.items():
        print(f"{room}: {agent.act(room, temp)} (temp={temp}°C)")