---
title: "Field Definitions: CM Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-company-setup/about-the-cm-company-parameters-form/field-definitions-cm-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/accounting/cash-management/set-up-and-maintain-cash-management/cm-company-setup/about-the-cm-company-parameters-form/field-definitions-cm-company-parameters-form"
---

# Field Definitions: CM Company Parameters Form

The following is a list of field descriptions for the CM Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## CM Company

Enter a valid company number. Companies must first be set up in Headquarters.

## GL Co#

Enter a valid GL company to which to post/validate entries.
Note: Once you have set up accounts (CM Accounts), the GL company cannot be changed.

##  Journal

 Enter the journal that will accumulate any transactions posted from CM to GL. The corresponding description will display.

## GL Interface Level

Indicate the level of detail that will be sent to GL when posting entries from CM adjustments or transfers. If on the Info tab, select

- No update—Do not update the General Ledger.

- Summary—Create summary entries for each affected GL account code in a batch. Enter the description that will be used for each of these transactions in the Summary GL Description field below. Also select items for the detail description (using the Info tab). Even though summary is chosen here, if a GL account is set up in the Chart of Accounts to interface detail, then that account will receive detail entries.

- Detail—Create GL transactions for each CM transaction in a batch. In the ‘Select Available Items for Detail’ box (on the Info tab), highlight each of the details to include in the GL transaction description. As you highlight an item, it is added to the description line to the right. When posting the transactions, the system will extract this data to create the transaction description.

##  Summary GL Description

 Enabled only when GL Interface Level is ‘Summary’.
 Enter the description that will be used for each transaction posted from CM to GL.

##  Select Available Items for Detail Level GL Descriptions

 Select each of the items you want included in the detail level description for each transaction posted to GL. As items are selected, they are added to the description displayed to the right. Select items in the order you want them to appear in the description.

## Audit Options

The audit options determine when new records of changes are added to the HQ Master
 Audit (HQMA) database table.
For
 example, if you change a setting on the company parameters form, the system creates a new
 record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the HQ module. See [About Viewing the Master Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA table.
The following is a detailed list of the audit options.

- Company Parameters — CM Company Parameters. This option will always be checked and disabled.

- CM Accounts — Check this box to keep an audit trail of changes made using the CM Accounts form.

- Transaction Detail — Check this box to keep an audit trail of transactions created using the CM Outstanding Entries, CM Transfers.

Note: When setting up a company, the entry of invalid data in certain fields will cause a warning; however, entries will be allowed and you will be able to save the record. This primarily applies to (but is not limited to) required data such as the ‘interface to’ companies and journals, since it is sometimes necessary to set up the company information before you can set up the data being requested.

## Allow Changes to Statement Beginning Balance

Check this box to allow beginning balances to be overridden when setting up a new statement. This box should be checked when first implementing Cash Management, but unchecked after normal processing has begun. The beginning balance of each new statement will automatically be updated with the ending balance of the prior statement.

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

## Notes

Use this tab to enter any miscellaneous notes about this item. The space allowance is
 virtually unlimited.

### Spelling Check

 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.

### Add a Standard Note

Standard notes allow you to insert
 frequently used text into some fields in the application. This text is created and
 maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard
 Notes from the shortcut menu, which opens the Standard Note Copy window.
 Then enter the standard note to copy (or select from F4 lookup) and click OK. The
 system inserts the selected note into the field.
