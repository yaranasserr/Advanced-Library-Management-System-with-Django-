import os
import subprocess

# Path to your Django project
project_path = "/home/yara/Desktop/yara/bit68/LibrarySystem/librarysystem/"

# Settings path in your Django project
settings_path = os.path.join(project_path, 'librarysystem', 'settings.py')

# The language you want to add
language_code = "ar"
language_name = "Arabic"

# Step 2: Create translation files using `makemessages`
def create_translation_files():
    print(f"Creating translation files for {language_name}...")
    
    os.chdir(project_path)  # Change directory to the project root
    
    # Run makemessages to create the translation file
    subprocess.run(["python3", "manage.py", "makemessages", "-l", language_code])

    print(f"Translation files for {language_name} created.")

# Step 3: Compile translations using `compilemessages`
def compile_translations():
    print(f"Compiling translations for {language_name}...")
    
    os.chdir(project_path)  # Change directory to the project root
    
    # Run compilemessages to compile the translations
    subprocess.run(["python3", "manage.py", "compilemessages"])

    print(f"Translations for {language_name} compiled.")

# Step 4: Optional RTL handling (for Arabic)
def adjust_rtl_support():
    print(f"Adjusting RTL support for {language_name}...")

    # Find all HTML files in the templates directories of all apps
    html_files = []
    for root, dirs, files in os.walk(project_path):
        if 'templates' in dirs:
            template_dir = os.path.join(root, 'templates')
            for file in os.listdir(template_dir):
                if file.endswith(".html"):
                    html_files.append(os.path.join(template_dir, file))

    # Modify each HTML file to include `dir="rtl"`
    for html_file_path in html_files:
        print(f"Adjusting {html_file_path} for RTL...")
        with open(html_file_path, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            if '<html' in line:
                if 'dir="rtl"' not in line:
                    lines[i] = line.replace('<html', '<html dir="rtl"')
                    break

        with open(html_file_path, 'w') as file:
            file.writelines(lines)

    print(f"RTL support for {language_name} adjusted for all HTML files.")

# Main execution
if __name__ == "__main__":

    # Step 2: Create translation files
    create_translation_files()

    # Step 3: Compile translations
    compile_translations()

    # Step 4: Optional RTL adjustments for Arabic
    if language_code == "ar":
        adjust_rtl_support()

    print("Language automation script completed.")
