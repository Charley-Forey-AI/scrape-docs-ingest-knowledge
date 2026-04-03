---
title: "Security Schemes Overview | Trimble Help"
source_url: "https://help.trimble.com/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/security-schemes-overview"
fetched_at: "2026-04-03T20:47:47.926179+00:00"
menu_path: "/en/spectrum/spectrum/tools/enterprise-management/spectrum-menus/maintenance-overview/security-schemes-overview"
---

# Security Schemes Overview

Before setting up operators, consider how you want to set up your security.
Use the Security Schemes screen to set up and maintain security schemes. Security schemes may help your company to easily adjust to growth and personnel changes
Before you set up your operators, you will need to conceptualize how you want to set up your security. If you have many operators who will have the same level of security access, you can probably make good use of security schemes, designed for groups of operators who share the same security requirements. If each individual operator will have specific restrictions, security schemes may not benefit you as much.
Using schemes, you can control what users can or cannot see and what write permissions they have. Schemes may be applied to individual operators, or to companies as a whole, or different configurations to both. For example, you may set up a scheme for management personnel, another for data entry personnel, and still another for operators at a subsidiary company.
Security schemes are especially helpful if you have multiple operators who need to have the same security access. If you are using security schemes and later on you add a new module to the system, it is easy to grant operators access to this module by adding the new module to each applicable scheme.
Schemes may be applied to individual operators, companies, or both. For example, you may set up different schemes for management personnel, data entry personnel, and for operators at a subsidiary company.
In granting company access, you can apply an additional security override or a different security scheme to the operator. For example, if operator RST has access to multiple companies and is assigned a security scheme that allows too much or too little security access for the company he is currently working in, then you can apply an override to operator RST so that it's in effect while he's working in this particular company.
You also have the option of using a combination of security schemes and individual settings within the same company, as long as you're aware that a single operator can only use security schemes or individual security settings while logged on to a given company. For example, operator SFM may be assigned to use a security scheme while logged on to company XYZ, but she may be set up with a security override to use individual settings while logged on to company CCC. In this example, you would use security schemes to apply the same security settings to multiple operators, but then you would use the Operator Maintenance - Scheme tab to grant operator SFM customized access based on her specific needs.
