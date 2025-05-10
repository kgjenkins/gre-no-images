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
vAuthors = []
vAuthorsDraft = []
vAuthorsNotDraft = []
iGardens = 0
iGardensFinished = 0
# Navigate the directory tree start at a predefined root directory
for sRoot, vDirs, vFiles in os.walk(sBaseDir):
	
	# Loop through all the files in the current directory
	for sFilename in vFiles:
		_, sExt = os.path.splitext(sFilename)   # Get file extension (looking for .md)
		
		# Skip the meta pages
		vExcluded = ['about.md', 'citation.md', 'contribute.md']
		if sFilename in vExcluded:
			continue
		
		# Work with only .md files, but not with any _index.md files
		# This leaves only the entries proper
		if sExt == '.md' and not sFilename == '_index.md':
			
			iGardens += 1
			# print(sFilename)
			
			with open(os.path.join(sRoot,sFilename),'r') as f:
				sFile = f.read()
				f.close()
			
			# bDraft = sFile.lower().find('draft: false') == -1
			bDraft = sFile.lower().find('draft: false') > -1
			
			if True:# bDraft:
				iGardensFinished += 1
				
				reAuthor = re.compile('author\:\s+([^\n]+)\n')
				
				mAuthor = reAuthor.search(sFile)

				# Print out the match
				if mAuthor is None:
					raise Exception('No author in: ' + sRoot + ' // ' + sFilename)
				else:
					sEntryAuthor = mAuthor.groups(0)[0]
					print(sEntryAuthor)
					vEntryAuthors = re.split('[\"\(\)\[\]\,]| and ', sEntryAuthor)
					vEntryAuthors = [ s.strip() for s in vEntryAuthors ]
					print(vEntryAuthors)
					
					for s in vEntryAuthors:
						if len(s):
							vAuthors.append(s)
							if bDraft:
								vAuthorsDraft.append(s)
							else:
								vAuthorsNotDraft.append(s)
					# vAuthors.append(mAuthor

# Make one list of all the keywords
vAuthors = list(set(vAuthors))
vAuthors.sort()

vAuthorsDraft = list(set(vAuthorsDraft))
vAuthors.sort()

vAuthorsNotDraft = list(set(vAuthorsNotDraft))
vAuthorsNotDraft.sort()

# 
# sAuthorList = ''
# for tAuthor in vAuthors:
# 	sAuthorList += '%s\n' % tAuthor
# 
# 
# sAuthorList = sAuthorList.strip()

# Save that list to a file
with open('authors.txt', 'w') as f:
	f.write('\n'.join(vAuthors).strip())
	f.close()

with open('authors_draft.txt', 'w') as f:
	f.write('\n'.join(vAuthorsDraft).strip())
	f.close()

with open('authors_not_draft.txt', 'w') as f:
	f.write('\n'.join(vAuthorsNotDraft).strip())
	f.close()

# Copy the list to the clipboard (for pasting in Google Sheet)
# pyperclip.copy(sAuthorList)

print('Number of gardens: %i\t,Number of finished gardens: %i' % (iGardens, iGardensFinished))
# Print it out for us to see
# print(sAuthorList)
