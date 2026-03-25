---
title: "About the GL Batch Process Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-batch-process-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-journals/about-the-gl-batch-process-form"
---

# About the GL Batch Process Form

Use the GL Batch Process form to process General Ledger
 batches.
You can access the GL Batch Process form from the main menu
 or by selecting File > Process Batch in any of
 the posting programs in GL (GL Auto Journal Entry, GL Auto Reversal
 Entry, and GL Journal Transaction Entry).
Once you specify the month and batch to process, the Info
 section displays information about the batch (i.e.
 creator, creation date, source, and status).

## Audit Lists

The next step in batch processing is to
 validate the information in the batch.
This is done by clicking on the Validate button.
 The program runs through all the data in the batch
 and creates Audit Reports that you can preview
 and/or print before you proceed with posting the
 batch. It is recommended that you print the audit
 lists before posting a batch, because once the
 batch is posted, the audit lists are no longer
 available.

- Batch List — Prints the GL
 Journal Entries Audit List, GL Auto Entry Batch
 Audit List, or GL Reversal Batch Audit List,
 depending on the batch you are processing. Shows
 related information for each entry in the batch.


- GL Account Distribution —
 Prints the GL Journal Entries Distribution List,
 GL Auto Entry Distribution List, or GL Reversal
 Entries Distribution List, depending on the batch
 you are processing. Shows distribution information
 from the batch sorted by account.

- Error List — Lists the
 sequence number and the error message for any
 entries where errors were found in the validation
 process. Errors must be corrected before the batch
 can be posted.

Note: Users who
 have access to batch processing forms do not
 automatically have access to the related audit
 reports. It is recommended that if they will be
 processing batches, you give them access to the
 related audit reports using VA Report Security. If
 users do not have access, they will receive an
 error message when trying to preview/print those
 reports to which they do not have access. In
 addition, if using the ‘Attach Batch Report to HQ
 Batch Control’ feature (assigned in GL Company
 Parameters), restricted access to one or more
 audit reports will prevent the user from posting
 the batch.
Once the batch is ready for processing, enter the
 posting date and click the Post button at the
 bottom of the screen.

## Clearing the Batch

When you create a batch, the system adds the
 data to a batch table and stores it until you are
 ready to post the batch.
Data is not updated online; therefore, you can
 delete it completely without affecting any
 modules, including the module in which you created
 the batch. To clear a batch table of stored data,
 select ‘Clear Batch’ from the File menu. The
 system will clear/delete all data from the batch.
 (Note: Previously posted transactions added to the
 batch are only cleared from the batch—they are not
 deleted.)
Note: The system
 creates an audit record each time you clear a
 batch. For information about cleared batches (i.e.
 user who cleared batch, as well as the date and
 time the batch was cleared), use the VA 'Other
 Events' Statistics report.
The Clear Batch option is disabled if the batch’s
 status is 4 (Posting in Progress). This is to
 prevent partially updated batches from being
 deleted should the update process be interrupted
 (i.e. power outage, system failure, etc.). When a
 batch update is interrupted, only a portion of the
 intended updates may occur. If a user later clears
 the batch, there is no way to determine the
 updated data.
