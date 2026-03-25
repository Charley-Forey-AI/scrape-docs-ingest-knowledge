---
title: "Search Work Orders | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/service-management/work-orders/search-work-orders"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/service-management/work-orders/search-work-orders"
---

# Search Work Orders

 You can use the Search filters in SM Work Orders to show only those work orders you want to see.

You can quickly locate specific work orders in SM Work Orders using the expandable Search panel above the work order header. Once you enter your desired criteria and initiate the search, the system loads only the work orders that match your filters.You can save your filter settings for future by use by selecting Save. The system automatically applies the saved filters each time you open the form. To clear your saved filters and return to the default view, select Delete.
Note: Saved searches apply only to the current user; they are not visible to other users. In addition, saved search filter values override any F3 settings you have defined for fields in the Search panel. Once you delete a saved search, the F3 settings are applied.

For more information about each of the search fields, see the F1 help.

1. Open the SM Work Orders form and select the Search dropdown to expose the search fields.

1. In the Search By dropdown, select one of the following options:

- A-All (default) – Select this option to show all customer and job work orders.

- C-Customer – Select this option to show only customer work orders. For additional filtering, use the Customer field to enter the customer.

- S-Service Site – Select this option to show only work orders for a specific service site. Then use the Service Site field to enter the service site.

- J-Job – Select this option to show only job work orders. For additional filtering, use the JC Co and Job fields to enter a specific JC Co and/or Job.

1. To filter by status, use the Status dropdown to select the work order status:

- Not Closed

- New

- Open

- Closed

- All

1. To filter by service center, use the Center field to enter the service center or press F4 to select from a list of valid service centers.

1. To filter by date range, use the Date fields to enter the beginning and ending dates.

1. To filter by work orders that are ready for review, use the Ready for Review dropdown to select one of the following options. For more information about each option, see the [F1 Help](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form/field-definitions-sm-work-orders-form#concept-1625--en).

- Primary – Show ready for review work orders for which you are the primary reviewer.

- Alternate – Show ready for review work orders for which you are an alternate reviewer (that is, you are not assigned as the primary reviewer)

- All – If the Use Review Process checkbox is selected in SM Company Parameters, select this option to show all work orders that you are assigned to review or that are assigned to reviewers for whom you are an authorized user (HQ Reviewers, User Names tab). If the Use Review Process checkbox is not selected, select this option to show all work orders needing a billing review, regardless of reviewer.

Note: For all options, search results will show only those work orders with at least one scope that is flagged as Complete or Closed and has an unbilled amount.

1. Select Search. The grid populates with work orders meeting your selected search criteria.Note: You can enter additional filter values or change the saved filter values at any time to change the search results. To clear the filter values, select Reset. This resets the search filters to their default saved values or system default values (if not a saved search).

1. If saving your search values, select Save.The system saves the specified filter values and defaults the settings each time you open the SM Work Orders form.Note: Filter settings are saved for the current user only. You can delete the saved search by selecting Delete. However, to clear the filter values, you must select Reset or close the form.It is important to note that saved search filters override any F3 settings you have applied to fields in the Search panel. Once you delete a saved search, the F3 overrides are applied.

Related information

- [SM Work Orders Form](/en/vista/vista/service-management/work-orders/service-management-work-order-forms/sm-work-orders-form)
