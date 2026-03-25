---
title: "About the CM Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/processing/transaction-entry/about-the-cm-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/processing/transaction-entry/about-the-cm-batch-process-form"
---

# About the CM Batch Process Form

The CM Batch Process form is used to process CM batches. You can access the CM Batch Process form from the main menu or by selecting the Process Batch option
 from the File menu of any of the posting programs in CM (CM Outstanding Entries and CM
 Transfers).
Once you have specified the month and batch to process, the Info section displays information about the batch (i.e. creator, creation date, source, and status).

## Audit Reports

The next step in batch processing is to
 validate the information in the batch. This is done by clicking on the Validate
 button. The program runs through all of the data in the batch and creates Audit
 Reports that you can preview and/or print before you proceed with posting the batch.

- Batch List
 — Prints the CM Outstanding Entry Audit List or CM Transfers
 Audit Lists, depending on the batch source (i.e., the posting form). Shows
 related information for each entry in the batch, with totals by account and
 batch.

- GL Account
 Distribution — Prints the CM GL Outstanding Entries
 Distribution List or CM GL Transfer Distribution Lists, depending on the
 batch source. Shows distribution information from the batch by GL account.

- Error
 List — Lists the sequence number and the error message for
 any entries where errors were found in the validation process. Errors must
 be corrected before the batch can be posted.

It is recommended that you print the
 audit lists before posting a batch, because once the batch is posted, the audit
 lists are no longer available.
Note: Users who have access to batch processing forms
 do not automatically have access to the related audit reports. It is recommended
 that if they will be processing batches, you give them access to the related audit
 reports using VA Report Security. If users do not have access, they will receive an
 error message when trying to preview/print those reports to which they do not have
 access. In addition, if using the ‘Attach Batch Report to HQ Batch Control’ feature
 (assigned in CM Company Parameters), restricted access to one or more audit reports
 will prevent the user from posting the batch.
For information about setting up
 security for audit reports, see [VA Report Security Form](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form#ID-000494c6--en__ID-000494c6).

## Updates

Updating a batch is the process that
 takes each batch entry and makes all the necessary transaction updates. This may
 involve posting transactions to other modules as well as in CM. The following is a
 list of the updates that occur when an AR batch is posted.

- GL Interface — Displays the
 interface option selected in the CM Company Parameters form.

- Journal — Displays the journal
 to which these distributions will be posted.

Once the batch is ready for processing,
 enter the posting date and click the Post button at the bottom of the screen. After
 all the entries have been successfully updated, the entries are cleared and the
 batch is closed.

## Clearing the Batch

When you create a batch, the system adds
 the data to a batch table and stores it until you are ready to post the batch. Data
 is not updated online; therefore, you can delete it completely without affecting any
 modules, including the module in which you created the batch. To clear a batch table
 of stored data, select ‘Clear Batch’ from the File menu. The system will
 clear/delete all data from the batch. (Note: Previously posted transactions added to
 the batch are only cleared from the batch—they are not deleted.)
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
