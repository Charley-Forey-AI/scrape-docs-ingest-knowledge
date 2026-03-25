---
title: "Field Definitions: SM Technician Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-technicians-form/field-definitions-sm-technician-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-technicians-form/field-definitions-sm-technician-form"
---

# Field Definitions: SM Technician Form

The following is a list of field descriptions for the SM
 Technician form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Technician

Required.
Enter a code to identify this SM technician, up to 15 characters. Not validated.

-  Entering the employee's sort name (in all caps) or
 employee number as defined in PR Employees will automatically default the PR employee
 number in the Employee field below once you move off this field.

- Although you must associate this technician with a
 valid Payroll employee, you cannot press F5 from this field to access PR Employees.
 You must use the Employee field below to enter the
 PR employee to which this technician is associated. If the technician does not exist
 as an employee in PR Employees, you can press F5 from the Employee
 field to access PR Employees.

## PR Co

Enter the payroll company (set up in PR Company Parameters) to which this technician is associated. Defaults to the PR company specified for this SM company in SM Company Parameters.

## Employee

Enter the employee number (from PR Employees)
 that identifies this Service Management technician. Press F4 for list of
 valid PR employees for the PR company specified above. If you entered the employee's sort
 name or employee number (as defined in PR Employees) in the Technician
 field above, this field automatically defaults the PR employee number.

- Technicians set up here must first be set up in PR
 Employees and be flagged as Active. If you are adding a technician that has not been
 set up in PR Employees, you can press F5 from this field to go to the PR
 Employees form and set up the employee. When you are returned to this form, you can
 then enter the new employee number here.

- If you enter an employee that is flagged as "inactive" in PR Employees, the system displays "Employee is Inactive" message next to the technician's name/number once you save the record. You will be unable to reference the technician on SM work orders, or in SM Customers, SM Service Sites, SM Technician Preferences, SM Advanced Labor Overrides, or PR Timecard Entry.

## Rate

Enter the default labor rate to use when calculating estimated labor costs for service work performed by this technician on a work order. This rate will typically represent the total expected labor cost (per hour), and will therefore include the technician's base rate (as defined in PR Employees) plus burden.
Note: This rate will only be used if the pay type specified
 when entering work completed labor on a work order uses a Cost Method of
 0-Multiplier. The system will multiply this rate by the factor defined for the pay type to
 derive the Cost
 Rate for the labor line.
The system ignores this rate if the pay type's
 Cost
 Method is 1-Dollar Rate; in which case, the rate specified for the pay type
 is used.

## IN Co

The IN Co field on the SM Technicians form.
Entry in this field is only required if you will be
 specifying a default location in the IN Location field.
Enter the Inventory company from which this
 technician generally pulls parts when performing service work. Press F4 for a list
 of valid IN companies.
The company specified here will default as the IN company when entering work completed inventory lines (type 4-Inventory) in SM Work Orders that reference this technician. If you leave this field blank or you enter a company here, but leave the IN Location field blank, the work completed inventory line will default the IN Co from SM Company Parameters.

## IN Location

Entry in this field requires that you also enter a company in the
 IN
 Co field.
Enter the location from which this technician
 generally pulls parts when performing service work (e.g. service truck, warehouse, etc.).
 Press F4 for a list of valid locations (set up in IN Locations) for the specified
 IN company.
Note: The location specified here will default as the IN Location when entering work completed inventory lines (type 4-Inventory) in SM Work Orders that reference this technician.

## Active

Check this box to activate this technician. Technician will be available for selection when adding technicians to a dispatch board (in SM Dispatch Board Setup) or when entering transactions prompting for technician (e.g. work completed, required labor on agreements, etc.). In addition, technician will be included in "Active Technician" F4 lookups.
Uncheck this box to deactivate this technician. Technician will not be available for selection when adding technicians to a dispatch board (in SM Dispatch Board Setup) or when entering transactions prompting for technician (e.g. work completed, required labor on agreements, etc.). Technician will also be excluded from "Active Technician" F4 lookups; however, technician will be include in All SM Technician lookups.
Note: This flag is not associated with the Active flag in
 PR Employees. If a technician is flagged as Active and the employee is changed to inactive
 in PR Employees, the Active flag must be manually unchecked in
 SM Technicians in order to deactivate the technician and ensure accurate representation of
 the technician's status.

## Work Day: Monday - Sunday

Check the box for each day of the week (Monday through Sunday) that this technician works.
Leave the box unchecked for each day of the week that the technician is off.

## Work Hours: Start

Enter the starting work time, in 24-hr format.

## Work Hours: End

Enter the ending work time, in 24-hr format.

## Break: Start

Enter the starting break time, in 24-hr format.

## Break: End

Enter the ending break time, in 24-hr format.
