---
title: "PR Timecard Validation Rules Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form"
---

# PR Timecard Validation Rules Form

Use the PR Timecard Validation Rules form to enable timecard validation rules, set severity levels, and configure rule parameters.
You can access this form via the Payroll main menu or the Timecard Rules tab in PR Company Parameters. However, it is only accessible if you selected the Enable Timecard Compliance checkbox in PR Company Parameters (Info tab).
This form is automatically populated with system-defined validation rules. You can enable rules and set their severity levels, but you cannot add or delete rules.
Available Rules are as follows:

- Daily hours variance rule

- Meal Break Compliance Rule

- Minimum wage compliance rule

- Multiple site detection rule

- New state or local code rule

- Overtime Validation

- Pay period hours variance rule

- Pay rate validation rule

For each of these rules, you specify whether to enable the rule and if enabled, what level of severity to use. The severity level determines how timecard discrepancies are handled when they are encountered in a timecard batch.

- Allowed No Warning - If this option is selected, the system does not warn you when discrepancies are found in the timecard batch, and allows you to post the batch.

- Allowed With Warning - If this option is selected, the system warns you when discrepancies are found in the timecard batch, and allows you to either accept the discrepancies or correct them, before you post the batch.

- Not Allowed - If this option is selected, the system warn you when discrepancies are found in the timecard batch, but will only allow you to post the batch once you have corrected the errors.

The system identifies discrepancies in a timecard batch by applying the rules defined and enabled here. In addition, depending on the rule, the system may also consider employee history, compliance rules, and/or business rules to determine if discrepancies exist.
