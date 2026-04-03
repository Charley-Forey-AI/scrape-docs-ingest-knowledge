---
title: "Equipment Main Properties - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-main-properties/equipment-main-properties---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-main-properties/equipment-main-properties---field-descriptions"
---

# Equipment Main Properties - Field Descriptions

Use the table below for reference when completing the
 fields in this screen.

 Fields
 Descriptions
Identification
DescriptionEnter the full equipment description.
DivisionEnter the division code for this piece of equipment. This
 is used in conjunction with the Validate
 equipment division with G/L department field on the
 Equipment Control Installation screen.

 TypeEnter the equipment type code, or press Enter to select
 from a list of valid equipment types. The corresponding equipment type
 description will display to the right of the code. This must be an equipment
 type previously defined in Equipment Type File Maintenance; entry in this
 field is required.
YearEnter this equipment's two-digit year.
MakeEnter the make of this equipment (for example, on a 2012
 Ford LTD, enter "Ford"), or use the drop-down list to select from available
 makes as set up in the [Make File Maintenance](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/make-file-maintenance) screen. Entries may be up to 20 characters
 long.
ModelEnter the model of this equipment (for example, on a 2012
 Ford LTD, enter "LTD"), or use the available drop-down list to select from
 available models. Entries may be up to 20 characters long.
Serial # / VINEnter the equipment serial number or vehicle
 identification number, if desired. Entries may be up to 50 characters long.
RFID #Enter the Radio Frequency Identification number
 associated with this piece of equipment, if applicable.
GPS tracking #Enter the Global Positioning System number associated
 with this piece of equipment, if applicable.
Current info
Home yard AreaEnter the yard and location code you want to associate
 with this equipment, or double-click on these fields to select yard and
 location codes. Use this field to differentiate the home yard from the
 current location. For example, the home yard might be Seattle, but the
 equipment is currently parked at the Vancouver yard.
Current locationThe current location will be based upon the equipment GPS
 table.
Currently scheduledThe current job assignment displays if the Resource
 Scheduling module is present, and an inquiry button (adjacent to the
 Currently scheduled field) will open the Resource Scheduling > Equipment Schedule History Inquiry window.
Current defaults
Wage codeEnter the wage code for this equipment, or double-click
 on this field to select from a list of available wage codes. Up to 10
 characters are allowed.
When equipment hours are entered for this piece of
 equipment during payroll Time Card Entry, this wage code will default. Note
 that this code will not default if a default wage code has been entered in
 Job File Maintenance for the job on which this equipment is used. Wage codes
 must have been previously set up in Wage Code Maintenance.

Billing codeEnter the billing code for use in Time + Material. The
 billing code can be up to 10 characters. When equipment hours are entered
 for this piece of equipment in Payroll Time Card Entry, this billing code
 will default. A lookup window is available for viewing valid billing codes.
 Note: This field is relevant only if the Time
 + Material module is also installed.

Fuel code Enter the fuel code for this equipment, or double-click
 on this field to select from a list of available fuel codes.Note: An oil code cannot be selected for this
 field.

A/P invoice approval
Default routing code If invoice approval routing for equipment is being used,
 select an approval routing code to route invoices pertaining to equipment
 repairs and maintenance for approval.

Invoice dollar limit
Routing code over limit
The dollar limit which should trigger the use of the over-limit routing code, and the routing code to use when an invoice amount exceeds the dollar limit. If there is no established invoice dollar limit, leave this field blank.Note: You can opt to leave both fields blank and instead manage the approval routing by entering Approval Limits on the Routing Code. For additional information, see [Approval Limits](/en/spectrum/spectrum/accounting/accounts-payable/spectrum-menus/data-entry-overview/about-invoice-approval/approval-limits).

StatusEnter the status code associated with this piece of
 equipment's status, or double-click on this field to select from a list of
 available status codes.


- If an Inactive
 status code is selected and then an attempt is made to assign a new
 transaction to this equipment, the following message displays: Warning – Equipment code has inactive
 status. The user will be warned of its status throughout the application.
 To continue, select OK and proceed with entering
 the new data.

- If a Retired status code is selected and then an attempt is
 made to assign a new transaction to this equipment, the following message
 displays: Error – equipment code entered is
 not available for use. This error message disallows further data
 entry.

If you are using the Equipment Service System
(ESS) product and you have the Equipment Tracking module installed, you should
 review the equipment status codes used for Equipment Tracking operations and
 switch the status type of some Inactive codes to Active as necessary because
 all job site equipment interfacing with the ESS product must be assigned an
 Active status code.

Equipment image Use the Add button to upload an image file of the equipment that
 will then display as a thumbnail on the related InfoBar throughout the
 system. Select the Picture drop-down in the InfoBar to hide the image.
