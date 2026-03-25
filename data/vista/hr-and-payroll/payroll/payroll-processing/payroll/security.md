---
title: "Security | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/security"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/payroll-processing/payroll/security"
---

# Security

You can control access to sensitive payroll information.
Although there is nothing unique to Payroll regarding the setup of security, a discussion of the options may assist in determining how security can be implemented.
Security is set up in Viewpoint Administration (VA), and you should refer to the Help for that module for information and implementation steps.
Some commonly used VA forms for Payroll security are:

- [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form) to restrict access to specific forms.

- [VA Tab Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-tab-security-form) to restrict access to tabs within some forms. PR Employees was designed to have more sensitive information, such as pay rates, on the second tab (Add’l Info). Access could be allowed on the Information tab only.

- [VA Form Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-form-security-form) to allow some users to access employees in one company but not in another.

- [VA Report Security](/en/vista/vista/administration/viewpoint-administration/application-security/data-record-and-content-security/va-report-security-form) to restrict access only to reports that do not have sensitive information.

System Administrators can also use the [System Overrides: Mask Text](/en/vista/vista/system-tools/user-interface-guide/system-forms/about-the-field-properties-form/field-definitions-field-properties-form#ID-0004caa2--en) flag in the Field Properties form to replace data in text fields with asterisks (*). This prevents all users from reading the data in these text fields.
Iit is common to allow access to field employee information, but to want to restrict access to information on administrative and executive employees. The best way to accomplish this is to implement Data security on employees. Each employee record is assigned one or more security groups. Users can then be given access to some security groups but not to others. These users are able to fully process and report on some employees, but will not have access to others. The advantage to using data security on employees in Payroll is to have all the data in one system and in one company so that reporting, such as W-2’s and quarterly taxes, can be done on the whole company while still maintaining restricted access. Users with the higher access to all employees will need to run the reports covering all employees. When setting up data security on employees, review the tables to be included. Only include those that really have sensitive information. These can be changed as needed.
Data level security on employees also prevents access to the data in the tables from third-party tools such as Excel, Access, etc.
An additional option is to prevent the pay rate from displaying in the PR Timecard Entry screen using the VA User Profile form.
