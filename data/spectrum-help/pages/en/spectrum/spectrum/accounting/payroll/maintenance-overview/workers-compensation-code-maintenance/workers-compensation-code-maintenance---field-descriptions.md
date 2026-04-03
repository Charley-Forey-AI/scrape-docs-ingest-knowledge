---
title: "Worker's Compensation Code Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance/workers-compensation-code-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance/workers-compensation-code-maintenance---field-descriptions"
---

# Worker's Compensation Code Maintenance - Field Descriptions

Use the table below as a reference when completing or editing fields in the Worker's Compensation Code window.
Fields/Buttons
Descriptions

Worker's compensation base code
This must be a valid base code previously set up in [Worker's Comp Base Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance/workers-comp-base-code-maintenance). When a worker's comp code is selected here, then the corresponding worker's compensation 'covered earnings' will be adjusted (raised) when the add-on is recorded in the time card file and the rate per $100 computation will be performed during Check Calculation.

State code
 This must be a valid state code set up in the tax tables, up to 10 characters are allowed. When a worker's compensation code will be used in multiple states, the screen must be completed once for each state, entering the state code in this field.

Properties

Descriptions
Enter a description for the worker's comp code in this field.

Rate per $100
Enter the worker's compensation rate that should be paid per one hundred dollars of gross income. The cursor will skip the next two prompts if data is entered in this field. A drill-down window is also available for entering up to 10 multiple rates with descriptions. [Component Rate Detail](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/component-rate-detail).

Entity Override button
This button only displays if 'Entity tracking' is enabled in Enterprise Installation and this company is operating in the US and this is not the US tax code. Click this button to open the Entity-Specific Rates per Hour or Entity-Specific Rates per $100 window and enter the entity-specific worker's compensation rates here.
Note: The 'main company entity' will always read for the general
 rate during the pay cycle.
An Optional Component Rate Detail window may also be available. This displays when accessing the 'Rate' column when accessing this sub-window for an entity. This window displays the same component 'Description', 'G/L account' and G/L 'Description' recorded in the main 'Rate Detail' sub-window for this code and state.

Rate per hour deduction rate
Enter the deductible amount per hour, or press Enter to accept the corresponding default rate that displays.
For Washington State employers, the special Labor and Industries employee deduction rate and total (composite) rate can be entered in the rate per hour fields. These rates are based on hours worked (not vacation, holiday, and so forth) and are used to compute the employee withholding amount and the employer burden. They are reported on the Worker's Comp Rate Per Hour Report.

Rate per hour total rate
Enter the composite rate per hour for this class, or press Enter to accept the corresponding default rate that displays.

Liability G/L account
Enter the General Ledger code for the worker's compensation liability. No entry is required if the account status is Not Used.

Aatrix electronic tax type
If you are using Aatrix for eFiling tax forms, select the Aatrix electronic tax type code that maps to the Spectrum tax code in this field.
Note: Aatrix eFiling is only available to hosted customers.

Calculation method
To view an example of the difference between the two calculation methods, [Calculation Method Example](/en/spectrum/spectrum/accounting/payroll/data-entry/payroll-payment-processing/calculation-method-example).

Rate per $100 limits

Limit basis
Select to make the limit basis applicable to all codes in this state or only to this code.

Limit method
In the Limit method field, select whether the worker's compensation has no limit, is limited per pay cycle, or has an annual cap.

-  If you select No limit, the system will calculate worker's compensation on all covered earnings and add-ons recorded in the time card file.

-  If you select Annual limit, the system will apply the tax rate on a year-to-date basis for an employee up to the limit specified in the Rate per $100 limit field (below).

-  If you select Pay cycle limit, the system will apply the tax rate across check sequences for an employee up to the limit specified in the Rate per $100 limit field (below).

- Quarterly and monthly limit options are also available.

Policy start date
Enter the date when the policy should go into effect.

Rate/$100 limit
Enter a numeric limit.

Buttons

Listing
Click this button to display the [Worker's Comp Code Listing](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance/workers-comp-code-listing) screen where you can generate a report of codes by code or state.

Base code
Click this button to display the[Worker's Comp Base Code Maintenance](/en/spectrum/spectrum/accounting/payroll/maintenance-overview/workers-compensation-code-maintenance/workers-comp-base-code-maintenance) screen where you can establish a set of codes to be used for specific types of work.
