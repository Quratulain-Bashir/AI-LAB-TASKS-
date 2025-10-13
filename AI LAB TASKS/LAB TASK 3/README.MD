# Quratulain 
## roll no: 156 
### section : bsai 3c
******************************
# Model-Based Reflex Agent — Thermostat Simulation

## Purpose
This small Python script implements a model-based reflex agent that controls heaters for multiple rooms. It applies a desired temperature and a hysteresis (deadband) to avoid rapid on/off switching.

## Files
- `model based reflexive agent.py` — agent implementation and a simple simulation in `__main__`.

## How it works
- The `ModelBasedReflexAgent` class stores:
  - `desired_temperature` (float): target temperature for all rooms.
  - `hysteresis` (float): range around the target where no change is made.
  - `heater_state` (dict): mapping room name -> bool (True = heater on).
- The `act(room, current_temperature)` method:
  1. Reads previous heater state for `room` (defaults to off).
  2. Compares `current_temperature` to `desired_temperature ± hysteresis`.
     - If below `desired - hysteresis` → desired state = ON.
     - If above `desired + hysteresis` → desired state = OFF.
     - If inside the deadband → desired state = previous state (no change).
  3. If desired state differs from previous, updates `heater_state` and returns
     `"Turn on heater"` or `"Turn off heater"`. Otherwise returns `"No action"`.

## Key concepts
- Hysteresis / deadband: prevents rapid toggling when temperature fluctuates near the set point.
- Model-based reflex: the agent remembers previous heater states (model) and uses that memory when deciding action inside the deadband.

## Usage
Run the script with Python 3:

    python "model based reflexive agent.py"

The `__main__` section provides an example simulation with three rounds of readings and prints actions per room.

## Example output (approximate)
Living Room: Turn on heater (temp=18.0°C)  
Bedroom: No action (temp=22.0°C)  
Kitchen: Turn on heater (temp=20.0°C)  
Bathroom: Turn off heater (temp=24.0°C)

## Extension ideas
- Per-room desired temperatures.
- Per-room hysteresis values.
- Integrate with real sensor input or a scheduler.
- Add logging and unit tests.

## Requirements
- Python 3.8+ (uses type annotations and dict[str, bool]).
