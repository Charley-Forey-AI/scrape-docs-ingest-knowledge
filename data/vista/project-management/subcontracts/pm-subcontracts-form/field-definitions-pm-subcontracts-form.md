---
title: "Field Definitions: PM Subcontracts Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/project-management/subcontracts/pm-subcontracts-form/field-definitions-pm-subcontracts-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/project-management/subcontracts/pm-subcontracts-form/field-definitions-pm-subcontracts-form"
---

# Field Definitions: PM Subcontracts Form

The following is a list of field descriptions for the PM
 Subcontracts form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Project

Enter a project number or press F4 to select
 one from a list.
If you enter a project with a closed status
 (hard or soft), the status displays in red to the right of the project description. You
 will only be able to add or modify subcontracts for the project if you allow posting to
 hard- and/or soft-closed jobs (flags in JC Company Parameters checked).
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Subcontract

The Subcontract field on the PM Subcontracts form, header section.
Enter +,
 N, or NEW to have the system
 automatically assign the next available subcontract number. The system generates a
 subcontract number based on the Subcontract Format Options selected in PM Company
 Parameters. For more information about subcontract numbers, see [About Subcontract, PO, and MO Number Formats](/en/vista/vista/project-management/setupmaintenance/about-subcontract-po-and-mo-number-formats).
You can also manually enter a subcontract number that has not already been used. You can
 enter up to 30 characters and use any format you want; however, it is recommended that
 you use the subcontract number format defined in PM Company Parameters.
Note: If you export subcontract information to Textura using the SL Textura Subcontract
 Export and SL Textura Subcontract Compliance Export reports, you must limit your
 subcontract numbers to 20 characters. Textura allows a maximum of 20 characters for
 subcontract numbers; subcontract numbers that exceed 20 characters are truncated
 during the export.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Description

Enter the description of the subcontract. This field can be up to 60 characters long.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Document Type

 Use this field to categorize the subcontract
 that you are creating. Press F4 to select a document type from a
 list.
Document types are created and maintained using the [PM Document Types ](/en/vista/vista/project-management/setupmaintenance/pm-document-types-form) form.
Required when using 'Send with Transmittal'
If you select  >  Send with
 transmittal, a document type must be selected in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create & Send feature.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Vendor

Enter the vendor number of the vendor associated with the subcontract
 or press F4 to select it from a list. You can only select a vendor that is set up in the
 [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form) form.
Note:If you are manually adding a subcontract and the
 vendor you specify has an 'inactive' status, a warning displays indicating that the
 vendor must be active. You will be unable to save the record until specify an active
 vendor or change the inactive vendor's status to active (in AP Vendors).

If the subcontract was created with an
 inactive vendor in PM Subcontract Detail, you will need to either specify an active vendor
 or change the inactive vendor's status to active (in AP Vendors) before the subcontract can
 be interfaced.

##  Hold Code

 Enter a hold code (from HQ Hold Codes) for this subcontract, if applicable.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Pay Terms

 Press F4 to select the payment terms of the subcontract. Payment terms are created and
 maintained using the [ HQ Payment Terms ](/en/vista/vista/administration/headquarters/payment-terms-setup/about-the-hq-payment-terms-form) form.
 This field will default based on the payment
 terms set up on the selected vendor. Payment terms are set up on a vendor using the Payment
 Terms field on the Info tab of the [AP Vendors ](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form) form.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Comp Group

If tracking compliance for this subcontract, enter the compliance group that will be used to initialize compliance codes for this subcontract in SL. Initially defaults to the compliance group specified in [PM Projects](/en/vista/vista/project-management/projects-and-contracts/projects/pm-projects-form).
Compliance groups are created and maintained using [HQ Compliance Groups ](/en/vista/vista/administration/headquarters/compliance-setup/about-the-hq-compliance-groups-form).
Note:Changing the compliance group does not automatically delete existing compliance codes; you will need to manually delete them using SL Compliance Detail (File menu, SL Compliance). To ensure that compliance codes in the new compliance group are updated for the subcontract, you must first delete the current compliance group and save the record. Then add the new compliance group and save the record. All compliance codes not already existing for the subcontract are added; existing compliance codes are left intact.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Start Date

 Specify the start date for this subcontract. This can be the date of the subcontract or the date the work specified on the subcontract is expected to begin.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Approved

The Approved checkbox on the PM Subcontracts form, Info tab.

This checkbox is enabled:

- If you are not using the Process Workflow feature.

- If you are using the Process Workflow feature and the subcontract is fully approved (Workflow Status of Approved) or if the subcontract does not require approval (Workflow Status is Approval Not Required).

Select this checkbox to approve this subcontract. When selected, the By field displays the approver's username.
Note: This checkbox must be selected in order to interface the subcontract (via PM Interface). In addition, the Send checkbox (on the Non-Interfaced tab) must be selected for any subcontract items that you want included in the interface.

Leave this checkbox unselected if the subcontract has not been approved or should not be interfaced with the accounting modules.

### Workflow Process

If you are using the Process Workflow feature, this checkbox is disabled for subcontracts with a Workflow Status of Approval Required, Submitted for Approval,Partial Approval, or Rejected. You can see the progress of a subcontract's review/approval process by selecting the Workflow button.
Once the subcontract is fully approved (all assigned reviewers have reviewed and approved it), the system sets the Approved checkbox to selected, populates the Approved By field with the username of the final approver, and sets the Workflow Status to Approved.
Note: This checkbox is enabled if the Workflow Status is Approved or Approval Not Required.

For more information about the review/approval process, see [Review/Approval Process Workflow](/en/vista/vista/system-tools/work-flow/reviewapproval-process-workflow)

### Unapprove a Subcontract

You can unapprove a subcontract, as long as it is not associated with a subcontract change order (SubCO). If you attempt to unapprove a subcontract that is linked to a SubCO, the system displays an error and prevents you from saving the record.
If you are using the Process Workflow feature, you can unapprove a subcontract in one of two ways:

- You can change, delete, or add non-interfaced items. Once you make changes, the system automatically deselects the Approved checkbox and changes the Workflow Status to Approval Required.

- Reviewers can unapprove a subcontract via the PM Work Center by selecting the purchase order from the Subcontracts query (in the Procurement folder) and then selecting Tasks > Approve/Unapprove. When a subcontract is unapproved with this method, the system deselects the Approved checkbox and sets the Workflow Status to Submitted for Approval.

Note: You can manually deselect this checkbox, but the Workflow Status is only updated if you make changes to the subcontract. Additionally, the 'approved by' field is only cleared if the final approver deselects this checkbox; for all other users, it is left intact.

## Claim Approval Required

This box only applies to the subcontract claims process ([More](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/about-subcontract-claims/process-subcontract-claims)).
When this box is checked, the claim must be
 processed using AP Unapproved Invoice Entry.
When this box is not checked, the claim can be
 processed using either AP Transaction Entry or AP Unapproved Invoice Entry.
Note: This box it is only enabled when a subcontract is pending
 (the SL
 Status field in this form is set to 3-Pending)

## SL Status

The SL Status field on the PM Subcontracts form, Info tab.
This field is display only and shows the status of the subcontract throughout its life cycle.
0-OpenOnce interfaced, the status is updated to 0-Open and no further changes can be made to the subcontract. However, you do have the ability to add new items to an interfaced subcontract
1-CompleteThis status can only be applied to a subcontract via SL Subcontract Entry. Subcontracts with this status cannot be changed or invoiced.
2-ClosedThis status is automatically assigned to subcontracts that are closed using the SL Close form; you cannot manually set a subcontract's status to Closed. Subcontracts with this status cannot be changed or invoiced, but are available for purging via SL Purge.
3-PendingAll subcontracts created in the PM Subcontracts or PM Subcontract Detail forms are automatically assigned this status. They will retain this status until the subcontract is interfaced.

Note: You can restrict the recordset in PM Subcontracts to exclude subcontracts that have been fully interfaced (that is, the header and all items have been interfaced). This is done by selecting the Show Only SL’s with Non-interfaced Detail option in the Options menu. When selected, only subcontracts that have not been interfaced or that have been partially interfaced will display. If not selected, all subcontracts will display regardless of whether they have been interfaced.

## Set WC Maximum Retention

Use this field to select how you would like to set the maximum retention amount.

- None - Select this option if you do not want to set a maximum
 retention amount for the subcontract.

- Percent of Subcontract - Select this option if you want to set the
 maximum retention amount for the subcontract by percentage. When you select this option,
 the system enables the % of Subcontract,  Include Chg Orders in
 Max Retention by %, and the Adjust Maximum Invoice fields.

- Maximum Amount - Select this option if you want to set a flat
 amount for maximum retention. When you select this option, the system enables the
 Retention
 Amount and Adjust Maximum Invoice fields.

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/set-maximum-retention-amounts)Setting maximum retention amounts
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview - Subcontract Buyout
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontracts

## % of Subcontract

The % of Subcontract field on the PM Subcontracts form, Info tab.
This field is only enabled when setting up maximum retention as a percentage of the contract.
Enter the percent of the subcontract amount used to calculate the total retainage allowed. The percentage specified here will be used with the Total Original Subcontract amount or Total Current Subcontract amount (if including change orders in maximum retention) to determine the maximum retention amount.
For example:
Subcontract Totals
Total Original: $550,000
Total Current: $675,000
Maximum Retention Amount
% of Subcontract: 10%
Max Amt by % (Include Chg Orders box unchecked): $55,000 (550,000 x .10)
Max Amt by % (Include Chg Orders box checked): $67,500 (675,000 x .10)
 The system allows retainage to be withheld until the maximum amount (in this example, $55,000 or $67,500) is reached; once this limit is reached, the system will no longer continue withholding retainage for the subcontract.

## Include Chg Orders in Max Retention %

Check this box to include change order amounts in percentage-based maximum retainage calculations. When you check this box, the system calculates the maximum retention amount based on the current subcontract value.
Uncheck this box to exclude change order amounts in percentage-based maximum retainage calculations. The system will calculate the maximum retention amount based on the original subcontract value.
This box is only enabled when Percent of
 Subcontract is selected.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/set-maximum-retention-amounts)Setting maximum retention amounts
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview - Subcontract Buyout
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontracts

## Retention Amount

The system enables this field when you select
 Maximum
 Amount for setting maximum retention amounts.
Enter the maximum retention amount for this subcontract.
[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/set-maximum-retention-amounts)Setting maximum retention amounts
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview - Subcontract Buyout
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontracts

## Adjust Maximum Invoice

Select an option in the drop down. This field
 is only enabled when the Percent of Subcontract or Maximum Amount
 boxes are checked.
Composite Percentage
With this option, the system takes the final retention amount and calculates an overall percentage rate which it applies to all subcontract items equally.
For example, if you have set the maximum retention amount for a subcontract at $10,000, and you have already created invoices with retention amounts totaling $8,000, you will only have $2,000 left before you reach the maximum retention setting.
If you invoice $3,000 retention for two more items, the system will calculate a composite retention percentage and apply it to each item.
Retention Amounts Prior to Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
10%
$1,000

Item #2
$20,000
10%
$2,000

The system uses this calculation to determine the composite retention percentage: Maximum retention remaining ($2,000) / New Invoice Items Total ($30,000) = Composite Retention Percentage (.066666). The system then updates the work complete retention percentage and work complete retention amounts based on the composite retention percentage.
Retention Amounts After Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$10,000
6.67%
$668

Item #2
$20,000
6.66%
$1,332

Item Percentage from Invoice
With this option, the system distributes the final retention amount based on the work complete retainage percent value for each line. The system continues to distribute in this manner until the retention amount is depleted. The system places any leftover amount on one final item on the subcontract, resulting in a calculated retention percentage value for that item only. The system sets the work complete retainage percent to zero for all remaining items on the subcontract.
The tables below display how the system would distribute the retention amount for a subcontract with a maximum retention of $400.
Retention Amounts Prior to Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
10.00%
$300

Item #4
$3,000
10.00%
$300

Retention Amounts After Distribution
This Invoice
Invoice Amount
Retention %
Retention Amount

Item #1
$1,000
10.00%
$100

Item #2
$2,000
10.00%
$200

Item #3
$3,000
3.33%
$100
* Notice how the remaining amount is added to a single subcontract item.

Item #4
$3,000
0.00%
$0

[](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-management/set-maximum-retention-amounts)Setting maximum retention amounts
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview - Subcontract Buyout
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontracts

## Qualified for PBA Reporting?

Qualified for PBA Reporting? checkbox on the PM Subcontracts form, Australia only
This checkbox is selected by default if the contract associated with the project/job is flagged as subject to PBA.

When selected, the system will track and report payment activity when you apply payments against subcontracts (SL Subcontract Claims) and include those payment amounts when computing results for the CM PBA Reconciliation report.

## PBA Eligible Date

PBA Eligible Date field on the PM Subcontracts form, Australia only
Required only if the Qualified for PBA Reporting? checkbox is selected.

Enter the date when the subcontract qualified as subject to PBA tracking and reporting (not necessarily the subcontract start date).

##  Responsible Person

Press F4 to select the person responsible for
 this subcontract from a list.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Send To Firm

Enter the firm that should receive the
 document(s) generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature or press F4 to select a
 firm from a list.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
Drag and Drop
 To drag and drop firms/contacts to the distribution grid, double-click the Distribution tab (label) or select View  >  Project Firms List. This displays the Project Firm Contacts list. You can then select a firm/contact and drag it to the grid.
Note: If you manually add a firm/contact to the grid that is
 not set up for the project, upon saving the record, the system displays a message
 indicating the firm/contact does not exist in PM Firms and gives you the option to add the
 firm/contact. Select Yes to add the firm/contact to the
 distribution list and to PM Firms. Select No to add the firm/contact to the
 distribution grid only.Distribution
 defaults

When creating a new record, the Distribution
 tab will automatically populate with any PM firm contact set up as a distribution default.
For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', you can use the distribution default feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created, that contact will automatically populate on the Distribution tab.
Click [here](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) for more information on distribution defaults.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Send To Contact

Enter the contact that should receive the
 document(s) generated using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature, or press F4 to select
 one from a list. Only contacts associated with the firm selected in the Sent To Firm
 field can be selected.
Contacts are associated with firms using [PM Firm Contacts ](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).
Distribution defaults
When creating a new record, the Distribution tab will automatically populate with any PM firm contact set up as a distribution default.
For example, if a contact at an architecture firm should receive a copy of all drawing logs of document type 'ARCH', you can use the distribution default feature to set up that contact as a default for 'ARCH' documents. When drawing logs of that type are created, that contact will automatically populate on the Distribution tab.
Click [here](/en/vista/vista/project-management/create-and-send/pm-assign-distribution-defaults-form) for more information on distribution defaults.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Send

Check this box if the contact should receive communications generated using the [Create and Send ](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
When this box is not checked, the contact can
 be manually added to a Create and Send email but they will not automatically populate in
 the To,
 Cc,
 or Bcc
 fields on the Message tab of the PM Send Documents form.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
If a communication has already been sent
If this contact was added to an email generated using the Create and Send feature, this box will be checked.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Preferred Method

Use this field to select which type of communication should be sent to the contact when using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature. This field defaults based on the preferred method set up using [PM Firm Contacts](/en/vista/vista/project-management/setupmaintenance/about-the-pm-firm-contacts-form).

- M -Print — Print a hard copy of the generated PDF document(s). When this option is selected, the contact will not receive a copy of the email body text.

- E -Email — Send the generated PDF document(s) using email. The email address of the contact is pulled from the Email field on the Info tab of the PM Firm Contacts form. F -Fax — Send the generated PDF document(s) suing fax. The system will use the fax number set up on the PM Firm Contacts form.
Note:This option requires that you have a fax server set
 up in the Fax Server Name field on the Info tab of [PM Company Parameters ](/en/vista/vista/project-management/setupmaintenance/pm-company-parameters-form).

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Send Type

Select how the contact should be added to the communication generated from the Create and Send feature: To, Cc, Bcc.
When a communication is created using the Create and Send feature (), the contact will automatically be added using the selection in this field.
Click [here](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) for an overview of the Create and Send feature.
If a communication has already been sent
If an email generated using the Create and Send feature has already been sent to the contact, this field will display how the contact was included on the last communication.
For example if the contact was added to an
 email in the To field on the PM Send Documents form, To will display
 in this field. When a new email is created using the Create and Send form, the contact will
 automatically populate in the To field.
"Vendor on firm does not match the subcontract vendor"
The error message above will display if you select
 To
 in the
 Send Type
 field on a contact that is not associated with the vendor on the subcontract (Info tab
 Vendor
 field).
You can only have one
 To
 contact on a subcontract, and that contact must be associated with the same vendor as the subcontract.
If multiple project contacts should receive a
 copy of the subcontract, select Cc in the Send Type field
 on the Distribution tab.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature)Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Date Sent

This field displays the date a communication was sent to the contact using the [Create and Send](/en/vista/vista/project-management/create-and-send/about-the-create-and-send-feature) feature.
If several communications have been sent, the most recent date will display.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Notes

Enter any notes that relate to this contact. You can double click in the field if you need more space to enter information.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
Create and Send - Overview
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Item

Manually enter the subcontract item number, or enter '+', 'n', 'N', or 'New' if you want the system to automatically assign the new item the next available number.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Description

Enter a description for this subcontract item. The value in this field can be up to 60 characters long.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Item Type

Indicate the type of subcontract item.

- 1 = Regular

- 2 = Change Order

- 3 = Backcharge

- 4 = Add-on

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Add-On #

This field is only enabled if '4-Add-on' is
 selected in the Item Typefield.
Specify the add-on to use for this subcontract item. Must be a valid add-on defined in SL Add-Ons.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Phase

 Specify the phase for this subcontract item. For ‘add-on’ items (Item Type ‘4’), defaults the phase specified for the add (in SL Add-Ons), if applicable.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Cost Type

Enter the cost type for this subcontract item. For ‘add-on’ items (Item Type ‘4’), defaults the cost type specified for the add (in SL Add-Ons), if applicable.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Add-On %

This field is only enabled when '4-Add-on' is
 selected in the Item Type field and the add-on type is percent.
Enter the percentage used to calculate the add-on amount for this subcontract item. Initially defaults the percentage specified for the add-on in SL Add-Ons. For negative add-ons, make sure to enter a minus sign (-) in front of the percentage.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Units

Enabled only if Item Type is not ‘4-Add-on’ and UM is not ‘LS’.
Enter the number of units for this subcontract item.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## U/M

Disabled if Item Type is ‘4-Add-on’.
 Specify the unit of measure for this subcontract item. Initially defaults the unit of measure specified for subcontracts in PM Company Parameters (SL Params tab). If ‘add-on’ item, defaults the cost type specified for the add-on (in SL Add-Ons), if applicable.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Unit Cost

Enter the unit cost for this subcontract item.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Amount

Enter the amount for this subcontract item. If UM is not ‘LS’, defaults an amount based on Units x Unit Cost. If you change the default, unit cost will be re-calculated.
For add-on items, defaults an amount based on the add-on type. If the add-on type is Amount, defaults the amount specified for the add-on in SL Add-Ons. If the add-on type is Percent, defaults an amount based on the total of regular and change order items times the specified percentage. For example, if your subcontract total is $15,000, but the total of regular and change order items is 10,000, assuming an add-on percentage of 5% (5.00), the add-on amount would be $500.00.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## SubCO

The SubCO field on the SM Subcontracts form, Non-Interfaced Items tab.
This field is only enabled when a subcontract change order has already been associated with a subcontract item.
Displays the subcontract change order number associated with this subcontract item.
If you wish to remove the subcontract change order, delete the value in this field. This does not delete the subcontract change order; it only removes the subcontract item from the subcontract change order. You can see this if you open the subcontract change order in the PM Subcontract Change Orders form. The subcontract item will no longer display in the lower portion of the form.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Send

 Check this box if this subcontract item is ready to be interfaced. If checked, item will be included when subcontract is interfaced (via PM Interface).
 Leave this box unchecked if this subcontract item is not ready to be interfaced.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Work Complete Retainage %

Enter the work complete retainage percent for the subcontract item. This is used to calculate default retainage amounts on AP invoices or when initializing work complete retainage in the [SL Worksheet](/en/vista/vista/costs-and-contracts/subcontract-ledger/sl-worksheet/sl-worksheet-form) form.
 When creating new subcontract items, this
 field will default based on the phase entered in the Phase field.
How is the default value selected?
The diagram below outlines how the system determines the default value for this field.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Stored Materials Retainage %

 Enter the stored materials retainage percentage. This is used to calculate retainage amounts when initializing stored materials retainage in SL Worksheet.
 When creating new subcontract items, this
 field will default based on the phase entered in the Phase field.
The diagram below outlines how the system
 determines the default value for this field.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Tax Type

Specify the tax type for this subcontract item.

- 1-Sales– Use for tax amounts that are payable to the vendor.

- 2-Use– Use for tax amounts that are accrued and paid later to the appropriate State or Local taxing authority.

- 3-VAT(Value Added Tax) – Use for taxes paid on goods and services.
Default Value

This field initially defaults as follows:

- If the Use default tax code for
 subcontracts box is checked in PM Projects and, the active company's
 Default Country is 'US' (in HQ Company Setup), defaults as 1-Sales. the active
 company's Default Country is other than 'US' (e.g Canada or Australia), defaults as
 3-VAT.

- If the Use default tax code for subcontracts box is unchecked, tax type defaults as null, regardless of country.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Tax Code

Enter the
 tax code for this subcontract item or press F4  to select a tax code from a list.
Tax code defaults as follows:

- If the Use default tax code for subcontracts box
 (PM Projects, Additional Info tab) is checked, the default for this field is determined
 based on the setting in the Base Tax On drop-down field (PM Projects,
 Info tab). If the field is set to J-Job, the tax code defaults from PM
 Projects ( Tax
 Code field). If the field is set to V-Vendor, the tax code defaults from AP
 Vendors ( Tax
 Code field). If the field is set to O-Vendor Override, the tax code defaults
 from AP Vendors. If a tax code is not specified there, the tax code will default from PM
 Projects.

- If the
 Use default tax code for subcontracts
 box is unchecked, tax code defaults as null.

Note:If using
 F4
 to look up valid tax codes, the Tax Type determines the lookup to display. For Sales and Use tax, the standard Tax Codes lookup is used. If the tax type is VAT, the VAT Tax Codes lookup displays.

 Tax codes are created and maintained using the [HQ Tax Codes](/en/vista/vista/administration/headquarters/tax-code-setup/about-the-hq-tax-codes-form) form.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

##  Supplier

 Enter the supplier for this subcontract, if applicable. If a supplier is indicated, a two-party check will be printed when paying on this subcontract in AP Payment Posting.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Sequence

This field will automatically populate with the next available sequence number when creating a new inclusion or exclusion. Double click on a new line in the grid to populate this field, or enter '+', 'n', 'N', or 'New'.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Type

Select either inclusion or exclusion from the drop down menu.

- Inclusion - The work described in the Detail field
 is included in the subcontract.

- Exclusion - The work described in the Detail field
 is not included in the subcontract.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Phase

Enter the phase associated with the
 inclusion/exclusion or press F4 to select one from a list.
[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Detail

Enter detail information about the inclusion/exclusion.
Double click in this field if you are going to enter a lot of information. This will open the Grid Notes form.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Notes

Enter any notes associated with the inclusion or exclusion.
Spelling Check
 Click the Spelling icon on the toolbar or select Tools >  Spelling  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract

## Notes

Enter any miscellaneous notes about this
 subcontract (Notes tab) or subcontract item (Non-Interfaced/Interfaced Items tabs). If
 entering notes for subcontract items, you can double-click in the Notes column
 for additional space in which to write notes. This will bring up the PM Notes window,
 allowing you virtually unlimited space for your notes and information.
Spelling Check
 Click the Spelling icon on the toolbar or
 select Tools > Spelling
  to spell check the text in this field.
Add a Standard Note
Standard notes allow you to insert frequently used text into some fields in the application. This text is created and maintained using the [HQ Standard Note](/en/vista/vista/administration/headquarters/standard-notes/about-the-hq-standard-note-form) form.
To insert a standard note into the field,
 right click the mouse while focus is in the field and select Standard Notes
 from the shortcut menu, which opens the Standard Note Copy window. Then enter the standard
 note to copy (or select from F4 lookup) and click OK. The system inserts the selected note
 into the field.

[](/en/vista/vista/project-management/subcontracts/about-subcontract-buyout)Overview of the Subcontract Buyout Process
[](/en/vista/vista/project-management/subcontracts/pm-subcontracts-form)PM Subcontract
