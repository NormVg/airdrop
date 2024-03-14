import subprocess

def copy_file_to_clipboard(file_path):
    try:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            subprocess.run(['xclip', '-selection', 'clipboard'], input=file_content, check=True)
            print("File content copied to clipboard successfully!")
    except FileNotFoundError:
        print("File not found!")

# Example usage:
file_path = "image.png"
copy_file_to_clipboard(file_path)
