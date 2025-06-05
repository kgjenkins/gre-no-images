# Gardens of the Roman Empire Project

This repo contains the source files of the *Gardens of the Roman Empire* project.


## Hugo

We are using [Hugo](https://gohugo.io) with the [Mainroad](https://themes.gohugo.io/mainroad/) theme.  The rendered website can be viewed locally by running `hugo server` from the main directory.  This will update the website files in the `/docs` directory.  Note that the any changes to the `/docs` will be ignored when committing changes -- this helps to keep the repo size down.

The public website is built by running a GitHub Action that uses Hugo to publish the site to a separate repo named `roman-gardens.github.io`.  There are also actions to publish updates to a test website -- this can be used to test changes before updating the public website.


## Basic Development

Create a new garden page using the `hugo new` command, for example:

```hugo new province/achaea/athens/my_garden.md```

In this example, we have specified the full path to the province and sublocation (`achaea/athens`).  Some gardens may have more levels of hierarchical sublocations (`italia/pompeii/region_viii/insula_iii`).

The text after the final slash (`my_garden.md`) should be the full name of the garden as it will be written in the article, with any spaces replaced with underscores, plus the extension `.md`.  For example, a garden named "Big Two-Hearted River" becomes: `big_two-hearted_river.md` -- note the difference between the underscores and the hyphen.  Do not include spaces or any other punctuation in the filename!


## Committing changes

(TO DO) We will use VSCode...


## Reporting issues

(TO DO)

minor change
another
