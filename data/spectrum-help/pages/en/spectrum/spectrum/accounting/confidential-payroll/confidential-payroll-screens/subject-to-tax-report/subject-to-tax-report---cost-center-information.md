---
title: "Subject-to-Tax Report - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/subject-to-tax-report/subject-to-tax-report---cost-center-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/subject-to-tax-report/subject-to-tax-report---cost-center-information"
---

# Subject-to-Tax Report - Cost Center Information

If cost centers are being used in this company, then when running the Confidential Payroll format of the Subject-to-Tax Report, Spectrum includes the employee on the report only if the operator requesting the report has permission to access the employee's information. For employees in the current company, Spectrum compares the cost center assigned to the employee with cost centers in the operator's assigned scheme; if the cost center is not included, then that employee is not shown on the report.
When the Confidential Payroll version of this report is printed, Spectrum will
 determine whether the Enterprise Installation option for Cost centers is set to Yes for
 any company codes listed in Confidential Payroll > Company Maintenance. If cost centers are used in any included companies, Spectrum will
 validate that the operator has permission to access the employee's information in that
 company. Spectrum compares the cost center assigned to the employee with cost centers in
 the operator's assigned scheme for that company; if the cost center is not included,
 then information for that employee will not be included on the Confidential Payroll
 report.
For employees in non-confidential companies, cost center validation is performed based on settings in each included company. If the cost center feature is enabled in the Enterprise Installation screen for the non-confidential company, then the cost center assigned to the employee in the non-confidential company must be included in the list of valid cost centers for the operator's scheme in that non-confidential company. If the cost center feature is disabled in the Enterprise Installation screen for the non-confidential company, then all employees from that company will display on the report.
