import os

def generate_index_html(directory):
    # Start building the HTML content
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Files Index</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
        a {
            text-decoration: none;
            color: #007BFF;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>Markdown Files</h1>
    <ul>
"""

    # Walk through the directory and its subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                # Get the relative path of the file
                relative_path = os.path.relpath(os.path.join(root, file), directory)
                html_content += f'        <li><a href="{relative_path}">{relative_path}</a></li>\n'

    # Close the HTML tags
    html_content += """    </ul>
</body>
</html>
"""

    # Write the HTML content to an index.html file
    output_file = os.path.join(directory, "index.html")
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)

    print(f"index.html has been generated in {directory}")

# Specify the directory containing the .md files
directory = "C:/Users/meetm/OneDrive/Documents/Obsidian Vault"  # Change this to your desired directory
generate_index_html(directory)