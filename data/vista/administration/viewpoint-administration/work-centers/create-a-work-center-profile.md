---
title: "Create a Work Center Profile | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/viewpoint-administration/work-centers/create-a-work-center-profile"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/viewpoint-administration/work-centers/create-a-work-center-profile"
---

# Create a Work Center Profile

You can create a customized set of profiles for Project
 Management, Service Management, Accounting, and Dashboard Work Centers, and then associate
 each template/profile with security groups.
Users that are associated with any of the same security groups will then be able to apply the profile to their application window using the [Work Centers](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-work-centers-form) form. This can reduce the amount of set up that each user has to perform before using the Work Centers feature.
To create a new profile and associate it with security groups.

1. Open VA Work Center
 Profile using the Programs folder of the VA module.

1. On the Grid or Info tab,
 click the New Record icon () at the top of the form and then enter a profile
 name in the Name field. Users will use
 this name to select a profile when they apply it using the [Work Centers](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-work-centers-form) form.

1. Use WC Tabs to define
 which Work Centers should display on the profile. Each item in this grid
 represents a tab that will display at the top of the main application window
 when this profile is applied to a user account.

Note: The maximum number of work centers that you can add to your
 application window is 6 or less and depends on the value in the Number of
 Tabs field in the [VA Site Settings](/en/vista/vista/administration/viewpoint-administration/setup-and-maintenance/get-started-in-the-va-module/va-site-settings-form) form.
Add a tab to the profile

1. In the Seq# field, enter + or N to create a new line item.

1. In the Tab Number field, enter a
 number to indicate in what order the tab should display on the main
 application window. For example, enter "1" if the tab should appear as the
 first tab after the Menu tab. Click [here](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-profile-form/field-definitions-va-work-center-profile-form#ID-0004a268--en) for more information about the
 Tab Number field.

1. In the Tab Name field, enter the
 name of the tab as it should appear on the the main application window.

1. In the Work Center field, enter
 the work center template group type or press F4 to select from a list of valid work center template
 groups.

1. For Dashboard profiles only, enter the template type in the Template Name field or
 press F4 to select from a list of dashboard templates types. The template type determines the layout of the Dashboard work center.

1. For PM, SM, or Accounting profiles only, enter the navigation style in the Navigation field or press
 F4 to select from a list of defined navigation styles.For Dashboard work center
 profiles, leave this field blank.

1. Click Save.

1. Add security groups to
 the profile using the Security Groups tab. Only users that belong to one of the
 selected security groups will have access to the profile using the User
 Profile drop down field on the [Work Centers](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-work-centers-form) form. Click [here](/en/vista/vista/administration/viewpoint-administration/application-security/user-security/va-security-groups-form) for general information on security
 groups.

1. Click Save. The work center profile is
 complete. Users with access to this profile can now apply the profile to
 their application window using the Work Centers form. For more information,
 see [Applying a Work Center Profile](/en/vista/vista/system-tools/work-centers/about-work-center-setup/assign-a-work-center-profile-to-your-user-account).

Related information

- [About the VA Work Center Profile Form](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-profile-form)

- [About Work Center Setup](/en/vista/vista/system-tools/work-centers/about-work-center-setup)

- [About the VA Work Center Tab Navigation Form](/en/vista/vista/administration/viewpoint-administration/work-centers/about-the-va-work-center-tab-navigation-form)

- [About the Work Centers form](/en/vista/vista/system-tools/user-interface-guide/about-the-main-menu/main-menu-options/about-the-work-centers-form)
