---
title: "Service Management Features | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/service-management/service-management-features"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/whats-new/whats-new-in-vista/previous-vista-releases/2022-releases/whats-new-in-vista-2022-r1/service-management/service-management-features"
---

# Service Management Features

Vista 2022 R1 delivers on user-requested Service Management enhancements, fixes, and other improvements.

## Auto-Add New Customer/Service Site from a Quote

You can now have the system automatically set up new customers and service sites from a work order quote.
 To enable this functionality, the following changes were made in SM Work Order Quotes:

- Added New Customer and New Site checkboxes to the quote header. Both checkboxes default as selected for new quote records. If the quote is for an existing customer and/or service site, deselect the applicable checkbox.

- Added a Copy button to the Customer section to allow copying the customer's address to the new site. This button is enabled only when the New Site checkbox is selected, and should only be used if the new site's address is the same as the customer's address.

- Added Add'l Address fields to the Customer and Site sections, and relabeled the Street fields to Address for consistency with other address fields throughout Vista.

- Added a Create Customer / Site button to the bottom of the form. This button is enabled only when the New Customer and/or New Site checkboxes are selected. Once you enter the required information (Quote ID, customer ID and name, site ID and description, and service center) and click Create Customer / Site, the system sets up the new customer in AR Customers and SM Customers and/or the new site in SM Service SItes with the specified information. If custom fields exist in the quote header for either the customer or site, and those fields exist in AR Customers, SM Customers, and SM Service Sites, respectively, the values in the UD fields are copied as well. You can update the customer and site information as needed in the applicable forms.

## View Customer and Site Notes for Service Calls

You can now view customer and service site notes from a call record in SM Call Handler.
 Previously, if customer and/or service site notes existed, a Customer Notes and/or Site Notes alert displayed in the Alerts section above the tabs. Now, when you hover over the alerts, a pop-up displays, showing the notes entered for the customer (in SM Customers) or service site (in SM Service Sites). Additionally, if the notes are extensive, you can click on the applicable alert and a notes window displays (Customer Notes or Site Notes) so that you can view the notes in their entirety.

## Relabeled Address Fields in SM Call Handler

For consistency with other address fields throughout Vista, the Address 1 and Address 2 fields were relabeled to Address and Add'l Address.

## SM Trip Closeout Email for Service Sites and Customers

You can now select contacts to receive a notification email when a trip is closed on a work order.
Select this checkbox if this contact should receive an email when a trip to the service site is completed. When you close a trip in Vista Field Service for a work order associated this this service site, any contact with this checkbox selected receives an email indicating the trip was closed.
Leave this checkbox unselected if this contact should not receive emails when trips to this service site are completed.
To include a customer in the notification email, navigate to Service Management > Programs > SM Service Site or SM Customers > Contacts. Check Include Trip Close Email.

## Updated Customer Lookup in SM Customers

When using the F4 function in the Customer field in SM Customers, the SM Customer Info lookup option (default) now shows both active and inactive SM customers. If you want to see only active SM customers, select the Active Customers by Sort Name option.

## Check Issue Status

To see a list of defects fixed in this version, go to the [Track Cases/Issues page](https://support.viewpoint.com/s/browse-cases-and-issues) of the Viewpoint Customer Portal. Use the filter options to select your product and module. In the Fixed in Version field, select this version, then select Apply Filters.
