---
title: "Field Definitions: SM Advanced Non Material Overrides Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-adv.-non-material-overrides-form/field-definitions-sm-advanced-non-material-overrides-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-adv.-non-material-overrides-form/field-definitions-sm-advanced-non-material-overrides-form"
---

# Field Definitions: SM Advanced Non Material Overrides Form

The following is a list of field descriptions for the SM
 Advanced Non Material Overrides form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

## Cost Type

Cost Type field on the SM Adv. Non-Material Overrides form.
Enter a cost type for non-material purchases based on cost type (instead of at the rate-template level).
Press F4 for SM Cost Types Lookup, or F5 to open the SM Cost Types form.

## Markup Percent

Markup Percent field on the SM Adv. Non-Material Overrides form.
Enter the override markup percent to apply to non-material Misc and Purchase work completed lines. Enter 5% as 5.00000.
 Non-material work completed lines are defined as follows:

- Miscellaneous lines specifying a non-material SM Cost Type (one with a cost type category other than M-Material) with no material specified or lines were where no SM Cost Type is specified and no material is specified.

- Purchase lines with a non-material SM Cost Type or null SM Cost Type and no material specified

The system applies this rate to the Cost Rate of the work completed purchase line to determine the Billable Rate.
Enter 0.00 if no markup will be applied to non-material purchases.

## Break Point

The Break Point field on the SM Advanced Non-Material form, Rate Break Points tab.
Enter the total dollar amount to use as a break point when calculating markups on non-material purchases for an SM work order.
When you enter a non-material work completed purchase or miscellaneous line, the system compares the line's total amount to the break points defined here to determine which markup rate to use. If the line's total amount reaches this break point amount, the system applies the markup rate specified to the right.

## Percent

The Percent field on the SM Adv. Non-Material Overrides form, Rate Break Points tab.
Enter the override percent to use when applying markups to non-material work completed lines referencing the SM Cost Type (specified on the Info tab) on an SM work order (for example, enter 5% as 5.00000).
 The system only applies this percentage when the total dollar amount for the work completed line reaches the break point amount specified in the Break Point field for this entry.
