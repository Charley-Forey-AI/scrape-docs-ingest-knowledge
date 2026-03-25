---
title: "Field Definitions: JB Company Parameters Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form/field-definitions-jb-company-parameters-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form/field-definitions-jb-company-parameters-form"
---

# Field Definitions: JB Company Parameters Form

The following is a list of field descriptions for the JB
 Company Parameters form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  JB Company

 Enter a valid company number (from HQ) for Job Billing processing.

##  Auto Sequence Invoice #

 The Auto Sequence Invoice # checkbox on the JB Company Parameters form.
Select this checkbox to have the system automatically generate invoice numbers. Checking this box enables the Last Invoice Option section for specifying the last invoice option and invoice number.
Do not select this checkbox if you will enter invoice numbers manually.

Related information

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

##  Last Invoice Option

 This section enabled when the Auto Sequence Invoice # option is checked.
 Specify the last invoice number option to use.

- Job Billing - Select this option to use the JB Last Invoice # field (below) to determine the next invoice number to assign to JB invoices.

- Accounts Receivable - Select this option to use the Last Invoice # field in AR Company Parameters to determine the next invoice number to assign to JB invoices.

## JB Last Invoice #

If using the ‘auto-sequence invoice numbers’
 feature, the system updates this field automatically with the last invoice number used in
 JB. When first setting up Job Billing, you can specify a starting invoice number (up to 10
 digits) or leave blank to have invoice numbering begin with ‘1’. Once set up, you should
 not need to edit this field.
Note: Invoice numbers assigned manually do not update this
 field.

##  Allow Changes to Previous and Contract Amounts

 The Allow Changes to Previous and Contract Amounts checkbox on the JB Company Parameters form.
Select this checkbox to allow changes to previous and contract amounts when posting in JB Progress Billing. Contract Units, Contract Amount, Previous Units, and Previous Amount fields are available for input and previous and contract amounts may be changed for existing and/or new invoices. Changes to ‘previous’ amounts only affect the figures that print on invoices. Changes do not update General Ledger, Accounts Receivable, or Job Cost.
 Do not select this checkbox if you do not allow changes to previous and contract amounts. The Contract Units, Contract Amount, Previous Units, and Previous Amount fields (JB Progress Billing) will be skipped and cannot be accessed for input.
Note: You will typically only select this checkbox when first setting up the Job Billing module.

Related information

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

##  Automatic Update of Prev Billed and ChgOrder Amounts...

 The Automatic Update of Prev Billed and Chg Order Amounts on Future Bills checkbox on the JB Company Parameters form.
 Select this checkbox to automatically update the previous amount on all future billings when changes are made to progress and T&M billings. When you change a billing, the system will automatically update the previous billed amounts, as well as the current contract amount and units on all subsequent (future) billings for that contract/customer.
 For progress billings, changes made to approved change order items (in JB Progress Change Order) will update the previous change order additions and deductions. Any manual changes to previous amounts will be recalculated based on the previous and current amounts of the previous billing.
Note: When this option is selected (recommended), it is strongly suggested that you do NOT check the "Allow Changes to Previous and Contract Amounts" option (above).
 Do not select this checkbox if changes made to billings should not automatically update previous amounts, change order adds/deducts, and current contract/contract units. Updates to these values will need to be made manually using the update options in the File menus of the JB Progress Billing and JB T&M Bill Edit forms. When updates are done manually, the system adds the value of the change for the current billing to the current billing's previous amount and recalculates the previous amounts for all subsequent billings.

Related information

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

##  Allow Changes to Progress Bill Data…

 The Allow Changes to Progress Bill Data When Both Progress and T&M Exists checkbox on the JB Company Parameters form.
 Select this checkbox to allow changes to progress billings (in JB Progress Billing) when both progress and T&M billings are used. Because T&M billings are not updated with changes made to a progress billing, this option should only be used if you are not concerned with Progress and T&M billings being out of sync.
Leave this checkbox unselected if you do not allow changes to a progress billing when a T&M billing exists. Instead all changes to progress billings will be made through T&M billings.

Related information

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

##  Flag JC Transactions Not Defined on Template…

 This flag indicates what billing status will be assigned to job cost detail records that do not have a source/cost type defined in a template or are set up with the Bill Flag set to ‘Neither’ in JC Phase Cost Types.
 Check this box to mark detail records as ‘unbillable’ (status 2). Records with this billing status will not be available for future billing even if you define a source/cost type on a template later or the bill flag in JC Phase Cost Types is changed. These records will appear on an error report for review on this billing but will not be included in the invoice.
 Leave this box unchecked if you do not want detail records assigned a billing status. Records will appear on the error report but will not be included in the invoice. If you do not change the Bill Flag in JC Phase Cost Types or the template to include these records, they will continue to come up on future invoices as errors.
 It is recommended that all sources and cost types be defined in the templates, even if they are defined as non-billable (typically Burden). If you commonly have phase/cost types that are non-billable but specific to a job, checking this flag will keep them from coming up on each billing.

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

## Suppress $ 0 bill item lines when Interfacing to AR

The Suppress $ 0 bill item lines when Interfacing to AR checkbox on the JB Company Parameters form, Info tab.

Select this checkbox if you do not want bill item lines with a zero (0.00) amount sent to AR during the interface process.
If not selected, all bill item lines, including those with zero amounts, will be sent to AR during the interface process.

## Use Review and Approval Workflow

The Use Review and Approval Workflow checkbox on the
 JB Company Parameters form.
Select this checkbox to enable the review and approval workflow for Progress
 and T&M billings. Selecting this checkbox enables the Review Level drop-down below, as well
 as the Review Level and JB Reviewer
 Group fields in JB Contract Info, JC Contracts, and PM
 Contracts.
Clear this checkbox if you are not using the review and approval workflow for Progress and T&M billings.

## Review Level for AR Interface

The Review Level for AR Interface drop-down on the JB Company Parameters form.
This field is enabled only when the Use Review and Approval Workflow
 checkbox (above) is selected.
From the drop-down, select the review level.


- 0 - Any

- 1 - Ready for Review

- 2 - Draft Approved

- 3 - Sent to Customer

- 4 - Approved for Billing

The option selected here determines the minimum level of the review process
 that is required to interface billings to Accounts Receivable. For example, if you
 select 3 - Sent to Customer
 here, you must select the Sent to
 Customers or Approved for
 Billing checkbox for the selected billing (in JB Progress Billing or JB
 T&M Billing) before you can interface that bill. If you select the Ready to Review or Draft Approved checkboxes, that
 billing will not be available for selection in JB Interface.
Note: You can override the Review Level by contract in JB
 Contract Info, JC Contracts, or PM Contracts. However, because these three forms
 share a table, updating the Review Level in one form automatically updates the
 Review Level in the other two forms

## Certify Progress Billing Claims

(AU) The Certify Progress Billing Claims checkbox on the JB Company Parameters form.
This checkbox only displays if you have
 Australia set up as your default country in HQ Company Setup (Default Country
 field).
Select this checkbox to enable the
 certification process for progress billing claims in JB Progress Billing. When you check
 this box, the system enables the Certified, Claim Date, and Certify Date fields on the Info
 tab of JB Progress Billing. For more information, see About Certifying Billings.
Note: Additional fields (Units Claimed and Amount Claimed)
 are available on the Items tab for tracking/certifying claimed amounts. However, these
 fields are initially hidden and must be set to ‘Show in Grid’ using the Field Properties
 (F3) form.
Leave this box unselected if you are not
 tracking and certifying claimed amounts.

Related information

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

## Progress Bills Invoice Format

The Progress Bills Invoice Format field on the JB Company Parameters form, Info tab.

Enter the custom or standard invoice report to use when delivering progress invoices (via JB Invoice Delivery) for this company. Press F4 to select from a list of valid reports.
Note: The value entered here must be the exact title name of the report; therefore, it is recommended that you use the F4 lookup to specify the invoice format.

### Invoice Format Overrides

You can override the progress bill invoice format at the customer level (in AR Customers) and/or contract level (in JC Contracts) if the customer or contract requires a different invoice format than the one specified at the company level.
When delivering progress invoices, the system automatically defaults the invoice format defined for the Job Billing company. If you specify an invoice format at the customer level, the invoice format specified for the customer overrides the format specified for the JB company. If you also specify a format for a contract associated with the customer, the contract's invoice format overrides the customer format for any invoice associated with that contract.
If no invoice format is defined at the company, customer, or contract levels, the system will not know what format to use and therefore, will be unable to deliver invoices.

Related information

- [Set Invoice Delivery Options](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-invoice-delivery-options)

## T&M Bills Invoice Format

The T&M Bills Invoice Format field on the JB Company Parameters form, Info tab.

Enter the custom or standard invoice report to use when delivering T&M invoices (via JB Invoice Delivery) for this company. Press F4 to select from a list of valid reports.
Note: The value entered here must be the exact title name of the report; therefore, it is recommended that you use the F4 lookup to specify the invoice format.

### Invoice Format Overrides

You can override the T&M bill invoice format at the customer level (in AR Customers) and/or contract level (in JC Contracts) if the customer or contract requires a different invoice format than the one specified at the company level.
When delivering T&M invoices, the system automatically defaults the invoice format defined for the Job Billing company. If you specify an invoice format at the customer level, the invoice format specified for the customer overrides the format specified for the JB company. If you also specify a format for a contract associated with the customer, the contract's invoice format overrides the customer format for any invoice associated with that contract.
If no invoice format is defined at the company, customer, or contract levels, the system will not know what format to use and therefore, will be unable to deliver invoices.

Related information

- [Set Invoice Delivery Options](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-invoice-delivery-options)

## JB T&M Template

Specify the T&M template (from JB T&M Template Setup) to use as a
 default when entering new contracts with a bill type of “T&M” or “Both.” Once a
 contract is set up and saved in JC Contracts, this template will default into the 'T&M
 Template' field in JB Contract Info.
This template will also default for existing
 contracts modified in JC Contracts, where the contract's bill type is 'T&M' or 'Both',
 and no T&M template is assigned to the contract in JB Contract Info.

##  Audit Options

 The Audit Options section on the JB Company Parameters form.
The audit options determine when new records of changes are added to the HQ Master Audit (HQMA) database table. For example, if you change a setting on the company parameters form, the system creates a new record of the change in the HQMA table.
You can view records in the HQMA table using the HQ Audit Detail report in the
 HQ module. See [View the Audit Log](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/maintenance/view-the-audit-log) for more information about viewing audit records in the HQMA
 table.
The following list describes the audit options.

- Company Parameters – (JB Company Parameters) This option is always checked and is disabled. Any changes made to the JB Company Parameters program will be tracked in the Master Audit file.

- JB Bill – Check this box if you want to track changes made to the bill header and items in JB Progress Billing, and to the bill header on T&M billings.

- JB Template – Check this box to track changes made to T&M templates.

Note: When setting up a company, the entry of invalid data in certain fields will cause a warning; however, entries will be allowed and the record can be saved. This primarily applies to (but is not limited to) required data such as the “interface to” companies and journals, since it is sometimes necessary to set up company information before setting up the data being requested.

Related information

- [JB Company Parameters Form](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form)

## From Address

From Address field on the JB Company Parameters form, Email Settings tab.

Enter the email address to use as the reply email address.
 You can enter multiple email addresses if needed; however, you must separate them with a semi-colon. For example, jane.doe@email.com; johnd@email.com; joe.smith@email.com.

## Subject

Subject field on the JB Company Parameters form, Email Settings tab.

Enter the text that should appear in the Subject line of the email. Up to 60 characters allowed.

## Body

Body field on the JB Company Parameters form, Email Settings
 tab.

Enter the text that will appear in the body of the email. You can format your email text using the text-formatting toolbar above this field.

## Restrict Bill Changes By User

Restrict Bill Changes By User checkbox on the JB Company
 Parameters form, Bill Control Options tab.
Select this checkbox to limit which users are allowed to edit or delete bills
 assigned to other users. Only the users assigned to the role entered in the All Bills Access Role will be able to
 edit or delete bills assigned to any user.
This setting is optional and enforced per JB Company.
Note: Individual users can still add, edit,
 or delete any bills assigned to themselves (identified in the Assigned To field on JB Progress
 Billing or JB T&M Bill Edit), even if they are not part of this role.

For more information about configuring this setting, see [Set Bill Controls to Restrict Changes to Bills Assigned to Other
 Users](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-assigned-to-other-users).

## All Bills Access Role

All Bills Access Role field on the JB Company Parameters form,
 Bill Control Options tab.
Enter a role. Users assigned to this role have permissions to add, edit, or
 delete any bill (Progress or T&M) created by any user in that JB Company.
The role must be an active HQ Role. Select F4
 to open the lookup and choose a role from the list. To set up a new role and assign
 specific users to it, select F5 to launch the HQ Roles form. See
 [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) for details.
Alternatively, you can leave this field blank (with Restrict
 Bill Changes By User selected) if you want to prevent all users in your
 JB company from being able to access any other user's JB bills.
Note: Even if users are not assigned to this
 All Bills Access Role:


- Individual users can still add new bills, as well as edit or delete any
 bills assigned to themselves (identified in the Assigned To field on JB
 Progress Billing or JB T&M Bill Edit).

- Users can still interface open month bills.

For more information about configuring this setting, see [Set Bill Controls to Restrict Changes to Bills Assigned to Other
 Users](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-assigned-to-other-users).

## Closed Mth Bill Control

Closed Month Bill Control checkbox on the JB Company
 Parameters form, Bill Control Options tab.
Select this checkbox to limit which users are allowed to add, edit, or delete
 bills in a closed month. Only the users assigned to the role entered in the Closed Mth Bill Access Role will be
 able to add, edit, or delete bills in closed JB months.
This setting allows you to close the month in JB independent of the
 last month closed in GL. The setting is optional and enforced per JB Company.
If you select this checkbox to enable this setting, you must enter a value in [Last Month Closed](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/jb-company-parameters-form/field-definitions-jb-company-parameters-form#concept-5zexam3e--en).
For more information about configuring this setting, see [Set Bill Controls to Restrict Changes to Bills in Closed
 Months](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-in-closed-months).
For more details about making changes to closed-month billings, see [About Changing Interfaced or Closed-Month Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings).

## Last Month Closed

Last Month Closed field on the JB Company Parameters form,
 Bill Control Options tab.
If Closed Mth Bill
 Control is selected, this Last Month Closed field is required and defaults to the closed month
 entered for the AR subledger.
You can also manually update this field as needed. Enter a month in
 the field to close that month, which stops the entry of new invoices and prevents
 further changes in Job Billing for that month. Only users assigned to the Closed Mth Access Role will be able
 to add, edit, or delete bills assigned to them in the month entered here.
The month you enter can be the current month, as this would allow your
 accounting team time to finish tasks while the AR Subledger and General Ledger remain
 open, but without having to account for new JB invoices. In other words, this
 Last Month Closed in JB may be different from the last month
 closed in GL.
When the GL Month End Close process is run for your company, if the month
 closing in the AR subledger is more recent (greater) than the close month entered here
 in JB, this Last Month Closed
 value will automatically update to match the closing AR month.

## Closed Mth Bill Access Role

Closed Mth Bill Access Role field on the JB Company Parameters
 form, Bill Control Options tab.
Enter a role. Users assigned to this role have permissions to add new
 bills, as well as edit or delete existing bills (Progress or T&M) in that JB Company
 after the JB month is closed.
The role must be an active HQ Role. Select F4 to open the lookup and
 choose a role from the list. To set up a new role and assign specific users to it,
 select F5 to launch the HQ Roles form. See [HQ Roles Form](/en/vista/vista/administration/headquarters/role-setup/hq-roles-form) for details.
Alternatively, you can leave this field blank (with Closed Mth Bill Control selected) if
 you want to prevent all users in your JB company from being able to create, edit, or
 delete bills in closed JB months.
Note: As long as the AR Subledger month is
 open, users can still interface closed-month bills even if they are not assigned to
 a Closed Month Bill Access Role.If the
 bill was created in a closed month but was interfaced to AR after the AR
 Subledger was closed, that bill will be posted in the first open month in
 AR.

For more information about configuring this setting, see [Set Bill Controls to Restrict Changes to Bills in Closed
 Months](/en/vista/vista/costs-and-contracts/job-billing/setup-and-maintenance-of-job-billing/set-up-job-billing/set-bill-controls-to-restrict-changes-to-bills-in-closed-months).
For more details about making changes to closed-month billings, see
 [About Changing Interfaced or Closed-Month Billings](/en/vista/vista/costs-and-contracts/job-billing/billing/progress-billing/about-changing-interfaced-or-closed-month-billings).
