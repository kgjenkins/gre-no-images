# Packages that contain useful code for us to use
import os # Lets us do file operations
import re # Regular Expressions!

# The RegEx string we're going to use to extract the desired text
reKeywordEntries = '\-\s+\[([^\]]+)\]\(([^\)]+)\)'

# Print a bunch of blank lines to separate each run's output
print('\n'*100)

# Define the directory to start from
sBaseDir = '../content/province'
# sBaseDir = 'test_data'

vKeywordsAll = []

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
				f.close()
			
			reDraft = re.compile('draft\:\s+[Tt]rue')
			bDraft = reDraft.search(sFile) is not None
			# bDraft = False
			
			# Get the keyword section of the file
			sKeywords = ''
			iStart = sFile.find('### Keywords')
			if iStart > -1 and not bDraft:
				sKeywords = sFile[iStart+13:]
				iEnd = sKeywords.find('#')
				sKeywords = sKeywords[:iEnd].strip()
			else:
				sKeywords = ''
			
			# Extract a list of keywords
			vKeywords = []
			for tMatch in re.findall(reKeywordEntries, sKeywords):
				print(tMatch)
				if not tMatch in vKeywords:
					sKeyword = tMatch[0]
					sKeyword = re.sub(r'\[([^\]]+)\](\([^\)]*\))', r'\1', sKeyword)
					sKeyword = sKeyword.strip()
					if len(sKeyword):
						vKeywords.append(sKeyword)
			
			# Skip the file if it does not contain any keywords
			# if len(vKeywords) > -1:
			# print('File does not contain keywords: %s // %s' % (sRoot, sFilename))
			# continue
			
			# Compile the list into a new 'tags' entry
			vKeywords.sort()
			
			# Get the metadata section of the file
			sMetaData = sFile
			iEnd = sMetaData.find('---\n', 5)
			if iEnd == -1:
				raise Error('File does not contain Metadata: %s' % sFilename)
			
			sMetaData = sMetaData[:iEnd+4]
			sMetaData = re.sub('\-\-\-\n', '', sMetaData)
			sMetaData = sMetaData.strip()
			
			sFile = sFile[iEnd+4:].strip()
			
			# Extract any 'tags' section already in the metadata
			iTags = sMetaData.find('tags:')
			if iTags > -1:
				sMetaData = sMetaData[:iTags].strip()
			
			# Create MetaData tag list
			sTags = 'tags:\n'
			for sKeyword in vKeywords:
				vKeywordsAll.append(sKeyword)
				sTags += ' - "%s"\n' % sKeyword
				print(sKeyword)
			
			if len(vKeywords):
				sMetaData = '---\n%s\n%s---\n\n' % (sMetaData, sTags)
			else:
				sMetaData = '---\n%s\n---\n\n' % (sMetaData)
			
			# Control switch for modifying files (for debugging)
			if True:
				with open(os.path.join(sRoot,sFilename),'w') as f:
					f.write(sMetaData + sFile)
					f.close()


# Make one list of all the keywords

vKeywordsAll = list(set(vKeywordsAll))
vKeywordsAll.sort()

sKeywordList = ''
for tKeyword in vKeywordsAll:
	sKeywordList += '%s\n' % tKeyword

sKeywordList = sKeywordList.strip()

# Save that list to a file
with open('keywords.txt', 'w') as f:
	f.write(sKeywordList)
	f.close()