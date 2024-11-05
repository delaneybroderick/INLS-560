# Import the required modules
import os  # allows us to create directories, work with file paths
import re  # provides regular expression functionality for pattern matching

# slugify the function 
def slugify(title):
    """Convert the page title to a filename-friendly slug."""
    # if statement
    if title.lower() == "home":  # Ensure 'Home' becomes 'index.html'
        return "index.html"
    # regular expression (re.sub) is used here to convert spaces and symbols in the title to dashes
    return re.sub(r'\W+', '-', title.strip().lower()) + ".html"

# Generate navigation function 
def generate_nav(titles, active_title):
    """Generate a dynamic navigation bar with an active page highlight."""
    nav_links = ""
    # for loop iterates through each title to create navigation links
    for title in titles:
        filename = slugify(title)
        # f-string to format strings with the filename and active class if applicable
        active_class = ' class="active"' if title == active_title else ""
        nav_links += f'\t\t\t<a href="{filename}"{active_class}>{title}</a>\n'
    return nav_links.strip()

# Create html function 
def create_html_file(title, titles, output_dir="build"):
    """Generate and write HTML content based on the page title."""
    filename = slugify(title)
    nav = generate_nav(titles, active_title=title)

    # f-string used to dynamically insert title and navigation into HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <nav>
            {nav}
        </nav>
        <div class="content">
            <h1>{title}</h1>
            <p>This is the {title.lower()} content.</p>
        </div>
    </body>
    </html>
    """

    # os.makedirs() ensures the output directory is created if it doesn't exist
    output_path = os.path.join(output_dir, filename)
    os.makedirs(output_dir, exist_ok=True)  # directory creation

    # with open() as file to open the file in write mode
    with open(output_path, 'w') as file:
        # file.write writes the HTML content to the file
        file.write(html_content)

    print(f"Created {filename} in the '{output_dir}' directory.")

# Create main function 
def main():
    """Main function to generate pages and styles. MUST HAVE HOME!!!"""
    # dictionary: titles is a list here but could be replaced by a dictionary for more complex data
    titles = ["Home", "About Me", "My Videos", "My Favorite Photos"]

    # for loop to create HTML files for each title in the titles list
    for title in titles:
        create_html_file(title, titles)

    # pass statement could be used here as a placeholder if we had unfinished code
    # create_css_file()  # uncomment if you add the function for creating a CSS file.

if __name__ == "__main__":
    main()
