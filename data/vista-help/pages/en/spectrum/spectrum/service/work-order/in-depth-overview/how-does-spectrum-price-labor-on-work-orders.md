---
title: "How does Spectrum price labor on Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/work-order/in-depth-overview/how-does-spectrum-price-labor-on-work-orders"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/work-order/in-depth-overview/how-does-spectrum-price-labor-on-work-orders"
---

# How does Spectrum price labor on Work Orders

Spectrum uses a variety of options to set the price of labor on work orders.

## How does Spectrum price labor on a work order?

The labor billing rate is based on a hierarchy of tables. When adding a new labor transaction in Work Order or Payroll, the employee's billing code is compared to the following hierarchy to determine if there are any special labor pricing rules to follow.

- Service Contract Specific Billing Rate: If the work order references a service contract, the software checks to see if there are any special pricing rules for this billing rate on this service contract.

- Site Specific Billing Rate: If there were no contract specific billing rates, the software looks to see if there are any special pricing rules for this billing rate on this site.

- Customer Specific Billing Rate: If the software did not find any contract or site-specific rules, it looks to see if there are any special pricing rules for this customer.

- Standard Billing Rate: If the software did not find any override rates above, it uses the standard billing rates.

- The billing rate will default to blank. If the software still has not found a rate, the billing rate field will default to <blank>. You can modify the rate or accept the rate of zero.

The software continues down this hierarchy until it finds the first occurrence of a non-zero rate

## How is the employee's billing code determined?

The system looks to Technician File Maintenance to see which Labor Category has been assigned. Then it looks to the Labor Category table to see what billing code has been set up.

## Contract Labor Billing Rates Maintenance

Use this screen to set up and maintain labor rates for a specific service contract. It can be accessed from Service Contracts > Maintenance or by selecting the Contract button from the Site, Customer or Standard Labor Billing Rates screens.

## Site Labor Billing Rates Maintenance

This screen is used to set up site-specific labor rates. Select the Site button on the Labor Billing Rates Maintenance screen to access the screen.

## Customer Labor Billing Rate Maintenance

Use this screen to set up and maintain billing rates for a specific customer. It is accessed by selecting the Customer button on the Labor Billing Rates Maintenance screen.

## Labor Billing Rates Maintenance

This screen is used to maintain the standard labor billing rates.
Using the Rate Adjustment Utility
The Rate Adjustment Utility can be used to globally adjust labor billing rates by a certain percentage or dollar amount. This function is located in the Utilities tab of the Work Order module. This utility will update default labor billing rates for a range of billing codes. Select to change the billing rate by a percent or dollar amount.

## Percentage Adjustments

Enter the percent change for each pay type (Regular, Overtime, Double time). To leave the rate unchanged, accept the default of 0.000. Positive and negative entries are allowed. For example, enter 15.000 to increase rates by 15% or -3.000 to reduce rates by 3%.

## Dollar Amount Adjustments

Enter the dollar amount change for each pay type (Regular, Overtime, Double time). To leave the rate unchanged, accept the default of 0.00. Positive and negative entries are allowed. For example, enter 25.00 to increase the rate by $25.00 or -5.00 to decrease the rate by $5.00.

## Using User-Defined Fields in your Selections

When you select to update customer specific or site specific rates, you can optionally further refine your selection with User-Defined Fields. By design, the first alpha user-defined field is available on the utility start screen. Because the screen uses the first alpha user-defined field, it may be necessary to move the desired field to the first position. Follow these steps to change the field order:

1. Navigate to the user-defined field's Maintenance screen.

1. Select the Edit All button.

1. Highlight the item you would like to move and select the Move Up button.

1. Repeat steps 2 and 3 until the field is moved to the first position on your list.
 User-defined fields can be set up for ALL companies or specific companies. The determination whether this utility displays the first user-defined field for the company or for ALL companies is determined by the prompt titled "Show non-company-specific fields…"

- If this prompt is selected, the first user-defined field is used regardless of whether it is company-specific or for company ALL.

- If the prompt is not selected, the first user-defined field for the company is used.

Important: To make writing your own Crystal Reports easier, it is recommended that you do not set up any company-specific user-defined fields.
