import os
import subprocess
import shlex

def execute_command(command_line):
    """
    Parses and executes a command line with support for pipes (|)
    and redirection (<, >).
    """
    # 1. Handle Pipes first (Split the command into segments)
    # Example: "ls -la | grep .py" becomes ["ls -la", "grep .py"]
    try:
        commands = command_line.split('|')
    except Exception:
        print("Error parsing pipes.")
        return

    processes = []
    prev_pipe_out = None  # To store output of the previous process in the chain

    # Loop through each command in the pipe chain
    for i, cmd_str in enumerate(commands):
        cmd_str = cmd_str.strip()      
        # Separate Input/Output Redirection
        input_file = None
        output_file = None
        append_mode = False

        # --- Handle Output Redirection (>) ---
        if '>' in cmd_str:
            parts = cmd_str.split('>')
            cmd_str = parts[0].strip() # The command part
            filename = parts[1].strip() # The filename part
            try:
                output_file = open(filename, 'w')
            except IOError as e:
                print(f"Error opening output file: {e}")
                return

        # --- Handle Input Redirection (<) ---
        if '<' in cmd_str:
            parts = cmd_str.split('<')
            cmd_str = parts[0].strip()
            filename = parts[1].strip()
            try:
                input_file = open(filename, 'r')
            except IOError as e:
                print(f"Error opening input file: {e}")
                return

        # --- Prepare Arguments ---
        # shlex.split helps handle spaces inside quotes properly
        # e.g., echo "Hello World" -> ['echo', 'Hello World']
        try:
            args = shlex.split(cmd_str)
        except ValueError:
            print("Error parsing command arguments.")
            return

        if not args:
            continue

        # --- Determine STDIN (Input) ---
        # If it's the first command, input comes from file (if < exists) or None (User keyboard)
        # If it's not the first command, input comes from the previous pipe
        if i == 0:
            stdin_target = input_file
        else:
            stdin_target = prev_pipe_out

        # --- Determine STDOUT (Output) ---
        # If it's the last command, output goes to file (if > exists) or None (Console)
        # If it's not the last command, output goes to the next pipe
        if i < len(commands) - 1:
            stdout_target = subprocess.PIPE
        else:
            stdout_target = output_file

        # --- Execute the Process ---
        try:
            # Popen starts the process
            p = subprocess.Popen(
                args,
                stdin=stdin_target,
                stdout=stdout_target,
                stderr=subprocess.PIPE, # Capture errors to print later
                text=True # Treat input/output as text strings, not bytes
            )
            
            # Save the current process to list
            processes.append(p)
            
            # Save this process's stdout to be the next process's stdin
            prev_pipe_out = p.stdout
            
            # Important: If we passed an input_file, we can close the wrapper now
            # subprocess has its own handle
            if input_file: input_file.close()

        except FileNotFoundError:
            print(f"Command not found: {args[0]}")
            return
        except Exception as e:
            print(f"Execution error: {e}")
            return

    # --- Wait for completion ---
    # We only really need to wait for the last process in the chain to finish
    # and communicate with the user
    last_process = processes[-1]
    
    # communicate() reads remaining data from stdout/stderr and waits for exit
    output, error = last_process.communicate()

    # If there was output (and it wasn't redirected to a file), print it
    if output:
        print(output, end='')
    
    # If there were errors, print them
    if error:
        print(error, end='')

    # Clean up: Close the output file if we opened one
    if output_file:
        output_file.close()


def main():
    print("Welcome to Python Shell (Type 'exit' to quit)")
    
    while True:
        try:
            current_dir = os.getcwd()
            user_input = input(f"{current_dir} $ ")

            if not user_input.strip():
                continue

            if user_input.strip().lower() == "exit":
                print("Exiting shell...")
                break

            # 'cd' must be handled by the shell itself, not subprocess!
            if user_input.startswith("cd "):
                try:
                    target_dir = user_input.split(" ", 1)[1].strip()
                    os.chdir(target_dir)
                except FileNotFoundError:
                    print(f"Directory not found: {target_dir}")
                except Exception as e:
                    print(f"Error changing directory: {e}")
                continue

            # 5. Execute General Commands
            execute_command(user_input)

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\nType 'exit' to quit.")
        except Exception as e:
            print(f"Shell Error: {e}")

if __name__ == "__main__":
    main()