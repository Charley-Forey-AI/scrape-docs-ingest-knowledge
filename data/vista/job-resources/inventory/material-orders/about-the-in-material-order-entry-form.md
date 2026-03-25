---
title: "About the IN Material Order Entry Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form"
---

# About the IN Material Order Entry Form

Use this form to enter material orders.
Material Orders are used to assign and allocate materials to jobs, creating committed units and costs for the specified job/phase/cost type. These costs are relieved and posted as actual costs once the material order is confirmed.
You can manually enter a material order or you can copy an existing one using the IN Material Order Copy form (File > Copy Material Orders). This can save time if you have standard material orders. For information about copying material orders, see [Copy a Material Order](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form/copy-a-material-order).
Each material order consists of a header and items. Header detail includes the material order number, job, order date, and who ordered the materials. Items are entered in the lower section of screen and specify which location is supplying the materials, the material being ordered, the job, phase and cost type to which the material is allocated, the date material is required, and the material's unit of measure, units, unit price, and tax code. Also included are display-only fields that review the confirmed and remaining units and costs associated with an item. Current values from Inventory are also displayed based on the location and material.

## Committed Costs

Material Orders represent a job's committed costs, which are stored in the JCCP (Costs By Period) database table.
When a material order is set up, the total committed costs for the job increases. These costs will only change when material orders are added, changed, or deleted. The Remaining Committed Costs column in JCCP accumulates all of the order information and is then decreased each time a material order is confirmed (in Material Order Confirmation).
If a material's standard unit of measure equals the Job Cost U/M or can be converted to it (using the conversion factors in HQ Material Units of Measure), Total and Remaining Committed Units and Costs will be updated to the Cost by Period table (JCCP) each time you post a Material Order Entry, Confirmation, or Close batch.
If the Update Committed Cost detail to JC checkbox is selected in the IN Company Parameters form, entries are also generated in the Cost Detail database table (JCCD). These detail entries are made at the material order item level, and are created whenever the Committed Units or Costs on a material order are modified.
If the units of measure do not match, or cannot be converted, then units and costs are not updated.

## Field Tickets

Field tickets enable you to link labor, material, and equipment costs related to specific work activity on a job, and facilitate owner billing. When you enter a material order item, you can assign it to a field ticket associated with the contract for the specified job. You can assign multiple material order items to a single field ticket, as long as the ticket is still open (that is, it has a status of O-Open in JC Field Ticket). Once the status is set to Closed, Approved, Rejected, or Billed, you can no longer post costs to that ticket.Note: Costs associated with approved field tickets only impact T&M billings; therefore, assigning field tickets to material order items is only useful if the job's contract/contract item has a bill type of T&M or Both. Additionally, once you process a material order batch, entries associated with approved field tickets appear on the Cost Detail tab in JC Field Ticket for the specified field ticket.

 For more information about field tickets, see [JC Field Ticket Form](/en/vista/vista/costs-and-contracts/job-cost/jobs-and-contracts-setup/jc-field-ticket-form).

Related information

- [Copy a Material Order](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-entry-form/copy-a-material-order)

- [About the IN Material Order Confirmation Form](/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirmation-form)

- [Types of Cost Information](/en/vista/vista/costs-and-contracts/job-cost/types-of-cost-information)
