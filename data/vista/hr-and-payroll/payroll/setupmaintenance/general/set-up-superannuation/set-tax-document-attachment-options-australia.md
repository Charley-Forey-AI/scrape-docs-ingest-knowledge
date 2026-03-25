---
title: "Set Tax Document Attachment Options: Australia | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/set-tax-document-attachment-options-australia"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/set-up-superannuation/set-tax-document-attachment-options-australia"
---

# Set Tax Document Attachment Options: Australia

You can set up your payroll company to attach PDF copies of PAYG payment summaries to employee PAYG summary records so that they can be included when sending email notifications to employees. These attachments can be password-secured.
To enable your employees to receive attachments of PAYG payment summaries:

1. From the Main Menu, select Payroll > Programs > PR Company Parameters.

1. In the PR Company field, enter the payroll company to work with or press F4 to select from a list.

1. Click on the Report Info tab.

1. (Optional) In the Document Password Format field, select the format to use for system-generated document passwords. Choices are:

- 1 - Birth date YYYMMDD & ending digits of SSN/TFN/SIN

- 2 - Employee number & ending digits of SSN/TFN/SIN

-  3 - First 4 letters of Last Name (lowercase) & ending digits of SSN/TFN/SIN.

1. Select the PAYG INB Summary checkbox.The PAYG Attachment Type field is enabled.

1.  (Required) In the PAYG Attachment Type field, enter the attachment type for PAYG INB summaries or press F4 to select from a list.

1. Click Save.A message displays asking if you want to update employees with a valid email address in the PR Employees form to receive their PAYG INB Summary tax documents via email.

1. Select Yes to have the system automatically select the PAYG INB Summary checkbox in the PR Employees form (Add'l Info tab, Tax Document Email Settings section) for all employees with a valid email address. Select No if you want to manually select the checkbox for applicable employees.Note: If you select Yes and an employee does not have an email address, the checkbox is enabled, but not selected in PR Employees. You must enter an email address in order for the employee to receive their PAYG tax documents via email.

Your Payroll company is now set up to attach PAYG payment summaries to employee PAYG summary records in the PR Employee PAYG Summaries form.In order to email PAYG summaries to employees, you must have met the prerequisites for emailing payroll-related documents. For more information, see [Prerequisites for Emailing Payroll Documents](/en/vista/vista/hr-and-payroll/payroll/payments/prerequisites-for-emailing-payroll-documents).

In the PR Employees form, verify that each applicable employee has a valid email address and the PAYG INB Summary checkbox is selected.Note: To ensure summaries are attached to summary records, you must initiate the print process in the PR PAYG Payment Summary INB form (by clicking the Print button), *even if all employees are configured to receive their summaries via email*.If you do not need to print physical copies of summaries, you can cancel out of the print process.
Initiating the print process causes the system to generate and attach a PDF copy of each summary to the employee's summary record for emailing purposes. When you send email notifications to employees, the system attaches the PDF to the email.

Related information

- [About Earnings Code Sequences](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/about-earnings-code-sequences)

- [PR Company Parameters Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/general/payroll-general-setup-forms/pr-company-parameters-form)

- [PR Employees Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/employee/pr-employees-form)

- [PR Employee PAYG Summaries Form](/en/vista/vista/hr-and-payroll/payroll/quarteryear-end-reporting/payg-payment-summaries/payroll-australia-payg-forms/pr-employee-payg-summaries-form)
