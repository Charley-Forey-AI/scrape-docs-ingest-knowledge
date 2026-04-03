---
title: "User Roles | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/service/service-hub/manage-users/user-roles"
fetched_at: "2026-04-03T18:19:14.179823+00:00"
menu_path: "/en/spectrum/spectrum/service/service-hub/manage-users/user-roles"
---

# User Roles

User roles define a user's permissions as well as which
 Service Hub features they can
 access.
ERP AdminDefault Business Context:
 ERP
 Administrator
This is a special
 non-customer user role assigned to the ERP user responsible for
 configuring Service Hub company portals. All Service Hub ERP instances must be assigned at least
 one ERP Admin.
ERP Admins can manage the
 portal. This includes onboarding new companies, disabling companies,
 configuring company payment settings, configuring service request
 settings, and adding new ERP Admins and Company Admins. They can also
 manage customer users.
For instructions on adding another ERP Admin,
 see [Invite an ERP Admin](/en/spectrum/spectrum/service/service-hub/manage-users/invite-an-admin#task-e7171fa2-aee4-4a5d-93f7-d6080912884c--en).Tip: If an ERP Admin
 needs additional permissions within a company, they can assign themself
 additional roles.
Company AdminDefault Business Context:
 ERP
 Administrator
Company Admins
 have the same permissions as ERP Admins (except adding new ERP Admins
 and onboarding new companies) but only for a single company.
 For
 instructions on adding a Company Admin, see [Invite a Company Admin](/en/spectrum/spectrum/service/service-hub/manage-users/invite-an-admin#task-6c822fad-0dbb-4016-bdd8-cc3960036b65--en).Tip: If a Company
 Admin needs additional permissions, they can assign themself additional
 roles.
Customer AdminDefault Business Context: Customer User
This is the primary administrator for the Service Hub portal. All
 service customer portals must be assigned at least one Customer Admin.
 Customer Admins have the permissions of all other customer roles across
 all companies.
Finance UserDefault Business Context: Customer
 User
Finance Users have elevated permissions related
 to managing and financing services. They can pay invoices plus read invoices
 and work orders.Site AdminDefault Business Context: Customer
 User
Site Admins have elevated permissions related to
 managing and scheduling services. They can request service plus read
 invoices and work orders.Portal UserDefault Business Context: Customer
 User
This is the most basic account role. Portal
 Users have read-only access to work orders and no other permissions.
PermissionsERP AdminCompany AdminCustomer AdminFinance UserSite AdminPortal User
View Work OrdersNoNoYes for one companyYes for one companyYes for one companyYes for one company
Request ServiceNoNoYes for one companyNoYes for one companyNo
View InvoicesNoNoYes for one companyYes for one companyYes for one companyNo
Pay InvoicesNoNoYes for one companyYes for one companyNoNo
Manage Customer UsersYes for all companiesYes for one companyYes for one companyNoNoNo
Manage Portal Settings, Admins, and
 NotificationsYes for all companiesYes for one companyNoNoNoNo
