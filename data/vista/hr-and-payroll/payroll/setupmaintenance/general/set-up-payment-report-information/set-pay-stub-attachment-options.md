---
title: "Set Pay Stub Attachment Options | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/set-pay-stub-attachment-options"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-payment-report-information/set-pay-stub-attachment-options"
---

# Set Pay Stub Attachment Options

You can set up your payroll company to attach a PDF of payment information (pay stubs and direct deposit advice stubs) to employee pay sequences so that they can be included when sending email notifications to employees.
You can also secure attachments by requiring a password to open them.
When you print a check or direct deposit advice stub, the system attaches a PDF copy of the payment information to the corresponding employee record using the specified attachment type. Then, when you send email notifications to employees, the system attaches the PDF to the email.

1. From the Main Menu, select Payroll > Programs > PR Company Parameters.

1.  In the PR Company field, enter the payroll company to work with or press F4 to select from a list of valid PR companies.

1.  Select the Report Info tab.

1.  (Optional) In the Document Password Format field, select the format to use for system-generated document passwords. Choices are:

- 1 - Birthdate YYYMMDD & ending digits of SSN/TFN/SIN

- 2 - Employee number & ending digits of SSN/TFN/SIN

- 3 - First 4 digits of Last Name (lowercase) & ending digits of SSN/TFN/SIN

1.  Select the Attach Pay Stub to Employee Pay Sequence checkbox. The system enables the attachment report fields.

1. In the Report Title for Check/Cheque Attachment field, accept the defaulted standard report or enter the custom report for check/cheque stubs. Press F4 for a list of reports.Note: The defaulted standard report will differ depending on country. See the [F1](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form#ID-00035d04--en) help for more information.

1. In the Report Title for EFT Attachment field, accept the defaulted standard report or enter the custom report for direct deposit stubs. Press F4 for a list of reports.Note: The defaulted standard report will differ depending on country. See the [F1](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form/field-definitions-pr-company-parameters-form#ID-00035d04--en) help for more information.

1. (Required) In the Stub Attachment Type field, enter the stub attachment type or press F4 to select from a list of valid attachment types.

1. Select Save.

Your company is now set up to attach payment information to employee pay sequence records (in PR Employee Pay Sequence Control).
If you will be emailing pay stubs to employees, you must set up each applicable employee with a valid email address and a pay stub delivery method of A-Email with attachment in PR Employees.

Related information

- [About Setting up Automatic Overtime](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-setting-up-automatic-overtime)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

- [About the PR Employee Pay Sequence Control Form](/en/vista/vista/hr-and-payroll/payroll/payments/about-the-pr-employee-pay-sequence-control-form)
