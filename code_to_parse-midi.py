import mido
import json

def preprocess_midi(file_path, output_path, threshold=60):
    midi_file = mido.MidiFile(file_path)
    notes = []

    # Default tempo in microseconds per beat (120 BPM)
    tempo = 500000  
    ticks_per_beat = midi_file.ticks_per_beat  # Get ticks per beat from the file

    current_time = 0  # Time accumulator in ticks
    for track in midi_file.tracks:
        for msg in track:
            current_time += msg.time  # Increment time in ticks

            # If a tempo change occurs, update the tempo
            if msg.type == 'set_tempo':
                tempo = msg.tempo

            # Process note_on messages with velocity > 0 (active notes)
            if msg.type == 'note_on' and msg.velocity > 0:
                # Convert time from ticks to microseconds
                time_in_microseconds = (current_time / ticks_per_beat) * tempo
                notes.append({
                    'note': msg.note,
                    'time': time_in_microseconds / 1_000_000,  # Convert to seconds for MicroPython
                    'type': 'high' if msg.note > threshold else 'low'
                })

    # Save the notes to a JSON file
    with open(output_path, 'w') as f:
        json.dump(notes, f)

# Run the script
preprocess_midi('Jingle bells.mid', 'midi_data.json', threshold=60)
