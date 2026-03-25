---
title: "Assign Add-on Earnings to a Craft Class | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft-class"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/assign-add-on-earnings-to-a-craft-class"
---

# Assign Add-on Earnings to a Craft Class

You can assign add-on earnings to a class using the Add-on
 Earnings tab in PR Craft Classes.
Add-on earnings are earnings added to an employee's total whenever he works in this craft and class. Add-ons set up here will override add-ons setup in PR Craft, and will be used unless you override them at the template level.
Important: Add-ons defined at the craft level do not need to be set up in PR Craft Classes unless you are overriding the existing rate(s). If you do not override an existing rate here, the rate defined at the craft level will be used. If you want a specific rate excluded from calculations, set it up here with a 0.00 amount. Note that overrides set up at the craft template or craft/class template level will override any rates set up here or at the craft level. Requiring only override rates to be defined here eliminates having to update multiple levels each time a rate change occurs.
The following instructions detail how to assign add-on earnings to a class.

1. In PR Craft Classes,
 select the craft class for which to set up add-on earnings. Select the Add-on
 Earnings tab.

1. In the Earn
 Code field, enter the earnings code for this add-on earnings or
 press F4 to select from a list of valid earnings codes.

1. If the calculation
 method is V (variable), in the Factor field, enter the earnings factor that
 applies to this class. For all other calculation methods, the factor is set to
 0.000000 and cannot be changed. In the Old Rate field, enter the old rate for
 the earnings code. The system will use this rate for timecards entered prior to
 the Effective Date specified in PR Crafts or PR Craft Template. In the New Rate
 field, enter the new rate for the earnings code. The system will use this rate
 for timecards entered on or after the Effective Date specified in PR Crafts or
 PR Craft Template. Save the record.

Related information

- [About the PR Craft Classes Form](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/about-the-pr-craft-classes-form)

- [Set Up Craft Classes](/en/vista/vista/hr-and-payroll/payroll/setupmaintenance/craftclass/set-up-craft-classes)
