---
title: "Open Linked Data"
date: 2021-04-20T12:29:09-04:00
editor: David Ratzan
draft: false
---

**GRE adopts [open linked data](https://en.wikipedia.org/wiki/Linked_data#Linked_open_data) approaches whenever it can.** Data is **linked** when one data set reuses or relies on another. Such linked data is **open** when the target data is free and open to the public to use. This approach and its advantages are perhaps best illustrated by an example.

In GRE, we use [Pleiades](https://pleiades-stoa-org.proxy.library.nyu.edu/) identifiers for our geographic data. In other words, each garden in GRE has metadata fields related to geography, since each garden exists in space. Instead of defining these geographic places for ourselves -- and in the process not only needing to collect lots of data (e.g., representative longitude and latitude) and creating a necessarily idiosyncratic list of places (e.g., which name should we use, ancient or modern, from which period, which spelling or transliteration, etc.) -- we instead reused the existing collection of open geographic data related to places in the ancient world as represented in Pleiades.

Such an approach holds several advantages.
- the basic work of collection has already been done by Pleiades contributors and editors (and we can suggest corrections if needed, since it is an open project)
- Pleiades data is peer-reviewed, giving us some assurance of quality
- Pleiades has a well-conceived and consistent system for naming, classifying, and relating places to each other (more technically, it has a well-defined ontological [controlled vocabulary](https://guides.lib.utexas.edu/metadata-basics/controlled-vocabs))
- Each place has a unique, stable identifier

Any scholar or project that uses Pleiades will therefore be able to query the GRE data (available in our [github repository](https://github.com/roman-gardens/gre) and reuse our data with confidence, since they will know that we are talking about the same places with great precision.

Also, since Pleiades is an open, collaborative project, we can create new places as we may need, including “gardens” (as opposed to other types of places, like villas, temples, villages, etc.).

In other words, we do all of our ancient geographical work in Pleiades, which is optimized for that sort of work; and in relying on and linking to Pleiades data, we are free to concentrate our efforts on gardens, our main interest. Indeed, one aim of GRE is to become an open linked data resource for scholars and readers interested in Roman gardens.

## GRE open linked datasets and controlled vocabularies

Some of the open linked data resources and controlled vocabuli GRE currently uses include (main use in parentheses):
- [CITE URNs](https://www.homermultitext.org/hmt-doc/cite/index.html) (usually through [Perseus](https://catalog.perseus.org/) for Greek and Latin texts and authors)
- [Getty Art & Architecture Thesaurus](https://www.getty.edu/research/tools/vocabularies/aat/) (art historical and architectural terms)
- [Getty Thesaurus of Geographical Names](https://www.getty.edu/research/tools/vocabularies/tgn/) (geography)
- [ORCID](https://orcid.org/) (authors)
- [papyri.info](https://papyri.info/) (papyri)
- [Pleiades](https://pleiades-stoa-org.proxy.library.nyu.edu/) (ancient places and geography)
- [Wikipedia](https://en.wikipedia.org/wiki/Main_Page) (general reference)
- [WorldCat](https://www.worldcat.org/) (bibliography)
