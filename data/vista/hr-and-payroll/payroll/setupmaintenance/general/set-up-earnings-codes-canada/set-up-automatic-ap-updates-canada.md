---
title: "Set up Automatic AP Updates: Canada | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-automatic-ap-updates-canada"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada/set-up-automatic-ap-updates-canada"
---

# Set up Automatic AP Updates: Canada

Set up automatic updates to the Accounts Payable (AP) module.
Note: Prior to setting up automatic AP update information, you must first [set up the associated earning code](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-australia).

Entering information on this tab enables the system to automatically create AP transactions from the amounts that you post to the specified earnings code during payroll processing.
Typical use is for for earnings codes that represent negative earnings such as Registered Retirement Savings Plans, which employees pay completely. When updating payroll information to AP (via the PR AP Update form), the system reverses all transactions created for the negative earnings so that they become positive AP payments. See [PR AP Update Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-ap-update-form) for more information.
Use the Addl Info tab on the PR Earnings Codes form to set up automatic updates to the Accounts Payable (AP) module.

1. Select the Automatic
 Update to Accounts Payable checkbox.The system enables the
 remaining fields.

1. In the Vendor field, enter the vendor number or press F4
 to select from a list.

1. To create a separate
 transaction for each employee, select the Separate AP
 Transaction per Employee checkbox.Note: If you select this checkbox, the
 system uses each employee's first and last name as the transaction
 description. If you do not select this checkbox, the system uses the
 earnings code description.

1. In the Payable
 Type field, enter the payable type or press F4
 to select from a list. Note: The payable type you enter here
 determines the GL payable account to credit when posting the AP transaction.

1. In the GL
 Account field, enter the GL account number for debiting during
 AP transaction posting.

1. In the Frequency field, enter the frequency code that identifies how
 often the system updates AP with posted transactions associated with this
 earnings code.

1. Save the record.

Related tasks

- [Set Up Pre-Tax Deductions](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/set-up-pre-tax-deductions)

Related information

- [PR Allowances Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-allowances-form)

- [Set up Earnings Codes: Canada](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-earnings-codes-canada)

- [PR Earnings Codes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-earnings-codes-form)

- [PR AP Update Form](/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/pr-ap-update-form)
