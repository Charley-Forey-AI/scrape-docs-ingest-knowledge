---
title: "Change the Customer for a Service Site | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/service-management-setup/about-service-sites/change-the-customer-for-a-service-site"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/service-management-setup/about-service-sites/change-the-customer-for-a-service-site"
---

# Change the Customer for a Service Site

You can change the customer assigned to a service site and, if applicable, update any agreements associated with that customer via the SM Change Agreement Customer form.
 The following steps detail how to change the customer for a service site that is associated with one or more service agreements.

1. Open the SM Service Sites form.

1. In the Service Site field, enter the service site or press F4 to select from a list of valid service sites.

1. In the Customer field, enter the new customer for the service site or press F4 to select from a list of valid SM customers.If there are service agreements (in active or quote status) associated with the customer/service site, the SM Change Agreement Customer form displays and provides a list of all agreements for the site.

1. For each agreement you want to transfer, select the Transfer checkbox. Note: Agreements that do not have the Transfer checkbox selected are terminated once you process the changes. Only those with the Transfer checkbox selected are transferred to the new customer.

1. In the Start Date field, enter the new start date or accept the defaulted (today's) date.

1. Click Make Changes.

The agreements are transferred and the New Agreement column displays the new agreement number. If more than one site is associated with the agreement, the existing agreement is terminated and a new agreement quote created. For sites with a customer unchanged, the agreement is terminated and a new quote is entered for the same agreement. You can edit and approve the agreement quotes by double-clicking on the agreement in the grid (which opens the SM Agreements form) or you can close the SM Change Agreement Customer form and access the agreements later for edits and approval.

Related information

- [SM Service Sites Form](/en/vista/vista/service-management/service-management-setup/service-management-setup-forms/sm-service-sites-form)

- [SM Agreements Form](/en/vista/vista/service-management/agreements/agreement-setupmaintenance/service-management-agreements-forms/sm-agreements-form)
