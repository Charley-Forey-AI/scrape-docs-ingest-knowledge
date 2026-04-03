---
title: "Scale Ticket Journal Update - by Job | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-journal-update---by-job"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/materials/materials-management/spectrum-menus/data-entry-overview/scale-ticket-journal-update---by-job"
---

# Scale Ticket Journal Update - by Job

If multiple items were entered for a ticket, a list of these items for each ticket will display when the update is previewed.
If job requisitions are selected, the following information will be included:
job item code description ticket# date um quantity phase ct
Spectrum
Materials Management
Comments

Requisition#
N/A
system generated

Req. date
SI transaction date
transaction date entered at time of update

Status
N/A
always 'S' for shipped

Job
si.job
valid job

Special Instructions
N/A
blank

Ship via
N/A
blank

Ship date
Si transaction date
same as above

Entered by
SI batch code
summarize by batch code

From warehouse
si.plant
summarize by plant

Item code
si.item
same valid code

Description
N/A
from item master

Unit of Measure
N/A
from item master

From warehouse
si.plant
same as above

Markup%
N/A
defaults from item master

Ordered quantity
si.netwt
net weight summarized

Unit cost
N/A
actual cost from inventory master file (use std cost if no qty computed from mix processing)

Phase
si.phase
summarized by phase

Cost Type
si.ct
Summarized by ct

The miscellaneous cost charges and freight costs (cost amounts, not billing) are transferred as separate line items in Job Requisition Entry. They are transferred as non-stock items and the inventory category is used to default the general ledger department. (The miscellaneous charges category is set up in the installation and the freight category is set up for each hauler.) If the general ledger department is blank for the freight or miscellaneous category, then Warehouse / GL Department Maintenance is used. If the general ledger department is not found here, the software looks in Inventory Control Warehouse File Maintenance for the G/L department.
The cost type assigned to separate freight and/or miscellaneous charges is based on the cost type stored in the G/L chart of accounts for the Freight/Miscellaneous G/L code, as long as the resulting phase/cost type is a valid combination for the particular job. If not, then the cost type of the material line is used for Freight/Miscellaneous job requisition lines.
The item code for miscellaneous and freight is also specified and is used for the non-stock item code. For job requisitions, the tickets are summarized by item, job, phase, and warehouse, and then individually listed in the 30-character message line; up to four tickets can then be summarized per line, if more then a new line is created. This message line is accessed in Expand mode for each line item of job requisition. the software also allows you to enter non-stock items with the category code first, then "!" and an item Id (as in Order Processing) in the job requisition entry.
A use tax code is assigned to the job requisition line if use tax classifications are used. The same logic is applied during the Scale Ticket Update as would occur if the job requisition line were added manually in Job Requisition Entry.
