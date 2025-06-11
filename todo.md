
# New for Launch on April 15, 2021

- [ ] Set `draft: true` in:
    - [ ] Gallia
    - [ ] Hispania
    - [ ] Other ?
- [ ] Update template with new look and feel
- [ ] Page should have an alphabetical list of authors with hyperlinks to searches for those names, so that if someone clicks on it, it pulls up the search results for that author.

# General

- [x] Make a really cool project
- [ ] Check all the keywords for one standard getty url
- [ ] Check for all comments containing some mention of "cross references", add links to relevant pages
- [x] Go through punchlist for each article
- [x] Get province information into general province page (somehow)
- [x] Get keywords into tags list in header (as in bancroft example)
- [x] Get geographic regions into sidebar using categories list (as in bancroft)
- [x] DONT Put `lead:` in the header for each article to make loglines/subtitles (e.g. Dalmatia/salona/salona_tomb...)
- [ ] Check that all keywords are in controlled vocab (Programmatically)
- [ ] Figure out why there are so many unattached images (e.g. Achaea Nemea has a figure which is not in the proper images folder)
- [x] Deal with empty stuff in headers (by commenting out for now)
- [ ] Deal with empty stuff that is now commented out (by deleting)
- [ ] Should "urban villas" be removed and (if necessary) replaced with "villae urbanae"?
- [ ] Deal with all smart quotes (“”)
- [ ] Fix any quotes in `figure` attributes
- [ ] Redo all pub dates as YMD
- [ ] Implement [LOC Datetime format](https://www.loc.gov/standards/datetime/)
- [x] Add a keyword that means "hasInscription"
- [x] Check for any ">>>>>>" merge conflict stuff in the articles
- [x] Take every heading down one level
- [ ] Add a takedown notice (copy from DCAA/DSCC)
- [x] Suppress empty headings
- [ ] Finish creating documentation
- [x] Change keywords to bulleted list
- [ ] Fix all links that have [text](#) or [text](link)

# Article Punchlist

- Title in title case with spaces?
- Province `relref` correct?
- Location
    - folder `relref`
    - Pleiades ID
- Keywords, separated by newline (`\` at end of line)
- Sublocation `relref` present? -> comment out for now
- Pleiades ID
    - Numbers in link?
    - `"(Pleiades)"` in link? -> delete
    - Two links present, one with `relref` -> delete `relref`
- figures linked correctly?
- check all `ref`s to other gardens, should be `relref`s

# Articles in need of a second look

- achaea/corinth/corinth_circus, images with no links (image folder empty -JEM)
- ger sup/dietikon, no orcid for Christa Ebnöther
- ger sup/vallon, two map images are broken, replace with new


# Image cropping and straightening

- [x] achaea
- [x] britannia
- [x] dacia_traiana
- [x] dalmatia
- [x] germania_inferior
- [x] germania_superior
- [x] macedonia
- [x] pannonia

# Pompeii Notes/Issues

- Titles (I.ii.10). Right now if a location doesn't have a specific name, using the I.ii.10 ID.
- [x] Artifacts: TBD on how to note
- [x] Green (additions to entries?). What to do? There appears to be ORANGE now as well.
- [x] Add span style color families to new green parts of entries.
- [ ] Someone should relook over the bibs to see if they know what book the author is referring to, as I can't figure it out with just an author last name.
- [x] Image PATHs might need modifying.
- [x] Note to self: relook over entries and add [statue] keyword.
- [x] Note if it has literary evidence/artifacts.
- [x] Issue: I have found a entry that is House of Epidius Fortunatus (I.iii.3) and another that is I.iii.3. If there is a distinction, should we make it clearer?
- [x] *Aedicula lararium* added as one keyword merged from the two currently listed.
- [x] Should I include excavations dates in date section?
- [x] Province edits for keywords


# TODO 2025

- [x] merge nav-merge into master-new (which will be renamed "main" and become the default branch)
- [x] remove unused layouts
- [x] remove PROVINCE_ID from front matter - province is part of the directory structure
- [ ] move province descriptions from garden to separate files?
- [ ] recover gallia aquitania entries? https://github.com/roman-gardens/gre/commit/06b191b293c531a31dca04631b02d031a3a1b32d
- [ ] document how theme files should be edited (not in mainroad directory!)
- [ ] Bibliography first item actually two? https://roman-gardens.github.io/province/italia/rome/regio_x_palatium/domus_augustana/
- [x] move all images to separate repo? -- experiment and assess pros/cons
- [ ] alternative names -- example https://roman-gardens.github.io/test-a/id/5c8aada6d5
- [ ] standardize and document recommendations for entry titles
        - House name, or house number, or both?
        - Roman/Arabic numerals for region, insula, house (e.g. Pompeii VIII.4.30 vs VIII.iv.30)
        - ideally, don't depend on upper/lowercase for meaning
- [ ] consistent heading levels in articles (h1, h2, h3, etc.)
- [ ] add author/editor/date metadata to (top or bottom?) of article -- no need to duplicate in the markdown
    - use a partial that will use the frontmatter values and automatically add ORCID, email, etc.
    - or link to a separate person page, [like Pleiades does](https://pleiades.stoa.org/author/thomase)
- [ ] frontmatter quoting: omit, unless ambiguous

# from 2025-03-04, 2025-04-04, 2025-05-06 meetings
- [ ] when we restart blog/news, add the posting date and snippet to the list of posts
- [ ] people: Change Pleiades liaison from Gabriel to Tom Elliott?
- [ ] maps: fix/remove blank maps
- [ ] documentation: rewrite software setup
- [ ] list of keywords as glossary (option to search GRE or go to Getty Thesaurus, etc.)
- [ ] keywords section in article text vs tags in front matter
- [x] fix capitalization in garden list for "VIa", "VIlla" etc. (getting mangled by Roman numeral processing)
- [ ] garden list sort order (currently alphabetical, but most recent first?)
- [ ] browse by province -- only list most recent updates?
- [ ] move province description to browse page for the province
- [x] "garden entries" have been published
- [x] remove numbers like 563 from Herculaneum entry titles
- [ ] shortcodes for Pleiades, TGN, Periodo, POWO, AAT, Perseus, Worldcat, etc.

# Province pages
- [ ] review which sections should be retained in province pages (and also for gardens...)
- [ ] move content from garden entries to the province _index.md
- [ ] generate new "gre_id" and "alias" values for new province pages

# Images
- [x] rename 37 JPG files to jpg
- [ ] many dupl images in thugga -- warning!  the "2" image may be older (missing additional label/green patch)
- [x] convert .tif, .ai, and .ppt files to .jpg or .png
- [ ] some photos we want lower resolution (so copyright holder can control access to full resolution)
- [ ] link to reuse/take-down policy in image captions



# User forks

User forks of the old GRE repo that have updates, as of 2025-03-26:
- [ ] [amartyashri](https://github.com/roman-gardens/gre/compare/main...amartyashri:gre:master) (Amartya Shri) - 28 files, Pleaides links, removed empty sections
- [ ] [crc034](https://github.com/roman-gardens/gre/compare/main...crc034:gre:master) (Clarie Campbell, Univ. Arkansas) - 4 files: draft=false, ignore /docs files
- [ ] [jemillar](https://github.com/roman-gardens/gre/compare/main...jemillar:gre:master) (Jane Millar, UT Austin) - 36 files: links, tags, etc.
- [ ] [joshuarosenheim](https://github.com/roman-gardens/gre/compare/main...joshuarosenheim:gre:master) (Joshua Rosenheim, Cornell) - 9 files: coordinates, but beware some files have moved
- [x] LXB41 (Leigh-Ann Bedal, Penn State) - updates already in gre/main

Users with forks that have no updates:
- dmratzan (David Ratzan, ISAW)
- DorscJ (June Dorsch, ISAW)
- emacaulaylewis (Elizabeth Macaulay, CUNY)
- jlvenner (Jessica Venner, Univ. Birmingham)
- Kiara1980 (Kiara Beaulieu, Univ. Antwerp)
- KJTS (Kaja Tally Schumacher, formerly Cornell, now at Harvard)
- klg16 (Kathy Gleason, Cornell)
- mmeyer5 (Max Meyer, Cornell alum, now at Brown)
- rmpare (Rhiannon Pare, Princeton)
- worldofyuki (?)
- XueXia329 (Xue Xia, Cornell alum)
- yifanli7 (Yifan Li, Cornell alum)
- yK755 (Yaniv Korman, Cornell alum)

