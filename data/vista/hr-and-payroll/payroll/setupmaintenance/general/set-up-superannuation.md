---
title: "Set Up Superannuation | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation"
---

# Set Up Superannuation

(Australia only) A high-level overview of how to configure
 Vista to process superannuation liabilities, associate superannuation funds with fund
 clearing houses, and generate Super Contributions files.
You must [Initialize Routines](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-payroll-routines/initialize-routines). This is ordinarily done after every release that contains payroll routine updates, but if you are unsure whether it was done, there's no harm in repeating the process.Note: The SuperMin routine is necessary for calculating superannuation if you are using weekly minimum amounts or if you want to take into account the monthly earnings threshold amount for superannuation.

To set up superannuation:

1. In the PR Routines form, enter the current earnings threshold in the Misc Amt #1 field; that is, the minimum amount of monthly gross earnings.Note: You must update this field every time the threshold changes.

1. In the HQ Super Funds form, set up each superannuation fund that you offer to employees. For more information, see [Set Up and Maintain Superannuation Funds](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/set-up-and-maintain-superannuation-funds).

1. For each fund that you create in the HQ Super Funds form, create a corresponding liability code in the PR Deductions/Liabilities form. For more information, see [Setting Up Liability Codes for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/setting-up-liability-codes-for-superannuation).

1. Associate a superannuation liability code for each employee in the PR Employee Dedns/Liabs form. Make sure to enter the employee's superannuation membership number in the Membership # field.

1. If necessary, set a weekly minimum superannuation amount by craft/class/template or employee. For more information, see [Set Weekly Minimums for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/set-weekly-minimums-for-superannuation). Tip: You can run the PR and AP Superannuation report to review the contributions for each employee along with their associated membership number.

1. [Set Up and Maintain Superannuation Funds](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/set-up-and-maintain-superannuation-funds) in Vista using the HQ Super Funds form.

1. [Set up superannuation fund clearing houses](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/set-up-superannuation-fund-clearing-houses) (one ore more) in Vista using the HQ Super Clearing House form.

1. [Associate Funds with a Superannuation Fund Clearing House](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/set-up-superannuation/associate-funds-with-a-superannuation-fund-clearing-house) for each PR company, using the PR Super Clearing House Fund form.

1. [Generate a Superannuation Contributions File in .csv Format](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/generate-a-superannuation-contributions-file-in-.csv-format) using the PR Super File Generate form.

Related information

- [About the PR Super Clearing House Funds Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/about-the-pr-super-clearing-house-funds-form)

- [About the PR Super File Generate Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/superannuation/about-the-pr-super-file-generate-form)

- [PR Deductions/Liabilities Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-deductionsliabilities-form)

- [Create Deduction and Liability Codes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-creating-deductionliability-codes/create-deduction-and-liability-codes)

- [Setting Up Liability Codes for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/setting-up-liability-codes-for-superannuation)

- [Set Weekly Minimums for Superannuation](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/set-weekly-minimums-for-superannuation)
