---
title: "New Equipment | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/quick-equipment-setup-maintenance/new-equipment"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/quick-equipment-setup-maintenance/new-equipment"
---

# New Equipment

After clicking the New button on the main screen, this window
 displays and prompts for a minimal amount of information in order to add new equipment.
After this window displays, the software opens a new Spectrum tab.
When a quick-equipment Group code is specified and this code is set to copy the setting to the new equipment code, information in the Year, Make, Model, Type, Division, and Status fields defaults from the 'from' equipment code.
Fields
Descriptions

Use quick equipment setup?
Select this checkbox if you want fields to be copied from Equipment (for example, model, type, filters, and all notes) and define the equipment code mask with the next sequential number so you will have a numbering scheme based on an equipment group (for example, DZ001 for the first dozer).

Group code
This field only displays if the option to use quick equipment setup is selected. Enter or select a code from the available drop-down list.

Name

Equipment code
When a quick equipment Group code is specified above, the equipment code from 'Quick equipment setup' is assigned if a code with auto-numbering was designated.

Description
Enter the full equipment description.

Year
Enter this equipment's year (for example, on a 2012 Ford LTD, enter "2012").

Make
Enter the make of this equipment (for example, on a 2012 Ford LTD, enter "Ford"), or use the drop-down list to select from available makes as set up in the [Make File Maintenance](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/make-file-maintenance) screen. Entries may be up to 20 characters long.

Model
Enter the model of this equipment (for example, on a 2012 Ford LTD, enter "LTD"), or use the available drop-down list to select from available models. Entries may be up to 20 characters long.

Classification

Type
Enter the equipment type code, or press Enter to select from a list of valid equipment types. The corresponding equipment type description will display to the right of the code. This must be an equipment type previously defined in Equipment Type File Maintenance; entry in this field is required.

Division
Enter the division code for this piece of equipment. This is used in conjunction with the Validate equipment division with G/L department field on the Equipment Control Installation screen.

Status
Enter the status code associated with this piece of equipment's status, or double-click on this field to select from a list of available status codes.

- If an Inactive status code is selected and then an attempt is made to assign a new transaction to this equipment, the following message displays: Warning – Equipment code has inactive status. The user will be warned of its status throughout Spectrum. To continue, click OK and proceed with entering the new data.

- If a Retired status code is selected and then an attempt is made to assign a new transaction to this equipment, the following message displays: Error – equipment code entered is not available for use. This error message disallows further data entry.

Note: Regarding Equipment Status Codes and ESS:If you
 are using the Spectrum Equipment Service System
 product and you have the Equipment Tracking module installed, you should
 review the equipment status codes used for Equipment Tracking operations
 and switch the status type of some Inactive codes to Active as necessary
 because all job site equipment interfacing with the ESS product must be
 assigned an Active status code.

Cost center
This field associates the equipment with a particular cost center. When adding a new piece of equipment, the Cost center field must be completed, and the entry must be a valid cost center for your operator.
