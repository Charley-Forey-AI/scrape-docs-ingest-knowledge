---
title: "Equipment Control Installation \u2013 Properties | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-installation--properties"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/equipment-control-installation-overview/equipment-control-installation--properties"
---

# Equipment Control Installation – Properties

 Use this screen to select default properties settings for
 the Equipment Control module.
These settings can be changed at any time.Note: When the installation screen is selected for the first time, the system will beep and a
 dialog box stating "CONTROL RECORD HAS NOT BEEN CREATED OK TO PROCEED" will display on
 the screen. Once this installation screen has been completed and the information saved,
 the message will not appear again.

Fields
Descriptions

Validate make and model entries?
Select this checkbox if you want to require entry of pre-defined makes and
 models for equipment, components, and tires. When selected, equipment setup
 fields (for example, those found in Equipment) will
 provide a search window and will accept only makes and models that have
 already been set up in Make File Maintenance or
 Model File Maintenance.
When editing existing make and model field entries, validation only occurs when changes are made to these fields.

Automatically add transactions for attached
 equipment?
Select this checkbox if you want the software to automatically create new transactions in the data entry screens each time an equipment entry is added for a code that has attachments set up, or leave this checkbox clear if you wish to be prompted each time an equipment entry is added.

Multi-company?
Select this checkbox to allow equipment transaction information entered in this company to be distributed to other companies set up in Spectrum.
If this checkbox is selected, the system will allow you to specify an alternate company code. When you do this, the system will accept Equipment, G/L and/or Job Cost codes from the other company and will update accordingly.
If intercompany transactions are not desired, do not select this checkbox.

Payroll burden cost category
The system is prompting for the cost category where labor burden is to be
 recorded during Update Payroll. The system will use the burden cost
 category entered in this field during the payroll update when equipment cost
 (example: labor to repair equipment) is specified in Time Card Entry.

- Entry in this field does not apply when equipment
 usage is recorded in Payroll.

- Enter your desired cost category to be used by the
 system when payroll labor costs are updated to equipment control module.
 Be sure to include this cost category when you enter your cost categories
 using Cost Category File Maintenance.

- Entry in this field is irrelevant if the Payroll
 module is not installed in this company.

Equipment cost type
The system is prompting for the primary cost type designated in the job cost
 module for equipment used on jobs. Press F4 or double-click on this
 field to select from a list of available equipment cost types. The cost type
 designated in this field will be used during equipment job usage transaction
 entry as the default cost type. The system may also use the cost type
 entered in this field during the payroll update when job equipment usage is
 specified in the time card file. During the payroll update, the system will
 first use the cost type designated in the G/L chart of accounts for the
 equipment expense. If no cost type is specified there, the code designated
 in this field will be used during the payroll update. Equipment usage, based
 on the time card hours and rate, will be recorded in the job cost file using
 the job and phase specified on the time card line, and the cost type either
 from the G/L chart of accounts or this field.

Normal hours/week
Enter the number of hours that this piece of equipment will normally be used
 each week. This is used when using Enter Equipment Meter Reading. If
 an entry is made for a piece of equipment with an hour meter that exceeds
 this normal usage, a warning message will beep. If this field is left blank,
 no warning message will be given.

Normal miles/week
Enter the number of miles per week that this piece of equipment will normally
 be driven each week. During Enter Equipment Meter Reading, this
 figure is used to check for reasonable entries.

Normal kilometers/week
Enter the number of kilometers per week that this piece of equipment will
 normally be driven each week. During Enter Equipment Meter Reading,
 this figure is used to check for reasonable entries.

Default status
The system is prompting for the default status to display during the addition
 of a new piece of equipment in the Equipment screen.
 The status code must have previously been entered in the
 Equipment Status File Maintenance screen at the
 time of Transaction Entry.

Payroll burden type
Note: Entry in this field is irrelevant if the Payroll module is not installed
 in this company, or when equipment usage (EU) is recorded in Payroll.
The system is prompting for you to select the desired method for recording
 labor burden in equipment control files associated with equipment costs
 during Update Payroll. Select the desired burden costing method: Actual,
 Percentage of labor cost, or Dollar amount per hour.
The system will use the burden method entered in this field during the payroll
 update when equipment cost (example: labor to repair equipment) is specified
 in Time Card Entry and during the Transaction Entry - PR update.
If the specified payroll burden type is Percentage of labor cost or
 Dollar amount per hour, the system will prompt for burden amount;
 enter the chosen burden percentage (example: "32" for 32%) or dollar amount
 (example: "5" for $5.00/hr).

Post rental use from
The system is prompting for you to select either Accounts Receivable or Payroll, whether to update equipment usage information to the equipment cost history files from Payroll or from Accounts Receivable, to avoid double-posting rental revenue.

- If this field is set to Payroll, the equipment revenue history
 files will be updated for equipment usage on rental (non-job) Time Card
 Entry lines. The General Ledger will also be updated for this equipment
 usage. Equipment usage for jobs will be updated from Payroll regardless
 of entry in this field; this option relates specifically to rental usage.

- If this field is set to Accounts Receivable, the equipment
 revenue history files will be updated for equipment usage recorded in A/R Invoice Entry. The General Ledger
 will also be updated when invoices are updated for rental revenue. In
 this case, Payroll will not update equipment rental figures.
