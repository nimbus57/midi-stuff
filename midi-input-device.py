import mido
import time

# List to store MIDI events and timestamps
midi_events = []

# Open a MIDI input portS
with mido.open_input() as input_port:
    print(f"Listening for MIDI input on: {input_port.name}")

    try:
        while True:
            for msg in input_port.iter_pending():
                # Get current time in seconds since the epoch
                event_time = time.time()
                
                # Record the event and its timestamp in the list
                # midi_events.append((event_time, msg))
                # Print the event for live feedback
                # print(f"Time: {event_time}, Message: {msg}")
                if msg.type != 'clock':
                    print(f"{msg}")
                    midi_events.append((event_time, msg))

    except KeyboardInterrupt:
        print("\nRecording stopped.")
        print(f"Total events recorded: {len(midi_events)}")

# Display the list of MIDI events with timestamps
for event in midi_events:
    print(event)
