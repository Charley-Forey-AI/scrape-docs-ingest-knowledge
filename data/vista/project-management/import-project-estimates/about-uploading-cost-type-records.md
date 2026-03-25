---
title: "About Uploading Cost Type Records | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-uploading-cost-type-records"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-uploading-cost-type-records"
---

# About Uploading Cost Type Records

Information about cost type records.
The following process is used when uploading
 cost type records:

- If the cost type does not exist in
 JCCH (JC Cost Header), it will be added.

- If the phase/cost type exists in
 JCCH, and both the import and JCCH units of measure match, the import units will
 be added to the existing Original Units.

- If the units of measure do not
 match, and detail exists in JCCD (JC Cost Detail) for the phase/cost type other
 than 'OE' (original estimate), original units will not be updated with the
 import units.

If no JCCD records exist that meet the above
 criteria, the import unit of measure will be used, and the import units will become the
 original units.
