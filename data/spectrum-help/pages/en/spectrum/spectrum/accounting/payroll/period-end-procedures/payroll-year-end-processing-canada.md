---
title: "Payroll Year-End Processing (Canada) | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada"
fetched_at: "2026-04-03T20:47:07.463050+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada"
---

# Payroll Year-End Processing (Canada)

This topic walks through the different Spectrum functions you will use for year-end processing of Canada payrolls.

## Tax Table Maintenance

Visit the [Canadian Revenue Agency](http://www.cra-arc.gc.ca/tx/bsnss/tpcs/pyrll/menu-eng.html) (CRA) website for graduated income tax numbers used in revising the tax table for rate changes effective starting in the new year.

## T5018 Slips

When the 'Payroll reporting' option is set to 'Canada' in the Payroll Installation screen, you can build T5018 Slips, edit vendor data, review an edit listing, print the 'T5018 Slip' forms (on plain paper), and produce an export file for filing.
Refer to [T5018 Slip Maintenance](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/period-end-overview/t5018-slip-maintenance) for T5018 processing information.

## T4 Slip Processing

The Build T4 Slips screen clears the T4 file and calculates T4 information based on the payroll earnings history file. One row displays for every deduction and add-on code in the current company.

- Save the T4's from the prior year before starting.

- After reviewing this screen and making any necessary changes, select Continue to run the update. During the update, a number of values (taxes, earnings, add-ons, deductions) are allocated across the employee's T4 Slips whenever multiple provinces are present.

For additional information on completing this screen and producing T4s, refer to [New T4 Slip](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/t4-slip-maintenance/new-t4-slip) and the [Canada Revenue Agency (CRA) website.](http://www.cra-arc.gc.ca/E/pub/tg/rc4120/rc4120-e.html#P234_16836)

## T4 Slip Maintenance

Use this screen to enter T4 Tax information. Data entered here will be used to print the slip and create the electronic file.
Build the T4 information, make any needed modifications, and print the T4 slips to give to the employee. Instead of supporting a T4 Summary form, Viewpoint provides electronic files which don't require summaries.
For employees who had more than one province or territory of employment within the year, complete separate T4 slips. For each location, indicate the total remuneration paid to the employee and the related deductions, such as CPP/QPP contributions, EI premiums, PPIP premiums, and income tax.
The software supports up to six "Other" codes per employee. In the event that the employee has more than six of these codes, you must create additional T4 Slips here.
ColumnsDescriptions
Payer tax IDDefault value is based on setup. Accessible only when Entities are used.
Employee codeEnter the employee code here.
ProvinceThis is the 2 digit province or territory code. If the employee worked in the United States, use US.
Last name
First name
The employee's last and first name display.
Social insurance #The employee's Social Insurance Number (SIN) displays. If the employee doesn't have a SIN, enter nine zeros.
14 - incomeThis is the total employment income before deductions. It includes all salary, wages, bonuses, vacation pay, tips, honorariums, director's fees, management fees, and executor's and administrator's fees for administering an estate.
22 - income taxThis is the total income tax deducted from the employee's remuneration and retiring allowances.
Tax codeTax codes reflect any employment commissions, taxable allowances and benefits, deductible amounts, fisher's income, and other entries if they apply.
Form #All forms start at 01 and increase sequentially.

## Cost Center Information

If cost centers are being used in this company, then when adding or editing employees in the T4 Slip Maintenance screen, Spectrum allows the employee code to be entered only if you have permission to access the employee. Spectrum compares the cost center assigned to the employee with cost centers in your operator's assigned cost center scheme, and if the cost center is not included, then entry of that T4 is not allowed.
If entity tracking is enabled for the current company in the Enterprise Installation screen, the employee T4 records display based on whether the operator has authorization for the assigned entity. If at least one authorized cost center is assigned to the specified entity code, all T4 Slips for that entity display.

## T4 Slip Listing

Use this listing report to review T4 Tax information prior to year-end filing, including the total number of employees and the total number of slips that will need to be printed.
The Employee code defaults to all employees unless a saved selection is present.
While used as a selection field, the actual Federal tax ID does not display on the report for each employee.
If cost center entity tracking is being used in the current company, an 'Entity' code selection field is available. The software verifies that the operator has security authorization for the selected entity before proceeding.

## Print T4 Slips

Per the CRA, companies aren't required to print their "Payroll account number" on the T4 slip.
Important: For each employee, the Crystal Report print two slips for one employee, followed by the T4 instructions, so you may opt to print on both sides of the paper.
Refer to the table below for assistance when completing this screen.
FieldsDescriptions
Employee codeDefaults to ALL employee codes unless a saved selection is present.
EntityThis field displays only if cost centers are being used and entity tracking is also enabled in the current company.
Enter or select an Entity code to include T4s for that entity. The software verifies that the current operator has security authorization for the selected entity before proceeding. If this field is left <blank>, the main company entity is used and the form prints the company name and address from Company Installation.
The system includes all employee forms within the specified entity which match all other starting screen selection criteria.

YearEnter the four-digit year.
Print employer's 'Payroll account number'?Clear by default because CRA specifications state the employee's copy should not show the employer's number.

## Export T4 File

Use this screen to compile T4 Tax information and create the XML file for year-end electronic filing.
See the [CRA's document](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/rc4120/employers-guide-filing-t4-slip-summary.html) "Employers' Guide Filing the T4 Slip and Summary" for information on how to complete this screen.

Related information

- [Terminology](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/terminology)

- [Key Assumptions](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/key-assumptions)

- [Important Rules](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/important-rules)

- [Allocating Earnings](/en/spectrum/spectrum/accounting/payroll/period-end-procedures/payroll-year-end-processing-canada/allocating-earnings)
