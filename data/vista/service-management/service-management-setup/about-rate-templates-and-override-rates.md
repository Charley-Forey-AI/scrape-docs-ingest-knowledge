---
title: "About Rate Templates and Override Rates | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates"
---

# About Rate Templates and Override Rates

SM uses rate templates to determine the labor, material, equipment, and non-material purchase rates used when capturing work completed on work orders (in SM Work Orders).
You can assign a rate template to a service
 site and the system will default that rate template each time you create a work order
 for the service site. If you do not assign a rate template to the service site, work
 orders will default the rate template as follows:

- For customer work orders, the system
 defaults the rate template specified for the customer in SM Customers. If no
 rate template is specified in SM Customers, no rate template defaults and you
 must assign a rate template before you can enter work completed lines.

- For job work orders, the system
 defaults the rate template as blank and you must assign a rate template before
 you can enter work completed lines.

If you charge the service site different
 rates for labor, equipment, materials, and non-material purchases based on specific
 criteria, you can set up override rates using the SM Rate Override Base form (accessed
 by clicking the Override Rates button). Override rates will only be applied if the
 criteria defined for an override rate matches the information entered on a work
 completed line in SM Work Orders. If no match is found, the system will use the rate
 template assigned to the service site to determine the rates to use.
Note: Since you can set up overrides at multiple levels
 (rate template, effective date, customer, service site, and work order quote), the
 system determines the correct rates to use based on a specific hierarchy. For more
 information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy), [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy), or [Material Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides/material-rate-hierarchy).
For more information about setting up
 override material rates, see [Material Rate Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/about-setting-up-material-rate-overrides).
