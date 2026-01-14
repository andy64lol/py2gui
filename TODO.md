# TODO List - Fix Pylance "None" attribute access errors in game_example.py

## Task: Fix 7 locations where .lower() is called on potentially None values from user_type_in()

### Locations to fix:
- [ ] Line 259: `response.lower()` in mushroom puzzle
- [ ] Line 475: `answer.lower()` in library riddle
- [ ] Line 492: `response.lower()` in statue room puzzle
- [ ] Line 507: `response.lower()` in treasure room puzzle
- [ ] Line 519: `play_again.lower()` in play method
- [ ] Line 603: `command.lower().strip()` in process_command
- [ ] Line 646: Direct call in start_game

### Fix Pattern:
For each location:
1. Store `user_type_in()` result in a variable
2. Check `if variable is not None:` before calling `.lower()`
3. Handle `None` case with appropriate default behavior

### Changes to make:
1. Line 259: Add None check for mushroom puzzle response
2. Line 475: Add None check for riddle answer
3. Line 492: Add None check for statue room response
4. Line 507: Add None check for treasure room response
5. Line 519: Add None check for play_again prompt
6. Line 603: Add None check for command input
7. Line 646: Add None check for return to menu prompt

