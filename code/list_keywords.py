######
# DEPRECATED
# USE add_tags.py









# Packages that contain useful code for us to use
import os		   # Lets us do file operations
import re		   # Regular Expressions!
import pyperclip	# Let's us copy to the clipboard


# Print a bunch of blank lines to separate each run's output
print('\n'*100)

# Define the directory to start from
sBaseDir = '../content/province'
# sBaseDir = 'test_data'

# This list will hold all of the keywords we find
vKeywords = []
iGardens = 0
iGardensFinished = 0
# Navigate the directory tree start at a predefined root directory
for sRoot, vDirs, vFiles in os.walk(sBaseDir):
	
	# Loop through all the files in the current directory
	for sFilename in vFiles:
		_, sExt = os.path.splitext(sFilename)   # Get file extension (looking for .md)
		
		# Work with only .md files, but not with any _index.md files
		# This leaves only the entries proper
		if sExt == '.md' and not sFilename == '_index.md':
			
			iGardens += 1
			# print(sFilename)
			
			with open(os.path.join(sRoot,sFilename),'r') as f:
				sFile = f.read()
				f.close()
			
			bDraft = sFile.lower().find('draft: false') == -1
			bDraft = sFile.lower().find('draft: false') > -1
			
			iStart = sFile.find('## Keywords')
			if not bDraft:
				iGardensFinished += 1
				
				if iStart >= 0:
					sKeywords = sFile[iStart+12:]
					iEnd = sKeywords.find('\n#')
					sKeywords = sKeywords[:iEnd].strip()
					
					print('Keywords:\n'+sKeywords)
					
					for sLine in sKeywords.split('\n'):
						sLine = sLine.replace('\\', '')
						sLine = sLine.strip()
						if len(sLine) and not sLine in vKeywords:
							vKeywords.append(sLine)
							print('Line:\t'+sLine)
						
					print('\n'*2)

# Make one list of all the keywords
sKeywordList = ''
for tKeyword in vKeywords:
	sKeywordList += '%s\n' % tKeyword

sKeywordList = sKeywordList.strip()

# Save that list to a file
with open('keywords.txt', 'w') as f:
	f.write(sKeywordList)
	f.close()

# Copy the list to the clipboard (for pasting in Google Sheet)
pyperclip.copy(sKeywordList)

print('Number of gardens: %i\t,Number of finished gardens: %i' % (iGardens, iGardensFinished))
# Print it out for us to see
# print(sKeywordList)