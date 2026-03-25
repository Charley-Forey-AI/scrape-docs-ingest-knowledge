---
title: "Field Definitions: EM Asset Setup Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form/field-definitions-em-asset-setup-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/equipment-management/depreciation/em-asset-setup-form/field-definitions-em-asset-setup-form"
---

# Field Definitions: EM Asset Setup Form

The following is a list of field descriptions for the EM
 Asset Setup form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  Equipment

 Enter the equipment (from EM Equipment) for which to set up this asset.

## Asset

Use this field to identify a unique asset. This allows you to set up multiple asset depreciation items for a single piece of equipment.
 Enter a unique asset code. The asset code can be up to 20 digits long.

## Description

 Enter a description of the asset. The description can be up to 60 characters long.
If you are creating the first asset on the equipment and the equipment is inactive, the description of the equipment will populate in this field along with the text "Status = Inactive".
Note: Equipment is inactive if the Inactive box on
 the Info tab of the [EM Equipment ](/en/vista/vista/job-resources/equipment-management/setupmaintenance/about-the-em-equipment-form)
 form is checked.

##  Purchase Price

 Enter the purchase price of this asset.

##  Residual Value

 Specify the residual value for this asset; that is, the expected value of this asset when fully depreciated. The amount specified here should be the amount that you do not expect to depreciate.

##  Sale Price

 Enter the sale price for this asset, if applicable.

##  First Month to Depreciate

For US and Canadian companies only.
 Specify the first (calendar) month for which to calculate depreciation on this asset.

## Depreciation Start Date

For Australian companies only.
Enter the date on which to start depreciating
 this asset. This will typically be the date you first use the asset or install it to be
 ready for use.

##  # of Months to Depreciate/# of Months Held

For US and Canadian companies
This field displays as # of Months to
 Depreciate.
 Enter the total number of months for which to calculate depreciation on this asset. This will typically be the expected ‘useful’ life of the asset.
 For Australian companies
This field displays as # of Months
 Held.
Enter the total number of months, beginning
 with the Depreciation Start Date, that this asset will be held. This will typically
 be the expected ‘useful’ life of the asset.

## Total Amt to Depreciate

This field displays the total amount to depreciate, which is the purchase price less the residual value.

##  Month Disposed Of

 For US and Canadian companies only.
Leave blank until asset has been disposed of, and then enter the last month for which depreciation will be taken. Make sure you recalculate the schedule to prevent any further depreciation of the asset.
Note: When the depreciation schedule is recalculated, the system will not recalculate any of the schedule’s values; it will only truncate the schedule, removing any months after the specified disposal month.

## Date Disposed / Transferred

For Australian companies only.
Enter the date this asset was disposed of (e.g. sold) or transferred to a low-value pool.

##  Method

 Indicate which of the following depreciation methods applies to this asset.
Note: The declining balance method of depreciation changes
 based on the country set for the company. The country is determined by the value in the
 Default
 Country field in HQ Company Setup.For US companies

- Straight Line - Select this option to
 depreciate the same amount each month.

- Declining Balance - Select this
 option to base the monthly depreciation amount for this asset on an acceleration
 factor (specified in the Factor field). This method will
 automatically switch to straight line at the point when the depreciation amount
 calculated by the straight line method is greater than declining balance. For more
 information, see [Declining Balance Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation).
For Canadian companies

- Straight Line - Select this option to
 depreciate the same amount each month.

- Declining Balance - Select this
 option to base the monthly depreciation amount for this asset on an acceleration
 factor (specified in the Factor field). For more
 information, see [Declining Balance Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation).
For Australian companies

- Straight Line (Prime Cost) - Select
 this option to depreciate the same amount each month.

- Diminishing Value - Select this
 option to base the monthly depreciation amount for this asset on an acceleration
 factor (specified in the Factor field). For more
 information, see [Declining Balance Depreciation](/en/vista/vista/job-resources/equipment-management/depreciation/about-depreciation/about-declining-balance--diminishing-value-depreciation).

##  Factor

 Specify the acceleration factor for calculating depreciation on this asset. Entry must be greater than 1.00 but less than or equal to 2.00. A factor of 1.00 would be identical to using the straight-line method. A factor of 2.00 will take twice as much the first year as would be taken using the straight-line method.

##  Accumulated Depr

 Enter the GL account to use for accumulated depreciation for this asset. Entry in this field is necessary only if overriding the Accumulated Depreciation GL Account specified for this equipment’s department in EM Departments.

##  Depreciation Exp

 Enter the GL account to use for depreciation expense for this asset. Entry in this field is necessary only if overriding the GL account specified for this equipment’s depreciation cost type in EM Departments.

##  Asset

 Enter the GL account to use for this asset. Entry in this field is necessary only if you will be running reports that show assets by asset account.

## Recalculation for Year Ending

This field displays only when recalculating the depreciation schedule for ‘Declining Balance’ method.
Specify the year-end month of the fiscal year with which to begin recalculation of this asset’s depreciation schedule.
Note: Must be a valid fiscal year end month set up in the EM
 company's GL company (specified in GL Co field in EM Company
 Parameters).

## Month

Display only, the month in which to take the calculated depreciation.
 For US and Canadian companies
The months generated for this schedule are
 based on the vales entered in the First Month to Depreciate and the
 # of Months to
 Depreciate fields (on the Info tab). You can manually add or delete months
 in the schedule; however, you cannot change the month for an existing entry.
For Australian companies
The months generated for this schedule are
 based on the vales entered in the Depreciation Start Date and the
 # of Months
 Held fields (on the Info tab). You can manually add or delete months in the
 schedule; however, you cannot change the month for an existing entry.

##  Amount to Take

 This amount is calculated automatically for each month once you run the schedule calculation function (Calculate button). You may override this amount if necessary.

##  Amount Taken

Enter the total depreciation amount taken for the specified month. Initially defaults the amount calculated when processing depreciation (in EM Depreciation Processing). If you change this amount, it will have no affect on existing depreciation detail in the Cost Detail file (EMCD), nor will it affect any depreciation costs already posted to GL. Changes will only affect the depreciation amount calculated by the system the next time you run the EM Depreciation Posting program.
