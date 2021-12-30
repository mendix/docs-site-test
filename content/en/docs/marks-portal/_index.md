---
title: "Mark's Portal Test"
description: "A section of the Docsy docs site to do lots of controlled tests"
cascade:
    sitemap: 
        priority: 0.7
#linktitle: "A title for links - need to look this up - used in restore-backup-locally.md"
#tags: ["These", "are", "Example", "Tags"]
#weight: 10
#notoc: true
#layout: wide
#draft: true
#toc-level: "3"as
#sitemap: false (remove from Google sitemap)
#disable_sitemap: true (also remove from Google bot)
#nosearch: true (remove from Algolia)
# aliases:
#   - /xyzzy.html
---

## 1 Test

First subsection of Mark's Portal

**This is the file /content/en/docs/marks-portal/_index.md**

### Links (to other test pages)

[RSS]({{< relref "mark-portal-section-1"  >}} "Go to page with RSS example") (relref and tooltip/title)
**Should always use relref, otherwise development links will point to production site**

[Shortcodes]({{< ref "mark-portal-section-3" >}}) (ref)

[Cascading banner]({{< ref "mark-portal-section-3" >}}) (ref)

[Normal link to anchor 3](#anchor3)

[relref to anchor 3]({{< relref "#anchor3" >}})

[Cascading banner](mark-portal-section-3) and [Shortcodes](mark-portal-section-3)

Natasa's test:

[Ref to mark-portal-section-3]({{< ref "mark-portal-section-3" >}})

[Relref to mark-portal-section-3]({{< relref "mark-portal-section-3" >}})

[Normal link to mark-portal-section-3 anchor 3](mark-portal-section-3/#anchor3)

[relref to anchor 3]({{< relref "#anchor3" >}})

[relref to mark-portal-section-3 anchor 3]({{< relref "mark-portal-section-3#anchor3" >}})


[Ref to java-programming]({{< ref "java-programming" >}})

[Relref to java-programming]({{< relref "java-programming" >}})

[Normal link to java-programming](/refguide/troubleshooting/)

### Attachment from attachments in this bundle

Insert with Markdown

![Insert lights bundle image](attachments/lights-bundle.png)

insert with figure {{< figure src="attachments/lights-bundle.png" >}}

### Attachment from static

Insert with Markdown (don't include the first `/static`!)

![](/attachments/docs/marks-portal/lights-static.png)

insert with figure {{< figure src="/attachments/docs/marks-portal/lights-static.png" >}}

## 2 Second Section

This is a second section

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### 2.1 First Subsection of the Second Section

You've guessed it.


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

### 2.2 Second Subsection of the Second Section

This subsection has two sub-subsections.


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

#### 2.2.1 Two Point Two Point One

This is the first sub-subsection.


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

#### 2.2.2 Two Point Two Point Two

This is the second sub-subsection.


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

## 3 Section Three{#anchor3}

The last section.


Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
