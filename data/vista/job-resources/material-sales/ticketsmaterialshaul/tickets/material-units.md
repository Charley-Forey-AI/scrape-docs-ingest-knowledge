---
title: "Material Units | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-units"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/material-units"
---

# Material Units

When entering tickets, material units are either entered manually, calculated based on the material’s unit of measure and the vehicle’s net weight (gross minus tare weight), or calculated based on the number of loads and the vehicle’s capacity.
Typically, you will use manual entry when no
 haul charges are entered on the ticket.

## Units Sold Based on Net Weight

When material units calculate based on
 the ‘net weight’ of a haul, you should consider the following:

- Set the Weight Option in IN
 Locations to Tons, Lbs, or Kilograms for the sales location.

- Specify a Weight Conversion
 factor for non-stocked materials in HQ Materials.

- Specify a Weight Conversion
 factor for stocked materials in IN Location Materials.

- The vehicle’s weight and weight
 unit of measure must be defined in EM Equipment (materials hauled with own
 equipment) or MS Vendor Trucks (materials hauled using haul vendor).

- If the Sales UM differs from the
 standard unit of measure, you must have a conversion set up in HQ Material
 Units of Measure.

The Weight Option section in IN
 Locations determines whether the gross, tare, and net weights on tickets and hauler
 time sheets are expressed in tons, pounds, or kilograms. If the vehicle’s weight
 unit of measure differs from the selected weight option, the system converts it to
 the location’s weight option in order to get an accurate net weight. For example, if
 the vehicle’s tare weight is in tons, and the weight option is lbs., the tare weight
 of vehicle converts to lbs. You must then enter the gross weight in lbs. in order
 for the correct net weight to be calculated. However, if the vehicle’s weight unit
 of measure is other than TON, LBS, or kg, no conversion occurs and the tare weight
 defaults as 0.00. You must then enter weights manually.
The net weight of the vehicle is
 determined by subtracting the tare weight from the gross weight. The net weight is
 then converted to the material’s standard unit of measure using the ‘weight’
 conversion factor specified for the material in either HQ Materials (materials
 purchased from material vendor) or IN Location Materials (materials sold from
 on-hand stock). The weight units are then converted to the ‘sales’ unit of measure
 using the conversion factor specified for the material in HQ Material Units of
 Measure or IN Material Units of Measure, providing the material units (units sold)
 for the material.
If unable to default ‘units sold’ based
 on weight (i.e. no conversion is set up or the Weight Option is ‘None’), the form
 attempts to use the vehicle capacity and number of loads to determine the ‘units
 sold’. If a number of loads has been specified and the vehicle’s capacity is not
 null, and the volume or weight capacity unit of measure is convertible to the
 ticket's material unit of measure, then the ‘units sold’ will be the number of loads
 x the vehicle capacity. If not convertible, units sold will default as null.

## Units Sold Based on Loads

If you are not using weights to provide
 a default for units sold (i.e. the gross or tare weights are 0.00, weight fields are
 removed from the Ticket Entry form, or the weight conversion factor is 0.00 for the
 material), then the capacity of the delivery vehicle and number of loads will be
 used to calculate the material units.
In order for this feature to be used,
 you must make sure that weight capacity information has been set up for the vendor
 truck (MS Vendor Trucks) or the equipment (in EM Equipment). If you also set up
 volume capacity for your equipment, this information may be used to calculated
 material units. Make sure the vehicle’s capacity unit of measure is valid for the
 material (i.e. set up for the material in HQ Material Units of Measure.)
Once the vendor truck or equipment is
 entered on a ticket or timesheet, the system will calculate units by multiplying the
 specified number of loads by the vehicle’s weight capacity. If using your own
 equipment, the volume capacity will be used if no weight capacity has been
 specified. The units are converted to the standard unit of measure for the material
 (using the conversion factor for the capacity unit of measure), then converted to
 the ‘sales’ unit of measure for the material using the conversion factor for the
 material.

Related information

- [About the MS Ticket Entry Form](/en/vista/vista/job-resources/material-sales/ticketsmaterialshaul/tickets/about-the-ms-ticket-entry-form)

- [About the HQ Materials Form](/en/vista/vista/administration/headquarters/material-setup/about-the-hq-materials-form)

- [About the IN Locations Form](/en/vista/vista/job-resources/inventory/setup--maintenance/locations/about-the-in-locations-form)
