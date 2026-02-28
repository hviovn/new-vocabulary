import os
import re
from datetime import datetime
from collections import defaultdict

def update_readme():
    images_dir = 'images'
    readme_path = 'README.md'

    # Regex to match weekly_YYYY.MM.DD.jpg
    pattern = re.compile(r'weekly_(\d{4})\.(\d{2})\.(\d{2})\.jpg')

    # Group images by (year, month)
    monthly_images = defaultdict(list)

    if not os.path.exists(images_dir):
        print(f"Directory {images_dir} not found.")
        return

    for filename in os.listdir(images_dir):
        match = pattern.match(filename)
        if match:
            year, month, day = match.groups()
            monthly_images[(int(year), int(month))].append(filename)

    # Sort years and months in descending order
    sorted_months = sorted(monthly_images.keys(), reverse=True)

    # Header of README
    readme_content = [
        "# New Vietnamese Vocabulary\n\n",
        "![GitHub License](https://img.shields.io/github/license/hviovn/new-vocabulary)\n",
        "![GitHub Release](https://img.shields.io/github/v/release/hviovn/new-vocabulary)\n\n",
        "Learn new Vietnamese Vocabulary from the Watchtower each week.\n"
    ]

    for year, month in sorted_months:
        month_name = datetime(year, month, 1).strftime('%B')
        readme_content.append(f"\n### {month_name} {year}\n\n")

        # Sort images in the month by date (ascending)
        images = sorted(monthly_images[(year, month)])

        # Take up to 5 images
        images = images[:5]

        # Create HTML for clickable images next to each other
        img_html = " ".join([f'<a href="images/{img}"><img src="images/{img}" width="49%"></a>' for img in images])
        readme_content.append(img_html + "\n")

    with open(readme_path, 'w') as f:
        f.writelines(readme_content)

    print("README.md updated successfully.")

if __name__ == "__main__":
    update_readme()
