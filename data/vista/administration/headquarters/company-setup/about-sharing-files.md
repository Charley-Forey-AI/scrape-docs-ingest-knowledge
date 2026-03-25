---
title: "About Sharing Files | Trimble Help"
source_url: "https://help.trimble.com/en/vista/vista/administration/headquarters/company-setup/about-sharing-files"
fetched_at: "2026-03-25T16:24:33.094126+00:00"
menu_path: "/en/vista/vista/administration/headquarters/company-setup/about-sharing-files"
---

# About Sharing Files

Many of the codes in Headquarters are set up in master files.
Master files contain information that will be shared by all companies and modules; for example, earn types, frequency codes, units of measure, states, and so forth. These files are set up once; they do not need to be set up for each company you set up in HQ.
The exceptions to this are the customers, vendors/firms, material categories/materials, tax codes/rates, phases/cost types, cost codes/revenue codes, and shops files. These files must be set up for each company or shared by multiple companies. This is accomplished using Groups, which are set up in [HQ Groups](/en/vista/vista/administration/headquarters/company-setup/hq-groups-form). When you set up each Headquarters company, you identify the groups that will be used whenever processing in that company. If you want multiple companies to share these files, you will need to assign the same groups to each company that will share the files. Otherwise, assign a different group to each company that will use its own files.
For example:
If multiple companies will share the same tax and material files, the setup might look like this:
HQ Co #Tax GroupMaterial Group
112
212
312

If each company will use its own tax and material files, the setup will look like this:
HQ Co #Tax GroupMaterial Group
111
222
333

 When you set up information in shared files (for example, customers and vendors), they are automatically set up in the group assigned to the active company. Using the first example above, if you add a tax code in Co #1, it will be set up in Tax Group 1. If you set up a material code in Co #1 it will be set up in Material Group 2. Since these files are shared by multiple companies, any additions or changes made in these files from any of the sharing companies will automatically affect all other companies sharing the files.

Related information

- [HQ Company Setup Form](/en/vista/vista/administration/headquarters/company-setup/hq-company-setup-form)
