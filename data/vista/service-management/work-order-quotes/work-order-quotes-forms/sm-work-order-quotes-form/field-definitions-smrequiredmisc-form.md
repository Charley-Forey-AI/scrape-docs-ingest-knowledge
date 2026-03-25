---
title: "Field Definitions: SMRequiredMisc Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-smrequiredmisc-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-order-quotes/work-order-quotes-forms/sm-work-order-quotes-form/field-definitions-smrequiredmisc-form"
---

# Field Definitions: SMRequiredMisc Form

The following is a list of field descriptions for the
 SMRequiredMisc form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Misc: Seq

Enter N, New, or +. The system will auto-generate a
 sequence number for the requirements entry.
For agreement services and work order quotes defaulting requirement records from a standard task (assigned on the Tasks tab), this field cannot be edited. However, you can add new requirement records.

## Misc: Task

Enter the task associated with this
 requirements entry or leave blank if this requirements entry is not related to a task.
 Press F4 for a list of valid tasks (those set up on the Tasks tab).

## Misc: Standard Item

Enter the standard item associated with this
 miscellaneous requirements entry. Press F4 for a list of valid standard
 items.
Leave this field blank if this miscellaneous requirements entry is not associated with a standard item.

## Misc: Description

Enter a description for this miscellaneous requirements entry, up to 60 characters.
 If you specified a standard item for this requirements entry, this field defaults the description defined for the standard item (in SM Standard Items). May be overridden.

## Misc: Cost Type

Enter the SM cost type for this miscellaneous
 requirements entry. Press F4 for a list of valid SM cost types.
If you specified a standard item for this requirements entry, this field defaults the cost type designated for the standard item (in SM Standard Items). May be overridden.

## Misc: Quantity

Enter the quantity for this miscellaneous requirements entry.

## Misc: Cost Rate

Enter the cost rate for this requirements line. Initially defaults the cost rate specified for the line's standard item in SM Standard Items. If you did not specify a standard item for this line, the cost rate defaults as blank.

## Misc: Cost Total

This field defaults the total cost for this requirements line. You may override the defaulted value. If you override the defaulted value, the system will automatically recalculate the Cost Rate.

## Misc: Billing Rate

This field only displays for work order and work order quote scopes with a Time and Materials pricing method, and agreement services with a Time of Service, Rate Template pricing method.
If you entered a standard item for this requirements line, this field defaults the billable rate from the standard item and cannot be changed.
If you did not enter a standard item for this required miscellaneous sequence, this field defaults as blank. Enter the billable rate for the sequence.

## Misc: Total Billable

Total Billable field on the Misc tab of the SM Service and SM Work Order Quotes forms.
If you entered a Standard Item for this requirements line, this field displays the total billable and cannot be changed.
If you did not enter a Standard Item for this
 required miscellaneous sequence, but you entered a Billing Rate, this field defaults the
 calculated total billable. If you override the default, the system will recalculate the
 Billing Rate. If you did not enter a value in the Billing Rate field, enter the total
 billable amount for this sequence. The system will automatically calculate the Billing
 Rate.

## Misc: Tax Type

If work covered by this miscellaneous line is taxable, specify the tax type:

- Blank

- 1-Sales

- 2-Use

- 3-VAT

For non-material related lines, only blank and Sales (US) or VAT (AU/CA) options are allowed for these lines.
For material-related lines (those referencing
 a taxable SM Cost Type with a Material cost type category), options allowed depend on the
 Material Tax
 Override option selected for the agreement service or work order quote scope
 and the billable status.
If Material Tax Override is:
Allowed Tax Types for Billable lines
Allowed Tax Types for Non-Billable lines

blank
blank, Sales (US), Use (US), VAT (AU/CA), or blank
blank or Use (US)

N-No Tax
blank (no tax)
blank (no tax)

S-Sales
Sales (US), VAT (AU/CA), or blank
blank

U-Use
Use (US) or blank
Use (US) or blank

## Misc: Tax Code

 The Tax Code field on the Misc tab of the SM Service and SM Work Order Quotes
 forms.
Enter the tax code to use for determining the tax amount for this miscellaneous sequence. This field defaults the tax code for the Service Site or Service Center, depending on the Tax Source specified for the agreement service or work order quote scope. If no tax code is specified for the service site or service center, defaults as blank.
If the Material Tax Override option is set to N-No Tax for the agreement service, work
 order scope, or quote scope, this field defaults as blank. No taxes may be entered for the
 line.

## Misc: Tax Basis

Tax Basis field on the Misc tab of the SM Service and SM Work Order Quotes forms.
Enter the taxable portion of the total amount for this miscellaneous line. This field defaults as follows:

- If the Tax Type is 1-Sales, this field defaults from the from the Total Billable field.

- If the Tax Type is 2-Use, this field defaults from the Pretax Cost field.

- If the Tax Type is 3-VAT, this field defaults from the Total Billable field.

## Misc: Tax Amount

 The Tax Amount field on the Misc tab of the SM Service and SM Work Order Quotes
 forms.
Display only, the total tax amount for this material sequence (tax basis x tax rate).
