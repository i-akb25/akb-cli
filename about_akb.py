import sys
import os
import time
import platform
import webbrowser
import shutil
import random
from datetime import datetime

class Colors:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GRAY = '\033[90m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class Cursor:
    BLOCK = '\033[2 q'
    LINE = '\033[6 q'
    RESET = '\033[0 q'

def play_sound(event):
    if platform.system() == "Windows":
        import winsound
        if event == "startup":
            winsound.Beep(800, 150)
            winsound.Beep(1200, 200)
        elif event == "success":
            winsound.Beep(1500, 200)
        elif event == "error":
            winsound.Beep(300, 300)
    else:
        if event in ["startup", "success", "error"]:
            sys.stdout.write('\a')
            sys.stdout.flush()  

if os.name == 'nt':
    os.system('')

history = []
visited_sections = set()
achievements = set()
TOTAL_ACHIEVEMENTS = 8

core_sections = ['about', 'education', 'experience', 'skills', 'projects', 'portfolio', 'contact', 'philosophy', 'timeline', 'goals', 'story']

def get_width():
    return shutil.get_terminal_size().columns

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typing_effect(text, speed=0.03, color=Colors.RESET):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(Colors.RESET + "\n")

def print_centered(text, color=Colors.RESET):
    width = get_width()
    for line in text.split('\n'):
        print(color + line.center(width) + Colors.RESET)

def print_separator(char="=", color=Colors.GRAY):
    print(color + char * get_width() + Colors.RESET)

def print_header():
    print(f"{Colors.CYAN}{Colors.BOLD}AKB CLI v1.0.0{Colors.RESET}")
    print(f"{Colors.GRAY}" + "-" * 32 + f"{Colors.RESET}\n")

def print_footer():
    print(f"\n{Colors.GRAY}" + "━" * 64)
    print(f"{Colors.YELLOW}Type 'help' to see commands.{Colors.GRAY}")
    print(f"{Colors.YELLOW}Type 'more' to have fun.{Colors.GRAY}")
    print("━" * 64 + f"{Colors.RESET}\n")

def progress_bar(width=30, speed=0.03):
    sys.stdout.write(Colors.CYAN)
    for i in range(width + 1):
        percent = int((i / width) * 100)
        bar = "█" * i + " " * (width - i)
        sys.stdout.write(f"\r[{bar}] {percent}%")
        sys.stdout.flush()
        time.sleep(speed)
    sys.stdout.write(Colors.RESET + "\n\n")

def continue_prompt():
    print()
    sys.stdout.write(f"{Colors.GRAY}Press [ENTER] to continue...{Colors.RESET}")
    sys.stdout.flush()
    input()
    clear_screen()

def unlock_achievement(title, desc):
    if title not in achievements:
        achievements.add(title)
        play_sound("success")
        print(f"\n{Colors.MAGENTA}🏆 Achievement Unlocked{Colors.RESET}")
        print(f"{Colors.YELLOW}☑ {title}{Colors.RESET}")
        print(f"{Colors.GRAY}{desc}{Colors.RESET}\n")
        time.sleep(1.0)

def fake_terminal_startup():
    clear_screen()
    if platform.system() == "Windows":
        version = platform.version()
        print(f"Microsoft Windows [Version {version}]")
        print("(c) Microsoft Corporation. All rights reserved.\n")
        print("C:\\Users\\Recruiter> python akb.py\n")
    else:
        print("recruiter@akb-macbook:~$ python akb.py\n")
    
    time.sleep(1.2)
    
    steps = [
        "Initializing Runtime...",
        "Loading Profile...",
        "Loading Experience...",
        "Loading Projects...",
        "Loading AI Modules...",
        "Loading Portfolio...",
        "Checking Dependencies...",
        "Loading Completed."
    ]
    
    for step in steps:
        print(f"{Colors.GRAY}{step}{Colors.RESET}")
        time.sleep(0.4)
    
    time.sleep(0.5)
    play_sound("startup")
    print(f"\n{Colors.GREEN}Ready.{Colors.RESET}\n")
    time.sleep(0.8)
    clear_screen()
    
    print_separator("═", Colors.CYAN)
    print_centered("AKB CLI", Colors.CYAN + Colors.BOLD)
    print_centered("Know me through code.", Colors.CYAN)
    print_separator("═", Colors.CYAN)
    
    print(f"\n{Colors.BOLD}System Information{Colors.RESET}\n")
    time.sleep(0.5)
    
    plat_str = f"{platform.system()} {platform.release()}"
    py_version = sys.version.split()[0]
    term_width = get_width()
    now = datetime.now()
    
    print(f"{Colors.GRAY}Platform{Colors.RESET}")
    print(f"{Colors.CYAN}{plat_str}{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.GRAY}Python{Colors.RESET}")
    print(f"{Colors.CYAN}{py_version}{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.GRAY}Terminal Width{Colors.RESET}")
    print(f"{Colors.CYAN}{term_width}{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.GRAY}Session Started{Colors.RESET}")
    print(f"{Colors.CYAN}{now.strftime('%B %d, %Y')}{Colors.RESET}\n")
    time.sleep(0.5)

def welcome_message():
    print_header()
    
    typing_effect("Hello there 👋", 0.03, Colors.GREEN)
    time.sleep(0.25)
    
    typing_effect("Thank you for taking a few moments to run this program.", 0.03, Colors.GREEN)
    time.sleep(0.25)
    
    typing_effect("Instead of introducing myself through another PDF...", 0.03, Colors.GREEN)
    time.sleep(0.25)
    
    typing_effect("I thought I'd introduce myself through code.", 0.03, Colors.GREEN)
    time.sleep(0.25)
    
    typing_effect("Welcome to AKB CLI.\n", 0.04, Colors.CYAN)

def cmd_about(is_tour=False):
    print_header()
    if is_tour: print(f"{Colors.YELLOW}Section 3 — Personal Profile{Colors.RESET}\n")
    
    typing_effect("Loading profile...", 0.02, Colors.GRAY)
    progress_bar(20, 0.02)
    
    print(f"{Colors.GRAY}Name{Colors.RESET}")
    time.sleep(0.25)
    print(f"{Colors.CYAN}Anurag Kumar Bharti{Colors.RESET}\n")
    time.sleep(0.25)
    
    print(f"{Colors.GRAY}Role{Colors.RESET}")
    time.sleep(0.25)
    print(f"{Colors.CYAN}Software Engineer{Colors.RESET}\n")
    time.sleep(0.25)
    
    print(f"{Colors.GRAY}Mission{Colors.RESET}")
    time.sleep(0.25)
    print(f"{Colors.CYAN}Build reliable software that solves\nreal-world problems.{Colors.RESET}\n")
    time.sleep(0.25)
    
    print(f"{Colors.GRAY}Focus{Colors.RESET}")
    time.sleep(0.5)
    print(f"{Colors.CYAN}• Backend Development{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}• Full Stack Engineering{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}• Industrial Automation{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}• AI-ready Systems{Colors.RESET}\n")
    
    if not is_tour: print_footer()

def cmd_skills(is_tour=False):
    print_header()
    if is_tour: print(f"{Colors.YELLOW}Section 4 — Technical Skills{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}Programming{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ Java     ✔ JavaScript{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ Python   ✔ C{Colors.RESET}\n")
    time.sleep(0.25)
    print(f"{Colors.YELLOW}Frontend{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ React.js ✔ HTML{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ CSS      ✔ Tailwind CSS{Colors.RESET}\n")
    time.sleep(0.25)
    print(f"{Colors.YELLOW}Backend{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ Node.js  ✔ Express.js{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ REST APIs{Colors.RESET}\n")
    time.sleep(0.25)
    print(f"{Colors.YELLOW}Database & Architecture{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ MongoDB  ✔ MySQL{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ Firebase{Colors.RESET}\n")
    time.sleep(0.25)
    print(f"{Colors.YELLOW}Automation & IoT{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ PLC      ✔ Arduino{Colors.RESET}")
    time.sleep(0.15)
    print(f"{Colors.CYAN}✔ RPi      ✔ IoT Sensors{Colors.RESET}\n")
    if not is_tour: print_footer()

def cmd_philosophy(is_tour=False):
    print_header()
    if is_tour: print(f"{Colors.YELLOW}Section 5 — Engineering Philosophy{Colors.RESET}\n")
    
    msg = (
        "Technology isn't valuable because it's complex.\n"
        "It's valuable because it solves real-world problems.\n\n"
        "I believe good engineering starts with understanding\n"
        "the problem before writing the first line of code.\n\n"
        "Stay curious.\n"
        "Keep learning.\n"
        "Never stop building.\n"
    )
    typing_effect(msg, 0.03, Colors.CYAN)
    if not is_tour: print_footer()

def cmd_goals(is_tour=False):
    print_header()
    if is_tour: print(f"{Colors.YELLOW}Section 6 — Career Goals{Colors.RESET}\n")
    
    points = [
        "• Engineer scalable, high-performance backend systems.",
        "• Bridge the gap between hardware (IoT/Automation) and software.",
        "• Contribute to impactful open-source projects.",
        "• Continuously integrate AI capabilities (like Local LLMs) into daily tools.",
        "• Work with a team that values clean code and continuous learning."
    ]
    for pt in points:
        print(f"{Colors.CYAN}{pt}{Colors.RESET}")
        time.sleep(0.2)
    print()
    if not is_tour: print_footer()

def cmd_contact(is_tour=False):
    print_header()
    if is_tour: print(f"{Colors.YELLOW}Section 7 — Contact Information{Colors.RESET}\n")
    
    print(f"{Colors.GRAY}Email{Colors.RESET}")
    print(f"{Colors.CYAN}anuragbhartiee25@gmail.com{Colors.RESET}\n")
    time.sleep(0.2)
    print(f"{Colors.GRAY}Portfolio{Colors.RESET}")
    print(f"{Colors.CYAN}https://ace-akb.vercel.app{Colors.RESET}\n")
    time.sleep(0.2)
    print(f"{Colors.GRAY}GitHub{Colors.RESET}")
    print(f"{Colors.CYAN}https://github.com/i-akb25{Colors.RESET}\n")
    time.sleep(0.2)
    print(f"{Colors.GRAY}LinkedIn{Colors.RESET}")
    print(f"{Colors.CYAN}https://linkedin.com/in/anuragkumarbharti{Colors.RESET}\n")
    if not is_tour: print_footer()

def cmd_portfolio(is_tour=False):
    print_header()
    if is_tour: print(f"{Colors.YELLOW}Section 8 — Portfolio Prompt{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}Open Interactive Portfolio?{Colors.RESET}\n")
    print(f"{Colors.CYAN}[Y] Yes{Colors.RESET}")
    print(f"{Colors.CYAN}[N] No{Colors.RESET}\n")
    
    sys.stdout.write(f"{Colors.GREEN}Choice > {Colors.RESET}")
    sys.stdout.flush()
    choice = input().strip().lower()
    
    if choice == 'y':
        print(f"\n{Colors.CYAN}Opening https://ace-akb.vercel.app...{Colors.RESET}\n")
        webbrowser.open("https://ace-akb.vercel.app")
    else:
        print(f"\n{Colors.GRAY}Action cancelled.{Colors.RESET}\n")
    
    if not is_tour: print_footer()

def show_menu():
    margin = max(0, (get_width() - 74) // 2)
    space = " " * margin
    c_b = Colors.CYAN; c_h = Colors.YELLOW; c_t = Colors.RESET; c_k = Colors.GREEN
    
    print()
    print(space + f"{c_b}╭────────────────────────────────────────────────────────────────────────╮{Colors.RESET}")
    print(space + f"{c_b}│{c_h}                           AVAILABLE COMMANDS                           {c_b}│{Colors.RESET}")
    print(space + f"{c_b}├─────────────────┬──────────────────────────┬───────────────────────────┤{Colors.RESET}")
    print(space + f"{c_b}│{c_h} Category        {c_b}│{c_h} Commands                 {c_b}│{c_h} Description               {c_b}│{Colors.RESET}")
    print(space + f"{c_b}├─────────────────┼──────────────────────────┼───────────────────────────┤{Colors.RESET}")
    print(space + f"{c_b}│{c_t} 1. Profile      {c_b}│{c_k} about, education         {c_b}│{c_t} Background & studies      {c_b}│{Colors.RESET}")
    print(space + f"{c_b}│{c_t} 2. Experience   {c_b}│{c_k} experience, timeline     {c_b}│{c_t} Work & progression        {c_b}│{Colors.RESET}")
    print(space + f"{c_b}│{c_t} 3. Technical    {c_b}│{c_k} skills, projects         {c_b}│{c_t} Tech stack & works        {c_b}│{Colors.RESET}")
    print(space + f"{c_b}│{c_t} 4. Vision       {c_b}│{c_k} philosophy, goals        {c_b}│{c_t} Mindset & future          {c_b}│{Colors.RESET}")
    print(space + f"{c_b}│{c_t} 5. Connect      {c_b}│{c_k} contact, portfolio       {c_b}│{c_t} Links & resume            {c_b}│{Colors.RESET}")
    print(space + f"{c_b}│{c_t} 6. Extras       {c_b}│{c_k} story, whyhireme         {c_b}│{c_t} Professional narrative    {c_b}│{Colors.RESET}")
    print(space + f"{c_b}│{c_t} 7. System       {c_b}│{c_k} help, more, clear, exit  {c_b}│{c_t} Navigation & utilities    {c_b}│{Colors.RESET}")
    print(space + f"{c_b}╰─────────────────┴──────────────────────────┴───────────────────────────╯{Colors.RESET}")
    print()

def cmd_more():
    margin = max(0, (get_width() - 74) // 2)
    space = " " * margin
    c_b = Colors.CYAN; c_h = Colors.YELLOW; c_t = Colors.RESET; c_k = Colors.GREEN
    
    print()
    print(space + f"{c_b}══════════════════════════════════════════════════════════════════════════{Colors.RESET}")
    print(space + f"{c_h}                     AKB CLI — Developer Playground                     {Colors.RESET}")
    print(space + f"{c_b}══════════════════════════════════════════════════════════════════════════{Colors.RESET}")
    print(space + f"{c_h}🎮 Mini Games{Colors.RESET}")
    print(space + f"{c_b}──────────────────────────────────────────────────────────────────────────{Colors.RESET}")
    print(space + f"{c_k}guess{c_t}      Guess the number")
    print(space + f"{c_k}memory{c_t}     Memory challenge")
    print(space + f"{c_k}binary{c_t}     Decode binary")
    print(space + f"{c_k}rps{c_t}        Rock Paper Scissors")
    print(space + f"{c_k}matrix{c_t}     Matrix mode\n")
    
    print(space + f"{c_h}🕵 Hidden Commands{Colors.RESET}")
    print(space + f"{c_b}──────────────────────────────────────────────────────────────────────────{Colors.RESET}")
    print(space + f"{c_k}hello       coffee      42          akb")
    print(space + f"{c_k}hire        sudo hire anurag")
    print(space + f"{c_k}easteregg   motd        history\n")
    
    print(space + f"{c_h}🏆 Achievements{Colors.RESET}")
    print(space + f"{c_b}──────────────────────────────────────────────────────────────────────────{Colors.RESET}")
    print(space + f"{c_t}Unlocked : {len(achievements)} / {TOTAL_ACHIEVEMENTS}\n")
    
    print(space + f"{Colors.GRAY}Developer Notes: This area exists for curious people.")
    print(space + f"Some commands were intentionally left undocumented.")
    print(space + f"Good luck :){Colors.RESET}")
    print()

def cmd_education():
    print_header()
    print(f"{Colors.CYAN}{Colors.BOLD}National Institute of Technology Patna{Colors.RESET}")
    print(f"{Colors.YELLOW}Bachelor of Technology{Colors.RESET}")
    print(f"{Colors.GRAY}Electrical Engineering{Colors.RESET}")
    print(f"{Colors.GRAY}Graduated 2025{Colors.RESET}\n")
    print_footer()

def cmd_experience():
    print_header()
    print(f"{Colors.YELLOW}Graduate Engineer Trainee{Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}JSW Steel{Colors.RESET}")
    print(f"{Colors.GRAY}• Electrical Maintenance{Colors.RESET}")
    print(f"{Colors.GRAY}• Industrial Automation{Colors.RESET}")
    print(f"{Colors.GRAY}• PLC Systems{Colors.RESET}")
    print(f"{Colors.GRAY}• Level-2 Automation{Colors.RESET}\n")
    
    print(f"{Colors.GRAY}" + "-" * 32 + f"{Colors.RESET}\n")
    
    print(f"{Colors.YELLOW}Full Stack Developer {Colors.RESET}")
    print(f"{Colors.CYAN}{Colors.BOLD}Remote Intern{Colors.RESET}")
    print(f"{Colors.GRAY}• MERN Stack{Colors.RESET}")
    print(f"{Colors.GRAY}• REST APIs{Colors.RESET}")
    print(f"{Colors.GRAY}• MongoDB{Colors.RESET}")
    print(f"{Colors.GRAY}• React.js{Colors.RESET}\n")
    print_footer()

def cmd_projects_list():
    print_header()
    print(f"{Colors.CYAN}ADHAYAN{Colors.RESET}")
    print(f"{Colors.CYAN}Titan{Colors.RESET}")
    print(f"{Colors.CYAN}Drone Delivery System{Colors.RESET}")
    print(f"{Colors.CYAN}Portfolio Website{Colors.RESET}\n")
    print(f"{Colors.GRAY}Type{Colors.RESET}")
    print(f"{Colors.YELLOW}project <name>{Colors.RESET}\n")
    print(f"{Colors.GRAY}Example{Colors.RESET}")
    print(f"{Colors.YELLOW}project adhayan{Colors.RESET}\n")
    print_footer()

def cmd_project_detail(name):
    projects = {
        "adhayan": {
            "Title": "ADHAYAN",
            "Subtitle": "Digital Learning Platform",
            "Problem": "Inefficient manual academic tracking and resource management.",
            "Solution": "A robust digital education platform and portal.",
            "Tech": "React\nNode.js\nMongoDB\nExpress",
            "GitHub": "https://github.com/i-akb25"
        },
        "titan": {
            "Title": "Titan OS: Industrial Edge Telemetry",
            "Subtitle": "Industrial Automation IoT",
            "Problem": "Unexpected machine failures and costly downtime.",
            "Solution": "Real-time IIoT platform with predictive maintenance, TTF estimation, and live telemetry dashboard.",
            "Tech": "React.js\nNode.js\nPython\nMySQL\nDocker",
            "GitHub": "https://github.com/i-akb25/Titan-Edge-Telemetry"
      },
        "drone": {
            "Title": "Drone Delivery System",
            "Subtitle": "Autonomous Logistics",
            "Problem": "Inefficient last-mile delivery in constrained environments.",
            "Solution": "Autonomous payload delivery and dropping mechanism.",
            "Tech": "Raspberrypi\nIoT\npixhawk\npython\nSensors",
            "GitHub": "https://github.com/i-akb25"
        },
        "portfolio": {
            "Title": "Portfolio Website",
            "Subtitle": "Interactive Digital Identity",
            "Problem": "Static, unengaging traditional digital resumes.",
            "Solution": "An interactive, terminal-inspired web portfolio.",
            "Tech": "Next\nTailwind CSS",
            "GitHub": "https://github.com/i-akb25/portfolio"
        }
    }
    
    key = name.lower().replace(" project", "").strip()
    if key == "drone delivery system": key = "drone"
    elif key == "portfolio website": key = "portfolio"
        
    if key in projects:
        p = projects[key]
        print_header()
        print(f"{Colors.GRAY}────────────────────────────{Colors.RESET}")
        print(f"{Colors.CYAN}{Colors.BOLD}{p['Title']}{Colors.RESET}")
        print(f"{Colors.YELLOW}{p['Subtitle']}{Colors.RESET}")
        print(f"{Colors.GRAY}────────────────────────────{Colors.RESET}\n")
        print(f"{Colors.GRAY}Problem\n────────{Colors.RESET}")
        print(f"{Colors.CYAN}{p['Problem']}{Colors.RESET}\n")
        print(f"{Colors.GRAY}Solution\n────────{Colors.RESET}")
        print(f"{Colors.CYAN}{p['Solution']}{Colors.RESET}\n")
        print(f"{Colors.GRAY}Tech Stack\n────────{Colors.RESET}")
        print(f"{Colors.CYAN}{p['Tech']}{Colors.RESET}\n")
        print(f"{Colors.GRAY}GitHub\n────────{Colors.RESET}")
        print(f"{Colors.CYAN}{p['GitHub']}{Colors.RESET}\n")
        print(f"{Colors.GRAY}────────────────────────────{Colors.RESET}\n")
        print_footer()
    else:
        print_header()
        print(f"{Colors.RED}Project '{name}' not found. Type 'projects' to see the list.{Colors.RESET}\n")
        print_footer()

def cmd_timeline():
    print_header()
    print(f"{Colors.YELLOW}2021{Colors.RESET}")
    print(f"{Colors.CYAN}Started B.Tech at NIT Patna{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.YELLOW}2022{Colors.RESET}")
    print(f"{Colors.CYAN}TESLA Club & Robotics Club Leadership{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.YELLOW}2023{Colors.RESET}")
    print(f"{Colors.CYAN}Industrial Training{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.YELLOW}2024{Colors.RESET}")
    print(f"{Colors.CYAN}Automated Drone Delivery Project{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.YELLOW}2025{Colors.RESET}")
    print(f"{Colors.CYAN}MERN Stack Internship & Graduate Engineer Trainee{Colors.RESET}\n")
    time.sleep(0.15)
    print(f"{Colors.YELLOW}2026{Colors.RESET}")
    print(f"{Colors.CYAN} Building Advanced AI Systems{Colors.RESET}\n")
    print_footer()

def cmd_story():
    print_header()
    steps = [
        ("2021", "Started B.Tech."),
        ("↓", ""),
        ("2022", "Joined TESLA Club & Robotics Club."),
        ("↓", ""),
        ("2023", "Completed my Industrial Training."),
        ("↓", ""),
        ("2024", "Built my first drone."),
        ("↓", ""),
        ("2024", "Hackathons."),
        ("↓", ""),
        ("2025", "Internship."),
        ("↓", ""),
        ("2025", "JSW Steel."),
        ("↓", ""),
        ("2026, Today","Building AI systems."),
        ("↓", ""),
        ("Tomorrow...", "Hopefully with your team.")
    ]
    
    for year, text in steps:
        if year == "↓":
            print_centered("↓", Colors.GRAY)
        else:
            margin = max(0, (get_width() - 40) // 2)
            space = " " * margin
            print(space + f"{Colors.YELLOW}{year}{Colors.RESET}")
            print(space + f"{Colors.CYAN}{text}{Colors.RESET}\n")
        time.sleep(0.4)
    print_footer()

def cmd_whyhireme():
    print_header()
    print(f"{Colors.YELLOW}Why Hire Me?{Colors.RESET}\n")
    
    points = [
        "• I enjoy solving real-world problems.",
        "• I learn quickly and adapt faster.",
        "• I bridge electrical engineering with software.",
        "• I have experience in industrial automation and modern web development.",
        "• I care about writing maintainable software, not just working software.",
        "• I believe the best engineers never stop learning."
    ]
    
    for pt in points:
        print(f"{Colors.CYAN}{pt}{Colors.RESET}")
        time.sleep(0.15)
        
    print(f"\n{Colors.GREEN}Thank you for considering my profile.{Colors.RESET}\n")
    print_footer()

def cmd_resume():
    print_header()
    typing_effect("Opening Resume...", 0.04, Colors.CYAN)
    time.sleep(0.5)
    print(f"{Colors.GREEN}✓ Resume opened.{Colors.RESET}\n")
    webbrowser.open("https://drive.google.com/file/d/1GjL9l9JEL-M5lGT-xCDe4q_7VQ910_N7/view?usp=sharing")
    print_footer()

def cmd_guess():
    print_header()
    print(f"{Colors.CYAN}I'm thinking of a number between 1 and 20.{Colors.RESET}\n")
    target = random.randint(1, 20)
    while True:
        try:
            sys.stdout.write(f"{Colors.YELLOW}Guess: {Colors.RESET}")
            sys.stdout.flush()
            guess = int(input().strip())
            if guess == target:
                print(f"\n{Colors.GREEN}Nice.{Colors.RESET}")
                time.sleep(0.5)
                print(f"{Colors.CYAN}Engineers don't guess.{Colors.RESET}")
                print(f"{Colors.CYAN}They iterate.{Colors.RESET}\n")
                unlock_achievement("Puzzle Solver", "Completed a mini-game.")
                break
            elif guess < target:
                print(f"{Colors.GRAY}Higher.{Colors.RESET}\n")
            else:
                print(f"{Colors.GRAY}Lower.{Colors.RESET}\n")
        except ValueError:
            print(f"{Colors.RED}Invalid input. Enter a number.{Colors.RESET}\n")
    print_footer()

def cmd_memory():
    print_header()
    print(f"{Colors.CYAN}Remember these.{Colors.RESET}\n")
    time.sleep(1)
    nums = [str(random.randint(1, 9)) for _ in range(5)]
    for n in nums:
        print(f"{Colors.YELLOW}{n}{Colors.RESET}")
        time.sleep(0.5)
    print(f"\n{Colors.GRAY}Press Enter.{Colors.RESET}")
    input()
    clear_screen()
    print_header()
    sys.stdout.write(f"{Colors.CYAN}Enter them again (no spaces): {Colors.RESET}")
    sys.stdout.flush()
    ans = input().strip()
    if ans == "".join(nums):
        print(f"\n{Colors.GREEN}Good memory.{Colors.RESET}")
        time.sleep(0.5)
        print(f"{Colors.CYAN}Debugging requires this too.{Colors.RESET}\n")
        unlock_achievement("Puzzle Solver", "Completed a mini-game.")
    else:
        print(f"\n{Colors.RED}Incorrect.{Colors.RESET}")
        print(f"{Colors.GRAY}It was {''.join(nums)}.{Colors.RESET}\n")
    print_footer()

def cmd_matrix():
    clear_screen()
    end_time = time.time() + 5
    width = get_width()
    while time.time() < end_time:
        line = "".join(chr(random.randint(33, 126)) for _ in range(width // 2))
        print(f"{Colors.GREEN}{line}{Colors.RESET}")
        time.sleep(0.05)
    clear_screen()
    print()
    typing_effect("Wake up, Neo.", 0.08, Colors.GREEN)
    time.sleep(1)
    typing_effect("Wrong universe, Server Crashed.", 0.05, Colors.GRAY)
    time.sleep(0.5)
    typing_effect("Returning...", 0.03, Colors.CYAN)
    time.sleep(1)
    clear_screen()
    print_header()
    unlock_achievement("Puzzle Solver", "Completed a mini-game.")
    print_footer()

def cmd_binary():
    print_header()
    print(f"{Colors.CYAN}01001000 01101001{Colors.RESET}\n")
    sys.stdout.write(f"{Colors.YELLOW}Decode: {Colors.RESET}")
    sys.stdout.flush()
    ans = input().strip().lower()
    if ans == "hi":
        print(f"\n{Colors.GREEN}Correct.{Colors.RESET}\n")
        unlock_achievement("Binary Decoder", "Translated binary to text.")
    else:
        print(f"\n{Colors.RED}Incorrect.{Colors.RESET}\n")
    print_footer()

def cmd_rps():
    print_header()
    print(f"{Colors.CYAN}Rock\nPaper\nScissors{Colors.RESET}\n")
    sys.stdout.write(f"{Colors.YELLOW}Choose: {Colors.RESET}")
    sys.stdout.flush()
    user = input().strip().lower()
    choices = ["rock", "paper", "scissors"]
    if user not in choices:
        print(f"\n{Colors.RED}Invalid choice.{Colors.RESET}\n")
        print_footer()
        return
    comp = random.choice(choices)
    print(f"\n{Colors.GRAY}I chose {comp}.{Colors.RESET}")
    if user == comp:
        print(f"{Colors.YELLOW}Tie.{Colors.RESET}\n")
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        print(f"\n{Colors.GREEN}Luck.{Colors.RESET}")
        time.sleep(0.5)
        print(f"{Colors.CYAN}Now let's build software.{Colors.RESET}\n")
        unlock_achievement("Puzzle Solver", "Completed a mini-game.")
    else:
        print(f"\n{Colors.RED}I win.{Colors.RESET}\n")
    print_footer()

def cmd_hire():
    print_header()
    typing_effect("Evaluating Candidate...\n", 0.03, Colors.YELLOW)
    time.sleep(0.5)
    
    traits = [
        ("Projects", "██████████"),
        ("Problem Solving", "██████████"),
        ("Learning", "██████████"),
        ("Communication", "██████████"),
        ("Curiosity", "██████████")
    ]
    
    for t_name, t_bar in traits:
        sys.stdout.write(f"{Colors.GRAY}{t_name.ljust(18)}{Colors.RESET}")
        sys.stdout.flush()
        time.sleep(0.15)
        print(f"{Colors.GREEN}{t_bar}{Colors.RESET}")
        time.sleep(0.2)
        
    print(f"\n{Colors.GRAY}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.RESET}\n")
    time.sleep(0.5)
    
    print(f"{Colors.CYAN}Recommendation{Colors.RESET}")
    time.sleep(0.5)
    print(f"{Colors.YELLOW}★★★★★{Colors.RESET}")
    time.sleep(0.5)
    print(f"{Colors.GREEN}{Colors.BOLD}Strong Hire{Colors.RESET}\n")
    time.sleep(0.5)
    
    print(f"{Colors.CYAN}Reason{Colors.RESET}")
    print(f"{Colors.GRAY}This engineer enjoys solving\nreal problems,\ncontinues learning,\nand loves building.{Colors.RESET}\n")
    time.sleep(0.5)
    
    print(f"{Colors.GRAY}(Generated locally 😄){Colors.RESET}\n")
    unlock_achievement("The One Who Hired Me", "Used the hire command.")
    print_footer()

def cmd_inspire():
    quotes = [
        '"First, solve the problem. Then, write the code."\n— John Johnson\n',
        '"Programs must be written for people to read."\n— Harold Abelson\n',
        '"Simplicity is the soul of efficiency."\n— Austin Freeman\n',
        '"Talk is cheap. Show me the code."\n— Linus Torvalds\n'
    ]
    print_header()
    typing_effect(random.choice(quotes), 0.04, Colors.CYAN)
    print_footer()

def exit_animation():
    clear_screen()
    print_separator("═", Colors.CYAN)
    print()
    msg = (
        "It was great meeting you.\n\n"
        "Thank you for taking the time to explore my work.\n\n"
        "Whether or not we work together,\n"
        "I hope you enjoyed this little engineering experiment.\n\n"
        "Let's build something meaningful.\n\n"
        "I would love to hear your feedback via mail.\n\n"
        "— Anurag Kumar Bharti\n"
    )
    print_centered(msg, Colors.GREEN)
    
    print_centered("Portfolio", Colors.GRAY)
    print_centered("https://ace-akb.vercel.app", Colors.CYAN)
    print()
    print_centered("GitHub", Colors.GRAY)
    print_centered("https://github.com/i-akb25", Colors.CYAN)
    print()
    print_centered("LinkedIn", Colors.GRAY)
    print_centered("https://linkedin.com/in/anuragkumarbharti", Colors.CYAN)
    print()
    print_centered("Email", Colors.GRAY)
    print_centered("anuragbhartiee25@gmail.com", Colors.CYAN)
    print()
    print_separator("═", Colors.CYAN)
    typing_effect("\nGoodbye 👋\n", 0.04, Colors.GREEN)
    sys.exit(0)

def cmd_exit_prompt():
    clear_screen()
    print_header()
    print(f"{Colors.YELLOW}Before you leave...{Colors.RESET}\n")
    visited_list = [s for s in core_sections if s in visited_sections]
    unvisited_list = [s for s in core_sections if s not in visited_sections]
    
    print(f"{Colors.CYAN}You explored:{Colors.RESET}")
    if visited_list:
        for v in visited_list:
            print(f"{Colors.GREEN}✔ {v.capitalize()}{Colors.RESET}")
    else:
        print(f"{Colors.GRAY}Nothing yet.{Colors.RESET}")
        
    print(f"\n{Colors.CYAN}Still waiting:{Colors.RESET}")
    if unvisited_list:
        for u in unvisited_list:
            print(f"{Colors.GRAY}• {u.capitalize()}{Colors.RESET}")
    else:
        print(f"{Colors.GREEN}Everything! Thank you.{Colors.RESET}")
        
    print(f"\n{Colors.GRAY}Type one of them or press ENTER to exit.{Colors.RESET}")
    sys.stdout.write(f"\n{Colors.GREEN}{Colors.BOLD}akb-cli > {Cursor.BLOCK}{Colors.RESET}")
    sys.stdout.flush()
    choice = input().strip().lower()
    sys.stdout.write(Cursor.RESET)
    
    if choice == "":
        exit_animation()
    else:
        return choice

def command_router(cmd):
    cmd_lower = cmd.lower().strip()
    if not cmd_lower:
        return True
    history.append(cmd_lower)
    if cmd_lower in core_sections:
        visited_sections.add(cmd_lower)
        
    if cmd_lower == "about": cmd_about()
    elif cmd_lower == "education": cmd_education()
    elif cmd_lower == "experience": cmd_experience()
    elif cmd_lower == "skills": cmd_skills()
    elif cmd_lower == "projects": cmd_projects_list()
    elif cmd_lower.startswith("project "):
        parts = cmd_lower.split(" ", 1)
        if len(parts) > 1:
            cmd_project_detail(parts[1])
            visited_sections.add("projects")
    elif cmd_lower == "philosophy": cmd_philosophy()
    elif cmd_lower == "goals": cmd_goals()
    elif cmd_lower == "timeline": cmd_timeline()
    elif cmd_lower == "contact": cmd_contact()
    elif cmd_lower == "portfolio": cmd_portfolio()
    elif cmd_lower == "story": cmd_story()
    elif cmd_lower == "whyhireme": cmd_whyhireme()
    elif cmd_lower == "help":
        clear_screen()
        show_menu()
    elif cmd_lower == "more":
        clear_screen()
        cmd_more()
    elif cmd_lower == "clear":
        clear_screen()
        print_header()
    elif cmd_lower == "exit":
        next_cmd = cmd_exit_prompt()
        if next_cmd:
            return command_router(next_cmd)
        return False
    elif cmd_lower == "resume": cmd_resume()
    elif cmd_lower == "version":
        print_header()
        print(f"{Colors.CYAN}AKB CLI{Colors.RESET}")
        print(f"{Colors.GRAY}Version v1.0.0{Colors.RESET}")
        print(f"{Colors.GRAY}Released July 2026{Colors.RESET}\n")
        print_footer()
    elif cmd_lower == "history":
        print_header()
        for i, c in enumerate(history, 1):
            print(f"{Colors.GRAY}{i}. {Colors.CYAN}{c}{Colors.RESET}")
        print()
        print_footer()
    elif cmd_lower == "date":
        print_header()
        print(f"{Colors.CYAN}{datetime.now().strftime('%B %d, %Y')}{Colors.RESET}\n")
        print_footer()
    elif cmd_lower == "time":
        print_header()
        print(f"{Colors.CYAN}{datetime.now().strftime('%H:%M:%S')}{Colors.RESET}\n")
        print_footer()
    elif cmd_lower == "motd": cmd_inspire()
    elif cmd_lower == "guess": cmd_guess()
    elif cmd_lower == "memory": cmd_memory()
    elif cmd_lower == "matrix": cmd_matrix()
    elif cmd_lower == "binary": cmd_binary()
    elif cmd_lower == "rps": cmd_rps()
    elif cmd_lower == "whoami":
        print_header()
        typing_effect("You are an engineer\nlooking for another engineer.\n\nNice to meet you 🙂\n", 0.04, Colors.CYAN)
        unlock_achievement("Curious Engineer", "Found a hidden command.")
        print_footer()
    elif cmd_lower == "hello":
        print_header()
        typing_effect("Hello 👋\n\nHope you're having a wonderful day.\n", 0.04, Colors.CYAN)
        unlock_achievement("Polite User", "Said hello.")
        print_footer()
    elif cmd_lower == "thankyou":
        print_header()
        typing_effect("You're welcome 🙂\n\nThank you for taking the time\nto know me beyond my resume.\n", 0.04, Colors.CYAN)
        unlock_achievement("Polite User", "Said thank you.")
        print_footer()
    elif cmd_lower == "coffee":
        print_header()
        print(f"{Colors.YELLOW}☕{Colors.RESET}")
        typing_effect("Compiling ideas...", 0.15, Colors.CYAN)
        typing_effect("Please wait...\n", 0.15, Colors.CYAN)
        unlock_achievement("Coffee Powered", "Found the coffee command.")
        print_footer()
    elif cmd_lower == "42":
        print_header()
        typing_effect("The answer is still 42.\n\nThe question is what problem are we solving today?\n", 0.04, Colors.CYAN)
        unlock_achievement("Hitchhiker", "Found the meaning of life, the universe, and everything.")
        print_footer()
    elif cmd_lower == "inspire": cmd_inspire()
    elif cmd_lower == "akb":
        print_header()
        print(f"{Colors.YELLOW}AKB{Colors.RESET}\n")
        typing_effect("Always Keep Building.\n", 0.04, Colors.CYAN)
        typing_effect("Because software is never finished.", 0.04, Colors.GRAY)
        typing_effect("It simply gets better.\n", 0.04, Colors.GRAY)
        unlock_achievement("Curious Engineer", "Found a hidden command.")
        print_footer()
    elif cmd_lower == "easteregg":
        print_header()
        print(f"{Colors.MAGENTA}🎉{Colors.RESET}\n")
        typing_effect("Congratulations!\n\nYou found the hidden command.\n", 0.04, Colors.CYAN)
        typing_effect("Curiosity is one of the best qualities\nan engineer can have.\n", 0.04, Colors.CYAN)
        typing_effect("You clearly have it.\n", 0.04, Colors.GREEN)
        unlock_achievement("Explorer", "Found the explicit easter egg.")
        print_footer()
    elif cmd_lower == "sudo hire anurag":
        print_header()
        print(f"{Colors.GREEN}Permission Granted.{Colors.RESET}\n")
        typing_effect("Offer Letter Generated.\n", 0.04, Colors.CYAN)
        print(f"{Colors.GRAY}Starting Date:{Colors.RESET}")
        print(f"{Colors.CYAN}Immediately.{Colors.RESET}\n")
        print(f"{Colors.GRAY}Salary:{Colors.RESET}")
        print(f"{Colors.CYAN}Let's discuss. 😄{Colors.RESET}\n")
        unlock_achievement("The One Who Hired Me", "Promoted to sudo.")
        print_footer()
    elif cmd_lower == "hire": cmd_hire()
    else:
        play_sound("error")
        print(f"\n{Colors.RED}Ooops! The page took a wrong turn at next door. Command not found: '{cmd}'{Colors.RESET}")
        print(f"{Colors.YELLOW}Type 'help' to head back home.{Colors.RESET}\n")
    return True

def command_loop():
    while True:
        try:
            sys.stdout.write(f"{Colors.GREEN}{Colors.BOLD}akb-cli > {Cursor.BLOCK}{Colors.RESET}")
            sys.stdout.flush()
            cmd = input()
            sys.stdout.write(Cursor.RESET)
            keep_running = command_router(cmd)
            if not keep_running:
                break
        except (KeyboardInterrupt, EOFError):
            print("\n")
            exit_animation()
        except Exception:
            print(f"\n{Colors.RED}An unexpected error occurred. Recovering...{Colors.RESET}\n")

def main():
    try:
        fake_terminal_startup() 
        continue_prompt()
        
        welcome_message()
        continue_prompt()
        
        cmd_about(is_tour=True)
        continue_prompt()
        
        cmd_skills(is_tour=True)
        continue_prompt()
        
        cmd_philosophy(is_tour=True)
        continue_prompt()
        
        cmd_goals(is_tour=True)
        continue_prompt()
        
        cmd_contact(is_tour=True)
        continue_prompt()
        
        cmd_portfolio(is_tour=True)
        
        clear_screen()
        print_separator("═", Colors.CYAN)
        print()
        msg = (
            "Interactive Profile Loaded.\n\n"
            "Everything you need to know about me\n"
            "is available through commands.\n\n"
            "Type \"help\" to begin exploring.\n"
            "Type \"more\" to have fun.\n"
        )
        typing_effect(msg, 0.03, Colors.CYAN)
        
        command_loop()
        
    except (KeyboardInterrupt, EOFError):
        print("\n")
        exit_animation()
    except Exception:
        print(f"\n{Colors.RED}An unexpected error occurred. Recovering...{Colors.RESET}\n")

if __name__ == "__main__":
    main()