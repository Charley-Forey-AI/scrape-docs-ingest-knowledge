---
title: "Employee Tax Setup - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-tax-setup/employee-tax-setup---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/employees/employee-properties/employee-tax-setup/employee-tax-setup---field-descriptions"
---

# Employee Tax Setup - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields/ButtonsDescriptions
Social security #Enter the employee's social security #
 in this field.
 If
 Payroll reporting is set to 'Canada' in [Payroll Installation - Properties](/en/spectrum/spectrum/accounting/payroll/installation-overview/payroll-installation---properties), the
 number entered here will be formatted to comply with Canadian mask
 guidelines, including a single space between the 3rd and 4th digits and a
 single space between the 6th and 7th digits.
Note: The social security number will not print on reports
 for security reasons.

Foreign employeeSelect this checkbox to adjust the
 Federal Exempt/Taxable settings.
If this checkbox is
 selected the Income tax, Disability and Unemployment insurance flags can be
 set to 'Taxable' or 'Exempt'. If this checkbox is not selected, these flags
 will be view-only and revert to 'Taxable'.
Note: This checkbox is hidden when the Allow non-US payroll
 processing? checkbox is selected in the Payroll Installation
 - Defaults screen.

Permanent residence / work
Tax codeSelect the appropriate federal, state,
 county and local tax codes from the corresponding drop-down menus. Up to 10
 characters are allowed. The selected tax codes will display in the header.
If the Allow non-US payroll processing? checkbox is selected in
 the Payroll Installation - Defaults screen, you can edit the Federal tax
 code and other fields on the Federal line. Otherwise, changes to the Federal
 tax code are not permitted.
If an employee is
 claiming exemption from income tax withholding, that employee may not be
 exempt from other taxes; therefore, it is recommended that the employee be
 recorded to claim 99 deductions.
The Federal field
 has a default tax code; this ensures that a W-2 will be generated for the
 employee. This default setting cannot be changed. If an employee is claiming
 exemption from Federal income tax withholding, the employee may not be
 exempt from other taxes. Therefore, it is recommended that the employee be
 set up to claim 99 exemptions.

Income taxSelect E from the drop-down menu if
 employee is exempt from state, county, or local income taxes; otherwise, press
 Enter to accept
 the system default of Taxable. Be sure to enter T if a W-2 will be required for
 this tax code and employee.
Disability (FICA/SDI)Select E from the drop-down menu if
 employee is Exempt from FICA or SDI taxes, otherwise, press Enter to accept the system
 default of Taxable.
UnemploymentSelect E from the drop-down menu if
 employee is Exempt from unemployment insurance taxes; otherwise, press
 Enter to accept
 the system default of Taxable.
Filing statusSelect one of the filing status codes
 from the drop-down menu of filing statuses for the particular tax code and
 assign it to the employee.
The Payroll tax tables allow
 an unlimited number of income tax filing statuses to be created in order to
 accommodate those who need the ability to set up more than four filing
 statuses for income tax withholding tables. In addition, the Payroll Manager
 can choose the name for these codes in order to match them with the filing
 statuses defined by the particular jurisdiction. Employee Tax Setup allows
 the Payroll Manager to assign the applicable user-defined filing status, and
 Check Calculation calculates income tax withholding based on the particular
 filing status for that employee.

ExemptionsEnter the number of federal exemptions
 that this employee is claiming. Repeat as needed for permanent work state,
 resident county and resident local, regardless of whether a tax code is entered
 for these rows.
Note Regarding Canadian
 Provinces
Up to 99,999 exemptions
 may be entered in this field for Canadian employees. The payroll manager
 should assign $1 as the exemption rate in the [Tax Table Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/tax-table-maintenance) screen. By
 assigning a rate of $1, the Check Calculation will automatically apply the
 correct dollar amount when determining the wages subject-to income tax.

Example: If the employee's exemption is $12,345,
 the Employees exemption will be set to 12,345. In the setup for the
 corresponding tax code, the exemption amount for Married, Single, Head of
 Household, and Other are each set to $1. During Check Calculation, the
 annualized gross pay subject-to income tax will be reduced by $12,345 before
 computing the income tax deduction.

Income tax overridesSelect to enter any income
 tax override types (% of gross,
 fixed amount, add-on) and amounts for the employee.
If the Federal filing status is 'US', the override window
 will contain additional fields for W-4 federal withholdings:

- Two jobs in total?

- Dependents claimed annually

- Other annual income

- Other annual deductions

- Extra withholding by pay period

Permanently override resident and work state unemploymentSelect to
 specify a permanent unemployment state in place of the resident and work state
 settings.
Unemployment stateNote: Enabled only when the
 Permanently override resident and work state unemployment checkbox is
 selected.
 Enter a state code or double-click to select from a list. This permanent unemployment state code
 will display on the Employee Master Report.
Permanently override resident and work state disability (SDI)Select to
 specify a permanent state disability insurance code in place of the resident and work state
 settings. When calculating SDI during payroll processing, the system ignores any resident and work states, and any temporary work state rules.
Disability insurance stateNote: Enabled only when the
 Permanently override resident and work state disability (SDI) checkbox is
 selected.
 Enter a state code or double-click to select from a list.
Temporary work
Override typeSelect an override type for the
 temporary work: State,
 County or Local.
CodeEnter a tax code for the selected
 override type, or press F4 to search for tax codes, up to 10 characters are allowed.
 The corresponding description will display to the right of this field.
Income taxSelect E from the drop-down menu if
 employee is exempt from state, county, or local income taxes for the temporary
 work; otherwise, press Enter to accept the system default of Taxable.
DisabilitySelect E from the drop-down menu if
 employee is exempt from FICA or SDI taxes for the temporary work; otherwise,
 press Enter to accept
 the system default of Taxable.
UnemploymentSelect E from the drop-down menu if
 employee is Exempt from unemployment insurance taxes for the temporary work;
 otherwise, press Enter to accept the system default of Taxable.
Filing statusSelect one of the filing status codes
 from the drop-down menu for the temporary override.
ExemptionsEnter the number of federal exemptions
 that this employee is claiming. Press Enter if this field does not
 apply.
Override typeSelect an income tax override type
 (% of gross, fixed amount,
 add-on) and specify override amount for the
 employee . If this field is left blank, the field will default to 'No
 override'.
Override types will default from this screen
 before going to the Tax Tables.

Res income taxSelect the employee's income tax status
 in their resident state.
Res disabilitySelect the employee's FICA or SDI tax
 status in their resident state.
Res unemploymentSelect the employee's unemployment
 insurance tax status in their resident state.
