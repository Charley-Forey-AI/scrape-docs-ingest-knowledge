---
title: "About Validation Rules | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/about-validation-rules"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/about-validation-rules"
---

# About Validation Rules

Smart Payroll's timecard validation uses a series of validation rules, along with compliance settings and/or employee history to determine if discrepancies exist when posting timecards.
There are several pre-defined timecard validation rules; you cannot add or delete rules, but you can enable or disable them and set their severity level (Allowed No Warning, Allowed With Warning, Not Allowed).
The following describes the available validation rules and how they are implemented.
Note: The system only flags timecards as exceptions for violated rules with a severity level of Allowed With Warning or Not Allowed

Daily hours variance ruleDescription: Checks if work hours in a day exceed a specified threshold for variance.How it works: The system analyzes each employee's historical data to establish a baseline of their typical work hours. It then uses this historical data to predict expected hours on a daily basis.
When a timecard is entered, the system evaluates the hours against the employee's historical average plus a variance tolerance factor. This factor, which can be set from a low to high deviation level, determines the sensitivity of the validation check. A "low" setting is more restrictive, while a "high" setting allows for greater deviation.
If an entry exceeds the expected hours and the allowed threshold, the system will flag the record. The action taken depends on the severity level set for the validation. For more information about severity levels, see [Severity](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form/field-definitions-pr-timecard-validation-rules-form#concept-42d5086c-640f-4f8a-8ca0-87d143663756--en).
Meal Break Compliance RuleDescription: Validates that meal breaks are taken according to state-specific rules for hourly, non-exempt employees, excluding PTO or other non-work hour earning codes based on each earning code set up in PR Earning Codes.How it works: The system references the unemployment state (Unemp State field) in the timecard entry and the HQ State Compliance form to determine the specific rules for an employee's work location. It calculates total daily hours by looking at both new (unposted) and existing (posted) timecards to ensure compliance throughout the workday.
There are two methods on the Parameters tab of PR Timecard Validation Rules that the validation can use. Depending on the method, your entry in the Value field differs:

- Meal Break Duration: Enter the required duration between a Start Time and the subsequent Stop Time.

- Meal Break Earning Code: If your company uses an earnings code to capture meal break time, enter the Earnings Code.

Depending on the Severity level selected for the validation rule, the PR Timecard Compliance form uses color-coded highlighting to flag violations—Allowed With Warning uses yellow, Not Allowed uses red.
With the Not Allowed flag, you must make the necessary changes to the timecard record to resolve the violation before you can save the record. The system prevents timecard posting until violations are corrected.
Minimum wage compliance ruleDescription: Checks that an employee's pay rate is not below the state-mandated minimum wage. How it works: During the validation process, the system first checks the FLSA Exempt status for each employee to determine who is subject to the rule. Validation only applies to non-exempt employees (those without the checkbox selected).
 In addition, the system only validates timecards that use an earnings code with an H-Rate per Hour method. During validation, the system compares the timecard date with the effective date in the HQ State Compliance form to identify the correct minimum wage rate for the corresponding state.
 The system then compares the employee's pay rate to the applicable state minimum wage and:

- If the pay rate meets or exceeds the state minimum wage, the system skips the timecard.

-  If the pay rate is below the state minimum wage, the system flags the timecard entry as an exception and indicates the discrepancy.

Multiple site detection ruleDescription: Checks time in/out for an employee working multiple sites to ensure no overlapping times.How it works: The system checks both posted and unposted timecards (per employee) for entries where an employee appears to be working at multiple physical locations at the same time. The system analyzes time entries for a given day, checking for any overlap between the Time In and Time Out records across different Location IDs, which can include specific jobs, service work orders, or equipment.
There are two types of overlapping entries:

- Partial Overlap - Occurs when a portion of one time entry's duration coincides with another. For instance, if an employee has one time entry for Job A from 7:00 AM to 3:00 PM and a second entry for Job B from 2:00 PM to 5:00 PM, both will be flagged..

-  Full Overlap - Occurs when two or more time entries for different locations share the exact same start and stop times, such as two entries from 7:00 AM to 3:00 PM.

Note: When checking for time overlaps, the system focuses on the overall time-in/time-out range of an employee's shift; it does not consider individual break segments.

New state or local code ruleDescription: Detect new state and local codes in employee timecard record. How it works: This rule actively prevents errors in tax withholding by identifying new state and local codes on employee timecards. The system cross-references timecard data against the employee's historical records and payroll setup.
If validation detects a new local code and the local code is missing from the employee's history or setup, a "New local code detected: ##" message displays (where ## represents the local code); however, no further withholding checks are performed.
If validation detects a new state:

- It first checks HQ State Compliance (State Form field) to see if that state requires a state-specific withholding certificate (for example, AL, LA, CA).

- If the state accepts the Federal form (the Fed Form Accepted checkbox is selected), a "New tax state detected: ##" message displays (where ## represents the state); no state-specific setup check is performed.

- If the state does require a specific withholding certificate, the system validates the employee's filing status against the required state withholding deduction (defined in PR State Information, Tax Dedn field).

- If the proper setup is found, a "New tax state detected, EE Setup for state withhold" message displays.

- If the proper setup is not found, the system flags the entry and a "New tax state detected: ##, EE NOT setup for state withhold" message displays.

If validation detects a new state and local code:

- If the state requires a state-specific withholding form and setup exists, the system will display the following message: "New tax state detected: ##, New local code detected: ##, EE setup for state withholding".

- If the state requires a state-specific withholding form and no setup exists, the system will display the following message: "New tax state detected: ##, New local code detected: ##, EE NOT setup for state withholding".

- If the state accepts the Federal form (the Fed Form Accepted checkbox is selected in HQ State Compliance), a "New tax state detected: ##, New local code detected: ##" and no state-specific setup check is performed.

Overtime ValidationDescription: Validates that overtime is applied or not applied according to the most favorable rule for the employee, considering classification (exempt/non- exempt), federal, state, union, job, and employee-specific overtime. How it works: The validation engine uses rules from several existing areas, including union overtime schedules (PR Crafts), job overtime schedules (JC Jobs / PR Craft Templates), state overtime requirements (HQ State Compliance), and individual employee overtime schedules (PR Employees).
 The Include Exempt Employees checkbox on the Parameters tab of PR Timecard Validation Rules allows you to choose whether the system should check overtime for exempt staff. By default, this is turned off (Value = N) to focus on hourly non-exempt workers. If your company pays overtime to exempt employees under certain conditions, ensure the checkbox is selected. Note: The FLSA Exempt checkbox in PR Employees > Add'l Info tab identifies the employee's status under the Federal Labor Standards Act.

Pay period hours variance ruleDescription: Checks if work hours in a pay period exceed a specified threshold or variance.How it works: The system analyzes each employee's historical data to establish a baseline of their typical work hours. It then uses this historical data to predict expected hours for an entire pay period.
When a timecard is entered, the system evaluates the hours against the employee's historical average plus a variance tolerance factor. This factor, which can be set from a low to high deviation level, determines the sensitivity of the validation check. A "low" setting is more restrictive, while a "high" setting allows for greater deviation.
If an entry exceeds the expected hours and the allowed threshold, the system will flag the record. The action taken depends on the severity level set for the validation. For more information about severity levels, see [Severity](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/smart-payroll-forms/pr-timecard-validation-rules-form/field-definitions-pr-timecard-validation-rules-form#concept-42d5086c-640f-4f8a-8ca0-87d143663756--en).
Pay rate validation ruleDescription: Cross-references each employee's timecard with their employment record to ensure the pay rate aligns with their designated position and contract agreement.How it works: The system checks the timecard pay rate against the employee's profile and any relevant craft class or job rates. If the timecard rate doesn't match any of these records, the system flags it as an 'unknown pay rate'.
 If the timecard rate is lower than the highest rate the employee is eligible for (based on their profile, craft class, or a specific job), the system then checks for any pay rate changes for the employee. If an employee is paid a new rate that isn't due to a job change, the system checks for a documented reason, like a craft class or salary history update and flags any rate changes that don't have this documentation.
 When calculating overtime, the system uses the pay code's earning factor and multiplies it by the employee's regular rate of pay, factoring in any applicable weighted average rates. The system highlights the pay rate field in yellow or red for any flagged issues and provides a specific error message.
Examples:
ViolationError Message
Rate matches a valid rate but not the highestA valid pay rate was found, but a higher rate exists for this employee. Please review the rate selection.
HR Salary History exists but effective date doesn't match the timecard post dateA matching salary history rate was found, but its effective date does not match the timecard post date.
No match found anywhereNo pay rate match found
No applicable craft or class foundNo applicable craft or class was found for this employee's pay rate validation.

Related information

- [Configure Timecard Validation Rules](/en/vista/vista/hr-and-payroll/payroll/time-entry/trimble-smart-payroll/configure-timecard-validation-rules)
