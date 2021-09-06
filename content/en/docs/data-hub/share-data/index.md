---
title: "Share Data Between Apps"
description: "Describes how to publish and register a simple data asset to Mendix Data Hub from Studio Pro and create a new apps that consumes this asset."
tags: ["data hub catalog", "data hub", "external entities", "landscape", "published OData service" ,"how to", "consume"]
aliases:
    - /data-hub/data-hub-catalog/use-data-catalog.html
    - /datahub/general/share-data/index.html
#If moving or renaming this doc file, implement a temporary redirect and let the respective team know they should update the URL in the product. See Mapping to Products for more details.
---

## 1 Introduction

This how-to will demonstrate how easy it is to build apps using data from different sources using Mendix Data Hub. The steps describe the following:

* Create a simple app in Studio Pro
* Publish an entity from the app and register it in the Data Hub Catalog
* Use the Data Hub Catalog to explore the data sources from the organization that are registered as assets
* Connect to the registered asset that you published earlier and use it in a new app
* Change data in the original app and see it updated in the new or consuming app
* See the network of shared data in the Data Hub Landscape


To use the Mendix Data Hub a license is required, which includes the integration of Data Hub in Studio Pro.


## 2 Prerequisites

Before starting this how-to, make sure you have completed the following prerequisite:

* Install Studio Pro version [8.14.0 or above](https://appstore.home.mendix.com/link/modelers/)
* Be familiar with app development using Mendix Studio Pro

## 3 Creating an App {#createapp}

Follow these steps to create a simple app in Studio Pro and populate it. You will use this data in another app through the Data Hub:

1. In Studio Pro, click **New App** to create a new app using the **Blank App** template. Call this app *{yourname}CustomerServiceApp*.
2. In the App Explorer, double click the **Domain Model** for **MyFirstModule** and click **Entity** in the toolbar above the main window to add an entity to the domain model.
3. Double-click the entity to open its properties and change its **Name** to *Customer*.
4. In the **Attributes** tab, click **New** to create the following attributes for the entity:

    | Name | Type |
    | :---------- | :--------- |
    | CustomerID | Autonumber |
    | FirstName   | String     |
    | LastName    | String     |
    | CompanyName | String     |
    | Address     | String     |

    ![entity properties](attachments/share-data/entity-properties-pane.png)

5. Click **OK** to see the entity and attributes in the domain model.
6. Right-click the entity and from the menu, select **Generate overview pages**.
7. In the **Generate pages** dialog box, select **Atlas_Default (Atlas_UI_Resources)** as the **Content layout** and click **OK**. Click **OK** to accept the informational box. Overview pages for the new entity are added in the **OverviewPages** folder of **MyFirstModule**.

    ![over pages](attachments/share-data/overview-pages-for-customer-entity.png)

7. In the **App Explorer**, double-click **Home_Web** to open the **Home_Web** page.
8. From the **App Explorer** drag **Customer_Overview** into the **Auto-fill** container under the "Welcome" banner.

 You have now created a simple app with the entity **Customer** and a web page where you can add data and view and edit details for this entity. Go ahead and customize your Home page further by changing the banner text.

 ![customer overview](attachments/share-data/customer-overview-home-page.png)

## 4 Publishing to the Data Hub Catalog {#publishing}

You want to register the **Customer** entity in the Data Hub Catalog which will provide the link to access the data that you will input for this entity for use in other apps. To do this you have to expose the **Customer** entity in a *published OData service* in Studio Pro. OData v3 is a REST-based protocol and a standard format that is used for registering services and the entity sets of entities that are exposed in the service in the Data Hub Catalog.

When the app is deployed to the Mendix Cloud, the service is automatically registered in the Data Hub Catalog along with the exposed entity. The entity set name of the entity will be displayed in the catalog.

The following steps take you through creating an OData service for your app to expose the **Customer** entity and register it in the Data Hub Catalog.

1. Add a folder called *APIs* to **MyFirstModule**.

    The published OData service functions as an API to your app. Some apps may have several published services, so it is good practice to keep them together in a folder for each module.

2. In the domain model, right-click the **Customer** entity and select **Expose as OData resource…**.

    ![expose odata](attachments/share-data/expose-as-odata-resource.png)

3. In the **Select Published OData Service** dialog box, select the **MyFirstModule** > **APIs** folder and click **New** to add a new OData service into this folder. Call this published OData service *{yourname}CustomerODataService* and press **OK**.

     ![select service](attachments/share-data/select-published-odata-service.png)

    The new **{yourname}CustomerODataService** is added to the module and the **Edit published resource** dialog box is displayed for the entity **Customer**.

    ![eidt resource](attachments/share-data/edit-published-resource-box.png)

4. For **Entity** click **Select…** to see at the list of **Exposed attributes and associations**. You will see the list of attributes that you defined in the last section. When publishing an entity to an OData service you can select the attributes that you want to expose in the service from here and also associations.

      Make a note of the the **Exposed entity set name**—by default this is the **Exposed entity name** with an "**s"** added at the end of it. When the service is registered in the Data Hub Catalog, the **Exposed entity set name** will be displayed as the available **Dataset**. 

5. Click **OK** twice to display the **OData Service** document. You will see the details of the service that will be included in the service metadata files and registered in the Data Hub Catalog.

      The **Version** number that is assigned to a service is important. It is possible to have different versions of the same OData service registered in the Data Hub Catalog. A connection to an entity by a consuming app will be to a specific service and version number. 

    ![odata service](attachments/share-data/customer-odata-service-page.png)

    Under **Entities**, the **Customer** entity is listed and details of the entity are displayed on the right where you select the attributes that you would like to expose in the OData service.

     If you want to expose several entities or datasets in a service, they can be added and edited on this page. 

6. Click **Publish** in the toolbar to deploy the app and publish it. When prompted, click **Save and continue** to save any unsaved changes to the app. The app will be deployed, and the OData service will be automatically registered in the Data Hub Catalog.

    ![publish](attachments/share-data/publish.png)

    The app has to be deployed to the Mendix Cloud or to your organization's environment using **Publish** for the service to be registered in the Data Hub Catalog.

7. Once the app is deployed, click **View App** to open the app in your browser. Your app is now ready to use.

8. On the app's home page, click **Customers Overview**.

9. Click **New** to add data for a customer entry.

10. You can now add data to your app. Go ahead and add several customers. This will consititute the entity set or dataset for this entity.

    ![external entities](attachments/share-data/add-data-in-app.png)

    When this entity set is consumed in another app via the Data Hub Catalog, a connection will be made to the data that you enter here.

## 5 Using the Data Hub Catalog and Curating your own Service

The **{yourname}CustomerODataService** from your app is now registered in the Data Hub and can be used in other apps. To explore the Data Hub Catalog and find this service, which is called a **Data Source** in the Catalog, and the exposed **Customer** entity set or **Dataset** (as it is referred to), follow these steps:

1. Go to [Mendix Data Hub](https://hub.mendix.com/):

    ![Data Hub screen](attachments/share-data/data-hub-home.png)

2. In the search field, enter the search term *customer*. All services and datasets that satisfy this search string are displayed in the **Search Results** pane in the **Search Details** screen.

3. When you look for your app in the search results you will not find it there. This is because there is a **Filter** active which is indicated by the **1**:

    ![Data Hub screen](attachments/share-data/filter-active.png)

    By default, a filter is set to show results in **Production** environments.

4. Your app was deployed to the **Mendix Free App** or **Sandbox** environment so you will have to change the filter settings so that search will also show results in this environment. Click **Filter** to see the **Filters** dialog box:

    ![Data Hub screen](attachments/share-data/dh-filter-box.png)

5. You can either check **Sandbox** to include it in the search results and or you can click **Clear Filters** to clear all active filters and then click **Apply Filters**.

6. From the new search results list, find the service that you published and click to select it.

7. Full details for the service is displayed in the search details screen and the service metadata panel on the right. This information was published in the OData service contract.

      You will note that in the Catalog, the **Exposed entity set name**  or **Dataset** is displayed for the entity that you published in the previous section; it is **Customers**. 

8. As you are the owner of the service, the **Curate** bar is also displayed. You have curate permissions which means that you can edit the information that is displayed for this service in the Catalog and also add additional information such as the **Business Owner**. The curation bar will state "**You are the owner of the service**":

    ![data hub](attachments/share-data/search-details-screen.png)

    For more information about the user and curator roles in Data Hub see [Roles in Data Hub](/data-hub/#data-hub-roles).

Owners of assets registered in the catalog and curators can edit details of the registered service and also set the **Discoverability** to other users. By default, services registered through a Studio Pro deployment will be set to **Discoverable** meaning that it is visible to all users. For further details about curating functions, see [How to Curate Registered Assets](/data-hub/data-hub-catalog/curate).

For more details on searching in the Data Hub Catalog and the **Search Details** screen, see [How to Search in the Data Hub Catalog](/data-hub/data-hub-catalog/search). You can also explore registered services in the Data Hub Landscape. For more information, see [How to Use the Data Hub Landscape](/data-hub/data-hub-landscape/).

## 6 Using the Customer Dataset in Another App

You are now going to create a new app and consume the data you have added to the **Customer** dataset through the **{yourname}CustomerODataService** service.

To do this follow these steps:

1. In Studio Pro, create a new app using the **Blank App** template and call it *{yourname}CustomerActionsApp*.

2. Go to the domain model.

    The **Data Hub** pane is displayed on the right.

     ![data hub pane](attachments/share-data/data-hub-pane-empty.png)

    If you do not see the Data Hub pane, click **View** > **Data Hub** to display the **Data Hub** pane:
    ![view data hub](attachments/share-data/view-data-hub.png)

3. In the [Data Hub](/refguide/data-hub-pane) pane, enter the search string *customer*.
4. The search results are listed in the **Data Hub** pane showing all the registered assets (services, datasets, and attributes) satisfying this search string. You will note that the app that you have created previously is not listed.
5. By default, search in the **Data Hub** pane will only show services in production environments. The app that you have deployed in this how-to was deployed to the Mendix Cloud for Free Apps, **Sandbox**.
6. Click the **Filter** icon next to the search area to include this non-production environment in your search:

    ![Filter Icon](attachments/share-data/filter-icon.png)

7. Check **Show development environments**. The search results will now show results for all environments including the **{yourname}CustomerOData_service** which is available in the Mendix Free App environment (which is displayed as **Sandbox** in the example below):

    ![data hub pane](attachments/share-data/data-hub-pane.png)

8. Find **{yourname}CustomerODataService** and drag the **Customer** entity from this service into the domain model for your app. The consumed service and entity will be shown in the **Data Hub** pane with a green check mark against them.

9. The entity that you now have in the domain model is different to the blue entity container that is created when you create an entity in the domain model. This purple colored entity is called an *external entity*.

    Entities that are used in an app from the **Data Hub** pane are called external entities. They are displayed as purple containers in the domain model, and the name of the OData service they are exposed in is displayed.

    The properties of external entities are different from other kinds of entities because the properties that define the data in the publishing app cannot be changed in the consuming app. For further information on external entities, see [External Entities](/refguide/external-entities) in the *Studio Pro Guide*.  

10. Click the information icon for the consumed service in the **Data Hub** Pane to see further information about the service as it is registered in the Data Hub Catalog. You can also click **View in Data Hub Catalog** to go to the service details screen in the Data Hub Catalog.

    ![external entities](attachments/share-data/external-entities-in-domain-model.png)

11. In the **App Explorer**, the service and location documents for the external entity that you have just included in your domain model are now listed. These documents specify the metadata for the service and provide the links for connecting to the shared data.

    ![external entities](attachments/share-data/external-entity-metadata-docs.png)

12. Right-click the entity and select **Generate overview pages** to generate overview pages for this entity.

13. In the **Generate pages** dialog box, for **Content layout** select **Atlas_Default(Atlas_UI_Resources)** and click **OK**. Overview pages for the new entity will be added to the **MyFirstModule** module. Confirm **OK** to accept the message that informs you of this.

14. Open the **Home_Web** page and, from **App Explorer**, drag **Customers_Overview** into the **Auto-fill** container under the "Welcome" banner. Go ahead and add a new banner and welcome text.

15. Click **Publish** to deploy the app. The app will be deployed and a link established to the data associated with the **Customer** entity in the publishing app (**{yourname)CustomerServiceApp**) through the **{yourname)CustomerODataService**.

## 7 Viewing the Shared Data in Your New App

To view the consumed data in your new app, follow these steps:

1. When the app has successfully been deployed, click **View App** to open the app in the browser.
2. Click **Customer Overview**.

 The overview page displays the list of the customers that you entered in the **{yourname}CustomerServiceApp** app.

 As this page displays data shared from another app, there are no buttons for adding or changing this data.

## 8 Seeing Changes in Data in the Consuming App

To see an example of consumed data being updated when data is changed in the originating app, follow these steps:

1. Open both apps that have been created in this how-to in separate browser windows and display them side by side.
2. Make some changes to the customer list in **{yourname}CustomerServiceApp** by adding a few more customers to the list and editing some existing entries.
3. Refresh the **{yourname}CustomerActionsApp** window by doing a **Search** to see the changes in the data displayed.

 In the example below, the consuming app is on the right:

    ![shared data](attachments/share-data/shared-data-in-new-app.png)

Congratulations, you have successfully used the Data Hub Catalog functionality to share data between Mendix apps!

You can now see your new apps in your organization's Data Hub Landscape.

## 9 Viewing Your Apps in the Data Hub Landscape

You will now learn how to do the following:

* Use and understand the [Data Hub Landscape](/data-hub/data-hub-landscape/) for locating sources of data
* View the dependencies between deployed apps and the direction of the dependencies in your Data Hub Landscape

You can view the two apps that you have created in the Data Hub Landscape and see the associations by following these steps:

1. Open the [Data Hub](https://hub.mendix.com/#/home) home page.
2. Click the **Landscape** tab to see a graphical representation of your company's data landscape
3. Find your app using the search pane. Remember to use the filter to ensure you can see apps in the Mendix free app environment (Sandbox):

    ![landscape](attachments/share-data/landscape-full-screen.png)

    In the Data Hub Landscape registered services are shown as circles with the number of entity sets or datasets that have been exposed in the service.

    The service **{yourname}CustomerODataAPI** is linked by a solid line to the runtime instance of **{yourname}CustomerCustomerServiceApp** (shown as a square icon), which is deployed as a Free App.

    The service is also linked by a dotted grey line to **{yourname}CustomerActionsApp** with an arrow that indicates that it is making a call to the service for data (or consuming data from it). If you click the entity icon on this consume line, the datasets that are being consumed will be listed in the metadata panel.

4. Click a node to see details of the selected item in the Data Hub Catalog metadata panel on the right. You can also click the **Search** tab to see full details in the **Search Details** screen.

5. Go ahead and search for another item. For large networks, you can use your mouse to zoom in out and pan to explore the network.
