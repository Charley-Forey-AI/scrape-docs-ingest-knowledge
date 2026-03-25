---
title: "About the IN Material Order Confirmation Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirmation-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/inventory/material-orders/about-the-in-material-order-confirmation-form"
---

# About the IN Material Order Confirmation Form

Use this form to confirm materials set up on a material order that have been pulled from stock and sent to the job.
Confirming a material order reduces both the stocked material’s “allocated” units and the job’s remaining committed costs, while increasing the job’s actual costs.
You can enter confirmations manually or using the IN
 Material Order Confirm Init form (accessed from this form via File > Initialize
 Confirmations or from the IN Programs menu). When using the initialization process,
 this form populates with each item confirmed on a material order. Each item is set up as
 a separate sequence and can be edited as necessary.
The Info tab on this form is used to specify the material order, item, confirmation date, and the number of units being confirmed. A memo field is provided for entering any notes or information. The Material Recap section of the form provides an informational display showing the ordered, confirmed, remaining, and total units and price for the current material order item, as well as the material's location, job, phase, and tax code.
Note: You can expand or collapse the Material Recap section using the chevron ( or ) button.
Once you have confirmed the material orders, process
 the batch as normal. This will relieve the committed costs and units specified, and post
 them as actual costs and units. Additionally, the update will decrease the 'on hand' and
 'allocated' amounts for the material as shown in the IN Location Materials
 form.

## Using the MO Worksheet

Before using the IN Material Order Confirmation form to confirm material orders, print the IN MO Worksheet report (Inventory Reports menu) for the material orders to be confirmed. Using the worksheet, manually indicate which materials on each material order have been pulled from stock, and the quantity (of the ordered amount) sent to the job. Once the worksheet is completed, use the worksheet as a guide when 'confirming' the materials in this form.
Tip: You can add the IN MO Worksheet report to the
 Options > Reports menu of this form (using RP Reports by Form), which will allow running the
 report without leaving the batch.
