---
title: "Data Hub Administration"
category: "General Info"
#menu_order: 20
description: "Describes the Mendix Admin functions for Data Hub Admin and curators."
tags: ["data hub", "Data Hub Admin", "curator", "custom owner", "administration"]
---

##This page is in Spanish 

## 1 Introduction

Every organization has one Mendix Data Hub Administrator. The Data Hub Admin can assign any number of curators who can manage the day to day administration and perform curate functions on the the registered assets in the Data Hub Catalog.

In the **Administration** tab of **Data Hub**, the operations that can be performed by these two types of users are as follows:

* **Data Hub Admin**:
  * Assign curators
  * Manage the list of custom owners that have been added as **Business** or **Technical Owners** when a service has been [Curated](/data-hub/data-hub-catalog/curate#custom-owner).
* **Curators**:
  Manage the list of custom owners that have been added as **Business** or **Technical Owners** when a service has been [Curated](/data-hub/data-hub-catalog/curate#custom-owner).


In the current release of Data Hub, the Data Hub Admin for the organization is assigned by [Mendix Support](https://support.mendix.com/hc/en-us): please contact your support representative.


This how-to describes the following:

- How the Mendix Data Hub Admin can assign the curator role to users
- How curators and the Data Hub Admin can manage the list of custom owners and their contact details

## 2 Managing Curators {#curator}

The Data Hub Curator can perform day-to-day management functions on all registered assets in the Data Hub Catalog and also enrich the Catalog information on registered assets that is displayed.

Curators can see and curate all registered assets in the Data Hub Catalog. Mendix users who own registered assets can curate their own items, but not those that they do not own.

The Data Hub Admin can add or remove the curator role by following these steps:

1. From **Data Hub** screen, click the **Administration** tab:

	![Administration](attachments/data-hub-admin/administration.png)

2. The Data Hub Admin will see the **Curator Management** tab displaying  the list of Data Hub curators for the organization.

3. To assign a curator role to a Mendix user, click **Add Curator**.

	A user with curator rights can access all assets registered in the Catalog. This also includes those that are set to **Non-discoverable**. Curators can also change the information that is registered for assets that are owned by other users. 

4. To search from the list of Mendix users in your organization, start typing in the search box and check the user(s) you want to assign the curator role to.

	This list will show all Mendix users for your organizations. It will not include non-Mendix users that are  added as *Custom Owners* as described in [Managing Custom Owners](#customowners).

5. If you want to remove the curator rights for a user, check the box against the name and confirm this by clicking **Remove Curator**.

	This will only remove the curator rights of the user, it will not remove the user as a Mendix platform user.

## 3 Managing Custom Owners {#customowners}

Custom owners are owners that have been added as the contact for a registered application. They may be added during the application [curation](/data-hub/data-hub-catalog/curate#custom-owner) or have been specified during app registration.

They are  the contacts for registered assets. Adding a custom owner does not give them access rights to the Catalog. Custom owners are displayed in the drop-down lists by an avatar that only displays their intitial (Mendix users have their peronalized avatar displayed).

Curators and the Data Hub Admin can manage the custom owner list under the **Owner Management** tab.


Curators will only see  **Owner Management** under the **Administration** tab.


![owner admin](attachments/data-hub-admin/owner-management.png)

From this screen, the following functions can be carried out:

* **Add Owners**—click and enter the name and email of the contact and click **OK**. This will be listed when **Business** or **Technical Owners** are curated for registered assets.

	Custom owners in this list are not Mendix platform users but serve as contact for the registered assets.  They will not be able to login to the Mendix Platform or curate registered assets in the Catalog. 

* Edit the details of the listed owners by clicking the edit pencil icon.
* Delete names from the list, click the **x** and confirm the removal of the name from the list.

	If a custom owner is removed from the list, they will also be removed from any registered assets where they were set as the owner. This means that the asset will not have a contact.

New custom owners can also be added when assets are being curated as described in [Changing the Technical and Business Owners of an App](/data-hub/data-hub-catalog/curate#custom-owner).