---
title: "Update Payroll Information to AP | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/update-payroll-information-to-ap"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/update-payroll-information-to-ap"
---

# Update Payroll Information to AP

The following instructions detail how to update AP with
 payroll information using the PR AP Update form.
You will use the PR AP Update form to create a batch of Accounts Payable transactions based on a pay period's deduction and liability amounts, as well as any earnings codes [set for automatic update in PR Earnings Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-united-states/set-up-automatic-ap-updates-united-states).
Once you process a batch in the form, you will be unable to reprocess the batch. If the generated AP batch is cleared, you will need to recreate the information from PR manually in AP. That is why it is important to run the update process once all changes are made to your pay period.

1. Enter the payroll group and period ending date in the PR Group and Pay Period Ending Date fields, respectively. Note: These fields default to the payroll group and period ending date that you last accessed.

1. If you want to restrict the update to a specific payment month, check the Restrict by Payment Month box and enter the month in the Include dedn/liabs on payments made in field.

1. If you want to restrict the update to a specific frequency code, check the Restrict by Frequency Code box and select the code from the selection box. Note: Make sure to highlight the correct frequency code in the selection box or the system will not process any updates.

1. Enter an override CM
 account number in the CM Account Override field if
 you want to override the account for the vendor (CM
 Account field, AP Vendors) or the AP company (CM Account
 # field, AP Company Parameters).

1. Enter the month that the system will use to create AP transactions in the Expense Month field. This month is then associated with the AP batch that the system creates.

1. In the Invoice Date field, enter the date that the system will apply to all AP transactions created in this batch.

1. Check the Create restricted AP batch box if you want to restrict the AP batch so that only your login can access it.

1. Select Post. The system creates an AP batch and displays a confirmation message. Note: During the update process, the system automatically assigns a unique AP reference number to all applicable transactions.

1. Select Close.

1. Repeat steps 1-9 for all additional payroll group and pay period combinations. Once you are finished updating AP, you are done processing your payroll for the current pay period.

Related information

- [PR AP Update Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-ap-update-form)

- [AP Vendors Form](/en/vista/vista/accounting/accounts-payable/vendors/ap-vendor-forms/ap-vendors-form)

- [AP Company Parameters Form](/en/vista/vista/accounting/accounts-payable/ap-company-setup/ap-company-setup-forms/ap-company-parameters-form)
