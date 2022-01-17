---
title: "Activities"
url: /refguide/activities/
parent: "microflows-and-nanoflows"
weight: 40
tags: ["studio pro", "microflows", "nanoflows", "activity"]
---

## 1 Introduction

Activities define the actions that are executed in a microflow or a nanoflow.

There are different types of activity, and these are grouped together in the Studio Pro toolbox. All the activities are listed below, follow the links for more information.

{{% alert color="info" %}}
Most activities can be used in both microflows and nanoflows. However, some can only be used in one of these types of flow, or the behavior may differ between microflows and nanoflows. Follow the links for more information.
{{% /alert %}}

## 2 Object Activities

Object activities can be used to create and manipulate objects. The [domain model](/refguide/domain-model/) defines the object types ([entities](/refguide/entities/)) that can be used.

| Graphic | Name | Description |
| --- | --- | --- |
| [![cast object](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/cast-object.png)](/refguide/cast-object/) | [Cast object](/refguide/cast-object/) *(microflows only)* | In combination with an [object type decision](/refguide/object-type-decision/) allows you to use the specialized members of the object. For more information on the specialized members of an object, see [Entities](/refguide/entities/). |
| [![change object](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/change-object.png)](/refguide/change-object/) | [Change object](/refguide/change-object/) |Allows you to change the members of an object. This can be done with or without committing, and with or without events. |
| [![commit object](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/commit-object.png)](/refguide/committing-objects/) | [Commit object(s)](/refguide/committing-objects/) | Allows you to commit changes to one or more objects. |
| [![create object](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/create-object.png)](/refguide/create-object/) | [Create object](/refguide/create-object/) | Creates an object. |
| [![delete object](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/delete-object.png)](/refguide/deleting-objects/) | [Delete object(s)](/refguide/deleting-objects/) *(microflows only)* | Deletes an object. |
| [![retrieve](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/retrieve.png)](/refguide/retrieve/) | [Retrieve](/refguide/retrieve/) | Gets one (or more) associated objects of another object. Furthermore, this activity can also get one or more objects directly from a database. |
| [![rollback object](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/rollback.png)](/refguide/rollback-object/) | [Rollback object](/refguide/rollback-object/) | Rolls uncommitted changes back that were made to an object in the part of the microflow preceding the activity. Furthermore, it deletes objects that have been created but have never been committed. |

## 3 List Activities

List activities can be used to create and manipulate lists of objects.

| Graphic | Name | Description |
| --- | --- | --- |
| [![aggregate list](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/aggregate-list.png)](/refguide/aggregate-list/) | [Aggregate list](/refguide/aggregate-list/) | Allows you to calculate aggregated values such as the maximum, minimum, sum, average, and total amount of objects over a list of objects. |
| [![change list](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/change-list.png)](/refguide/change-list/) | [Change list](/refguide/change-list/) | Allows you to change the content of a list variable. |
| [![create list](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/create-list.png)](/refguide/create-list/) | [Create list](/refguide/create-list/) | Creates a (empty) list variable. |
| [![list operation](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/list-operation.png)](/refguide/list-operation/) | [List operation](/refguide/list-operation/) | Combines or compares two lists with objects of the same entity. |

## 4 Action Call Activities

Action call activities can be used to call another microflow or to call a Java action.

| Graphic | Name | Description |
| --- | --- | --- |
| [![java action call](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/call-java-action.png)](/refguide/java-action-call/) | [Call Java action](/refguide/java-action-call/) *(only in microflows)* | Calls a Java action. Arguments can be passed to the action and the result can be stored in a variable. |
| [![javascript action call](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/call-javascript-action.png)](/refguide/javascript-action-call/) | [Call JavaScript action](/refguide/javascript-action-call/) *(only in nanoflows)* | Calls a JavaScript action. Arguments can be passed to the action and the result can be stored in a variable. |
| [![microflow call](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/call-microflow.png)](/refguide/microflow-call/) | [Microflow call](/refguide/microflow-call/) | Calls a microflow. Arguments can be passed to the microflow and the result can be stored in a variable. |

## 5 Variable Activities

Variable activities can be used to create or change a variable within a microflow.

| Graphic | Name | Description |
| --- | --- | --- |
| [![change variable](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/change-variable.png)](/refguide/change-variable/) | [Change variable](/refguide/change-variable/) | Allows you to changes the value of a variable. |
| [![create variable](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/create-variable.png)](/refguide/create-variable/) | [Create variable](/refguide/create-variable/) | Allows you to creates a new variable. |

## 6 Client Activities

Client activities can be used to have the web client of your application perform an action, such as showing a different page or downloading a file.

| Graphic | Name | Description |
| --- | --- | --- |
| [![nanoflow call](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/call-nanoflow.png)](/refguide/nanoflow-call/) | [Call nanoflow](/refguide/nanoflow-call/) *(only in nanoflows)* | Calls another nanoflow. Arguments can be passed to the nanoflow and the result can be stored in a variable. |
| [![close page](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/close-page.png)](/refguide/close-page/) | [Close page](/refguide/close-page/) | Closes the page that was opened last by the user who called the microflow in which this activity is used. |
| [![download file](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/download-file.png)](/refguide/download-file/) | [Download file](/refguide/download-file/) *(only in microflows)* | Can be used to enable the browser to download a specific file. The user who calls the microflow in which this activity is used gets a download pop-up window, or the file is shown directly in the browser. |
| [![show home page](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/show-home-page.png)](/refguide/show-home-page/) | [Show home page](/refguide/show-home-page/) *(only in microflows)* | Navigates to the home page for the current user. |
| [![show message](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/show-message.png)](/refguide/show-message/) | [Show message](/refguide/show-message/) | Allows you to show a blocking or non-blocking message to the user that calls the microflow in which this activity is used. |
| [![show page](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/show-page.png)](/refguide/show-page/) | [Show page](/refguide/show-page/) | Allows you to show a page to the user that calls the microflow in which this activity is used. |
| [![synchronize to device](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/synchronize-to-device.png)](/refguide/synchronize-to-device/) | [Synchronize to device](/refguide/synchronize-to-device/) *(only in microflows)* | Can be used to selectively synchronize one or more objects or lists to a device and store them in the offline database. |
| [![synchronize](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/synchronize.png)](/refguide/synchronize/) | [Synchronize](/refguide/synchronize/)  *(only in nanoflows)* | Synchronizes data. |
| [![validation feedback](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/validation-feedback.png)](/refguide/validation-feedback/) | [Validation feedback](/refguide/validation-feedback/) | Allows you to display a red text below a widget that displays an attribute or association. |

## 7 Integration Activities

Integration activities can be used to integrate with other systems, for example by calling a web service.

| Graphic                                                      | Name                                         | Description                                                  |
| ------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------------------------ |
| [![call REST service](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/call-rest-service.png)](/refguide/call-rest-action/) | [Call REST service](/refguide/call-rest-action/)        | Can be used to call a REST endpoint. You can use mappings to map results to entities or entities to requests. You can also use string templates and store the result in a string variable. |
| [![call web service action](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/call-web-service.png)](/refguide/call-web-service-action/) | [Call web service](/refguide/call-web-service-action/)  | Can be used to call one of the [imported web services](/refguide/consumed-web-services/). The content of the request can be edited. Furthermore the response of the webservice can be mapped to entities, stored in a variable or be ignored. |
| [![import with mapping](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/import-with-mapping.png)](/refguide/import-mapping-action/) | [Import with mapping](/refguide/import-mapping-action/) | Can be used to parse the data in a string variable or data stored in a file document, and store them to entities defined in the [domain model](/refguide/domain-model/) of the database. An [import mapping](/refguide/import-mappings/) is used to map the incoming XML or JSON to entities. |
| [![export with mapping](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/export-with-mapping.png)](/refguide/export-mapping-action/) | [Export with mapping](/refguide/export-mapping-action/) | Can be used to export the data stored in [domain model](/refguide/domain-model/) entities into an XML or JSON string. It can also be stored in a file document. An [export mapping](/refguide/export-mappings/) is used to map domain model entities into XML or JSON. |

## 8 Logging Activities

| Graphic                                                      | Name                       | Description                                                  |
| ------------------------------------------------------------ | -------------------------- | ------------------------------------------------------------ |
| [![log message](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/log-message.png)](/refguide/log-message/) | [Log message](/refguide/log-message/) | Allows you to create messages that appear in the log of your Mendix application. |

## 9 Document Generation Activities

| Graphic | Name | Description |
| --- | --- | --- |
| [![generate document](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/generate-document.png)](/refguide/generate-document/) | [Generate document](/refguide/generate-document/) *(only in nanoflows)* | Allows you to create a document of a certain type based on a [template](/refguide/document-templates/). |

## 10 Workflow Activities

Workflow activities are used in relation to workflows and their user tasks. 

| Graphic                                                      | Name                                           | Description                                                  |
| ------------------------------------------------------------ | ---------------------------------------------- | ------------------------------------------------------------ |
| [![](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/complete-task.png)](/refguide/complete-task/) | [Complete user task](/refguide/complete-task/)            | Sets which outcome the [user task](/refguide/user-task/) should follow. For example, this activity can be used to complete a user task using a microflow with custom validations. |
| [![](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/open-task-page.png)](/refguide/show-task-page/) | [Show user task page](/refguide/show-task-page/)          | Opens a user task page specified in [user task properties](/refguide/user-task/). |
| [![](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/open-workflow-page.png)](/refguide/show-workflow-page/) | [Show workflow admin page](/refguide/show-workflow-page/) | Opens a workflow overview page.                              |
| [![](/attachments/refguide/modeling/application-logic/microflows-and-nanoflows/activities/workflow-call.png)](/refguide/workflow-call/) | [Workflow call](/refguide/workflow-call/)                 | Triggers the selected workflow.                              |