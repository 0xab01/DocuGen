import tkinter as tk
from tkinter import filedialog
import os

def open_existing_file():
    # Open file dialog to select an existing .md file
    file_path = filedialog.askopenfilename(
        filetypes=[("Markdown Files", "*.md")]
    )

    if file_path:
        # Read the content of the selected file
        with open(file_path, "r") as file:
            content = file.read()

        # Extract information from the existing README file
        extract_information(content)


def extract_information(content):
    # Clear existing input fields
    clear_fields()

    # Extract title, description, installation, license, contribution, and usage sections from the content
    sections = {
        "Title": title_entry,
        "Description": description_text,
        "Installation": installation_text,
        "License": license_text,
        "Contribution": contribution_text,
        "Usage": usage_text
    }

    current_section = None

    # Split the content into lines and process each line
    for line in content.splitlines():
        line = line.strip()

        # Check if it's a section header
        if line.startswith("##"):
            current_section = line[2:].strip()
            continue

        # Check if it's a known section
        if current_section in sections:
            text_widget = sections[current_section]
            text_widget.insert(tk.END, line + "\n")


def clear_fields():
    title_entry.delete(0, tk.END)
    description_text.delete("1.0", tk.END)
    installation_text.delete("1.0", tk.END)
    license_text.delete("1.0", tk.END)
    contribution_text.delete("1.0", tk.END)
    usage_text.delete("1.0", tk.END)


def generate_readme():
    # Get user input from the GUI
    title = title_entry.get()
    description = description_text.get("1.0", tk.END)
    installation = installation_text.get("1.0", tk.END)
    license = license_text.get("1.0", tk.END)
    contribution = contribution_text.get("1.0", tk.END)
    usage = usage_text.get("1.0", tk.END)
    image_path = image_label.cget("text")  # Get the path of the uploaded image

    # Create the README content
    readme_content = f"# {title}\n\n"
    readme_content += f"## Description\n\n{description}\n\n"
    readme_content += "## Installation\n\n"
    readme_content += f"```\n{installation}\n```\n\n"
    readme_content += "## License\n\n"
    readme_content += f"```\n{license}\n```\n\n"
    readme_content += "## Contribution\n\n"
    readme_content += f"```\n{contribution}\n```\n\n"
    readme_content += "## Usage\n\n"
    readme_content += f"```\n{usage}\n```\n"

    # Embed the image in the README if provided
    if image_path:
        readme_content += f"![Project Image]({image_path})\n\n"

    # Open file dialog to save the README.md file
    save_file_path = filedialog.asksaveasfilename(
        defaultextension=".md",
        filetypes=[("Markdown Files", "*.md"), ("All Files", "*.*")],
    )

    # Save the README.md file
    with open(save_file_path, "w") as file:
        file.write(readme_content)


def upload_image():
    # Open file dialog to select an image file
    image_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif")]
    )

    # Display the selected image path in the GUI
    image_label.config(text=image_path)


# Create the main window
window = tk.Tk()
window.title("README Generator")

# Set colors
bg_color = "#F0F0F0"
fg_color = "#333333"
highlight_color = "#66CCFF"

# Set window background color
window.configure(bg=bg_color)

# Create title label and entry
title_label = tk.Label(window, text="Title:", bg=bg_color, fg=fg_color)
title_label.pack()
title_entry = tk.Entry(window)
title_entry.pack()

# Create description label and text box
description_label = tk.Label(window, text="Description:", bg=bg_color, fg=fg_color)
description_label.pack()
description_text = tk.Text(window, height=4)
description_text.pack()

# Create installation label and text box
installation_label = tk.Label(window, text="Installation:", bg=bg_color, fg=fg_color)
installation_label.pack()
installation_text = tk.Text(window, height=6)
installation_text.pack()

# Create license label and text box
license_label = tk.Label(window, text="License:", bg=bg_color, fg=fg_color)
license_label.pack()
license_text = tk.Text(window, height=4)
license_text.pack()

# Create contribution label and text box
contribution_label = tk.Label(window, text="Contribution:", bg=bg_color, fg=fg_color)
contribution_label.pack()
contribution_text = tk.Text(window, height=4)
contribution_text.pack()

# Create usage label and text box
usage_label = tk.Label(window, text="Usage:", bg=bg_color, fg=fg_color)
usage_label.pack()
usage_text = tk.Text(window, height=6)
usage_text.pack()

# Create image upload button
image_button = tk.Button(window, text="Upload Image", command=upload_image, bg=highlight_color, fg=fg_color)
image_button.pack()

# Create image label to display the selected image path
image_label = tk.Label(window, text="", bg=bg_color, fg=fg_color)
image_label.pack()

# Create open existing file button
open_file_button = tk.Button(window, text="Open Existing File", command=open_existing_file, bg=highlight_color, fg=fg_color)
open_file_button.pack()

# Create generate button
generate_button = tk.Button(window, text="Generate README", command=generate_readme, bg=highlight_color, fg=fg_color)
generate_button.pack()

# Start the GUI event loop
window.mainloop()
