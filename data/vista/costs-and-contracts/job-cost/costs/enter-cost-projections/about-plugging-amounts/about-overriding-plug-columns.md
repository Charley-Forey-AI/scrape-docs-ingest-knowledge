---
title: "About Overriding (Plug) Columns | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/about-plugging-amounts/about-overriding-plug-columns"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-cost/costs/enter-cost-projections/about-plugging-amounts/about-overriding-plug-columns"
---

# About Overriding (Plug) Columns

The % Complete, Over/Under, Remaining, and Final columns
 allow you four different ways to plug the projected final amount for each phase.
If you change the existing values for any of
 these columns, the program will recalculate each of the remaining columns and flag the
 item as ‘plugged’. Plugged entries are highlighted in yellow and will show an asterisk
 (*) in the P column of the Phases grid (if you specified to show column). (During batch
 processing, the ‘plugged’ flag is updated to the JC Cost by Period table (JCCP) for each
 applicable phase/cost type. This allows for use in reports.)
Note: If you enter a value in the % Complete
 field for a phase/cost type with estimate values for units, hours, or costs, and no
 actual values, the system will compute the Over/Under, Remaining,
 and Final fields as 0.00.
If you check the Buy Out
 flag for a plugged phase/cost type, and the plugged value is not equal to the buyout
 value, the line's color will be light blue. If the remaining committed cost plus actual
 cost for the phase exceeds the projected cost, the line color changes to peach (only if
 using Actual projection method). If you allow inactive phases and cost type to be
 included in cost projections (flag in JC Projection Options), inactive phases/cost types
 will be highlighted in gray (overrides all other colors).
Tip: Right clicking your mouse while in the projections grid
 will display an explanation of what the row colors represent.
It is important to note that the Projection
 posting options you selected in JC Company Parameters determine what data you can
 manipulate here. For example, to allow the percent complete figures to be manipulated in
 this program, make sure the Percent Complete option in the company file is checked. If
 an option is not checked, the corresponding column is disabled. Calculations will be
 displayed, but you will not be able to access the column for manipulations. The
 Projection Method selected in the company file determines whether projection
 calculations will be based on Actual Costs or Actual + Committed Costs, and the Minimum
 Percent Complete specified controls at what level of completion cost projections should
 begin.
