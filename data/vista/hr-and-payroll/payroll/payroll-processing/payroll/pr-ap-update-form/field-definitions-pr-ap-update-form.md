---
title: "Field Definitions: PR AP Update Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-ap-update-form/field-definitions-pr-ap-update-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-ap-update-form/field-definitions-pr-ap-update-form"
---

# Field Definitions: PR AP Update Form

The following is a list of field descriptions for the PR AP
 Update form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  PR Group

 Enter the PR Group.

##  Pay Period Ending Date

 Enter the pay period ending date that, when combined with the PR Group, identifies a closed pay period that has not been interfaced with AP. Initially defaults the last accessed pay period for the current user.

## Restrict by Payment Month

Check this box to limit the deductions and liabilities that will be interfaced. For example, if checks were posted to both November and December in a single pay period, and you want to update the deductions and liabilities for the November payments into a separate AP batch, restrict the payment month to 11/XX. You could then rerun this update later and select 12/XX as the payment month to create a new AP batch to process the December payments.
If you make multiple AP updates for a single pay period, be careful how you specify restrictions. For example, if you made the November update and then reran for December, but did not restrict the payment month, the form re-updates the November amounts. The form recalls that those November payments were updated to AP in November and creates a batch of November reversing transactions. Then, it adds new entries to the December batch for ALL payments made in either November or December. If you make this type of mistake, your best solution is to manually edit the AP batches from the AP Entry form, but remember that PR still considers all updates to have been made in December.

##  Include Deductions/Liabilities on Payments Made In

 If the Restrict by Payment Month box is selected, then enter the payment month here.

##  Restrict by Frequency Code

 Select this box to restrict the deductions and liabilities interfaced to AP by frequency code. Use the selection box to select the frequency code by which to limit the deductions and liabilities interfaced to AP. For example, if you want to interface some deductions ahead of others (e.g., taxes may need to be done faster than union dues), then you can control this here.

##  CM Account Override

 Enter a CM account number for AP transactions. This number overrides either the account
 number you specified in the CM Account field in AP Vendors or the account you specified in
 AP Company Parameters (CM Account # field, Subledgers tab).

##  Expense Month

 Enter the expense month that will be used to create AP transactions. It must be equal to or later than the employee’s payment month. If the payment month is not restricted, then any employee/pay sequence paid later than the expense month is automatically skipped.

##  Invoice Date

 Enter an invoice date, that will be used for all AP transactions created with this batch. For AP transactions created with this batch, all discount and due dates default based on the vendor’s payment terms; AP Reference, Hold Code, and Payment Control will be blank.

## Create Restricted AP Batch

 Check this box if you want to create a restricted batch when updating AP with the pay period entries. If checked, a restricted batch is created in AP and only the ‘creator’ has access to the batch.
 Do not check this box if the AP batch created by this update should not be restricted. If unchecked, any user has access to the AP batch.
