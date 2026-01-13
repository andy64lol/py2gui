from py2gui import display, user_type_in, run, clear, copy_text, select_all, exit_gui, user_write

def main():
    display("Hello, world!")
    name = user_type_in("Enter your name:  ")
    display(f"Hi {name}!")
    display("This is a test.")
    if user_type_in("type clear to clear  ") == "clear":
        clear()
    else:
        display("You didn't clear")
        if user_type_in("type copy to copy last line  ") == "copy":
            copy_text()
            display("Last line copied to clipboard.")
            user_write("So btw... how are you feeling?  ")
        else:
            display("You didn't copy")
    display("Select all text and copy it manually to see select_all in action.")
    if user_type_in("type select_all to select all text"   ) == "select_all":
        select_all()
        display("All text selected.")
        if user_type_in("type copy to copy all selected text  ") == "copy":
            copy_text()
            display("All text copied to clipboard.")
    else:
        display("You didn't select all")

        # Display some colored text
        display("=== ANSI Color Terminal Demo ===", parse_ansi=False)
        display("")
        
        # Basic colors
        display("Basic ANSI Colors:")
        display("\033[30mBlack\033[0m \033[31mRed\033[0m \033[32mGreen\033[0m \033[33mYellow\033[0m")
        display("\033[34mBlue\033[0m \033[35mMagenta\033[0m \033[36mCyan\033[0m \033[37mWhite\033[0m")
        display("")
        
        # Bright colors
        display("Bright Colors:")
        display("\033[90mGray\033[0m \033[91mBright Red\033[0m \033[92mBright Green\033[0m")
        display("\033[93mBright Yellow\033[0m \033[94mBright Blue\033[0m \033[95mBright Magenta\033[0m")
        display("")
        
        # Background colors
        display("Background Colors:")
        display("\033[40;37mBlack Background\033[0m \033[41mRed Background\033[0m")
        display("\033[42mGreen Background\033[0m \033[43mYellow Background\033[0m")
        display("")
        
        # Text styles
        display("Text Styles:")
        display("\033[1mBold\033[0m \033[3mItalic\033[0m \033[4mUnderline\033[0m \033[9mStrikethrough\033[0m")
        display("")
        
        # Combined styles
        display("Combined Styles:")
        display("\033[1;31mBold Red Text\033[0m")
        display("\033[1;4;32mBold Underlined Green Text\033[0m")
        display("\033[1;33;44mBold Yellow on Blue\033[0m")
        display("\033[1;37;41mBold White on Red\033[0m")
        display("")
        
        # Get user input
        display("Now let's get some input...")
        name = user_type_in("What's your name? ")
        if name:
            display(f"\033[1;32mHello, {name}!\033[0m")
        
        age = user_write("How old are you? ")
        if age:
            display(f"\033[1;36mYou are {age} years old.\033[0m")
        
    display("Rerun test?")
    if user_type_in("type yes to rerun"   ) == "yes":
        main()
    else:
        display("Goodbye!")
        exit_gui()

run(main)  # GUI runs on main thread, your logic runs in worker thread
