---
title: "Setting Up a Surcharge Material | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/material-setup/setting-up-a-surcharge-material"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/material-setup/setting-up-a-surcharge-material"
---

# Setting Up a Surcharge Material

If you are going to use surcharges in the Material Sales module, you must set up at least one material in HQ Materials to represent surcharges.
Follow the steps below to set up a surcharge material.

1. Open the HQ Materials
 form.

1. In the Material field, enter a material code to represent the
 surcharge.Note: The system has no way to distinguish
 between regular materials and surcharge materials. We recommend that you use
 a number range or naming scheme that allows you to easily identify this as a
 surcharge material. This will be particularly useful when using F4 lookups to select surcharge materials.

1. Complete the Description and Category fields.

1. In the Material
 Type field, select S-Standard from the drop-down
 menu.

1. Check the Active - valid
 for material posting box.Note: The system validates surcharge materials
 the same as any other material; you must check this box to enable surcharges
 based on this material.

1. The Taxable for
 purchases or sales field defaults as unchecked. However, the
 system ignores this flag for surcharges, so it is not necessary to change the
 default. Taxing of surcharges will be handled at the surcharge code level (in MS
 Surcharge Codes).

1. Check the Stocked in
 Inventory box.Note: Surcharge materials must be set up for
 applicable locations in IN Location Materials; checking this box enables
 setting up the material in IN Location Materials .)

1. In the Standard
 UM field, enter any valid unit of measure.Note: When assessing surcharges, the system
 will determine the UM to use based on the surcharge code basis (defined in
 MS Surcharge Codes). If you are using a basis of 2-Material Units, the
 system uses the UM specified for the material on the parent ticket when
 assessing surcharges. During batch validation, the system will validate this
 UM against the UMs defined for the surcharge material, and if the UM is not
 set up for the surcharge material, an error is generated. Therefore, if you
 will be assigning this surcharge material to any surcharge code using a
 basis of 2-Material Units, you will need to set up all possible UMs for this
 material on the Additional Units of Measure tab.
All other basis options use the
 surcharge material UM when assessing surcharges, so additional UMs setup is
 not required.

1. In both the Standard
 Unit
 Cost and Standard Unit Price fields, enter
 0.00. You will assign surcharge values in MS Surcharge Codes,
 and overrides (if applicable) by quote in MS Quotes.

1. In the Purchase
 UM and Sales UM fields, set the unit
 of measure equal to the Standard UM. Entry in the
 Metric UM field is not required, so you may leave this field
 blank.

1. In the Payment Discount
 section, leave the Discount Type and Rate/Amount fields as defaulted. The system ignores discount
 information in this form and bases discounts on the surcharge code and the
 parent ticket in MS Ticket Entry (the ticket to which the surcharge will be
 applied).

1. In the Matl
 Phase and Matl CT fields, enter the
 phase and/or cost type to which the surcharge will be posted. This phase and/or
 cost will only be used if the Phase and Cost Type Based On
 drop-down field in MS Surcharge Codes is set to 2-Material for the surcharge
 code used to track this material.If there is no standard phase and/or cost
 type for this surcharge, leave these fields blank. The system will post this
 surcharges to the same material phase and/or cost type specified for the parent
 ticket (i.e. the original ticket for which the surcharge was assessed).

1. In the Haul
 Phase and Haul CT fields, enter the
 phase and/or cost type to which the surcharge will be posted. This phase and/or
 cost will only be used if the Phase and Cost Type Based On
 drop-down field in MS Surcharge Codes is set to 1-Haul for the surcharge code
 used to track this material.If there is no standard phase and/or cost
 type for this surcharge, leave these fields blank. The system will post this
 surcharges to the same haul phase and/or cost type specified for the parent
 ticket (i.e. the original ticket for which the surcharge was assessed).

1. The Haul
 Code and Price Service ID fields,
 along with the Additional Unit of Measure and Escalation Price Index tabs, have
 no application for surcharges, so you may leave this information blank.

1. Click Save (in toolbar
 or Records menu).

1. [Initialize the surcharge material](/en/vista/vista/administration/headquarters/material-setup/initializing-materials-to-inventory-locations) to applicable
 Inventory locations (IN Location Materials).

1. Repeat the process for
 any other surcharge materials you need to set up.
[](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)HQ
 Materials
[](/en/vista/vista/job-resources/inventory/setup--maintenance/location-materials/about-the-in-location-materials-form)IN Location Materials
[](/en/vista/vista/job-resources/material-sales/setupmaintenance/about-the-ms-surcharge-codes-form)MS Surcharge Codes
