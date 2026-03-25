---
title: "PR Employees | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/pr-employees"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/imports/setup-and-maintenance/standard-import-templates/pr-employees"
---

# PR Employees

Additional information about the PR Employees import.
The PR Employees import automatically formats Social Security Numbers (i.e. include the dashes). However, SSN's that are entered manually in the IM Work Edit program will need to be entered with the dashes, as they will not be formatted automatically.

## Australian Users

PAYG INB SummariesIt is suggested that you select the Use Viewpoint Default checkbox for the EmailPAYGSumYN identifier in your employee import templates. When you import employee records, this allows the system to set the EmailPAYGSumYN flag for each employee based on the PAYG INB Summary checkbox setting for the Payroll company in PR Company Parameters and the employee's information as follows:

- If the PAYG INB Summary checkbox is selected for the Payroll company in PR Company Parameters and the employee has a valid email address, the EmailPAYGSumYN identifier defaults as Y.

- If the PAYG INB Summary checkbox is selected for the Payroll company in PR Company Parameters and the employee does not have a valid email address, the EmailPAYGSumYN identifier defaults as N.

- If the PAYG INB Summary checkbox is not selected for the Payroll company in PR Company Parameters, the EmailPAYGSumYN identifier defaults as N for all employees.

If you deselect the Use Viewpoint Default checkbox, you must manually enter the correct value in the EmailPAYGSumYN field for each employee record in IM Work Edit based on the company's PAYG INB Summary checkbox setting to avoid upload errors.
Working Holiday MakersThe PAYGIncomeType column (Identifier 62) must be set to S (Salary or wages) or H (Working holiday maker) in IM Work Edit. If you do not specify a PAYG income type in your text files, you can select the Use Viewpoint Default checkbox in Template Details to ensure the system automatically sets this field to S (Salary or wages) during the import process. If you have employees that are working holiday makers, you can manually set the PAYGIncomeType to H (Working holiday maker) in IM Work Edit prior to the upload process. Otherwise, you can change the PAYG Income Type value for the employee in PR Employees (Info tab).
The IncomeStreamCountry column (Identifier 680) must be set to null for regular employees (those with a PAYGIncomeType of S), and to a valid country code for working holiday makers (employees with a PAYGIncomeType of H). The country code cannot be blank, nor can you use country codes AU, CC, CX, HM, or NF.
