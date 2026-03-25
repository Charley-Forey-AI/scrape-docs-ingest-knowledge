---
title: "Field Definitions: GL Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form/field-definitions-gl-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/general-ledger/gl-setup-and-maintenance/about-the-gl-company-parameters-form/field-definitions-gl-company-parameters-form"
---

# Field Definitions: GL Company Parameters Form

The following is a list of field descriptions for the GL
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  GL Company

 Enter a valid company number. It must be set up in HQ Company Setup before you can set it up here.

##  Consolidated Company

 Check this box if this company will be used to consolidate account balances for financial statements.
 Leave this box unchecked if this company will be a working detail GL company with interfaces from various sub ledgers.

##  Last Month Closed

Sub Ledgers
 Displays the last calendar month closed in the Accounts Payable, Accounts Receivable, and All Other Sub Ledgers. The system automatically updates these fields when you close a month in GL Month End Close for the selected sub ledgers, and may not be changed once the transactions have been posted.
 During implementation, it is recommended that you set these fields to two months before the month that you plan to go live on the system. This allows you to enter balances up to the month before you will go live and then begin entering live data into the next month.
General Ledger
 Displays the last calendar month closed in GL. This period is always equal to or older than the period indicated for sub ledgers The GL Month End Close automatically updates this field and it may not be changed once transactions have been posted. It is recommended that you set the last month closed to be the last month of the prior fiscal year-end.

##  Max # of Open Months

 Indicate the maximum number of months beyond the last one closed in the subsidiary ledgers to which entries may be posted in the General Ledger. It is recommended that you enter a minimum of 2 in this field, and never more than 24. This field can be changed as necessary.

## Audit Options

The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following is a detailed list of the audit options.

- Company Parameters—Company Parameters will always be checked. Any changes to the Company Parameters form will be tracked in the Master Audit table.

- Accounts—Check this box to record changes made using GL Accounts.

- Auto Journal Entries—Check this box to record changes made using GL Auto Journal Entries.

- Account Balances—Check this box to record changes to Prior Years GL Account Balances and any year’s Beginning Balance using GL Prior Years Activity and GL Beginning Balances.

- Monthly Budgets—Check this box to record changes to Monthly Budgets using GL Budgets.

- Transaction Detail—Check this box to record details when posting transactions using GL Auto Journal Entry, GL Auto Reversal Entry, and GL Journal Transaction Entry.

##  Allow Unbalanced Entries

 Check this box to allow unbalanced journal entries. You will typically only need to check this box if there is a problem that creates a need to make one-sided entries to bring the GL back in balance.
 Leave this box unchecked to require all journal entries to be balanced.

##  Allow Interco GL Jrnl Entries

 Check this box to allow posting intercompany journal entries in GL Journal Transaction Entry. When checked, the "To Co" input (in GL Journal Transaction Entry) is enabled, allowing you to specify the company to update with the journal entry.
 Leave this box unchecked if you will not be posting intercompany journal entries.

## Attach Batch Reports to HQ Batch Control

The Attach Batch Reports to HQ Batch Control checkbox on the Company Parameters form
 for each module.
Select this check
 box to save batch (audit) reports and attach to the batch record when posting a batch.
 During the batch process, the system converts the related batch reports to a PDF file and
 attaches them to the HQ Batch Control record. The system stores the reports using the
 Attachment Storage Location and Subdirectory Structure parameters defined in DM Attachment
 Options. You can retrieve the reports later using the HQ Batch Control form (just enter the
 month and batch ID and click on the Attachments button).

- The system attempts to convert and attach batch reports before posting the batch. If the attempt is successful, the system posts the batch. However, if errors occur for any batch report, the system displays an error message and aborts the posting process. You must correct the errors before you can re-validate and post the batch.

- Because you can secure audit reports (in VA Report Security), access to attachments generated through this process is restricted to HQ Batch Control. If you have secured the HQ Batch Control form, users can only access batch reports if they have access to HQ Batch Control. Unlike regular attachments, indexes are not created for batch report attachments and you cannot access them using DM Attachment Search.

Do not select this checkbox if you do not want to save batch reports and attach them to HQ Batch Control records. Although not required, it is recommended that you print batch reports before posting the batch.

## Document Type

The Document Type field on the GL Company Parameters form, Workflow tab.

 Specify the type of document to which the workflow applies. Currently, PO-Purchase Order is the only option available.Note: You can have only one process for each document type.

Note: The workflow defined here overrides those defined in HQ Company Setup.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Process

The Process field on the GL Company Parameters form, Workflow tab.
Enter the workflow process to perform on purchase orders or press F4 to select from a list of valid workflows. Valid workflows are those that are associated with the PO-Purchase Order document type or those that do not specify a document type.Note: When you create a workflow (in [WF Workflow Process](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)), you will generally assign it to a specific document type. However, you may have generic workflows that are not associated with a specific document type (that is, the Document Type field is blank). You can assign these generic workflows to PO document types if applicable.

Note: The workflows defined here override those defined in HQ Company Setup.

For more information about the Workflow Process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Active

The Active checkbox on the GL Company Parameters form, Workflow tab.

Select this checkbox if this workflow should be applied when new POs are created.
For more information about the workflow process feature, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow).

## Notes

The Notes field on the GL Company Parameters form, Workflow tab.
Enter any notes about the workflow.
Add a Standard NoteStandard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
You can insert a standard note into the field using either of the following methods:

- Right-click the mouse while focus is in the field and select Standard Notes from the shortcut menu, which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

- If the Standard Notes option is not available from the shortcut menu, double-click in the Notes field to open the Grid Notes form. Then select Standard Notes from the shortcut menu or select the Standard Notes button in the toolbar. which opens the Std Note Copy window. Then enter the standard note to copy (or choose from F4 lookup) and select OK to insert the note.

Spelling CheckSelect the Spelling icon on the toolbar or select Tools > Spelling  to spell check the text in this field.
