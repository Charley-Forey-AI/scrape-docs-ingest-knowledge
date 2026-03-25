---
title: "Configure Timecard Validation Rules | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/configure-timecard-validation-rules"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/configure-timecard-validation-rules"
---

# Configure Timecard Validation Rules

If you are using the Timecard Compliance feature, you must specify which timecard validation rules to use for auto-validation of timecards and set their severity levels and parameters.
Before you can set timecard validation rules, you must select the Enable Timecard Compliance checkbox in PR Company Parameters (Info tab). If this checkbox is not selected, you will be unable to access the PR Timecard Validation Rules form or the Timecard Rules tab in PR Company Parameters.
 Validation rules are predefined; you cannot add new rules or delete existing ones. You can only enable the ones you want to use, set their severity levels, and configure their parameters.The following describes setting timecard validation rules using the PR Timecard Validation Rules form. However, you can also set timecard validation rules using the Timecard Rules tab in PR Company Parameters.

1. Open the PR Timecard Validation Rules form (Payroll > Programs > PR Timecard Validation Rules).

1. For each rule you want used in timecard validation, select the Enabled checkbox.

1. For each enabled rule, select the severity level.

- Allowed No Warning - Select this option to allow posting the timecard batch without a system warning when discrepancies are found.

- Allowed With Warning - Select this option to have the system warn you when discrepancies are found in the timecard batch and allow you to accept the discrepancies or correct them before posting the batch.

- Not Allowed - Select this option to have the system warn you when discrepancies are found in the timecard batch and prevent you from posting the batch until the errors are corrected.

1. Select Save.

1. For each rule you have enabled, configure the rule's parameters. Parameters may differ depending on the rule.

1. Select the Parameters tab.

1. For each parameter defined for the selected rule, use the Value field to specify the parameter value as follows:

- Look back months - Enter the number of months of historical data to use when performing timecard validation.

- Tolerance Factor - Indicate how much a validated record can vary from its usual historical average before it is flagged for review. See the [F1 Help](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form/field-definitions-pr-timecard-validation-rules-form#concept-b61bdc6f-aa97-4ba3-94c5-64e776dd2a0e--en) for further information about these settings.

- 1 = Low Deviation

- 2 = Medium Deviation

- 3 = Large Deviation

Timecard validation will now include each of the rules you enabled and provide a list of discrepancies based on your chosen severity levels and parameters.

Related information

- [About Validation Rules](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/about-validation-rules)
