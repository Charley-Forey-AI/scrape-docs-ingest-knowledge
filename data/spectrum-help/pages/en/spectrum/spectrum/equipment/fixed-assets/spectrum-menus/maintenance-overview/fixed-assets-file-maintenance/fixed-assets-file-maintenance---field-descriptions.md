---
title: "Fixed Assets File Maintenance - Field Descriptions | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/fixed-assets-file-maintenance/fixed-assets-file-maintenance---field-descriptions"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/equipment/fixed-assets/spectrum-menus/maintenance-overview/fixed-assets-file-maintenance/fixed-assets-file-maintenance---field-descriptions"
---

# Fixed Assets File Maintenance - Field Descriptions

Use the table below for assistance when entering fields on this screen.
FieldsDescriptions
SearchYou can search by asset number, asset description, G/L control code,
 Department code or Equipment code.Note: Only a partial
 entry is needed and the software will return any relative results. This
 allows you to filter your asset list.

G/L control codeEnter the G/L control code being assigned to this asset, or press
 F4 to select from a list of valid control codes.
 This must be a valid control code previously assigned in G/L
 Control Code Maintenance. Following entry of a code, the full
 corresponding description will display.
Asset numberEnter a unique code/number to be used in identifying this asset, or press
 F4 to select from a list of valid asset
 numbers.
Sequence #Enter a sequence number from 1 to 9. Enter 1 for assets being entered for the first time. Sequence
 numbers are changed only when the depreciation method changes. Press
 F4 to select from a list of valid sequence
 numbers.If a depreciation method should happen to change, the new sequence information
 should be a duplicate of the old, showing a different depreciation method
 and sequence. Also, when changing depreciation methods, change the
 Status field to Inactive
 for the older, obsolete depreciation method.

StatusSelect an option to assign a status to this asset.
Properties
Equipment codeIf an equipment code is entered, then the Update Depreciation to Master will
 post the entries to Equipment Control depreciation transaction file (DLI
 Entry), not the General Ledger, for depreciation. Enter an equipment code,
 or press F4 to select from a list of valid equipment
 codes.Note: If the equipment code status is set to
 Retired, data entry is prevented. If the equipment
 code status is set to Inactive, a warning message
 displays.
Cost center information:
Spectrum allows entry of an equipment code only if you have permission to assign that code. Spectrum compares the equipment code's cost center with cost centers in your operator's assigned cost center scheme, and if the cost center is not present, then that equipment cannot be assigned.
Spectrum also validates that the equipment cost center matches the cost center assigned to the fixed asset. The fixed asset cost center may be left blank, in which case any equipment that is valid for your operator may be assigned to the fixed asset.

DepartmentEnter the department to which this asset is assigned, or press
 F4 to select from a list of valid department
 codes. The full department description will display next to the department
 code. This must be a valid department previously defined in
 Department Code File Maintenance.
Serial numberEnter the serial number of this asset.
DescriptionEnter the description of this
 asset.
LocationEnter the location of this
 asset.
VendorEnter the vendor from whom this asset was purchased, or press
 F4 to select from a list of valid vendor codes. If
 the Accounts Payable module is installed, this must be a valid vendor code
 previously defined in Vendor Maintenance. The full
 vendor name will display following the vendor code.Note: If the vendor code status is set to Not
 Used, data entry is prevented. If the vendor code status is
 set to Inactive, a warning message displays.
Cost center information:
Spectrum allows entry of a vendor code only if you have permission to assign that code. Spectrum compares the vendor's list of shared cost centers with cost centers in your operator's assigned cost center scheme, and if there are no common cost centers, then that vendor code cannot be assigned.
Note: The vendor cost center
 doesn't have to match the cost center assigned to the fixed asset because
 the Vendor field is simply a memo field.

Property typeEnter this asset's property
 type.
Capitalization
Date capitalizedEnter the date that the asset was put into service, or, if depreciation methods are being changed for this asset, enter the date on which the new depreciation method takes effect.The date display provides a four-digit year in order to assure the proper century of capitalization is recorded.

Date retiredEnter the date on which this asset was taken out of service.
Original valueEnter the original dollar value of this asset. Entry in this field is required.
Sales priceEnter the price for which this asset was sold, if applicable.
Bonus depreciation
Book bonus depreciationEnter the amount of extra depreciation taken for the book figures.
Tax bonus depreciationEnter the amount of extra depreciation taken for the tax figures, if applicable.
Other bonus depreciationEnter the amount of extra depreciation taken for the other figures.
Section 179If a lump sum deduction is being taken per IRS section 179, enter the deduction amount.
Investment tax creditIf MACRS tables will be used, enter 0. Otherwise, enter the amount of the investment tax credit for this asset.
Depreciation
MethodEnter the number corresponding to the depreciation method to be used for this asset:

- Straight Line

- Declining Balance *

- Sum of the Years' Digits

- Accelerated Cost Recovery System (MACRS)*The percentage rate entered for this depreciation method is the straight line rate times the declining balance percentage.

LifeEnter the life of the asset in months.
TableThe cursor stops in this column only if method #4 (MACRS) was entered in the Depreciation method field.Enter the code of the MACRS table to be used for this asset, or press
 F4 to select from a list of valid MACRS codes.
 This must be a valid MACRS code as defined in MACRS Table
 Maintenance.

Db%The cursor stops in this column only if method #2 (Declining Balance) was entered in the Depreciation method field. If declining balance is the depreciation method for this asset, enter the percentage to be used in calculating the depreciation.Double Declining Balance Example:
The user purchases an asset at a cost of $10,000, with a salvage value of $1,000. It is to be depreciated over the 60 months (five years), using the double declining method. The percentage to be entered is 20% times 200%, which equals 40% and is the rate that should be entered in the table.
This formula is: 1/5 = 20%, which is the annual straight time rate for an asset with a five-year life. Since double declining depreciation was chosen, this means we will use the straight line rate times 200%.
The user may also choose a 150% declining balance, so that the calculation in this example would be 1/5 X 150%, or 30%. This calculated percentage is then applied to the asset value, as follows:
Remaining value of asset = purchase cost lest salvage value less accumulated depreciation
Depreciation amount = remaining value of asset X the % entered in this field.

SalvageEnter the salvage value of the asset, if more than zero. This value must be added at the time the fixed asset is added; once depreciation has been calculated, access to this field is no longer permitted.
LTD depreciationThe total accumulated depreciation of the asset since it was acquired displays in the life-to-date column.
