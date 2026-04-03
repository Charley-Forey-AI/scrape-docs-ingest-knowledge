---
title: "Switch Existing Equipment to be Tracked by Hilti | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/equipment/hilti-ontrack-integration-with-spectrum/enter-tools-in-spectrum-to-be-tracked-by-hilti/switch-existing-equipment-to-be-tracked-by-hilti"
fetched_at: "2026-04-03T20:05:26.860879+00:00"
menu_path: "/en/spectrum/spectrum/equipment/hilti-ontrack-integration-with-spectrum/enter-tools-in-spectrum-to-be-tracked-by-hilti/switch-existing-equipment-to-be-tracked-by-hilti"
---

# Switch Existing Equipment to be Tracked by Hilti

Change existing equipment from being tracked with Spectrum's
 standard equipment tracking to Hilti equipment tracking.
In general, you will
 create new tool / equipment records to [Enter Tools in Spectrum to be Tracked by Hilti](/en/spectrum/spectrum/equipment/hilti-ontrack-integration-with-spectrum/enter-tools-in-spectrum-to-be-tracked-by-hilti), but in some
 cases, you may wish to use existing equipment.

1. Open Equipment Control > Equipment > Equipment Main Properties, and select Edit for the piece of equipment you want to update.

1. Change the equipment Type to the Hilti-specific
 type you created when setting up the integration. (If you haven't already done
 so, [Create a Hilti Equipment Type](/en/spectrum/spectrum/equipment/hilti-ontrack-integration-with-spectrum/set-up-the-hilti-ontrack-integration-in-spectrum/create-a-hilti-equipment-type).)

1. Select Save.

Note: You cannot change or edit the equipment type for equipment that is currently issued on the Spectrum Deployment Log. You will see the following error message:ERROR - Equipment type cannot be changed when asset is currently issued on the Deployment Log.

To resolve this error, see the following steps:

1. For a piece of equipment already on the Deployment
 Log, return it as follows:

1. Go to Equipment
 Tracking > Data Entry > Deployment
 Log.

1. Select the piece(s) of equipment that you
 want to remove from the log and select Return.

1. Enter the appropriate equipment return
 information, then select Continue.The equipment is no longer on the Deployment
 Log.

1. Return to the Equipment Main Properties screen and
 change the equipment Type to your Hilti-specific type.

1. You also need to consider the accounting impact
 when removing a piece of equipment from the Deployment Log. Do an analysis and
 make any manual adjusting entries as needed.

Note: Equipment Attachments supported in Spectrum are not supported in Hilti ON!Track. Each piece of equipment has its usage tracked independently.
