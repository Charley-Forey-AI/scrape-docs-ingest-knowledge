---
title: "SM Advanced Non-Material Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-non-material-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-non-material-form"
---

# SM Advanced Non-Material Form

Use this form to enter override markup rates for non-material purchases on a work order by rate break point.
 Access this form by clicking the Advanced button in the Non-Material Purchases section of the SM Rate Template, SM Rate Template Effect Date, or SM Rate Override Base forms.
The system uses the overrides defined here to determine the markup rates used when entering non-material work completed purchase lines in SM Purchase Order Entry or PO Purchase Orders (SM work order lines only), and miscellaneous work completed lines via AP Transaction Entry or the Work Completed grid in SM Work Orders.
Rate break points allow you to define multiple levels of markup rates based on incremental dollar amounts. When you enter non-material purchases for a work order, the system applies the markup rate based on where the item's total cost amount falls in the defined rate break points.
For example, you set up your break points as follows:
Break Point ValuePercent
1,000.0000010.00000
25,000.000006.00000
50,000.000004.00000
100,000.000002.00000

 You then enter a non-material work completed purchase line in SM Purchase Order Entry, with a total cost of 5,600.00. Because the amount falls between the 1,000.00000 and 25,000.00000 breakpoints, the system uses the 10.00000 markup percent.Note: Break point rates override the standard non-material purchase rate defined for the rate template.

## Cost Type Overrides

You can enter override markup rates by cost type using the Cost Type Overrides tab. Markup rates defined by cost type override the break point rates defined on the Rate Break Points tab. For more information, see SM Adv. Non-Material Overrides.Note: You can also define override rates for non-material purchases at the customer, service site, and Effective Date levels. For detailed information about the hierarchy used to determine the markup rate for non-material purchases, see Non-Material Purchases Rate Hierarchy.

Click the following link for more information.
[Set up Override Rates for Non-Material Purchases](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-override-rates-for-non-material-purchases)
[Set up a Rate Template](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-a-rate-template)
[SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)
