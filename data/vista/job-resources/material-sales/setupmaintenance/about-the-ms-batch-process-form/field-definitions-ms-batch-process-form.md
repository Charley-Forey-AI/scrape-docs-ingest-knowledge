---
title: "Field Definitions: MS Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-batch-process-form/field-definitions-ms-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-batch-process-form/field-definitions-ms-batch-process-form"
---

# Field Definitions: MS Batch Process Form

The following is a list of field descriptions for the MS
 Batch Process form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Audit Reports

Prints the distribution information from the batch sorted according to updates to other modules.
Note: If there are no entries in the batch, the audit lists cannot be printed.  Also, it is recommended that you print the audit lists before you post a batch because once the batch is posted, the audit lists are no longer available.
The following audit lists are available when processing Material Sales batches. If a list is grayed out, it means that particular list is not available for the current batch. Although some audit lists are available for all types of batches, the audit list title and/or detail shown may differ slightly based on the batch type. Additionally, only those lists with the checkbox marked can be previewed or printed.

- Batch List - The name of the batch list will differ depending on the batch type (i.e. Ticket Entry Audit List, Haul Entry Audit List, Haul Worksheet Audit List, Invoice Audit List, etc.). Prints the entries in the batch in sequence order.  As long as entries exist in the batch, this report can be printed.

Note: If you are using the surcharges functionality, surcharges will only appear on this report after you validate the batch.

- Job Cost Distributions - Prints the MS Job Cost Distribution List. Detail shown will differ based on the batch type. Some of the information shown may include haul line (if haul batch), the phase/cost type, material, U/M, Units, tax code, ticket number, GL account, JC unit of measure, units, and unit cost.

- Equipment Usage - Prints the MS Equipment Usage Audit List, showing the equipment, from location, material, unit of measure, and revenue code, basis, rate, and total.

- Inventory Distributions - Prints the MS Ticket IN Distribution List, showing for each location, the transaction number and type, the material, ticket, unit price, sales price, stocked and posted unit of measure, stocked and posted units, stocked and posted, unit cost, and stocked and posted total cost.

- Auto Production - Prints the MS Ticket Production Audit, showing for each production location, the transaction number and type, material, inventory location, unit of measure, units, unit cost, unit price, and total cost and price.

- Invoice Distributions - Prints the A/R Interface Audit List, showing by invoice and invoice line, the customer job, customer PO, from location, GL company and account, invoice amount, tax code, basis, and total, the discount amount, line total, and invoice total.

- General Ledger Distributions - The GL distribution list will differ based on the type of batch being posted (i.e. MS GL Entry Distribution List, MS GL Invoice Distribution, etc.). Prints a list of each GL account that will be updated, along with the debit/credit amounts updated to each account.

- Error List - Lists the sequence number and the error message for any entries where errors were found in the validation process.

Note: Users who have access to batch processing forms do not automatically have access to the related audit or error reports. It is recommended that if they will be processing batches, you give them access to the related audit and error reports using VA Report Security. If users do not have access, they will receive an error message when trying to preview/print those reports to which they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in MS Company Parameters), restricted access to one or more audit reports will prevent the user from posting the batch.
Click Preview to view the selected list(s) on
 the screen.
Click Print to print the selected list(s).

## Format

This field is only enabled for the MS Ticket Entry and MS Hauler Time Sheet Entry forms.

- Detail - Select this option to print all audit lists in detail format.

- Summary - Select this option to print all audit lists in summary format.
