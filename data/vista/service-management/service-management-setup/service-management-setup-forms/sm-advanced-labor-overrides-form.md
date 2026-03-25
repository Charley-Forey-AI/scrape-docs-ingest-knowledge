---
title: "SM Advanced Labor Overrides Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-labor-overrides-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-advanced-labor-overrides-form"
---

# SM Advanced Labor Overrides Form

Use the SM Advanced Labor Overrides form to set up advanced labor rates for a rate template, customer, service site, or work order quote.
Access this form by
 clicking Advanced in the Labor Rates
 section of SM Rate Templates, SM Rate Template
 Effect Dates (accessed by double-clicking in the
 Effective Date grid in SM Rate Templates), and SM
 Rate Override Base (accessed by clicking Override
 Rates button in SM Customers or SM Service
 Sites).
Note: You will only need to use
 this form if labor rates differ by technician,
 craft, class, call type, and/or pay type. If you
 will be using the same labor rate for all work
 orders referencing this template, use the Rate field in SM Rate Templates
 (Labor Rates section) to specify that rate.
For each labor rate
 sequence you set up, you must specify the
 combination of criteria to which the labor rate
 applies. You can reference the same criteria on
 multiple sequences, as long as the same combination
 of criteria is not duplicated.
 For example:
SeqTechnicianPRCoCraftClassCall TypePay TypeRate
11001REG35.00
21001OT52.50
31001CARPJRNY1REG45.00
41001CARPJRNY2OT67.50

When entering work completed labor lines (in SM Work
 Orders, Work Completed tab), the system compares the data entered on the work completed line
 with the criteria specified here. If an exact match is found, the specified rate is used. If
 an exact match is not found, the system will move to the next level of the labor rate hierarchy
 and repeat the process until a match is found. If no match is found, the system uses the
 standard labor rate defined for the rate template.
[Setting up Labor Rate
 Overrides](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides)
[Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy)

Related information

- [SM Rate Templates Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-rate-templates-form)

- [Labor Rate Hierarchy](/en/vista/vista/service-management/service-management-setup/about-rate-templates-and-override-rates/set-up-labor-rate-overrides/labor-rate-hierarchy)
