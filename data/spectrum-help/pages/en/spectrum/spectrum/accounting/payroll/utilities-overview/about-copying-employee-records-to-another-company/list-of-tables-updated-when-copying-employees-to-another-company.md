---
title: "List of Tables Updated When Copying Employees to Another Company | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/list-of-tables-updated-when-copying-employees-to-another-company"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/list-of-tables-updated-when-copying-employees-to-another-company"
---

# List of Tables Updated When Copying Employees to Another Company

Note that history tables are only copied if the Include employee history checkbox is
 selected on the confirmation screen.
Below is a list of the Payroll and Human Resources tables that are
 updated during the [Copy Employees to Another Company - Confirmation](/en/spectrum/spectrum/accounting/payroll/utilities-overview/about-copying-employee-records-to-another-company/copy-employees-to-another-company---confirmation) process.
Payroll Tables:
PR.EM1 - Employee file #1
PR.EM2 - Employee file #2
PR.EM3 - Employee file #3
PR.EMPVD - Employee Recurring Deductions and Add-ons
PR.XALPH – Employee cross reference
PR.LOG – Employee change log
PR.EMCOM – Employee comments
PR.UEMP – Employee User-defined Fields
PR_UNAVAILABLE_SCHEDULE_MC
PR.EHIST - Payroll Check History
PR.STHIS - State Tax History
PR.TCHIS - Time Card History
PR.WCHIS - Workers' Compensation History
PR.EHVD – Deduction/Add-on Check History
PR.EM4 – Employee to-date information
PR.EM5 – Employee Deduction/Add-on information
PR_TIME_CARD_RETRO_HIST_MC - Time Card Retro Pay History
PR_EMPL_NONCASH_VOL_ADD_MC - Employee Non-Cash Add-on
PR_TC_DET_UNION_DED_HIST_MC - Payroll Union Deduction Detail History Table

## Human Resources Tables

HR_EMP_DEPENDENTS_MC
HR_EMP_DRUG_DET_MC
HR_EMP_DRUG_HDR_MC
HR_EMP_DRUG_REP_MC
HR_EMPL_ATTACHED_FILES_MC
HR_EMPLOYEE_BENEFITS_MC
HR_EMPLOYEE_CIVIL_MC
HR_EMPLOYEE_FMLA_MC
HR_EMPLOYEE_FORMS_MC
HR_EMPLOYEE_INSURANCE_MC
HR_EMPLOYEE_QUEST_ANSWERS_MC
HR_EMPLOYEE_TRAINING_MC
HR_INTERVIEWS_MC
HR_APPLICANT_EMP_HISTORY_MC
HR_REFERENCES_MC
HR_INCIDENTS_MC
HR_INCIDENTS_PEOPLE_MC
HR_INCIDENTS_PROPERTY_MC
HR_INC_USER_FIELDS_DET_MC
HR_INC_USR_DEF_FLD_XREF_MC
HR_EMPLOYEE_LOG_MC
Note Regarding the Payroll G/L Distribution Table and the Human Resources Accrual History Table:
The Copy Employees to Another Company feature does not include contents of the Payroll G/L History (PR_GL_HISTORY_MC) table or the Vacation / Holiday / Sick Accrual History (HR_ACCRUAL_HISTORY_MC) tables that retain historical information about the employee, even when purged. This information is not copied because it serves as the subsidiary ledger to the General Ledger of the original company, substantiating summary transaction values in the G/L accounts.
