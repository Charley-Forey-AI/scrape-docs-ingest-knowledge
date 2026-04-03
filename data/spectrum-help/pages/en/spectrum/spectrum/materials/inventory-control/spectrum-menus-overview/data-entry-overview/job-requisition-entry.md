---
title: "Job Requisition Entry | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/job-requisition-entry"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/job-requisition-entry"
---

# Job Requisition Entry

The Job Requisition Entry screen is used to requisition inventory items for use on a specific job.
The number of requisitioned items is deducted from the number available. Negative requisitions are entered if stock is returned to the warehouse from a job site. When updated, transactions created using this screen appear in inventory history as J (job) type transactions.
You may enter multi-company requisitions if the Multi-company requisitions  checkbox is selected in Inventory Control Installation. If this option is selected, the Job Requisition Entry screen prompts for the company ID on the header. The system posts G/L expenses and job costs to the company id entered. The inter-company G/L code entered on the Inventory Control Installation screen is used as the G/L credit account. This provides the ability to apply costs directly from inventory in one company to jobs in another company. Refer to the Inventory Control Installation section for more information on this function.
If items are shipped from multiple warehouses and contained on the same requisition, it is important to record shipping fulfillment one warehouse at a time if the Inventory Transaction Update is run for individual warehouses. If the quantity shipped is recorded for multiple warehouses at once, then updated for a single warehouse, all quantities due for other warehouses are back ordered. By updating all warehouses, or placing items for different warehouses on separate requisitions, this situation is eliminated. The Inventory Transaction Register warehouse selection reads detail warehouse.
Once you have completed this screen, select the Update button to print the [Inventory Transaction Report / Update](/en/spectrum/spectrum/materials/inventory-control/spectrum-menus-overview/data-entry-overview/inventory-transaction-report--update).
