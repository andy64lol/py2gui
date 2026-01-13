# Py2GUI - Terminal-Style GUI Framework for Python

Py2GUI is a lightweight, terminal-style GUI framework for Python that provides a console-like interface with modern features like ANSI color support, theme switching, and configurable menus. It's perfect for building interactive command-line applications with a graphical interface, educational tools, or any application that benefits from a terminal-like user experience.

## Features

### 🎨 **Advanced ANSI Color Support**
- Full ANSI escape code parsing (colors, styles, backgrounds)
- 16 basic colors (8 standard + 8 bright variants)
- 8 background colors
- Text styles: bold, italic, underline, strikethrough, reverse video
- Color disabling via configuration
- Direct color display methods with hex color support

### 🖥️ **Terminal-Style Interface**
- Terminal-like input field with prompt support
- Real-time input with Enter key support
- Scrollable text area with word wrap
- Copy/paste and select all functionality
- Auto-scrolling to latest output

### ⚙️ **Configuration System**
- JSON-based configuration file
- Disable specific menus, views, or colors
- Customizable themes
- Persistent configuration loading

### 🎭 **Multiple Themes**
- Default (white on black)
- Dark theme
- Light theme
- Matrix theme (green on black)
- Easy theme switching via menu

### 🧵 **Thread-Safe Operations**
- Safe multithreading support
- Worker thread execution
- Proper GUI updates from background threads
- Non-blocking input methods

### 📱 **User-Friendly Features**
- Built-in menus (File, Edit, View, Colors)
- Context-aware input methods
- Error handling and graceful exit
- Demo function for color display
- Configurable window size

## Installation

No installation required! Just copy the `Py2GUI.py` file to your project directory.

Requirements:
- Python 3.6+
- Tkinter (usually included with Python)

## Quick Start

```python
from Py2GUI import Py2GUI, run, display, user_type_in

# Create a simple application
def my_app():
    display("Welcome to Py2GUI!")
    display("\033[1;32mThis is bold green text!\033[0m")
    
    # Get user input
    name = user_type_in("What's your name? ")
    display(f"Hello, {name}!")
    
    # Use direct colored text
    display_colored("This is colored text!", fg_color="red", bg_color="yellow", bold=True)

# Run the application
if __name__ == "__main__":
    gui = Py2GUI("My Application")
    gui.run(my_app)
```

## API Reference

### Core Methods

#### `display(text: str, parse_ansi: bool = True)`
Display text in the output area. Automatically parses ANSI escape codes by default.

```python
# Plain text
display("Hello, World!")

# With ANSI colors
display("\033[1;31mError!\033[0m \033[33mWarning!\033[0m")

# Without ANSI parsing
display("Raw text with \033[ codes", parse_ansi=False)
```

#### `display_colored(text: str, fg_color: Optional[str] = None, bg_color: Optional[str] = None, bold: bool = False, underline: bool = False)`
Directly display colored text without ANSI codes.

```python
display_colored("Red text", fg_color="red")
display_colored("Blue on yellow", fg_color="blue", bg_color="yellow")
display_colored("Bold underlined", bold=True, underline=True)
display_colored("Hex color", fg_color="#ff00ff")
```

#### `user_write(prompt: str = "Input:") -> Optional[str]`
Open a dialog window for user input (traditional popup).

```python
name = user_write("Enter your name:")
```

#### `user_type_in(prompt: str = ">> ") -> Optional[str]`
Terminal-style input in the main window (recommended).

```python
command = user_type_in("Enter command: ")
```

#### `set_theme(theme_name: str)`
Change the application theme.

```python
set_theme("dark")    # Black background, white text
set_theme("light")   # White background, black text
set_theme("matrix")  # Green on black
set_theme("default") # Reset to default
```

### Utility Methods

- `clear()` - Clear the output area
- `copy_text()` - Copy selected text to clipboard
- `select_all()` - Select all text in output area
- `focus_input()` - Focus on the input field
- `exit()` - Close the application

## Configuration

Create a `config.json` file to customize Py2GUI:

```json
{
    "disabled_menus": ["Colors", "Edit"],
    "disabled_views": ["Demo ANSI Colors", "Focus Input"],
    "disabled_colors": ["31", "33", "91"],
    "show_clear_button": true,
    "show_demo_button": true
}
```

### Configuration Options

- **disabled_menus**: List of menu names to hide (File, Edit, View, Colors)
- **disabled_views**: List of view menu items to hide
- **disabled_colors**: List of ANSI color codes to disable
- **show_clear_button**: Show/hide clear button in toolbar
- **show_demo_button**: Show/hide demo button

## ANSI Color Codes

Py2GUI supports standard ANSI color codes:

### Text Colors
- `30`: Black
- `31`: Red
- `32`: Green
- `33`: Yellow
- `34`: Blue
- `35`: Magenta
- `36`: Cyan
- `37`: White
- `90`: Gray
- `91`: Bright Red
- `92`: Bright Green
- `93`: Bright Yellow
- `94`: Bright Blue
- `95`: Bright Magenta
- `96`: Bright Cyan
- `97`: Bright White

### Background Colors
- `40`: Black background
- `41`: Red background
- `42`: Green background
- `43`: Yellow background
- `44`: Blue background
- `45`: Magenta background
- `46`: Cyan background
- `47`: White background

### Text Styles
- `1`: Bold
- `3`: Italic
- `4`: Underline
- `7`: Reverse video
- `9`: Strikethrough
- `0`: Reset all attributes

## Examples

### 1. Interactive Command Processor

```python
from Py2GUI import Py2GUI, display, user_type_in, display_colored

def command_processor():
    display("\033[1;36m=== Command Processor ===\033[0m")
    
    while True:
        cmd = user_type_in("cmd> ")
        if cmd is None:  # User closed window
            break
            
        if cmd.lower() == "exit":
            display("Goodbye!")
            break
        elif cmd.lower() == "help":
            display("Available commands: help, echo, clear, exit")
        elif cmd.startswith("echo "):
            display(f"Echo: {cmd[5:]}")
        elif cmd.lower() == "clear":
            clear()
        else:
            display_colored(f"Unknown command: {cmd}", fg_color="red", bold=True)

gui = Py2GUI("Command Processor", width=100, height=30)
gui.run(command_processor)
```

### 2. Log Viewer with Color Coding

```python
from Py2GUI import Py2GUI, display, display_colored
import random
import time

def log_generator():
    log_levels = {
        "INFO": ("32", "green"),
        "WARN": ("33", "yellow"),
        "ERROR": ("31", "red"),
        "DEBUG": ("36", "cyan")
    }
    
    for i in range(20):
        level, (ansi_code, color_name) = random.choice(list(log_levels.items()))
        message = f"Log message {i+1}: Sample log entry with {level} level"
        display(f"\033[{ansi_code}m[{level}]\033[0m {message}")
        time.sleep(0.5)

gui = Py2GUI("Log Viewer")
gui.run(log_generator)
```

### 3. Game with Terminal UI

```python
from Py2GUI import Py2GUI, display, user_type_in, display_colored

def number_guessing_game():
    import random
    
    display("\033[1;35m=== Number Guessing Game ===\033[0m")
    secret = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess_input = user_type_in(f"Guess (1-100, attempt {attempts+1}): ")
        if guess_input is None:
            break
            
        try:
            guess = int(guess_input)
            attempts += 1
            
            if guess < secret:
                display_colored("Too low!", fg_color="blue")
            elif guess > secret:
                display_colored("Too high!", fg_color="red")
            else:
                display_colored(f"🎉 Correct! You guessed it in {attempts} attempts!", 
                              fg_color="green", bold=True)
                break
        except ValueError:
            display_colored("Please enter a valid number!", fg_color="yellow")

gui = Py2GUI("Guessing Game")
gui.run(number_guessing_game)
```

## Advanced Usage

### Custom Configuration

```python
# Load with custom config
gui = Py2GUI("My App", config_file="my_config.json")

# Or modify config after creation
gui.config["disabled_colors"] = ["31"]  # Disable red
```

### Direct ANSI Code Usage

```python
# Complex ANSI formatting
display("\033[1;4;33mBold underlined yellow text\033[0m")
display("\033[1;37;41mBold white on red background\033[0m")
display("\033[3;36mItalic cyan text\033[0m")
```

### Threading Example

```python
from threading import Thread
import time

def background_task():
    for i in range(10):
        display(f"Background task: {i+1}")
        time.sleep(1)

def main():
    display("Starting background task...")
    thread = Thread(target=background_task)
    thread.daemon = True
    thread.start()
    
    # Continue with main thread
    user_type_in("Main thread is still responsive. Press Enter to exit:")

gui = Py2GUI("Thread Example")
gui.run(main)
```

## Keyboard Shortcuts

- **Enter**: Submit input
- **Ctrl+C** (in some contexts): Copy
- **Ctrl+A**: Select all
- **Menu shortcuts**: Accessible via menu bar

## Troubleshooting

### Common Issues

1. **Colors not working**: Ensure you're using valid ANSI codes or check if colors are disabled in config
2. **Input not responding**: Make sure you're using `user_type_in()` for terminal-style input
3. **Threading issues**: Use the `run()` method with a worker function for proper threading
4. **Window not closing**: Use the exit() method or close via the File menu

### Debug Mode

For debugging, you can catch exceptions:

```python
try:
    gui = Py2GUI("My App")
    gui.run(my_function)
except Exception as e:
    print(f"GUI Error: {e}")
```

## License

MIT License. See [LICENSE](https://github.com/py2gui/Py2GUI/blob/main/LICENSE).

## Contributing

Feel free to fork and modify for your needs. Key areas for extension:

1. Additional ANSI code support
2. More theme options
3. Custom widget integration
4. Plugin system

---

**Py2GUI** makes it easy to create terminal-style applications with modern GUI features. Perfect for tools, educational software, or any application where a console interface is preferred but with enhanced visual capabilities.