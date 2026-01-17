#!/usr/bin/env python3
"""Claude Config Helper Skill Installer

Installs the claude-config-helper skill to a target Claude Code project.

Usage:
    python install_skill.py                         Interactive mode
    python install_skill.py "C:\path\to\project"   Install to project
    python install_skill.py "C:\path\to\project" --update  Update existing
    python install_skill.py --help                  Show help
"""

import argparse
import os
import shutil
import sys
from pathlib import Path


# ============================================================================
# ASCII Art and UI Components
# ============================================================================

ASCII_BANNER = r"""
   _____ _                 _        _____              __ _
  / ____| |               | |      / ____|            / _(_)
 | |    | | __ _ _   _  __| | ___ | |     ___  _ __ | |_ _  __ _
 | |    | |/ _` | | | |/ _` |/ _ \| |    / _ \| '_ \|  _| |/ _` |
 | |____| | (_| | |_| | (_| |  __/| |___| (_) | | | | | | | (_| |
  \_____|_|\__,_|\__,_|\__,_|\___| \_____\___/|_| |_|_| |_|\__, |
                                                            __/ |
  _    _      _                    _____  _    _ _ _       |___/
 | |  | |    | |                  / ____|| |  (_) | |
 | |__| | ___| |_ __   ___ _ __  | (___  | | ___| | |
 |  __  |/ _ \ | '_ \ / _ \ '__|  \___ \ | |/ / | | |
 | |  | |  __/ | |_) |  __/ |     ____) ||   <| | | |
 |_|  |_|\___|_| .__/ \___|_|    |_____/ |_|\_\_|_|_|
               | |
               |_|              Skill Installer v1.0
"""

MENU_BOX = """
+==============================================================+
|                      MAIN MENU                               |
+==============================================================+
|                                                              |
|   [1]  Install Skill      - Install to a new project        |
|   [2]  Update Skill       - Update existing installation    |
|   [3]  Show Help          - Display usage information       |
|   [4]  Exit               - Close the installer             |
|                                                              |
+==============================================================+
"""

HELP_TEXT = """
+==============================================================+
|                         HELP                                 |
+==============================================================+

  This tool installs the claude-config-helper skill to your
  Claude Code projects.

  WHAT IT DOES:
  - Copies skill files to target project's .claude/skills/
  - Creates .claude directory if needed (with confirmation)
  - Supports updating existing installations

  COMMAND LINE USAGE:
  install-skill.bat "C:\path\to\project"          # Install
  install-skill.bat "C:\path\to\project" --update # Update
  install-skill.bat --help                        # Help

  INTERACTIVE MODE:
  Double-click install-skill.bat to launch this menu.

+==============================================================+
"""

SUCCESS_BOX = r"""
   _____                              _
  / ____|                            | |
 | (___  _   _  ___ ___ ___  ___ ___| |
  \___ \| | | |/ __/ __/ _ \/ __/ __| |
  ____) | |_| | (_| (_|  __/\__ \__ \_|
 |_____/ \__,_|\___\___\___||___/___(_)
"""

ERROR_BOX = r"""
  ______                     _
 |  ____|                   | |
 | |__   _ __ _ __ ___  _ __| |
 |  __| | '__| '__/ _ \| '__| |
 | |____| |  | | | (_) | |  |_|
 |______|_|  |_|  \___/|_|  (_)
"""


def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_colored(text: str, color: str = None):
    """Print text (color codes for future enhancement)."""
    print(text)


def press_enter_to_continue():
    """Wait for user to press Enter."""
    input("\n  Press Enter to continue...")


def draw_progress_bar(current: int, total: int, width: int = 40):
    """Draw a simple progress bar."""
    filled = int(width * current / total)
    bar = '█' * filled + '░' * (width - filled)
    percent = current / total * 100
    print(f"\r  [{bar}] {percent:.0f}%", end='', flush=True)


# ============================================================================
# Core Functions
# ============================================================================

def get_script_dir() -> Path:
    """Get the directory where this script is located."""
    return Path(__file__).parent.resolve()


def get_source_skill_dir() -> Path:
    """Get the source skill directory path."""
    return get_script_dir() / ".claude" / "skills" / "claude-config-helper"


def validate_source_skill(source_dir: Path) -> bool:
    """Validate that the source skill directory exists and contains required files."""
    if not source_dir.exists():
        print(f"  [ERROR] Source skill directory not found:")
        print(f"          {source_dir}")
        return False

    skill_md = source_dir / "Skill.md"
    if not skill_md.exists():
        print(f"  [ERROR] Skill.md not found in source directory")
        return False

    return True


def validate_target_dir(target_dir: Path) -> bool:
    """Validate that the target directory exists."""
    if not target_dir.exists():
        print(f"  [ERROR] Target directory does not exist:")
        print(f"          {target_dir}")
        return False

    if not target_dir.is_dir():
        print(f"  [ERROR] Target path is not a directory")
        return False

    return True


def prompt_yes_no(message: str) -> bool:
    """Prompt user for yes/no confirmation."""
    while True:
        response = input(f"  {message} (y/n): ").strip().lower()
        if response in ('y', 'yes'):
            return True
        elif response in ('n', 'no'):
            return False
        else:
            print("  Please enter 'y' or 'n'.")


def ensure_claude_dir(target_dir: Path) -> Path | None:
    """Ensure .claude directory exists, prompting user if it needs to be created."""
    claude_dir = target_dir / ".claude"

    if not claude_dir.exists():
        print(f"  [INFO] Target does not have a .claude directory.")
        if prompt_yes_no("Create it?"):
            try:
                claude_dir.mkdir(parents=True)
                print(f"  [OK] Created: {claude_dir}")
            except PermissionError:
                print(f"  [ERROR] Permission denied")
                return None
            except OSError as e:
                print(f"  [ERROR] Failed to create directory: {e}")
                return None
        else:
            print("  [CANCELLED] Operation cancelled.")
            return None

    return claude_dir


def ensure_skills_dir(claude_dir: Path) -> Path | None:
    """Ensure skills directory exists within .claude."""
    skills_dir = claude_dir / "skills"

    if not skills_dir.exists():
        try:
            skills_dir.mkdir(parents=True)
            print(f"  [OK] Created: {skills_dir}")
        except PermissionError:
            print(f"  [ERROR] Permission denied")
            return None
        except OSError as e:
            print(f"  [ERROR] Failed to create directory: {e}")
            return None

    return skills_dir


def count_files(directory: Path) -> int:
    """Count total files in directory recursively."""
    return sum(1 for _ in directory.rglob('*') if _.is_file())


def install_skill(source_dir: Path, target_skill_dir: Path, update: bool = False) -> bool:
    """Install the skill to the target directory."""

    if target_skill_dir.exists():
        if not update:
            print(f"  [WARNING] Skill already exists at:")
            print(f"            {target_skill_dir}")
            print("  Use 'Update Skill' option to overwrite.")
            return False
        else:
            print(f"  [INFO] Removing existing skill...")
            try:
                shutil.rmtree(target_skill_dir)
            except PermissionError:
                print(f"  [ERROR] Permission denied")
                return False
            except OSError as e:
                print(f"  [ERROR] Failed to remove directory: {e}")
                return False

    print(f"\n  [INFO] Installing skill...")
    print(f"  From: {source_dir}")
    print(f"  To:   {target_skill_dir}\n")

    try:
        # Count files for progress bar
        total_files = count_files(source_dir)
        copied = 0

        # Create target directory
        target_skill_dir.mkdir(parents=True, exist_ok=True)

        # Copy files with progress
        for src_file in source_dir.rglob('*'):
            relative_path = src_file.relative_to(source_dir)
            dest_file = target_skill_dir / relative_path

            if src_file.is_dir():
                dest_file.mkdir(parents=True, exist_ok=True)
            else:
                dest_file.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src_file, dest_file)
                copied += 1
                draw_progress_bar(copied, total_files)

        print()  # New line after progress bar
        return True

    except PermissionError:
        print(f"\n  [ERROR] Permission denied copying files.")
        return False
    except OSError as e:
        print(f"\n  [ERROR] Failed to copy files: {e}")
        return False


def do_install(update: bool = False):
    """Execute installation process."""
    clear_screen()
    action = "UPDATE" if update else "INSTALL"
    print(f"\n  +{'='*56}+")
    print(f"  |{action:^56}|")
    print(f"  +{'='*56}+\n")

    # Get source directory
    source_dir = get_source_skill_dir()

    # Validate source
    if not validate_source_skill(source_dir):
        print(ERROR_BOX)
        press_enter_to_continue()
        return

    # Get target path from user
    print("  Enter the path to your project:")
    print("  (You can drag and drop a folder here)\n")
    target_path = input("  Path: ").strip().strip('"').strip("'")

    if not target_path:
        print("\n  [CANCELLED] No path provided.")
        press_enter_to_continue()
        return

    target_dir = Path(target_path).resolve()

    # Validate target
    if not validate_target_dir(target_dir):
        print(ERROR_BOX)
        press_enter_to_continue()
        return

    print()

    # Ensure .claude directory
    claude_dir = ensure_claude_dir(target_dir)
    if claude_dir is None:
        press_enter_to_continue()
        return

    # Ensure skills directory
    skills_dir = ensure_skills_dir(claude_dir)
    if skills_dir is None:
        press_enter_to_continue()
        return

    # Install
    target_skill_dir = skills_dir / "claude-config-helper"
    if install_skill(source_dir, target_skill_dir, update=update):
        print(SUCCESS_BOX)
        print(f"  Skill installed to:")
        print(f"  {target_skill_dir}")
    else:
        print(ERROR_BOX)

    press_enter_to_continue()


def show_help():
    """Display help information."""
    clear_screen()
    print(HELP_TEXT)
    press_enter_to_continue()


def interactive_mode():
    """Run the interactive menu interface."""
    while True:
        clear_screen()
        print(ASCII_BANNER)
        print(MENU_BOX)

        choice = input("  Enter your choice [1-4]: ").strip()

        if choice == '1':
            do_install(update=False)
        elif choice == '2':
            do_install(update=True)
        elif choice == '3':
            show_help()
        elif choice == '4':
            clear_screen()
            print("\n  Thank you for using Claude Config Helper Skill Installer!")
            print("  Goodbye!\n")
            sys.exit(0)
        else:
            print("\n  Invalid choice. Please enter 1, 2, 3, or 4.")
            press_enter_to_continue()


def cli_mode():
    """Run in command-line argument mode."""
    parser = argparse.ArgumentParser(
        description="Install claude-config-helper skill to a Claude Code project.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  install_skill.py                                 Interactive mode
  install_skill.py "C:\\path\\to\\project"         Install to project
  install_skill.py "C:\\path\\to\\project" --update Update existing skill
"""
    )

    parser.add_argument(
        "target_dir",
        type=str,
        nargs='?',
        default=None,
        help="Path to the target project directory"
    )

    parser.add_argument(
        "--update",
        action="store_true",
        help="Force update/overwrite existing skill"
    )

    args = parser.parse_args()

    # If no target_dir provided, launch interactive mode
    if args.target_dir is None:
        interactive_mode()
        return

    # CLI mode
    source_dir = get_source_skill_dir()
    target_dir = Path(args.target_dir).resolve()

    print("="*60)
    print("Claude Config Helper Skill Installer")
    print("="*60)
    print()

    if not validate_source_skill(source_dir):
        sys.exit(1)

    if not validate_target_dir(target_dir):
        sys.exit(1)

    claude_dir = ensure_claude_dir(target_dir)
    if claude_dir is None:
        sys.exit(1)

    skills_dir = ensure_skills_dir(claude_dir)
    if skills_dir is None:
        sys.exit(1)

    target_skill_dir = skills_dir / "claude-config-helper"
    if not install_skill(source_dir, target_skill_dir, update=args.update):
        sys.exit(1)

    print()
    print("="*60)
    print("Installation complete!")
    print(f"Skill installed to: {target_skill_dir}")
    print("="*60)


def main():
    """Main entry point."""
    cli_mode()


if __name__ == "__main__":
    main()
