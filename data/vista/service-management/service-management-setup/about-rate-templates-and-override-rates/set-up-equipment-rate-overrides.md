---
title: "Set up Equipment Rate Overrides | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides"
---

# Set up Equipment Rate Overrides

Equipment rate overrides are set up using the SM Rate Equipment Overrides form.
 You can access SM Rate Equipment Rate Overrides from one of the following forms:

- SM Rate Templates

- SM Rate Template Effect Dates (for Effective Date overrides)

- SM Rate Override Base (for Customer, Service Site, or Work Order Quote overrides)

With the exception of the SM Rate Templates form, these forms are not accessible from the main menu. The following instructions will guide you through setting up equipment rate overrides and will include instructions for accessing SM Equipment Rate Overrides from the forms indicated above.

1. See the section in the table below corresponding to where you are setting up equipment rate overrides.OptionDescription
Rate Template

1. From the Service Management main menu, double-click the SM Rate Template icon.This opens the SM Rate Template form.

1. In the Template field, enter the rate template for which to set up equipment rate overrides.

1. Proceed to Step 2.

Effective Date Rate Template

1. From the Service Management main menu, double-click the SM Rate Template icon. This opens the SM Rate Template form.

1. In the Template field, enter the rate template for which to set up equipment rate overrides.

1. Select on the Effective Dates tab.

1. In the grid, double-click on the desired Effective Date. The SM Rate Template Effect Dates form displays.

1. Proceed to Step 2.

Customer Rate Template

1. From the Service Management main menu, double-click the SM Customers icon. This opens the SM Customers form.

1. In the Customer field, enter the customer for which to set up equipment rate overrides.

1. Select the Override Rates button. The SM Rate Override Base form displays.

1. Proceed to Step 2.

Service Site Rate Template

1. From the Service Management main menu, double-click the SM Service Sites icon. This opens the SM Service Sites form.

1. In the Service Site field, enter the service site for which to set up equipment rate overrides (must be a customer service site or a job service site using a Markup costing method).

1. Select the Override Rates button. The SM Rate Override Base form displays.

1. Proceed to Step 2

Work Order Quote Rate Template

1. From the Service Management main menu, double-click the SM Work Order Quotes icon. This opens the SM Work Order Quotes form.

1. In the Quote ID field, enter the work order quote for which to set up equipment rate overrides.

1. In the quote Seq field (lower section of form), enter the quote sequence for which to set up equipment rate overrides. Must be a quote sequence with a Price Method of Time and Material.

1. Select the Override Rates button. The SM Rate Override Base form displays.

1. Proceed to Step 2.

1. Select the Advanced button in the Equipment Rates section. This opens the SM Rate Equipment Overrides form.

1. In the EM Co field, enter the EM company for this override rate. This should be the company in which the equipment resides.

1. Enter the equipment for which you are setting up the override rate in the Equipment field.

1. In the Rev Code field, enter the revenue code for which you are setting up the override rate. Press F4 for a list of valid revenue codes for the equipment or equipment category.

1. From the Rate Type drop-down, select M-Markup or F-Flat Rate to identify the rate type.

1. If you selected M-Markup as the rate type, enter the markup rate in the Markup Rate field. If you selected F-Flat Rate as the rate type, enter the flat rate in the Flat Rate field.
Note: The rate defined here will be used in calculating the Bill Rate for equipment work completed lines entered in SM Work Orders that reference the equipment/revenue code.

1. Save the record.

1. Repeat Steps 2-8 to enter additional equipment/revenue code rate overrides. Note: Since equipment rate overrides can be defined at different levels, the system will use a specific hierarchy to determine which equipment rates to use. For more information, see [Equipment Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-equipment-rate-overrides/equipment-rate-hierarchy).
