---
title: "SM Adv. Non-Material Overrides Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-adv.-non-material-overrides-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-adv.-non-material-overrides-form"
---

# SM Adv. Non-Material Overrides Form

Use the SM Adv. Non-Material Overrides form to enter override
 markup rates for non-material purchases on a work order by cost type and cost type break
 points. Access this form by double-clicking the Cost Type Overrides grid in the
 SM Advanced Non-Material form.
Once set up here, the system applies the appropriate markup rate when
 capturing non-material purchases on a work order based on the cost type specified on the
 work completed purchase line or work completed miscellaneous line. If no cost type match
 is found, the system uses the rate break points defined in the SM Advanced
 Non-Material form or the standard non-material markup rate defined for the rate template
 to determine which markup rate to use.

## Rate Break Point Overrides

You can override the markup rates defined for cost types by setting up break point rates on the Rate Break Points tab (these rate break points differ from the break point rates defined in SM Advanced Non-Material form).
 Break points allow you to define multiple levels of markup rates based on incremental dollar values. When you capture non-material purchases for a work order, the system looks for a cost type match. If one is found, it then looks at the rate break points and applies the markup rate based on where the item's total amount falls in the defined break points.
For example, you set up your break points as follows:
Break Point ValuePercent
1,000.0000010.00000
25,000.000006.00000
50,000.000004.00000
100,000.000002.00000

You then enter a non-material work completed purchase line in SM Purchase Order Entry, with a Total of 5,600.00. Because the Total falls between the 1,000.00000 and 25,000.00000 breakpoints, the system uses the 10.00000 markup percent.
If a line's total amount is less than the first break point, the system uses the cost type's markup rate.Note: You can also define override rates for non-material purchases at the customer, service site, and Effective Date levels. For detailed information about the hierarchy used to determine the markup rate for non-material purchases, see [Non-Material Purchases Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases/non-material-purchases-rate-hierarchy).

Click the following link for more information about using this form.
[Set up Override Rates for Non-Material Purchases](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases)

Related information

- [SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)

- [Set up a Rate Template](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-a-rate-template)
