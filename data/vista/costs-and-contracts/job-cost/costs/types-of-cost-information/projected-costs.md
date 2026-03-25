---
title: "Projected Costs | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/types-of-cost-information/projected-costs"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/types-of-cost-information/projected-costs"
---

# Projected Costs

One of the ways the JC module goes beyond just collecting
 accounting data to provide job management capabilities is with the JC Cost Projections
 program.
The Cost Projections program is designed to be
 extremely flexible; you decide how the screen should be arranged and set it up as such
 in the JC Company Parameters program.
The JC Cost Projections program
 integrates two distinct functions on one screen—calculating projections and entering
 projections. You can decide when and if to use either or both. Here are some
 different ways to work with projections:

1. You can ignore the Cost Projections program completely, and
 use the calculation abilities of Crystal Reports to build your own formulas into
 your job cost reports that calculate projections based on estimated, committed,
 and actual amounts.

1. You can use the Cost Projections program to let the system
 calculate projections for you, which can then be included on your Crystal
 reports.
 Note: This option requires only that you
 use the Initialize feature of the Cost Projections screen to let the
 system calculate projections for the jobs and phases you select. The
 projected calculations are stored in the Cost by Period table (JCCP) in
 the Projected Hours, Units, and $ fields that can then be drawn into any
 report you develop, and changes are stored in the Cost Detail (JCCD)
 table.

1. If you do not want to use the calculations at all, or you do
 not want to keep units complete up-to-date (in Progress Entry), you can ignore
 the calculation feature of Cost Projections and just use it as a data entry
 program for entering projections.

1. To get maximum value from this program, you can calculate your
 projections, and then override the particular job phases where the calculated amount
 does not adequately reflect the status of that work. Note that each time you
 recalculate, you have the option to leave those numbers that were previously
 overridden (plugged) intact, or to replace them with new calculations. You also have
 the option to initialize projections for all jobs at once, a specific range of jobs,
 or jobs by project manager (i.e. only those jobs that are assigned to the specified
 project manager in JC Jobs).
