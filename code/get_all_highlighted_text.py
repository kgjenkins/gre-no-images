# Packages that contain useful code for us to use
import os # Lets us do file operations
import re # Regular Expressions!
from termcolor import colored # Let's us display the output in color

# The RegEx string we're going to use to extract the desired text
reHighlightedText = r'<span\s+style=\"color\:\s*(\w+);*\">\s*([^<]*?)\s*</span>'

# Print a bunch of blank lines to separate each run's output
print('\n'*100)

# Define the directory to start from
sBaseDir = '../content/province'
# sBaseDir = 'test_data

# This list will hold all of the highlighted text we find
vHighlights = []

# Navigate the directory tree start at a predefined root directory
for sRoot, vDirs, vFiles in os.walk(sBaseDir):
    
    # Loop through all the files in the current directory
    for sFilename in vFiles:
        _, sExt = os.path.splitext(sFilename)   # Get file extension (looking for .md)
        
        # Work with only .md files, but not with any _index.md files
        # This leaves only the entries proper
        if sExt == '.md' and not sFilename == '_index.md':
            
            with open(os.path.join(sRoot,sFilename),'r') as f:
                sFile = f.read()
            
            for tMatch in re.findall(reHighlightedText, sFile):
                if not tMatch in vHighlights:
                    vHighlights.append(tMatch)

# Now that we've found them all and added them to a list, 
# we can go through the list and print them out or save them into a text file or whatever
for tHighlight in vHighlights:
    # We can use the color in the style attribute to set the text color!
    if tHighlight[0] == 'orange':
        print(colored(tHighlight[1], 'yellow'))
    elif tHighlight[0] == 'purple':
        print(colored(tHighlight[1], 'magenta'))
    else:
        print(colored(tHighlight[1], tHighlight[0]))