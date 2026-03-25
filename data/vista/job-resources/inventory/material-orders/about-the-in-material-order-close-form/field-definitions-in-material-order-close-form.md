---
title: "Field Definitions: IN Material Order Close Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-close-form/field-definitions-in-material-order-close-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-close-form/field-definitions-in-material-order-close-form"
---

# Field Definitions: IN Material Order Close Form

The following is a list of field descriptions for the IN
 Material Order Close form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  JC Co#

 Enter the JC Co# to restrict material orders by for closing. Only material orders posted to this Job Cost company that meet the selection criteria will be added to the batch. Leave blank to include material orders posted to all JC companies.

##  Job

 Specify the job by which to restrict material orders for closing. Only material orders posted to this job that meet the selection criteria will be added to the batch.
 Leave blank to include material orders for all jobs.

##  Include all 'Open' and 'Completed' Matl Orders on this Job

 Check this box to include all material orders with a status of 'Open' or 'Completed'. If you did not specify a JC Co# and Job above, will include material orders for all JC companies and jobs.
 Do not check this box if you want to specify the material order (or range of material orders) to close.

##  Beginning/Ending Material Order

 Specify the beginning and ending material order in a range of material orders to add to close batch. Leave blank to begin with first material order and end with the last.
Note: If you did not specify a JC Co# and Job above, range will include material orders for all JC companies and jobs.

## Include 'Open' Matl Orders with Remaining Units & Costs

Check this box to include material orders with a status of 'open' that have remaining cost or units. If you did not specify a JC Co# and Job above, will include material orders for all JC companies and jobs.
Do not check this box if you do not want to include 'open' material orders with remaining cost or units. Only material orders that are 'open' or 'complete' and have no remaining costs or units will be included.

##  Close Date

 Specify the close date for all material orders in this batch. Defaults the current date.
