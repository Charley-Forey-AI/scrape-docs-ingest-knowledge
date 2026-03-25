---
title: "Field Definitions: HR Company Asset Check Out Form | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-asset-check-out-form/field-definitions-hr-company-asset-check-out-form"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/hr-and-payroll/human-resources/setupmaintenance/about-the-hr-company-asset-check-out-form/field-definitions-hr-company-asset-check-out-form"
---

# Field Definitions: HR Company Asset Check Out Form

The following is a list of field descriptions for the HR
 Company Asset Check Out form. Many of the descriptions include links to other topics that provide additional information about or related to the topic.

##  HR Resource #

 Enabled when asset is 'Available' (status 0), disabled when asset is 'Unavailable' (status 1).
 If you are checking this asset out, specify the resource to which this asset is being assigned. This resource will display as the 'Assigned To' resource in the Assigned To section of HR Company Assets.
 If you are checking this asset in, this field displays the resource to which the asset is currently assigned. Cannot be overridden. Resource will display as the 'Last Assigned To' resource in the Assigned To section of HR Company Assets.

##  Date Out/Date In

 If this asset is being checked out, this field displays as Date Out.Specify the date this asset was checked out (i.e. assigned to the specified resource). The date specified here will display in the Assigned To section of HR Company Assets.
 If this asset is being checked in, this field displays as Date In.Specify the date this asset was checked in (i.e. turned in) by the assigned resource. The date specified here will display as the 'Returned' date in the Assigned To section of HR Company Assets.

## Memo Out/Memo In

If this asset is being checked out, this field displays as Memo Out.Enter any notes regarding this asset and/or resource, up to 60 characters (e.g. asset's condition at the time of checkout). Memo entered here will display as the 'Out Memo' in the Assigned To section of HR Company Assets.
If this asset is being checked in, the field displays as Memo In.Enter any notes regarding this asset and/or resource, up to 60 characters (e.g. asset's condition at the time of check in). Memo entered here will display as the 'In Memo' in the Assigned To section of HR Company Assets.
Button label will display as “Check In” for
 assets that are being checked in and “Check Out” for assets that are being checked out.
 Click the button to save the data.
If you are checking in an asset, the asset’s
 status will be set to ‘Available’ or ‘Unavailable’, depending on how you set the Make
 Available flag.
If you are checking out an asset, the asset’s
 status will be set to ‘Unavailable’.

##  Make Available

 Enabled only when checking in an asset.
 Checked – This asset has been checked in and is available for reassignment.
 Unchecked – This asset has been checked in, but is not available for reassignment (e.g. requires repairs, maintenance, etc.). Leaving this option unchecked allows the resource to 'check in' the asset for proper tracking, yet flag it as unavailable.
 Click the Check In button to save the data. If the Make Available option is checked, the asset’s status will be set to ‘Available’. If the Make Available option is unchecked, the asset’s status will be set to ‘Unavailable’.
