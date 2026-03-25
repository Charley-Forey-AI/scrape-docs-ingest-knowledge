---
title: "About the MS Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-batch-process-form"
---

# About the MS Batch Process Form

Use this form to process batches created in Material Sales.
 You can access this from by selecting File > Batch Process from any of the posting forms
 in MS.
Once you have specified the month and batch
 to process, the Info section of the screen displays the batch’s creator and creation
 date, the batch source, and the batch’s status, which is typically “open”.

## Audit Reports

The next step in batch processing is to validate the information in the batch. Do
 this by clicking the Validate button. The form runs through all the data in the
 batch and creates Audit Reports that you can preview and/or print before you proceed
 with posting the batch. It is recommended that you print the audit reports before
 posting a batch; audit reports are no longer available after posting.
Available audit reports for this module:

- Batch List - The name of the
 batch list will differ depending on the batch type (i.e. Ticket Entry Audit
 List, Haul Entry Audit List, Haul Worksheet Audit List, Invoice Audit List,
 etc.). Prints the entries in the batch in sequence order.  As long as
 entries exist in the batch, this report can be printed.

Note: If you are using the surcharges functionality,
 surcharges will only appear on this report after you validate the batch.

- Job Cost Distributions -
 Prints the MS Job Cost Distribution List. Detail shown will differ based
 on the batch type. Some of the information shown may include haul line
 (if haul batch), the phase/cost type, material, U/M, Units, tax code,
 ticket number, GL account, JC unit of measure, units, and unit cost.


- Equipment Usage - Prints the
 MS Equipment Usage Audit List, showing the equipment, from location,
 material, unit of measure, and revenue code, basis, rate, and total.


- Inventory Distributions -
 Prints the MS Ticket IN Distribution List, showing for each location,
 the transaction number and type, the material, ticket, unit price, sales
 price, stocked and posted unit of measure, stocked and posted units,
 stocked and posted, unit cost, and stocked and posted total cost.

- Auto Production - Prints the
 MS Ticket Production Audit, showing for each production location, the
 transaction number and type, material, inventory location, unit of
 measure, units, unit cost, unit price, and total cost and price.

- Invoice Distributions -
 Prints the A/R Interface Audit List, showing by invoice and invoice
 line, the customer job, customer PO, from location, GL company and
 account, invoice amount, tax code, basis, and total, the discount
 amount, line total, and invoice total.

- General Ledger Distributions
 - The GL distribution list will differ based on the type of batch being
 posted (i.e. MS GL Entry Distribution List, MS GL Invoice Distribution,
 etc.). Prints a list of each GL account that will be updated, along with
 the debit/credit amounts updated to each account.

- Error List - Lists the
 sequence number and the error message for any entries where errors were
 found in the validation process.

Users who have access to batch
 processing forms do not automatically have access to the related audit reports. It
 is recommended that if they will be processing batches, you give them access to the
 related audit reports using VA Report Security. If users do not have access, they
 will receive an error message when trying to preview/print those reports to which
 they do not have access. In addition, if using the ‘Attach Batch Report to HQ Batch
 Control’ feature (assigned in MS Company Parameters), restricted access to one or
 more audit reports will prevent the user from posting the batch.
Once the batch is ready for processing,
 enter the posting date and click the Post button at the bottom of the screen.

## Updates

Updating a batch takes each batch entry and makes all the necessary transaction
 updates. This may involve posting transactions to other modules as well as in MS.
 The following is a list of the updates that occurs when an MS batch posts. You can
 change update settings in MS Company Parameters, Ticket Updates tab.

- JC Interface

- EM Interface

- GL Interface

- IN Sales & Purchases


- IN Auto Production

- AR Interface

Once the batch is ready for processing,
 enter the posting date and click the Post button at the bottom of the screen. The
 system clears all entries and closes the batch.

## About Clearing the Batch

When you create a batch, the system adds
 the data to a batch table and stores it until you are ready to post the batch. Data
 is not updated online; therefore, you can delete it completely without affecting any
 modules, including the module in which you created the batch. To clear a batch table
 of stored data, select ‘Clear Batch’ from the File menu. The system will
 clear/delete all data from the batch. Previously posted transactions added to the
 batch are only cleared from the batch—they are not deleted.
Note: The system creates an audit record each time you
 clear a batch. For information about cleared batches (i.e. user who cleared batch,
 as well as the date and time the batch was cleared), use the VA 'Other Events'
 Statistics report.
The Clear Batch option is disabled if
 the batch’s status is 4 (Posting in Progress). This is to prevent partially updated
 batches from being deleted should the update process be interrupted (i.e. power
 outage, system failure, etc.). When a batch update is interrupted, only a portion of
 the intended updates may occur. If a user later clears the batch, there is no way to
 determine the updated data.

Related information

- [About the MS Move Transactions to Target Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-move-transactions-to-target-form)
