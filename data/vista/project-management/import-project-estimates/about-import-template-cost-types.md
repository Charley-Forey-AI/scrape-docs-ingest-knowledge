---
title: "About Import Template Cost Types | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/import-project-estimates/about-import-template-cost-types"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/import-project-estimates/about-import-template-cost-types"
---

# About Import Template Cost Types

Use the Create Cost Types tab to set up the cost types that you want created when importing estimate data.
For example, if you are bringing in labor
 data, and you wish to create a burden cost type record for each labor record, you would
 define that cost type here, as shown below:
Cost Type
Description
Create Cost Type
Description

1
Labor
7
Burden

Then when PM Upload Import Data is run, if a
 labor record is uploaded and no burden record exists in the work file, one will be
 created.
Costs are not uploaded with the newly
 created cost type; those will need to be entered manually. However, you can specify that
 you want the created cost type to use the same unit of measure, units, and hours as the
 cross-referenced cost type by setting the Use UM, Use Units, and Use Hours flags to Y
 (checked). Then when you run PM Upload Import Data, the results will look like this:
Cost Type
UM
Units
Hours
Created CT
UM
Units
Hours

1 (Labor)
CY
168.00
85.00
7 (Burden)
CY
168.00
85.00

If you set the Use UM, Use Units, and Use
 Hours flags to N (No):
Cost Type
UM
Units
Hours
Created CT
UM
Units
Hours

1 (Labor)
CY
168.00
85.00
7 (Burden)
LS
0.00
0.00

Once a unit of measure is required, the upload
 automatically assigns LS as the unit of measure, and sets the units and hours to 0.00.
 The UM, units, and hours can be edited manually in Project Management.
