---
title: "Set up Labor Rate Overrides | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides"
---

# Set up Labor Rate Overrides

Use the SM Advanced Labor Overrides form to set up labor rate overrides.
 You can access SM Advanced Labor Overrides from one of the following forms:

- SM Rate Templates

- SM Rate Template Effect Dates (for Effective Date overrides)

- SM Rate Override Base (for Customer, Service Site, or Work Order Quote overrides)

With the exception of the SM Rate Templates form, these forms are not accessible from the main menu. The following instructions will guide you through setting up labor rate overrides and will include instructions for accessing SM Advanced Labor Overrides from the forms indicated above

1. See the section in the table below corresponding to where you are setting up labor rate overrides.OptionDescription
Rate Template

1. From the Service Management main menu, double-click the SM Rate Template icon.  This opens the SM Rate Template form.

1. In the Template field, enter the rate template for which to set up equipment rate overrides.

1. Proceed to Step 2.

Effective Date Rate Template

1. From the Service Management main menu, double-click the SM Rate Template icon. This opens the SM Rate Template form.

1. In the Template field, enter the rate template for which to set up equipment rate overrides.

1. Click on the Effective Dates tab.

1. In the grid, double-click on the desired Effective Date. The SM Rate Template Effect Dates form displays.

1. Proceed to Step 2.

Customer Rate Template

1. From the Service Management main menu, double-click the SM Customers icon. This opens the SM Customers form.

1. In the Customer field, enter the customer for which to set up equipment rate overrides.

1. Click the Override Rates button. The SM Rate Override Base form displays.

1. Proceed to Step 2.

Service Site Rate Template

1. From the Service Management main menu, double-click the SM Service Sites icon. This opens the SM Service Sites form.

1. In the Service Site field, enter the service site for which to set up equipment rate overrides (must be a customer service site or a job service site using a Markup costing method).

1. Click the Override Rates button. The SM Rate Override Base form displays.

1. Proceed to Step 2

Work Order Quote Rate Template

1. From the Service Management main menu, double-click the SM Work Order Quotes icon. This opens the SM Work Order Quotes form.

1. In the Quote ID field, enter the work order quote for which to set up equipment rate overrides.

1. In the quote Seq field (lower section of form), enter the quote sequence for which to set up equipment rate overrides. Must be a quote sequence with a Price Method of Time and Material.

1. Click the Override Rates button. The SM Rate Override Base form displays.

1. Proceed to Step 2.

1. Click the Advanced button in the Labor Rates section. This opens the SM Advanced Labor Overrides form.

1. In the Seq field, enter N or +.  The system automatically assigns the next available sequence number.

1. In the Technician, PR Co, Craft, Class, Call Type, and Pay Type fields, enter any combination of one or more criteria for which to set up an override labor rate. Note: The PR Co is required and will automatically default the PR Co specified in SM Company Parameters. You may override the default as applicable.Entry of a Class requires that you also enter a Craft; however, entry of a Craft does not require entry of a Class.

1. In the Rate field, enter the rate for this labor rate sequence.

1. Save the record.

1. Repeat steps 3-7 for each additional labor rate sequence you wish to add to this template. Note: Since you can define labor rate overrides at different levels, the system uses a specific hierarchy to determine which labor rates to use. For more information, see [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy).
