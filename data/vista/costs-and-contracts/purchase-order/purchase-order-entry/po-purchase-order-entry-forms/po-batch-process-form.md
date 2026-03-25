---
title: "PO Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/purchase-order/purchase-order-entry/po-purchase-order-entry-forms/po-batch-process-form"
---

# PO Batch Process Form

Use this form to process batches created in Purchase Order.
Once you have specified the month and batch to process, the Info section of the screen displays the batch’s creator and creation date, the batch source, and the batch’s status, which is typically “open.”
The next step in batch processing is to validate the
 information in the batch. Do this by clicking on the Validate
 button. The form runs through all the data in the batch and creates Audit Reports that
 you can preview and/or print before posting the batch. It is recommended that you print
 the audit reports before posting the batch, as reports are no longer available once you
 post the batch.
Audit reports available for this module:

- Batch List - Prints the entries in the batch in
 sequence order. As long as entries exist in the batch, this report can be
 printed.

- Job Cost Distribution - Prints the JC Distributions
 List for the current batch. Data shown will be based on the batch you are
 processing. For example, if processing a batch of purchase orders, the list will
 show the PO#, vendor, material, current units, committed units and unit cost,
 and phase/CT. If processing a batch of purchase order receipts, shows the
 changes to PO received and backordered units, JC received units and costs, and
 JC committed units and costs.

- Inventory Distribution - Prints the PO IN
 Distribution List (PO Entry) or PO IN Receipts Distribution List PO Receipts
 Entry). Depending on the batch type, information may include vendor, purchase
 order, purchase order item, change units, std unit of measure, location,
 material, and units backorder, received not invoiced, and on order.

- Error List - Lists the sequence number and the error
 message for any entries where errors were found in the validation process. You
 must correct the errors before you can post the batch.

Note: Users who have access to batch processing forms do not
 automatically have access to the related audit reports. It is recommended that if they
 will be processing batches, you give them access to the related audit reports using VA
 Report Security. If users do not have access, they will receive an error message when
 trying to preview/print those reports to which they do not have access. In addition, if
 using the ‘Attach Batch Report to HQ Batch Control’ feature (assigned in PO Company
 Parameters), restricted access to one or more audit reports will prevent the user from
 posting the batch.
Once the batch is ready for processing, enter the
 posting date and click the Post button at the bottom of the
 screen.

- Updating the Batch - When batches are updated, each batch
 entry is processed and the system makes all necessary transaction updates. This
 may involve posting transactions to other modules as well as in PO. The updates
 displayed here are set in PO Company Parameters.

- Clearing the Batch - When you create a batch, the system adds the data to a
 batch table and stores it until you are ready to post the batch. Data is not
 updated online; therefore, you can delete it completely without affecting any
 modules, including the module in which you created the batch. To clear a batch
 table of stored data, select ‘Clear Batch’ from the File menu. The system will
 clear/delete all data from the batch.

- Previously posted
 transactions added to the batch are only cleared from the batch—they
 are not deleted.

- The system creates an
 audit record each time you clear a batch. For information about
 cleared batches (that is, user who cleared batch, as well as the
 date and time the batch was cleared), use the VA 'Other Events'
 Statistics report.

The Clear Batch option is
 disabled if the batch’s status is 4 (Posting in Progress). This is to
 prevent partially updated batches from being deleted should the update
 process be interrupted (i.e. power outage, system failure, etc.). When a
 batch update is interrupted, only a portion of the intended updates may
 occur. If a user later clears the batch, there is no way to determine the
 updated data.

[](/en/vista/vista/costs-and-contracts/purchase-order/setup-and-maintenance/po-setupmaintenance-forms/po-company-parameters-form)PO Company
 Parameters
[](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form)VA Report
 Security
