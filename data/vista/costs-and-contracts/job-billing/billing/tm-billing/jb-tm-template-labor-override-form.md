---
title: "JB T&M Template Labor Override Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-labor-override-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-labor-override-form"
---

# JB T&M Template Labor Override Form

Use this form (accessed from the main menu or by double-clicking a record on the Labor Rate Overrides tab in JB T&M Template Setup) to set up labor rate overrides for templates by category.
Labor categories are set up in JB Labor Categories and allow you to group specified classes and crafts together on a billing. You must set up labor categories before setting up labor rates and labor rate overrides.
Note: If you set the Labor Rate Option to Costs for a template (in JB T&M Template Setup), labor rates are disregarded during the billing process. You can still set up labor rate overrides here; however, the system will ignore this information when generating billings using the selected template.

## New Labor Rate Effective Date

This date identifies the effective date for labor rate overrides (as defined in JB
 T&M Template Labor Rates), allowing you to define new override rates ahead of
 time, while preserving the current override rates until the new ones are in effect.
Since the effective dates for override
 labor rates are assumed to be the same as those for standard labor rates, you will
 need to define effective dates using JB T&M Template Labor Rates.
When initializing billings or adding JC
 transactions to existing billings, the effective date is used to determine which
 override rates apply. The system bills labor transactions with 'actual' dates prior
 to the effective date at the old override rate and labor transactions with 'actual'
 dates on or after the effective date at the new override rate. If you do not specify
 an effective date, the new rate is used and the old rate ignored.
Note: You can automatically update the old rates for
 all entries in the grid using the Move New Rates to Old option (File menu). When
 selected, the system automatically updates the old rate for all entries in the grid
 with the new rates.

## Rate Restrictions

As with standard labor rates for a template, you will need to define override rates
 by category. However, in addition to earnings type, factor, and shift, overrides can
 also be specific to an employee, craft, and/or class. For example, you can specify
 that a labor rate will apply to all employees of a specific craft/class.

## Rate Option

The rate option assigned to each category determines how labor will be billed.

- C = Actual Costs. Bill labor
 using the actual costs posted to Job Cost.

- R = Rate. Bill labor using the
 Rate specified for the labor category.

- F = Factor. Bill labor using the
 earnings factor posted to JC multiplied by the Rate specified for the labor
 category.

Note: Labor rate overrides will only be used when
 initializing billings if the selected template has a Labor Rate Option of Rates and
 the Allow
 Labor Rate Overrides box is checked for the template (in JB T&M
 Template Setup). Otherwise, standard labor rates are used.

## Delete a Labor Rate Override

To delete a labor rate, select the rate’s line in the grid and click the Delete
 button. The system displays a message box confirming the deletion. Click Yes to
 delete the labor rate from the grid.

The following are related topics:

- [JB T&M Template Labor Rates Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-labor-rates-form)

- [JB T&M Template Setup Form](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/jb-tm-template-setup-form)

- [Set a Labor Rate Override](/en/vista/vista/costs-and-contracts/job-billing/billing/tm-billing/set-up-labor-rates-in-the-jb-tm-template-labor-rates-form/set-a-labor-rate-override)
