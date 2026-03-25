---
title: "Add a New Effective Date Template | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/add-a-new-effective-date-template"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/add-a-new-effective-date-template"
---

# Add a New Effective Date Template

You can add Effective Date rate templates to control the rates used for

 equipment, labor, material, non-material purchase, and standard item override rates
by specific effective dates.


 You will only need to set up Effective Date templates if your equipment, labor, material, non-material purchase, and standard item rates change routinely and are applied based on a specific date.For example, if you have current rates that are effective through the end of quarter one and new rates that are effective beginning in quarter two, you would set up one Effective Date template for 01/01/YY and one for 04/01/YY.
If you enter a work completed line with a date of 02/15/YY, the system uses the Effective Date 01/01/YY template, since the entry date falls after 01/01/YY, but prior to 04/01/YY. However, if the work completed line date is 05/30/YY, the system uses the 04/01/YY template, since the entry date falls after 04/01/YY. Work completed lines entered prior to the first Effective Date template (in this case, 01/01/YY) will use the standard rate template to derive the appropriate rates.

1. Open the SM Rate Templates form.

1. In the Template field, enter the rate template for which to set up
 effective dates.

1. Select the Effective
 Date tab.

1. Click the Add button
 (below grid). The SM Add Effective Date form displays.

1. In the New Effective Date field, enter the effective
 date for the new template.


1. In the Copy
 From group box, select the type of rate template to copy:

- Basic Template - Copy a standard rate template

- Effective Date - Copy an existing Effective Date template

1. If you selected to copy a Basic
 Template, skip to Step 8.If you selected to copy an Effective Date template, use the Effective Date field to enter the effective date template to copy.

1. Click Add. The system copies the source template to the new effective
 date template and returns you to the SM Rate Template form.

1. [Update Rates for Effective Date Templates](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/add-a-new-effective-date-template/update-rates-for-effective-date-templates).
