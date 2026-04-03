---
title: "Equipment Ownership Information - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-ownership-information/equipment-ownership-information---field-descriptions"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-ownership-information/equipment-ownership-information---field-descriptions"
---

# Equipment Ownership Information - Field Descriptions

Use this table for reference when completing the fields on this screen.
Fields
Descriptions

Acquisition

Original cost
Enter the purchase cost for this equipment. Entry in this field is not required, but a cost must be entered if the user wishes to use Depreciation processing.

Date
Enter the purchase date for this equipment. Entry in this field is not required, but a date must be entered if the user wishes to use Depreciation processing. The date display provides a four-digit year in order to assure the proper century of acquisition is recorded.

From
Select the source from which the equipment was purchased.

Condition
Select the equipment condition.

Type
Select the purchase type.

Road Usage
Select from the drop-down menu to designate this equipment as on road or off road. When adding new equipment this field defaults to On road unless the meter type in the Equipment File Maintenance screen has already been specified for Hours or Usage (hours).

Entry date
Enter the date this equipment was entered into the system. The system defaults the current Equipment Control processing date. If that date is not yet set up it will default based on the system date.

Cost accruals

Insurance
Enter the annual insurance cost for this equipment.

License
Enter the annual licensing cost for this equipment.

Depreciation
Enter the depreciation cost (per method) for this equipment.

Method
Select the depreciation method for the equipment from the drop-down menu: Annual, Meter, or Hour. In order for the system to accurately calculate a depreciation cost per year, the user must enter an original purchase date and original purchase cost in the purchase Date and purchase Cost fields.
Annual

1.  In the Depreciation field, enter the amount per year (for example, if the Equipment cost is 50,000, depreciated over 5 years, enter 10,000).

1.  The build calculation is 1/12th of amount.
Meter

1. In the Depreciation field, enter the amount per meter (hours, miles, kilometers).

1. Add/locate meter reading.

1. The build calculation is meter per period multiplied by the depreciation amount (for example, if the meter reading is 100 and depreciation amount is 2.50, the calculation is 250.00).
Hours

1. In the Depreciation field, enter amount per usage hour (revenue). In Meters, enter meter type 'Hours' or 'Usage hours'.

1. Add/locate 'Usage hours' in Revenue History (entered through EC Revenue Transactions).

1. The build calculation is the usage hours per period multiplied by the depreciation amount.

Current market value
Enter the current value of the equipment. The value entered here cannot exceed the Original cost value.

Retirement

Retired date
Enter the date that this equipment was retired, if applicable. Entry in this field does not require that the equipment status be set to Retired in the [Equipment Main Properties](/en/spectrum/spectrum/equipment/equipment-control/spectrum-menus/maintenance-overview/equipment/equipment-main-properties) but if you do enter a date in this field, a dialog box displays and you will be asked if you want to reset the status to Retired.

Equipment sold?
Select this checkbox if the equipment has been sold. If selected, three additional fields will display, asking for the sell price, the date sold, and to whom the equipment was sold.

Sell price
This field is only enabled if the Equipment sold checkbox is selected. Use this field to record the price that the equipment sold for.

Date of sale
This field is only enabled if the Equipment sold checkbox is selected. Use this field to record the date that the equipment sold.

Sold to
This field is only enabled if the Equipment sold checkbox is selected. Use this field to record the name of the person or company that purchased the equipment.
