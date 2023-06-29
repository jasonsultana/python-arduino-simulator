# Conventions
Files that you're intended to edit begin with an underscore. i.e - `_sketch.py` and `_setup.json`. 

# Starting the simulator
`python3 -m simulator.start`

# Setting up the board
Customise the board by modifying `_setup.json`. Eg:

```
{
    "message_type": "setup",
    "window_title": "Jason's Arduino Simulator",
    "components": [{
        "name": "led",
        "pin": 13,
        "x": 165,
        "y": 175
    }]
}
```

Once you're happy with the configuration, run it using `python3 ./setup.py`.

# Running a sketch
Write your sketch in `_sketch.py` and run it using `python3 -m _sketch`

# Dependencies
- pygame (for UI)
- pyzmq (for inter-process communication)
- pydantic (for serialisation)