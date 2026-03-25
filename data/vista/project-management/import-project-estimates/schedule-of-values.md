---
title: "Schedule of Values | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/schedule-of-values"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/schedule-of-values"
---

# Schedule of Values

The ‘schedule of values’ is a detailed statement providing allocation values for the various parts of work being performed.
If the import file does not provide item records,
 you can define a ‘schedule of values’ using the “When no item records are available to
 import…” section in PM Import Templates (Import Parameters tab). These options allow you
 to identify how items will be created when importing data. There are four options
 available when defining your schedule of values:

- One Item Only - This option assigns all phases to a single contract item, which you specify in the Contract Item field. A description is also defined for the contract item.

- Use Import Phase - This option creates a contract item based on the phase data being imported. You specify the beginning and ending character to use, and the contract item number is generated from the phase code based on those specifications.

For example, if the imported phase code is 01330-100-001:
Character Position:
1
2
3
4
5
6
7
8
9
10
11
12
13

Import Phase Code:
0
1
3
3
0
–
1
0
0
–
0
0
1

Beginning Character
Ending Character
Resulting Contract Item

1
3
013

11
13
001

- Use Viewpoint Phase - This option works the same as the Use Import Phaseoption except that instead of using the imported phase, it uses the cross-referenced Viewpoint phase to create the contract item based on the specified beginning and ending characters.

- None– Not applicable. This option is typically selected when the export file already contains the contract items and therefore does not require any of the above options to create contract items
