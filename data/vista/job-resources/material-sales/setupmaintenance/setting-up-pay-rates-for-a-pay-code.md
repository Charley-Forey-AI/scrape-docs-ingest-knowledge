---
title: "Setting Up Pay Rates for a Pay Code | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-pay-rates-for-a-pay-code"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/setupmaintenance/setting-up-pay-rates-for-a-pay-code"
---

# Setting Up Pay Rates for a Pay Code

Once you have set up a pay code in MS Pay Codes, you must define the pay rates that will be used to calculate pay charges.
Note: Pay rates are defined in hierarchical levels; the more criteria you enter, the more specific your rates will be. If you enter something in every field, the system will only apply the specified rate if the data entered on the ticket matches the criteria exactly.
The following instructions detail how to set up pay rates for a pay code.
Note: The Sequence field is display only;
 the system will automatically assign the next available sequence number once you
 enter a value in the
 Loc

 field.

1. In the Loc Grp field, enter the location group for the pay rate. Entry is required. Press F4 for a list of valid location groups.Once you enter the location group, the system automatically assigns the next available sequence number in the Sequence field.

1. In the From
 Loc field, optionally enter the location to which the pay rate
 applies. Press F4 for a list of valid IN
 locations.Leave this field blank to apply
 the pay rate to all locations within the specified location group.

1. In the Category field, enter the material category to which the pay rate applies. Entry is required if you will be applying the pay rate to a specific material. Press F4 for a list of valid material categories.Leave this field blank to apply the pay rate to all categories/materials. The system will not allow entry in the Material field, so skip to Step 5.

1. In the Material field, optionally enter the material to which the pay rate applies. Press F4 for a list of valid materials for the specified material category.Leave this field blank to apply the pay rate to all materials in the category specified in Step 3.

1. In the Truck Type field, optionally enter the truck type to which the pay rate applies. Press F4 for a list of valid truck types. Leave this field blank to apply the pay rate to all truck types.

1. In the Vendor field, enter the vendor to which the pay rate applies. Entry is required if you will be applying the pay rate to a specific vendor truck. Press F4 for a list of valid vendors. Leave this field blank to apply the pay rate to all vendors. The system will not allow entry in the Truck field, so skip to Step 8.

1. In the Truck field, enter the truck to which the pay rate applies. Press F4 for a list of trucks for the specified vendor. If you specified a truck type and vendor, and you leave this field blank, the pay rate will apply to all trucks for the specified vendor/truck type. If you specified a vendor but no truck type, the pay rate will apply to all trucks for the specified vendor.

1. In the UM field, enter the unit of measure to which the pay rate applies. Entry is required for pay codes with a basis of 1-Per Unit, 4-Units Per Mile, 5-Units Per Hour, or 7-Percent of Surcharge Total. Press F4 for a list of valid UMs. Note: If the pay code basis is 2-Per Hour, 3-Per Load, or 6-Percent of Haul, and you leave this field blank, the pay rate will apply to all UMs.

1. In the Zone field, optionally enter the haul zone to which the pay rate applies. Not a validated field, so any alpha-numeric entry is allowed. Leave this field blank to apply the pay rate to all haul zones.

1. In the Pay Rate field, enter the pay rate to use for calculating pay charges for this pay code.

1. In the Min Amt field, enter the minimum payment amount for this pay code. You will generally only enter an amount here if hired haulers are guaranteed a minimum payment, regardless of quantity delivered. Note: If this pay code has a basis of 7-Percent of Surcharge Total and will be assigned to a surcharge code with negative rates, you must set this amount to 0.00.
Once you have saved the current pay rate sequence, repeat the steps for any other pay rate combinations that apply to this pay code.

Related information

- [About the MS Pay Codes Form](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-pay-codes-form)
