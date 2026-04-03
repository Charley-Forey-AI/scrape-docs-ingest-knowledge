---
title: "What are the rules for the \"Update projected quantities\" checkbox to appear? | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/project-management/job-cost/troubleshooting/frequently-asked-questions/what-are-the-rules-for-the-update-projected-quantities-checkbox-to-appear"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/project-management/job-cost/troubleshooting/frequently-asked-questions/what-are-the-rules-for-the-update-projected-quantities-checkbox-to-appear"
---

# What are the rules for the "Update projected quantities" checkbox
 to appear?

The following is the algorithm for the visibility of this
 new checkbox in Job Phases:

1. Check the Unit of Measure (UM) assigned to the phase
 code/cost type. This UM is found in the corresponding A/R file and has a Price Type
 assigned to it. If the Price Method for this UM is "fixed," then the field should be
 disabled.

1. If the UM field is blank, or has a UM that isn't set
 up in A/R, then the price method simply follows the Phase. The Phase Price Method is
 the Price Method radio group in the Properties window of Phase Maintenance. If this
 is set to "fixed," disable the new checkbox.

1.  If the Phase Price Method is set to "job default"
 then the Price Method from the job master file is used. If the job is set to "fixed"
 then the field is hidden.

1.  This checkbox will be disabled if the phase is a 'LS'
 or not a unit price type UM, it will be hidden completely if the job is not a unit
 price job.

1.  The checkbox will default to checked when adding
 phases that have the quantity cost type identified in the Job Cost Installation
 screen. All others will have the checkbox deselected.
