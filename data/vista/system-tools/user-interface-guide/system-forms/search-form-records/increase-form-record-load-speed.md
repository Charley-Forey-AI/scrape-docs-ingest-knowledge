---
title: "Increase Form Record Load Speed | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/increase-form-record-load-speed"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/system-tools/user-interface-guide/system-forms/search-form-records/increase-form-record-load-speed"
---

# Increase Form Record Load Speed

Most of the work you will do in the system consists of
 interacting with forms or programs. To increase a form's load/refresh speed, you can set
 limits on the number of records that load when you initially open a form.
Most forms used to maintain records
 throughout the system are associated with the database table that stores the data.
 Some of these data sets are very large and can reduce the form’s load/refresh speed.
 To increase a form's load/refresh speed, you can assign record count limits to
 reduce the number of records returned. This method makes forms load faster by
 decreasing the number of records the system initially retrieves and displays to you.
 As a consequence, you may not initially see all the data maintained by the form.

1. If you are a system administrator, enter the maximum number of records to
 display on forms in the Page Size field in VA Site
 settings. The initial default is 500 records.

1. If you are an individual user, enter the maximum number of records to display
 in the Page Size field in VA User Profile or in the Forms field in
 User Options. As long as the user-specific entry is a smaller number than what
 is set in VA Site Settings, it overrides the company-wide limit.

1. If you need to see more records on the form you can do one of the
 following:

- Use the Search panel to locate a specific record.

- Access the Grid tab and use the Previous Page and Next Page navigation
 buttons to view additional pages of records.

- Enter the ID number in the appropriate key field to display
 that specific record (for example, you can enter a vendor number in the
 Vendor field of AP Vendors to display that vendor record).
