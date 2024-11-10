import json
import os
import random
import datetime
import sys

if getattr(sys, 'frozen', False):
    script_dir = os.path.dirname(sys.executable)
else:
    script_dir = os.path.dirname(os.path.abspath(__file__))

os.system('cls')

def new_session():
    os.system('cls')
    print("You chose to start a new session.\n")

    print("Please provide the type of the session you want to create. (222, 333, 444)\n")
    tmp_session_type = input()
    if tmp_session_type == "222" or tmp_session_type == "333" or tmp_session_type == "444":
        session_type = tmp_session_type
    else:
        os.system('cls')
        print("You did not provide a valid session type. Returning to the main menu...\n")
        return
    
    print("\nPlease provide the name of the session you want to create.\n")
    session_name = input()
    session_name = session_name.replace(" ", "_")
    
    if os.path.exists(session_path):
        os.system('cls')
        print("This session is already existing. Please continue an existing session. Returning to the main menu...\n")
        return

    session_path = os.path.join(script_dir, "your_sessions", f"{session_name}.csv")
    
    with open(session_path, "w", encoding="utf-8") as session_file:
        session_file.write(f'{session_type}\n')
        session_file.write('No.;Time;Scramble;Date;\n')

    os.system('cls')
    print("The " + session_name + " session was successfully created. Returning to the main menu...\n")
    return

def continue_session():
    os.system('cls')
    print("You chose to continue an existing session.\n")
    print("Please provide the name of the session you want to continue.\n")
    
    available_sessions = [f for f in os.listdir(os.path.join(script_dir, "your_sessions")) if f.endswith('.csv')]
    
    if not available_sessions:
        os.system('cls')
        print("No existing sessions found. Please start a new session. Returning to the main menu...\n")
        return
    else:
        print("Available sessions:")
        for session in available_sessions:
            print(session.replace('.csv', ''))
        
    print("\n")
    session_name = input()
    
    if not os.path.exists(os.path.join(script_dir, "your_sessions", f"{session_name}.csv")):
        os.system('cls')
        print("This session is not existing. Returning to the main menu...\n")
        return
    
    os.system('cls')
    
    session_path = os.path.join(script_dir, "your_sessions", f"{session_name}.csv")

    scrambles_222 = []
    scrambles_333 = []
    scrambles_444 = []
    scrambles_222_path = os.path.join(script_dir, "scrambles", "222.txt")
    scrambles_333_path = os.path.join(script_dir, "scrambles", "333.txt")
    scrambles_444_path = os.path.join(script_dir, "scrambles", "444.txt")
    
    with open(session_path, "r", encoding="utf-8") as file:
        session_type = file.readline().strip()

    if session_type == "222":
        with open(scrambles_222_path, "r", encoding="utf-8") as file:
            for line in file:
                scrambles_222.append(line.strip())
        while True:
            current_scramble = scrambles_222[random.randint(0, len(scrambles_222)-1)]
            with open(session_path, "r", encoding="utf-8") as session_file:
                lines = session_file.readlines()
                valid_lines = [line for line in lines[1:] if line.strip() and not line.startswith('No.')]
                if valid_lines:
                    current_solve = int(valid_lines[-1].split(";")[0].strip()) + 1
                else:
                    current_solve = 1
            print("This is a 222 session.")
            print("The scramble for the ",current_solve,". solve is: ",current_scramble,'\n',sep='')
            print("If you are done, please provide the time for this solve.\nPlease provide the time in seconds.\nMake sure you use '.' as a decimal point, not ','.\nMake sure you did not write letters or other symbols in the time.\n\nIf you want to leave, type 'exit'\n")
            time = input()
            if time == "exit":
                os.system('cls')
                break
            else:
                while True:
                    try:
                        time = float(time)
                        break
                    except ValueError:
                        os.system('cls')
                        print("You did not provide a valid time. Please provide the time in seconds, using '.' as the decimal point.\n")
                        time = input()
                dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                os.system('cls')
                print("Do you want to save this solve? (press enter, to save, write 'no', to not save)\n")
                save = input()
                if save == "no":
                    os.system('cls')
                    print("You chose not to save this solve.\n")
                else:
                    os.system('cls')
                    print("You chose to save this solve.\n")
                    if not os.path.exists(session_path):
                        with open(session_path, "w", encoding="utf-8") as session_file:
                            session_file.write('No.;Time;Comment;Scramble;Date;P.1\n')
                            session_file.write(f'{current_solve};{time:.2f};{current_scramble.strip()};{dateandtime};\n')
                    else:
                        with open(session_path, "r", encoding="utf-8") as session_file:
                            lines = session_file.readlines()
                            valid_lines = [line for line in lines[1:] if line.strip() and not line.startswith('No.')]
                            if valid_lines:
                                current_solve = int(valid_lines[-1].split(";")[0].strip()) + 1
                            else:
                                current_solve = 1
                        with open(session_path, "a", encoding="utf-8") as session_file:
                            session_file.write(f'{current_solve};{time:.2f};{current_scramble.strip()};{dateandtime};\n')

    elif session_type == "333":
        with open(scrambles_333_path, "r", encoding="utf-8") as file:
            for line in file:
                scrambles_333.append(line.strip())
        while True:
            current_scramble = scrambles_333[random.randint(0, len(scrambles_333)-1)]
            with open(session_path, "r", encoding="utf-8") as session_file:
                lines = session_file.readlines()
                valid_lines = [line for line in lines[1:] if line.strip() and not line.startswith('No.')]
                if valid_lines:
                    current_solve = int(valid_lines[-1].split(";")[0].strip()) + 1
                else:
                    current_solve = 1
            print("This is a 333 session.")
            print("The scramble for the ",current_solve,". solve is: ",current_scramble,'\n',sep='')
            print("If you are done, please provide the time for this solve.\nPlease provide the time in seconds.\nMake sure you use '.' as a decimal point, not ','.\nMake sure you did not write letters or other symbols in the time.\n\nIf you want to leave, type 'exit'\n")
            time = input()
            if time == "exit":
                os.system('cls')
                break
            else:
                while True:
                    try:
                        time = float(time)
                        break
                    except ValueError:
                        os.system('cls')
                        print("You did not provide a valid time. Please provide the time in seconds, using '.' as the decimal point.\n")
                        time = input()
                dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                os.system('cls')
                print("Do you want to save this solve? (press enter, to save, write 'no', to not save)\n")
                save = input()
                if save == "no":
                    os.system('cls')
                    print("You chose not to save this solve.\n")
                else:
                    os.system('cls')
                    print("You chose to save this solve.\n")
                    if not os.path.exists(session_path):
                        with open(session_path, "w", encoding="utf-8") as session_file:
                            session_file.write('No.;Time;Comment;Scramble;Date;P.1\n')
                            session_file.write(f'{current_solve};{time:.2f};{current_scramble.strip()};{dateandtime};\n')
                    else:
                        with open(session_path, "r", encoding="utf-8") as session_file:
                            lines = session_file.readlines()
                            valid_lines = [line for line in lines[1:] if line.strip() and not line.startswith('No.')]
                            if valid_lines:
                                current_solve = int(valid_lines[-1].split(";")[0].strip()) + 1
                            else:
                                current_solve = 1
                        with open(session_path, "a", encoding="utf-8") as session_file:
                            session_file.write(f'{current_solve};{time:.2f};{current_scramble.strip()};{dateandtime};\n')
        
    elif session_type == "444":
        with open(scrambles_444_path, "r", encoding="utf-8") as file:
            for line in file:
                scrambles_444.append(line.strip())
        while True:
            current_scramble = scrambles_444[random.randint(0, len(scrambles_444)-1)]
            with open(session_path, "r", encoding="utf-8") as session_file:
                lines = session_file.readlines()
                valid_lines = [line for line in lines[1:] if line.strip() and not line.startswith('No.')]
                if valid_lines:
                    current_solve = int(valid_lines[-1].split(";")[0].strip()) + 1
                else:
                    current_solve = 1
            print("This is a 444 session.")
            print("The scramble for the ",current_solve,". solve is: ",current_scramble,'\n',sep='')
            print("If you are done, please provide the time for this solve.\nPlease provide the time in seconds.\nMake sure you use '.' as a decimal point, not ','.\nMake sure you did not write letters or other symbols in the time.\n\nIf you want to leave, type 'exit'\n")
            time = input()
            if time == "exit":
                os.system('cls')
                break
            else:
                while True:
                    try:
                        time = float(time)
                        break
                    except ValueError:
                        os.system('cls')
                        print("You did not provide a valid time. Please provide the time in seconds, using '.' as the decimal point.\n")
                        time = input()
                dateandtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                os.system('cls')
                print("Do you want to save this solve? (press enter, to save, write 'no', to not save)\n")
                save = input()
                if save == "no":
                    os.system('cls')
                    print("You chose not to save this solve.\n")
                else:
                    os.system('cls')
                    print("You chose to save this solve.\n")
                    if not os.path.exists(session_path):
                        with open(session_path, "w", encoding="utf-8") as session_file:
                            session_file.write('No.;Time;Comment;Scramble;Date;P.1\n')
                            session_file.write(f'{current_solve};{time:.2f};{current_scramble.strip()};{dateandtime};\n')
                    else:
                        with open(session_path, "r", encoding="utf-8") as session_file:
                            lines = session_file.readlines()
                            valid_lines = [line for line in lines[1:] if line.strip() and not line.startswith('No.')]
                            if valid_lines:
                                current_solve = int(valid_lines[-1].split(";")[0].strip()) + 1
                            else:
                                current_solve = 1
                        with open(session_path, "a", encoding="utf-8") as session_file:
                            session_file.write(f'{current_solve};{time:.2f};{current_scramble.strip()};{dateandtime};\n')   
    else:
        os.system('cls')
        print("Unexpected error. Returning to the main menu...\n")
        return
        
def view_statistics():
    os.system('cls')
    print("You chose to view the statistics of a session.\n")
    print("Please provide the name of the session you want to view the statistics of.\n")
    print("Available sessions:")
    available_sessions = [f for f in os.listdir(os.path.join(script_dir, "your_sessions")) if f.endswith('.csv')]
    for session in available_sessions:
        print(session.replace('.csv', ''))
    print("\n")
    session_name = input()
    
    if not os.path.exists(os.path.join(script_dir, "your_sessions", f"{session_name}.csv")):
        os.system('cls')
        print("This session is not existing. Returning to the main menu...\n")
        return
    
    with open(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"), "r", encoding="utf-8") as file:
        lines = file.readlines()
        if len(lines) <= 2:
            os.system('cls')
            print("The file has no solves. Returning to the main menu...\n")
            return
    
    print("Fetching data...")
    
    fastest_solve = []
    with open(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"), "r", encoding="utf-8") as file:
        unnecessary_lines = file.readline()
        unnecessary_lines += file.readline()
        fastest_time = None
        fastest_scramble = None
        fastest_date = None
        for line in file:
            if line.strip():
                parts = line.split(';')
                if len(parts) >= 5:
                    time = float(parts[1])
                    scramble = parts[2]
                    date = parts[3].strip()
                    if fastest_time is None or time < fastest_time:
                        fastest_time = time
                        fastest_scramble = scramble
                        fastest_date = date
        if fastest_time is not None:
            fastest_solve.append((fastest_time, fastest_scramble, fastest_date))
    
    latest_solves = []
    with open(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"), "r", encoding="utf-8") as file:
        unnecessary_lines = file.readline()
        unnecessary_lines += file.readline()
        for line in file:
            if line.strip():
                parts = line.split(';')
                if len(parts) >= 5:
                    time = float(parts[1])
                    latest_solves.append(time)
    if len(latest_solves) >= 5:
        latest_ao5 = sum(sorted(latest_solves)[-5:]) / 5
        latest_ao5 = round(latest_ao5, 2)
    else:
        latest_ao5 = "Not enough time, to calculate your latest AO5"
    
    with open(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"), "r", encoding="utf-8") as file:
        unnecessary_lines = file.readline()
        unnecessary_lines += file.readline()
        for line in file:
            if line.strip():
                parts = line.split(';')
                if len(parts) >= 5:
                    time = float(parts[1])
                    latest_solves.append(time)
    if len(latest_solves) >= 12:
        latest_ao12 = sum(sorted(latest_solves)[-12:]) / 12
        latest_ao12 = round(latest_ao12, 2)
    else:
        latest_ao12 = "Not enough time, to calculate your latest AO12"

    with open(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"), "r", encoding="utf-8") as file:
        unnecessary_lines = file.readline()
        unnecessary_lines += file.readline()
        for line in file:
            if line.strip():
                parts = line.split(';')
                if len(parts) >= 5:
                    time = float(parts[1])
                    latest_solves.append(time)
    if len(latest_solves) >= 100:
        latest_ao100 = sum(sorted(latest_solves)[-100:]) / 100
        latest_ao100 = round(latest_ao100, 2)
    else:
        latest_ao100 = "Not enough time, to calculate your latest AO100"
        
    best_ao5 = "Not enough time, to calculate your best AO5"
    if len(latest_solves) >= 5:
        best_ao5 = min([sum(sorted(latest_solves)[i:i+5])/5 for i in range(len(latest_solves)-4)])
        best_ao5 = round(best_ao5, 2)

    best_ao12 = "Not enough time, to calculate your best AO12"
    if len(latest_solves) >= 12:
        best_ao12 = min([sum(sorted(latest_solves)[i:i+12])/12 for i in range(len(latest_solves)-11)])
        best_ao12 = round(best_ao12, 2)

    best_ao100 = "Not enough time, to calculate your best AO100"
    if len(latest_solves) >= 100:
        best_ao100 = min([sum(sorted(latest_solves)[i:i+100])/100 for i in range(len(latest_solves)-99)])
        best_ao100 = round(best_ao100, 2)

    os.system('cls')
    print("Your fastest solve is ",fastest_solve[0][0]," seconds. The scramble was ",fastest_solve[0][1], ". It happened on ",fastest_solve[0][2],".\n",sep='')
    print("Your latest AO5: ",latest_ao5,"\n",sep='')
    print("Your latest AO12: ",latest_ao12,"\n",sep='')
    print("Your latest AO100: ",latest_ao100,"\n",sep='')
    print("Your best AO5: ",best_ao5,"\n",sep='')
    print("Your best AO12: ",best_ao12,"\n",sep='')
    print("Your best AO100: ",best_ao100,"\n",sep='')

    _go_back = input("Press enter, to go back to the main menu.\n")
    os.system('cls')
    return


def import_session():
    os.system('cls')
    print("READ CAREFULLY!\nPlease have the file you want to import, in the 'import_session' folder.\nMake sure it is named 'import.txt'\nConfirm, that it is formatted in the correct way.\nMake sure, you only have one file named 'import.txt' in the 'import_session' folder.\nOnly import txt files, that are cstimer.net standards. We will support more types of files, in future updates.\nPlease aknowledge, that if you mess up one of the steps, your sessions can be permanently corrupted. The developers are not responsible for any data loss!\nType anything that is not 'yes', and you will be directed back to the main menu, exit the program, and do these steps. When you are done, come back here. If you want to proceed, then type 'yes'.\n")
    import_confirmation = input()
    if import_confirmation == "yes":
        os.system('cls')
        print("You chose to proceed.\n")
        
        print("Please provide the type of the session you want to create. (222, 333, 444)\n")
        tmp_session_type = input()
        if tmp_session_type == "222" or tmp_session_type == "333" or tmp_session_type == "444":
            session_type = tmp_session_type
        else:
            os.system('cls')
            print("You did not provide a valid session type. Returning to the main menu...\n")
            return
        
        print("Please provide a name for the session you want to import.\n")
        session_name = input()
        session_name = session_name.replace(" ", "_")
        if os.path.exists(os.path.join(script_dir, "your_sessions", f"{session_name}.csv")):
            os.system('cls')
            print("This session is already existing. Please choose a different name. Returning to the main menu...\n")
            return
        
        session_number = input("Please specify the session number you want to import from (1-15)\n\n").strip()
    else:
        os.system('cls')
        print("You did not choose to proceed. Returning to main menu...\n")
        return

    os.system('cls')
    print("Working...\n")

    import_file_path = os.path.join(script_dir, "import_sessions", "import.txt")
    sessions_dir = os.path.join(script_dir, "your_sessions")

    if not os.path.exists(import_file_path):
        os.system('cls')
        print("The import file does not exist. Returning to the main menu...\n")
        return
    else:
        # Read the import file
        with open(import_file_path, "r", encoding="utf-8") as import_file:
            data = json.load(import_file)

        if not session_number.isdigit() or not (1 <= int(session_number) <= 15):
            os.system('cls')
            print("Invalid session number. Returning to the main menu...\n")
            return
        else:
            session_type = f"session{session_number}"
            scrambles = data[session_type]

            session_path = os.path.join(sessions_dir, f"{session_name}.csv")

            if os.path.exists(session_path):
                os.system('cls')
                print("This session already exists. Please choose a different name. Returning to the main menu...\n")
                return
            else:
                with open(session_path, "w", encoding="utf-8") as session_file:
                    session_file.write(f'{session_type}\n')
                    session_file.write('No.;Time;Scramble;Date;\n')
                    for i, scramble_data in enumerate(scrambles, start=1):
                        # Debugging output to check the structure of scramble_data
                        print(f"Scramble data for index {i}: {scramble_data}")

                        time = scramble_data[0]
                        scramble = scramble_data[1].lstrip()

                        if isinstance(time, list) and len(time) >= 2:
                            time_before_decimal = time[0]
                            time_after_decimal = time[1]

                            time = float(f"{time_before_decimal}.{time_after_decimal}")
                        else:
                            print(f"Unexpected time format for index {i}: {time}")  # Debugging output
                            time = 0.0

                        try:
                            formatted_time = round(time, 2) if time else 0.0
                        except ValueError:
                            print(f"Error converting time for index {i}: {time}")  # Debugging output
                            formatted_time = 0.0

                        session_file.write(f'{i};{formatted_time:.2f};{scramble};0;\n')

                os.system('cls')
                print(f"The session '{session_name}' was successfully created and data imported.\n")
                print("Do you want to delete the import file? (yes/anything else)\n")
                delete_import_file = input()
                if delete_import_file == "yes":
                    os.remove(import_file_path)
                    print("The import file was successfully deleted.\n")
                print("Returning to the main menu...\n")
                return


def manage_sessions():
    os.system('cls')
    print("You chose to manage your sessions.\n")
    print("Please provide the name of the session you want to manage.\n")

    available_sessions = [f for f in os.listdir(os.path.join(script_dir, "your_sessions")) if f.endswith('.csv')]
    
    if not available_sessions:
        os.system('cls')
        print("No existing sessions found. Please start a new session. Returning to the main menu...\n")
        return
    else:
        print("Available sessions:")
        for session in available_sessions:
            print(session.replace('.csv', ''))
        
    print("\n")
    session_name = input()
    if not os.path.exists(os.path.join(script_dir, "your_sessions", f"{session_name}.csv")):
        os.system('cls')
        print("This session is not existing. Returning to the main menu...\n")
        return
    else:
        os.system('cls')
        print("You chose to manage the " + session_name + " session.\n")
        print("What do you want to do? (delete - d, rename - r, exit - anything else)\n")
        manage_session_question = input()
        
        if manage_session_question == "d":
            os.system('cls')
            print("Are you sure you want to delete the " + session_name + " session? (yes/anything else)\n")
            sure = input()
            if sure == "yes":
                os.system('cls')
                print("You chose to delete the " + session_name + " session.\n")
                os.remove(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"))
                print("The " + session_name + " session was successfully deleted.\n")
                return
            else:
                os.system('cls')
                print("You did not choose to delete the " + session_name + " session. Returning to the main menu...\n")
                return
        elif manage_session_question == "r":
            os.system('cls')
            print("You chose to rename the " + session_name + " session.\n")
            print("Please provide the new name for the session.\n")
            new_session_name = input()
            os.rename(os.path.join(script_dir, "your_sessions", f"{session_name}.csv"), 
                      os.path.join(script_dir, "your_sessions", f"{new_session_name}.csv"))
            os.system('cls')
            print("The " + session_name + " session was successfully renamed.\n")
            return
        else:
            os.system('cls')
            print("You did not choose a valid option. Returning to the main menu...\n")
            return

#main menu def

def main_menu():
    print("What do you want to do? (Choose a number)\n\n1: Start a new, or continue an existing session.\n2: View your statistics.\n3: Import a cstimer.net session.\n4: Manage your sessions.\n")
    main_menu_question = input()

    if main_menu_question == "1":
        os.system('cls')
        print("If you want to start a new session, just type 'new'.\nIf you want to continue an existing session, type 'cont'.\n")
        new_or_continue = input()
        if new_or_continue == "new":
            new_session()
        elif new_or_continue == "cont":
            continue_session()
        else:
            os.system('cls')
            print("You did not choose a valid option. Returning to main menu...\n")
            return

    elif main_menu_question == "2":
        view_statistics()

    elif main_menu_question == "3":
        import_session()

    elif main_menu_question == "4":
        manage_sessions()

    else:
        os.system('cls')
        print("You did not choose a valid option. Returning to main menu...\n")
#main program
while True:
    main_menu()

