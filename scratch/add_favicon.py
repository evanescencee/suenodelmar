import glob
import os

files = glob.glob('**/*.html', recursive=True)
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if '<link rel="icon"' not in content:
        # Determine correct path to assets based on whether file is in root or pages/
        # Use os.path.normpath to get consistent path separators
        norm_f = os.path.normpath(f)
        if os.sep in norm_f:
            prefix = '../'
        else:
            prefix = ''
        
        icon_tag = f'<link rel="icon" href="{prefix}assets/images/logo.avif" type="image/avif" />'
        content = content.replace('</title>', f'</title>\n    {icon_tag}')
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Added favicon to {f}")
