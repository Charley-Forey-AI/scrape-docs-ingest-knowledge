---
title: "Wage Code File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/wage-code-file-maintenance/wage-code-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/wage-code-file-maintenance/wage-code-file-maintenance---field-descriptions"
---

# Wage Code File Maintenance - Field Descriptions

Use the table below for reference when completing the fields on this screen.
Fields
Descriptions

Properties tab
Use this tab to establish a wage code in Spectrum (or change an existing one), including wage descriptions, hourly wage rates (up to nine levels), and to schedule wage rate changes for any future date.
Important: When you want to change a wage rate and/or effective
 date it is necessary to add a new rate because the old rate and dates are
 still there for the previous month's entries to calculate against. The
 current payroll processing date determines which rate displays in this
 screen (when editing existing rates).

Wage code
Enter the new wage code, up to 10 characters are allowed. If you are editing a wage code, no entry is allowed.

Union code
Enter the union code (up to 10 characters) to apply to the wage code or press F4 or double-click on this field to select from a list of available union codes. An alert message will display if the union code entered has an Inactive status, but you will be allowed to continue entry. If you are editing a wage code, no entry is allowed.

Abbreviated wage description
Enter an abbreviated description (up to 10 characters) for the wage code.

Full wage description
Enter the full description (up to 30 characters) of this wage code. When the Show employee title on certified reports checkbox in the Payroll Installation screen is not selected, the full wage code description appears if wage codes are used. If rates were set up in the union code file, those rates will default here. They may be accepted or overwritten, as necessary.
The Certified Payroll Report can be configured to use either the employee title or the wage code/union code descriptions. When the wage code/union code descriptions are used, the following hierarchy applies:

1. The software will first look to the wage code for the Full Wage Descriptions. If one exists,the report uses this description.

1. If a description does not exist, the software then looks to Union File Maintenance > Rates screen. The software then determines the level number
 entered on the time card line. The description used is a combination
 of the Union > Rates PLUS Level to determine the appropriate description for the
 report.

Worker's compensation code
Enter a worker's compensation code, or double-click on this field to select
 from a list of available worker's compensation codes. Entry in this field is
 optional. Please refer to the Worker's Comp Code
 Maintenance section for default hierarchy information.

Certified labor code
This field is applicable for those using the AASHTOWare XML electronic
 reporting feature. Data from this field will be written to the XML File.

Benefit tier
Specify a benefit tier for the selected union code. If left blank, all standard union add-ons and deductions will be calculated during Payroll Processing.

Status
Select to designate the wage code as Active or
 Inactive.

Hourly wage rates

Regular
Enter the total regular hourly rate for all nine wage levels, or window to
 enter regular hourly rates and have the software calculate all other rates.
 This window is used in conjunction with gross pay checkbox having
 been selected in the Union File Maintenance screen;
 by double-clicking on this field, the base will be increased by amounts to
 be included.
Base Rates
This window is used to either look up or enter base hourly rate amounts for use during payroll calculation. The base figure is used when calculating percent of base add-ons and deductions. The total rate is used for payroll tax purposes.
Entry of regular hourly rates for all nine levels may be done in this window. The software calculates overtime and double time rates based on the regular hourly rates entered here. Those calculated amounts may be accepted or overwritten, as desired.
Entry of wage rates for all levels in this window will cause rates to default to the corresponding fields for levels two through nine on the screen.
This window is available for the regular, overtime, and double overtime columns only on line one; the window is only available in level one.
Base Enter the base
 rate per hour for all levels.
Fringe If, on the
 main screen of Union File Maintenance, the gross pay checkbox is
 selected, fringe benefit per hour is calculated by the software and
 displayed. If none of the deduction codes are to be included in gross pay,
 this fringe field remains blank.
If the workday variable is used, the number of workdays will be treated as zero when calculating the fringe rate for deductions flagged to 'Include in gross pay.'
Total rate The total
 rate per hour (base plus fringe) is calculated by the software and
 displayed. This total rate will also display on the screen.

Overtime Double time
The software calculates overtime and double time rates based on the regular hourly rates entered . Those calculated amounts may be accepted or overwritten.

Bill code
For Time + Materials purposes, enter the billing code for each level. This field is not used of the Time + Materials module is not installed. Double-click on this field to select from a list of available labor billing codes.

Standard job rates
Enter the standard labor rates for Regular,
 Overtime, and Double time
 hours that will be used to post to Job Cost (if applicable). These rates
 will only be used when the option to Post to Job Cost using
 standard labor rates? is selected on the Payroll Installation > Defaults screen.
For more information about standard job rates, refer to the [Standard Costing in Payroll](/en/spectrum/spectrum/accounting/payroll/in-depth-overview/standard-costing-in-payroll) in-depth article.

Rate history tab
Use this tab to add or modify scheduled rate adjustments for the selected employee. An initial entry will appear in the list box when the employee is added based on the new employee's hire date; if no hire date is selected, then the current Payroll processing date will appear. The list box automatically sorts the data by Year effective date.

Effective date
This field defines the date on which the wage rate goes into effect. A future date may be selected. Press Enter to accept the default Payroll processing date, double-click on this field to select a different date.

Descriptions
Enter a description of the wage rate revision.

Hourly wage rates

Regular
Enter the regular rate for this pay level, or press Enter to accept the default rate. Double-click on this field to view base rate information for regular hours.

Overtime
Enter the overtime rate for this pay level, or press Enter to accept the default rate. Double-click on this field to view base rate information for overtime hours.

Double time
Enter the double time rate for this pay level, or press Enter to accept the default rate. Double-click on this field to view base rate information for double time hours.

Bill code
Enter the time and material billing code for this phase, or double-click on this field for a list of available codes. This is only used if the Time + Material module is installed and a Time + Material job is used.

Related information

- [Worker's Compensation Hierarchy](/en/spectrum/spectrum/accounting/payroll/default-hierarchies-overview/workers-compensation-hierarchy)
