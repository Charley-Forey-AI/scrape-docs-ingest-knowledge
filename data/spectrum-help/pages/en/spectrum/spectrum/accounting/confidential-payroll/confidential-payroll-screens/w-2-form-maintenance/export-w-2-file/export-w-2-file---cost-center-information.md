---
title: "Export W-2 File - Cost Center Information | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/w-2-form-maintenance/export-w-2-file/export-w-2-file---cost-center-information"
fetched_at: "2026-04-03T20:43:54.261868+00:00"
menu_path: "/en/spectrum/spectrum/accounting/confidential-payroll/confidential-payroll-screens/w-2-form-maintenance/export-w-2-file/export-w-2-file---cost-center-information"
---

# Export W-2 File - Cost Center Information

If cost centers are being used in the current company, the software assures that the operator has security authorization to access all employees to be included in the export file. In order to perform the 'Build' or to generate the 'Export File', the operator must have full security.
When 'entity tracking' is enabled, the screens and reports throughout W-2 Processing will hide W-2 records for entities the operator is not allowed to access.
Fields/ButtonsDescriptions
YearEnter the payment year.
EntityThis field only displays if cost centers are being used and entity tracking is also enabled in the current company.
Enter or select an Entity code. The software will verify that the current operator has security authorization for the selected entity before proceeding. If this field is left <blank>, the main company entity is used.

Tax table codeEnter the tax table code for which W-2 information should be submitted, or press F4 to select a code from the Payroll Income Tax Tables window. Note that the export file created will include the RV record, which is a total of the RS records.Important: For State electronic filers, the State code must be
 entered here in order to create "RS" lines in the file. Two additional fields display when a state code is
 specified:Tax ID Press Enter to accept the
 default employer identification number from the Tax Table Maintenance
 screen. Otherwise, enter the state tax ID number of the transmitting
 company.FIPS code Enter the postal numeric
 code for this tax table ID. Consult your Circular E for the numeric
 code or contact your accountant for details.

Submitter
Use company / entity default?Select this checkbox to use the submitting company's default address information.
Save as default?Select this checkbox to update the submitting company's mailing information on this screen.
Foreign Address buttonSelect to add or edit the submitter's foreign address, if applicable.
Submitter EINThe employer identification number will default from Income Tax Table Maintenance, or enter the employer identification number of the company transmitting these W-2s. Up to 20 characters are allowed in order to accommodate state tax tables; the electronic build strips out any dashes and left-fill zeros.
If quarterly reports use a different EIN, that EIN should be entered here.
Note: If entity tracking is enabled in Enterprise Installation, the 'Employer
 tax ID numbers' will be derived from the Payroll tax table or the
 entity-specific alternate tax ID number, if applicable.

User IDEnter the User ID for the employee who is authorized to submit this form. Entry in this field is required.
Submitter name, and addressEnter the submitter's name and mailing address. If you enter only one address line in Spectrum, either address 1 or 2, that address line will be written to the EFW2 file as the Delivery Address and the Location Address will be blank. This affects all EFW2 records that contain an address, specifically RA, RE, RW, and RS records.
Contact
Use company / entity default?Select this checkbox to use the contact's default address information.
Save as default?Select this checkbox to update the contact's mailing information on this screen.
Foreign Address buttonSelect to add or edit the contact's foreign address, if applicable.
Contact name and addressEnter the name and address of the person to contact in case of a problem or error.
E-mailEnter the contact person's email address for notification purposes.
PreparerUse the drop-down menu to indicate who prepared this file.
File return nameEnter the name of the company to which the IRS should return the transmission file.
Employer
Use company / entity default?Select this checkbox to use the employer's default address information.Note: If entity tracking is enabled in Enterprise Installation, the employer
 name and address fields will default entity-specific information instead
 of defaulting information from Company Installation.

Save as default?Select this checkbox to update the employer's mailing information on this screen.
Terminate business?Select this checkbox if this employer is terminating business during this tax year.
Foreign Address buttonSelect to add or edit this employer's foreign address, if applicable.
Agent indicatorIf applicable, enter an employer agent or use the drop-down menu to select an agent option.
Most users will input N/A in this field. Select 2678 Agent for an IRS-approved agent. Common paymaster is an IRS rule that some of our clients can use in submitting one W-2 file for multiple tax IDs (for example, one company in a group has met the minimums to be a "common paymaster" so they can pay all of their related companies' employees.)

Employer's EINThe employer's Federal tax identification number will default from the tax tables, or you can enter the correct employer ID number. Up to 9 characters are allowed; the electronic build strips out any dashes.
The submitter's EIN must begin with 10, 20, 26, 27, 30, 40, 50, 60, 80, or 90. Unacceptable submitter EIN submissions include 00, 07, 08, 09, 17, 18, 19, 28, 29, 49, 69, 70, 78, 79, and 89. Please see MMREF specifications or consult with your CPA for more information.
Note: If entity tracking is enabled in Enterprise Installation, the 'Employer
 tax ID numbers' will be derived from the Payroll tax table or the
 entity-specific alternate tax ID number, if applicable.

Other EINEnter the employer identification number submitted on quarterly reports from the previous year if it differs from this year's EIN.
Employment typeUse the drop-down menu to select the employment type.
EstEnter the establishment number, coverage group, or payroll record unit.
3rd partyEnter the amount of income tax withheld by third parties, if applicable.
Employer name and addressEnter the employer's name and mailing address.
