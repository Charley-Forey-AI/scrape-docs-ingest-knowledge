---
title: "Updating Custom Fields in Related Forms | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/call-handler--dispatch-board/updating-custom-fields-in-related-forms"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/call-handler--dispatch-board/updating-custom-fields-in-related-forms"
---

# Updating Custom Fields in Related Forms

You can add custom fields to most tabs in the SM Call Handler
 form using the VA Custom Fields Wizard.
For the Work Orders, Quotes, Serviceable Items, and Call History tab, custom fields are display only and are populated only if the custom field exists in the related form and contains a value. For example, if you add a custom field to the Quotes tab in SM Call Handler and select to also add the field to the SM Work Order Quotes form, then values entered in that field in SM Work Order Quotes will display on the Quotes tab in SM Call Handler when a call is entered referencing the customer specified on the quote.
Custom fields added to the Info tab in SM Call Handler, however, are editable and can be set up to update corresponding fields in the [SM Customers](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-customers-form), [SM Service Sites](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form), and/or [SM Work Orders](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form) forms when a new customer, service site, and/or work order is generated from the call record. This is done by individually adding the custom field to each of these forms in VA Custom Fields Wizard.
For example, say you want to add a "Custom Date" field to SM Call Handler and have its values updated to SM Customers and SM Service Sites. You would set this up as follows:

1. In VA Custom Field
 Wizard, add the field to SM Call Handler, making sure to select the Info tab in
 the Form
 Tab where the control will reside field.Make note of your selections as
 you go along to ensure consistency. Taking screen shots is an easy way to do
 this.

1. Launch VA Custom Fields Wizard again and add the same field to the Info tab in SM Customers, using your notes or screen shots to ensure your parameters are consistent.

1. Repeat the process, adding the same field to the Info tab in SM Service Sites. The next time you add a call record in SM Call Handler, if you enter data in the custom field and the call is for a new customer and service site, when you create the work order, the system will add the new customer to AR Customers and SM Customers, add the service site to SM Service Sites, and update the custom field in SM Customers and SM Service Sites with the value entered in SM Call Handler. If only the service site is new, then only the service site custom field is updated.

Related information

- [Create Custom Fields](/en/vista/vista/administration/viewpoint-administration/custom-formsfields/create-custom-fields)
