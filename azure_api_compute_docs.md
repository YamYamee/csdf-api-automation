# 📘 Compute API Full Documentation
> **추출된 API 버전:** 2025-04-01

## 🚀 Operations_List
**Description:** List the operations for the provider

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/providers/Microsoft.Compute/operations` |
| **Tags** | Operations |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `OperationListResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_ListBySubscription
**Description:** Lists all availability sets in a subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/availabilitySets` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| **$expand** | query | ❌ | `string` | The expand expression to apply to the operation. Allowed values are 'instanceView'. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `AvailabilitySetListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservationGroups_ListBySubscription
**Description:** Lists all of the capacity reservation groups in the subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/capacityReservationGroups` |
| **Tags** | CapacityReservationGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. Based on the expand param(s) specified we return Virtual Machine or ScaleSet VM Instance or both resource Ids which are associated to capacity reservation group in the response. |
| **resourceIdsOnly** | query | ❌ | `string` | The query option to fetch Capacity Reservation Group Resource Ids. <br> 'CreatedInSubscription' enables fetching Resource Ids for all capacity reservation group resources created in the subscription. <br> 'SharedWithSubscription' enables fetching Resource Ids for all capacity reservation group resources shared with the subscription. <br> 'All' enables fetching Resource Ids for all capacity reservation group resources shared with the subscription and created in the subscription. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservationGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHostGroups_ListBySubscription
**Description:** Lists all of the dedicated host groups in the subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/hostGroups` |
| **Tags** | DedicatedHostGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHostGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 Images_List
**Description:** Gets the list of Images in the subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/images` |
| **Tags** | Images |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ImageListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImagesEdgeZone_ListPublishers
**Description:** Gets a list of virtual machine image publishers for the specified Azure location and edge zone

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **edgeZone** | path | ✅ | `string` | The name of the edge zone. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImagesEdgeZone_ListOffers
**Description:** Gets a list of virtual machine image offers for the specified location, edge zone and publisher

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **edgeZone** | path | ✅ | `string` | The name of the edge zone. |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImagesEdgeZone_ListSkus
**Description:** Gets a list of virtual machine image SKUs for the specified location, edge zone, publisher, and offer

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **edgeZone** | path | ✅ | `string` | The name of the edge zone. |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |
| **offer** | path | ✅ | `string` | A valid image publisher offer. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImagesEdgeZone_List
**Description:** Gets a list of all virtual machine image versions for the specified location, edge zone, publisher, offer, and SKU

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **edgeZone** | path | ✅ | `string` | The name of the edge zone. |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |
| **offer** | path | ✅ | `string` | A valid image publisher offer. |
| **skus** | path | ✅ | `string` | A valid image SKU. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |
| **$top** | query | ❌ | `integer` | An integer value specifying the number of images to return that matches supplied values. |
| **$orderby** | query | ❌ | `string` | Specifies the order of the results returned. Formatted as an OData query. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImagesEdgeZone_Get
**Description:** Gets a virtual machine image in an edge zone

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **edgeZone** | path | ✅ | `string` | The name of the edge zone. |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |
| **offer** | path | ✅ | `string` | A valid image publisher offer. |
| **skus** | path | ✅ | `string` | A valid image SKU. |
| **version** | path | ✅ | `string` | A valid image SKU version. |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineImage` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImages_ListByEdgeZone
**Description:** Gets a list of all virtual machine image versions for the specified edge zone

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/edgeZones/{edgeZone}/vmimages` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **edgeZone** | path | ✅ | `string` | The name of the edge zone. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VmImagesInEdgeZoneListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 LogAnalytics_ExportRequestRateByInterval
**Description:** Export logs that show Api requests made by this subscription in the given time window to show throttling activities

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getRequestRateByInterval` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **parameters** | body | ✅ | `object` | Parameters supplied to the LogAnalytics getRequestRateByInterval Api. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `RequestRateByIntervalInput` | Parameters supplied to the LogAnalytics getRequestRateByInterval Api. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `LogAnalyticsOperationResult` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 LogAnalytics_ExportThrottledRequests
**Description:** Export logs that show total throttled Api requests for this subscription in the given time window

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/logAnalytics/apiAccess/getThrottledRequests` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **parameters** | body | ✅ | `object` | The request body |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `ThrottledRequestsInput` | The request body |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `LogAnalyticsOperationResult` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImages_ListPublishers
**Description:** Gets a list of virtual machine image publishers for the specified Azure location

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensionImages_ListTypes
**Description:** Gets a list of virtual machine extension image types

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **publisherName** | path | ✅ | `string` | - |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensionImages_ListVersions
**Description:** Gets a list of virtual machine extension image versions

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **publisherName** | path | ✅ | `string` | - |
| **type** | path | ✅ | `string` |  |
| **$filter** | query | ❌ | `string` | The filter to apply on the operation. |
| **$top** | query | ❌ | `integer` | - |
| **$orderby** | query | ❌ | `string` | - |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensionImages_Get
**Description:** Gets a virtual machine extension image

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmextension/types/{type}/versions/{version}` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **publisherName** | path | ✅ | `string` | - |
| **type** | path | ✅ | `string` |  |
| **version** | path | ✅ | `string` | - |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineExtensionImage` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImages_ListOffers
**Description:** Gets a list of virtual machine image offers for the specified location and publisher

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImages_ListSkus
**Description:** Gets a list of virtual machine image SKUs for the specified location, publisher, and offer

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |
| **offer** | path | ✅ | `string` | A valid image publisher offer. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImages_List
**Description:** Gets a list of all virtual machine image versions for the specified location, publisher, offer, and SKU

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |
| **offer** | path | ✅ | `string` | A valid image publisher offer. |
| **skus** | path | ✅ | `string` | A valid image SKU. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |
| **$top** | query | ❌ | `integer` | - |
| **$orderby** | query | ❌ | `string` | - |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineImages_Get
**Description:** Gets a virtual machine image

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/publishers/{publisherName}/artifacttypes/vmimage/offers/{offer}/skus/{skus}/versions/{version}` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **publisherName** | path | ✅ | `string` | A valid image publisher. |
| **offer** | path | ✅ | `string` | A valid image publisher offer. |
| **skus** | path | ✅ | `string` | A valid image SKU. |
| **version** | path | ✅ | `string` | A valid image SKU version. |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineImage` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineRunCommands_List
**Description:** Lists all available run commands for a subscription in a location

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/runCommands` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RunCommandListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineRunCommands_Get
**Description:** Gets specific run command for a subscription in a location

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/runCommands/{commandId}` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |
| **commandId** | path | ✅ | `string` | Specifies a commandId of predefined built-in script. Command IDs available for Linux are listed at https://aka.ms/RunCommandManagedLinux#available-commands, Windows at https://aka.ms/RunCommandManagedWindows#available-commands. |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RunCommandDocument` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 Usage_List
**Description:** Gets, for the specified location, the current compute resource usage information as well as the limits for compute resources under the subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/usages` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ListUsagesResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ListByLocation
**Description:** Gets all the VM scale sets under the specified subscription for the specified location

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/virtualMachineScaleSets` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_ListByLocation
**Description:** Gets all the virtual machines under the specified subscription for the specified location

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/virtualMachines` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineSizes_List
**Description:** This API is deprecated

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/locations/{location}/vmSizes` |
| **Tags** | N/A |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| LocationParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineSizeListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 ProximityPlacementGroups_ListBySubscription
**Description:** Lists all proximity placement groups in a subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/proximityPlacementGroups` |
| **Tags** | ProximityPlacementGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ProximityPlacementGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePointCollections_ListAll
**Description:** Gets the list of restore point collections in the subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/restorePointCollections` |
| **Tags** | RestorePointCollections |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RestorePointCollectionListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 SshPublicKeys_ListBySubscription
**Description:** Lists all of the SSH public keys in the subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/sshPublicKeys` |
| **Tags** | SshPublicKeyResources |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `SshPublicKeysGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ListAll
**Description:** Gets a list of all VM Scale Sets in the subscription, regardless of the associated resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/virtualMachineScaleSets` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetListWithLinkResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_ListAll
**Description:** Lists all of the virtual machines in the specified subscription

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/providers/Microsoft.Compute/virtualMachines` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| **statusOnly** | query | ❌ | `string` | statusOnly=true enables fetching run time status of all Virtual Machines in the subscription. |
| **$filter** | query | ❌ | `string` | The system query option to filter VMs returned in the response. Allowed value is 'virtualMachineScaleSet/id' eq /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}' |
| **$expand** | query | ❌ | `string` | The expand expression to apply on operation. 'instanceView' enables fetching run time status of all Virtual Machines, this can only be specified if a valid $filter option is specified |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_List
**Description:** Lists all availability sets in a resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `AvailabilitySetListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_Get
**Description:** Retrieves information about an availability set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `AvailabilitySet` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_CreateOrUpdate
**Description:** Create or update an availability set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create Availability Set operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `AvailabilitySet` | Parameters supplied to the Create Availability Set operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `AvailabilitySet` | Resource 'AvailabilitySet' update operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_Update
**Description:** Update an availability set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update Availability Set operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `AvailabilitySetUpdate` | Parameters supplied to the Update Availability Set operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `AvailabilitySet` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_Delete
**Description:** Delete an availability set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_CancelMigrationToVirtualMachineScaleSet
**Description:** Cancel the migration operation on an Availability Set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}/cancelMigrationToVirtualMachineScaleSet` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **204** | `A` | There is no content to send for this request, but the headers may be useful. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_ConvertToVirtualMachineScaleSet
**Description:** Create a new Flexible Virtual Machine Scale Set and migrate all the Virtual Machines in the Availability Set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}/convertToVirtualMachineScaleSet` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |
| **parameters** | body | ❌ | `object` | Parameters supplied to the migrate operation on the availability set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `ConvertToVirtualMachineScaleSetInput` | Parameters supplied to the migrate operation on the availability set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_StartMigrationToVirtualMachineScaleSet
**Description:** Start migration operation on an Availability Set to move its Virtual Machines to a Virtual Machine Scale Set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}/startMigrationToVirtualMachineScaleSet` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the migrate operation on the availability set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `MigrateToVirtualMachineScaleSetInput` | Parameters supplied to the migrate operation on the availability set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **204** | `A` | There is no content to send for this request, but the headers may be useful. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_ValidateMigrationToVirtualMachineScaleSet
**Description:** Validates that the Virtual Machines in the Availability Set can be migrated to the provided Virtual Machine Scale Set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}/validateMigrationToVirtualMachineScaleSet` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the migrate operation on the availability set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `MigrateToVirtualMachineScaleSetInput` | Parameters supplied to the migrate operation on the availability set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **204** | `A` | There is no content to send for this request, but the headers may be useful. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 AvailabilitySets_ListAvailableSizes
**Description:** Lists all available virtual machine sizes that can be used to create a new virtual machine in an existing availability set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/availabilitySets/{availabilitySetName}/vmSizes` |
| **Tags** | AvailabilitySets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **availabilitySetName** | path | ✅ | `string` | The name of the availability set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineSizeListResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservationGroups_ListByResourceGroup
**Description:** Lists all of the capacity reservation groups in the specified resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups` |
| **Tags** | CapacityReservationGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. Based on the expand param(s) specified we return Virtual Machine or ScaleSet VM Instance or both resource Ids which are associated to capacity reservation group in the response. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservationGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservationGroups_Get
**Description:** The operation that retrieves information about a capacity reservation group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}` |
| **Tags** | CapacityReservationGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the capacity reservations under the capacity reservation group which is a snapshot of the runtime properties of a capacity reservation that is managed by the platform and can change outside of control plane operations. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservationGroup` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservationGroups_CreateOrUpdate
**Description:** The operation to create or update a capacity reservation group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}` |
| **Tags** | CapacityReservationGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create capacity reservation Group. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `CapacityReservationGroup` | Parameters supplied to the Create capacity reservation Group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservationGroup` | Resource 'CapacityReservationGroup' update operation succeeded |
| **201** | `CapacityReservationGroup` | Resource 'CapacityReservationGroup' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservationGroups_Update
**Description:** The operation to update a capacity reservation group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}` |
| **Tags** | CapacityReservationGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update capacity reservation Group operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `CapacityReservationGroupUpdate` | Parameters supplied to the Update capacity reservation Group operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservationGroup` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservationGroups_Delete
**Description:** The operation to delete a capacity reservation group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}` |
| **Tags** | CapacityReservationGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservations_ListByCapacityReservationGroup
**Description:** Lists all of the capacity reservations in the specified capacity reservation group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}/capacityReservations` |
| **Tags** | CapacityReservations |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. Based on the expand param(s) specified we return Virtual Machine or ScaleSet VM Instance or both resource Ids which are associated to capacity reservation group in the response. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservationListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservations_Get
**Description:** The operation that retrieves information about the capacity reservation

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}/capacityReservations/{capacityReservationName}` |
| **Tags** | CapacityReservations |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **capacityReservationName** | path | ✅ | `string` | The name of the capacity reservation. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'InstanceView' retrieves a snapshot of the runtime properties of the capacity reservation that is managed by the platform and can change outside of control plane operations. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservation` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservations_CreateOrUpdate
**Description:** The operation to create or update a capacity reservation

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}/capacityReservations/{capacityReservationName}` |
| **Tags** | CapacityReservations |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **capacityReservationName** | path | ✅ | `string` | The name of the capacity reservation. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create capacity reservation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `CapacityReservation` | Parameters supplied to the Create capacity reservation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservation` | Resource 'CapacityReservation' update operation succeeded |
| **201** | `CapacityReservation` | Resource 'CapacityReservation' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservations_Update
**Description:** The operation to update a capacity reservation

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}/capacityReservations/{capacityReservationName}` |
| **Tags** | CapacityReservations |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **capacityReservationName** | path | ✅ | `string` | The name of the capacity reservation. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update capacity reservation operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `CapacityReservationUpdate` | Parameters supplied to the Update capacity reservation operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `CapacityReservation` | Azure operation completed successfully. |
| **202** | `A` | Resource update request accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 CapacityReservations_Delete
**Description:** The operation to delete a capacity reservation

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/capacityReservationGroups/{capacityReservationGroupName}/capacityReservations/{capacityReservationName}` |
| **Tags** | CapacityReservations |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **capacityReservationGroupName** | path | ✅ | `string` | The name of the capacity reservation group. |
| **capacityReservationName** | path | ✅ | `string` | The name of the capacity reservation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHostGroups_ListByResourceGroup
**Description:** Lists all of the dedicated host groups in the specified resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups` |
| **Tags** | DedicatedHostGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHostGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHostGroups_Get
**Description:** Retrieves information about a dedicated host group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}` |
| **Tags** | DedicatedHostGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the dedicated hosts under the dedicated host group. 'UserData' is not supported for dedicated host group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHostGroup` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHostGroups_CreateOrUpdate
**Description:** Create or update a dedicated host group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}` |
| **Tags** | DedicatedHostGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create Dedicated Host Group. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `DedicatedHostGroup` | Parameters supplied to the Create Dedicated Host Group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHostGroup` | Resource 'DedicatedHostGroup' update operation succeeded |
| **201** | `DedicatedHostGroup` | Resource 'DedicatedHostGroup' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHostGroups_Update
**Description:** Update an dedicated host group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}` |
| **Tags** | DedicatedHostGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update Dedicated Host Group operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `DedicatedHostGroupUpdate` | Parameters supplied to the Update Dedicated Host Group operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHostGroup` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHostGroups_Delete
**Description:** Delete a dedicated host group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}` |
| **Tags** | DedicatedHostGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_ListByHostGroup
**Description:** Lists all of the dedicated hosts in the specified dedicated host group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHostListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_Get
**Description:** Retrieves information about a dedicated host

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **hostName** | path | ✅ | `string` | The name of the dedicated host. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'InstanceView' will retrieve the list of instance views of the dedicated host. 'UserData' is not supported for dedicated host. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHost` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_CreateOrUpdate
**Description:** Create or update a dedicated host 

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **hostName** | path | ✅ | `string` | The name of the dedicated host. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create Dedicated Host. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `DedicatedHost` | Parameters supplied to the Create Dedicated Host. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHost` | Resource 'DedicatedHost' update operation succeeded |
| **201** | `DedicatedHost` | Resource 'DedicatedHost' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_Update
**Description:** Update a dedicated host 

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **hostName** | path | ✅ | `string` | The name of the dedicated host. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update Dedicated Host operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `DedicatedHostUpdate` | Parameters supplied to the Update Dedicated Host operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHost` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_Delete
**Description:** Delete a dedicated host

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **hostName** | path | ✅ | `string` | The name of the dedicated host. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_ListAvailableSizes
**Description:** Lists all available dedicated host sizes to which the specified dedicated host can be resized

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}/hostSizes` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **hostName** | path | ✅ | `string` | The name of the dedicated host. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `DedicatedHostSizeListResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_Redeploy
**Description:** Redeploy the dedicated host

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}/redeploy` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **hostName** | path | ✅ | `string` | The name of the dedicated host. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 DedicatedHosts_Restart
**Description:** Restart the dedicated host

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/hostGroups/{hostGroupName}/hosts/{hostName}/restart` |
| **Tags** | DedicatedHosts |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **hostGroupName** | path | ✅ | `string` | The name of the dedicated host group. |
| **hostName** | path | ✅ | `string` | The name of the dedicated host. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 Images_ListByResourceGroup
**Description:** Gets the list of images under a resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images` |
| **Tags** | Images |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ImageListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 Images_Get
**Description:** Gets an image

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}` |
| **Tags** | Images |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **imageName** | path | ✅ | `string` | The name of the image. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `Image` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 Images_CreateOrUpdate
**Description:** Create or update an image

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}` |
| **Tags** | Images |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **imageName** | path | ✅ | `string` | The name of the image. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create Image operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `Image` | Parameters supplied to the Create Image operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `Image` | Resource 'Image' update operation succeeded |
| **201** | `Image` | Resource 'Image' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 Images_Update
**Description:** Update an image

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}` |
| **Tags** | Images |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **imageName** | path | ✅ | `string` | The name of the image. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update Image operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `ImageUpdate` | Parameters supplied to the Update Image operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `Image` | Azure operation completed successfully. |
| **201** | `Image` | Resource 'Image' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 Images_Delete
**Description:** Deletes an Image

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/images/{imageName}` |
| **Tags** | Images |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **imageName** | path | ✅ | `string` | The name of the image. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 ProximityPlacementGroups_ListByResourceGroup
**Description:** Lists all proximity placement groups in a resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups` |
| **Tags** | ProximityPlacementGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ProximityPlacementGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 ProximityPlacementGroups_Get
**Description:** Retrieves information about a proximity placement group 

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName}` |
| **Tags** | ProximityPlacementGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **proximityPlacementGroupName** | path | ✅ | `string` | The name of the proximity placement group. |
| **includeColocationStatus** | query | ❌ | `string` | includeColocationStatus=true enables fetching the colocation status of all the resources in the proximity placement group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ProximityPlacementGroup` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 ProximityPlacementGroups_CreateOrUpdate
**Description:** Create or update a proximity placement group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName}` |
| **Tags** | ProximityPlacementGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **proximityPlacementGroupName** | path | ✅ | `string` | The name of the proximity placement group. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create Proximity Placement Group operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `ProximityPlacementGroup` | Parameters supplied to the Create Proximity Placement Group operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ProximityPlacementGroup` | Resource 'ProximityPlacementGroup' update operation succeeded |
| **201** | `ProximityPlacementGroup` | Resource 'ProximityPlacementGroup' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 ProximityPlacementGroups_Update
**Description:** Update a proximity placement group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName}` |
| **Tags** | ProximityPlacementGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **proximityPlacementGroupName** | path | ✅ | `string` | The name of the proximity placement group. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update Proximity Placement Group operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `ProximityPlacementGroupUpdate` | Parameters supplied to the Update Proximity Placement Group operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `ProximityPlacementGroup` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 ProximityPlacementGroups_Delete
**Description:** Delete a proximity placement group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/proximityPlacementGroups/{proximityPlacementGroupName}` |
| **Tags** | ProximityPlacementGroups |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **proximityPlacementGroupName** | path | ✅ | `string` | The name of the proximity placement group. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePointCollections_List
**Description:** Gets the list of restore point collections in a resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections` |
| **Tags** | RestorePointCollections |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RestorePointCollectionListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePointCollections_Get
**Description:** The operation to get the restore point collection

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}` |
| **Tags** | RestorePointCollections |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **restorePointCollectionName** | path | ✅ | `string` | The name of the restore point collection. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. If expand=restorePoints, server will return all contained restore points in the restorePointCollection. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RestorePointCollection` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePointCollections_CreateOrUpdate
**Description:** The operation to create or update the restore point collection

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}` |
| **Tags** | RestorePointCollections |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **restorePointCollectionName** | path | ✅ | `string` | The name of the restore point collection. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create or Update restore point collection operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `RestorePointCollection` | Parameters supplied to the Create or Update restore point collection operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RestorePointCollection` | Resource 'RestorePointCollection' update operation succeeded |
| **201** | `RestorePointCollection` | Resource 'RestorePointCollection' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePointCollections_Update
**Description:** The operation to update the restore point collection

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}` |
| **Tags** | RestorePointCollections |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **restorePointCollectionName** | path | ✅ | `string` | The name of the restore point collection. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update restore point collection operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `RestorePointCollectionUpdate` | Parameters supplied to the Update restore point collection operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RestorePointCollection` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePointCollections_Delete
**Description:** The operation to delete the restore point collection

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}` |
| **Tags** | RestorePointCollections |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **restorePointCollectionName** | path | ✅ | `string` | The name of the restore point collection. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePoints_Get
**Description:** The operation to get the restore point

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{restorePointName}` |
| **Tags** | RestorePoints |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **restorePointCollectionName** | path | ✅ | `string` | The name of the restore point collection. |
| **restorePointName** | path | ✅ | `string` | The name of the restore point. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'InstanceView' retrieves information about the run-time state of a restore point. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RestorePoint` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePoints_Create
**Description:** The operation to create the restore point

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{restorePointName}` |
| **Tags** | RestorePoints |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **restorePointCollectionName** | path | ✅ | `string` | The name of the restore point collection. |
| **restorePointName** | path | ✅ | `string` | The name of the restore point. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create restore point operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `RestorePoint` | Parameters supplied to the Create restore point operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **201** | `RestorePoint` | Resource 'RestorePoint' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 RestorePoints_Delete
**Description:** The operation to delete the restore point

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/restorePointCollections/{restorePointCollectionName}/restorePoints/{restorePointName}` |
| **Tags** | RestorePoints |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **restorePointCollectionName** | path | ✅ | `string` | The name of the restore point collection. |
| **restorePointName** | path | ✅ | `string` | The name of the restore point. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 SshPublicKeys_ListByResourceGroup
**Description:** Lists all of the SSH public keys in the specified resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/sshPublicKeys` |
| **Tags** | SshPublicKeyResources |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `SshPublicKeysGroupListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 SshPublicKeys_Get
**Description:** Retrieves information about an SSH public key

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/sshPublicKeys/{sshPublicKeyName}` |
| **Tags** | SshPublicKeyResources |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **sshPublicKeyName** | path | ✅ | `string` | The name of the SSH public key. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `SshPublicKeyResource` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 SshPublicKeys_Create
**Description:** Creates a new SSH public key resource

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/sshPublicKeys/{sshPublicKeyName}` |
| **Tags** | SshPublicKeyResources |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **sshPublicKeyName** | path | ✅ | `string` | The name of the SSH public key. |
| **parameters** | body | ✅ | `object` | Parameters supplied to create the SSH public key. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `SshPublicKeyResource` | Parameters supplied to create the SSH public key. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `SshPublicKeyResource` | Resource 'SshPublicKeyResource' update operation succeeded |
| **201** | `SshPublicKeyResource` | Resource 'SshPublicKeyResource' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 SshPublicKeys_Update
**Description:** Updates a new SSH public key resource

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/sshPublicKeys/{sshPublicKeyName}` |
| **Tags** | SshPublicKeyResources |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **sshPublicKeyName** | path | ✅ | `string` | The name of the SSH public key. |
| **parameters** | body | ✅ | `object` | Parameters supplied to update the SSH public key. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `SshPublicKeyUpdateResource` | Parameters supplied to update the SSH public key. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `SshPublicKeyResource` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 SshPublicKeys_Delete
**Description:** Delete an SSH public key

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/sshPublicKeys/{sshPublicKeyName}` |
| **Tags** | SshPublicKeyResources |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **sshPublicKeyName** | path | ✅ | `string` | The name of the SSH public key. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 SshPublicKeys_GenerateKeyPair
**Description:** Generates and returns a public/private key pair and populates the SSH public key resource with the public key

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/sshPublicKeys/{sshPublicKeyName}/generateKeyPair` |
| **Tags** | SshPublicKeyResources |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **sshPublicKeyName** | path | ✅ | `string` | The name of the SSH public key. |
| **parameters** | body | ❌ | `object` | Parameters supplied to generate the SSH public key. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `SshGenerateKeyPairInputParameters` | Parameters supplied to generate the SSH public key. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `SshPublicKeyGenerateKeyPairResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_List
**Description:** Gets a list of all VM scale sets under a resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Get
**Description:** Display information about a virtual machine scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'UserData' retrieves the UserData property of the VM scale set that was provided by the user during the VM scale set Create/Update operation |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSet` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_CreateOrUpdate
**Description:** Create or update a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **If-Match** | header | ❌ | `string` | The ETag of the transformation. Omit this value to always overwrite the current resource. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. |
| **If-None-Match** | header | ❌ | `string` | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will result in error from server as they are not supported. |
| **parameters** | body | ✅ | `object` | The scale set object. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSet` | The scale set object. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSet` | Resource 'VirtualMachineScaleSet' update operation succeeded |
| **201** | `VirtualMachineScaleSet` | Resource 'VirtualMachineScaleSet' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Update
**Description:** Update a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **If-Match** | header | ❌ | `string` | The ETag of the transformation. Omit this value to always overwrite the current resource. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. |
| **If-None-Match** | header | ❌ | `string` | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will result in error from server as they are not supported. |
| **parameters** | body | ✅ | `object` | The scale set object. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetUpdate` | The scale set object. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSet` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Delete
**Description:** Deletes a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **forceDeletion** | query | ❌ | `boolean` | Optional parameter to force delete a VM scale set. (Feature in Preview) |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ApproveRollingUpgrade
**Description:** Approve upgrade on deferred rolling upgrades for OS disks in the virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/approveRollingUpgrade` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ConvertToSinglePlacementGroup
**Description:** Converts SinglePlacementGroup property to false for a existing virtual machine scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/convertToSinglePlacementGroup` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **parameters** | body | ✅ | `object` | The input object for ConvertToSinglePlacementGroup API. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VMScaleSetConvertToSinglePlacementGroupInput` | The input object for ConvertToSinglePlacementGroup API. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Deallocate
**Description:** Deallocates specific virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/deallocate` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **hibernate** | query | ❌ | `boolean` | Optional parameter to hibernate a virtual machine from the VM scale set. (This feature is available for VMSS with Flexible OrchestrationMode only) |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_DeleteInstances
**Description:** Deletes virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/delete` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **forceDeletion** | query | ❌ | `boolean` | Optional parameter to force delete virtual machines from the VM scale set. (Feature in Preview) |
| **vmInstanceIDs** | body | ✅ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceRequiredIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetRollingUpgrades_StartExtensionUpgrade
**Description:** Starts a rolling upgrade to move all extensions for all virtual machine scale set instances to the latest available extension version

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensionRollingUpgrade` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetExtensions_List
**Description:** Gets a list of all extensions in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions` |
| **Tags** | VirtualMachineScaleSetExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetExtensionListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetExtensions_Get
**Description:** The operation to get the extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}` |
| **Tags** | VirtualMachineScaleSetExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmssExtensionName** | path | ✅ | `string` | The name of the VM scale set extension. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetExtension` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetExtensions_CreateOrUpdate
**Description:** The operation to create or update an extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}` |
| **Tags** | VirtualMachineScaleSetExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmssExtensionName** | path | ✅ | `string` | The name of the VM scale set extension. |
| **extensionParameters** | body | ✅ | `object` | Parameters supplied to the Create VM scale set Extension operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetExtension` | Parameters supplied to the Create VM scale set Extension operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetExtension` | Resource 'VirtualMachineScaleSetExtension' update operation succeeded |
| **201** | `VirtualMachineScaleSetExtension` | Resource 'VirtualMachineScaleSetExtension' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetExtensions_Update
**Description:** The operation to update an extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}` |
| **Tags** | VirtualMachineScaleSetExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmssExtensionName** | path | ✅ | `string` | The name of the VM scale set extension. |
| **extensionParameters** | body | ✅ | `object` | Parameters supplied to the Update VM scale set Extension operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetExtensionUpdate` | Parameters supplied to the Update VM scale set Extension operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetExtension` | Azure operation completed successfully. |
| **201** | `VirtualMachineScaleSetExtension` | Resource 'VirtualMachineScaleSetExtension' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetExtensions_Delete
**Description:** The operation to delete the extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/extensions/{vmssExtensionName}` |
| **Tags** | VirtualMachineScaleSetExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmssExtensionName** | path | ✅ | `string` | The name of the VM scale set extension. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ForceRecoveryServiceFabricPlatformUpdateDomainWalk
**Description:** Manual platform update domain walk to update virtual machines in a service fabric virtual machine scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/forceRecoveryServiceFabricPlatformUpdateDomainWalk` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **platformUpdateDomain** | query | ✅ | `integer` | The platform update domain for which a manual recovery walk is requested |
| **zone** | query | ❌ | `string` | The zone in which the manual recovery walk is requested for cross zone virtual machine scale set |
| **placementGroupId** | query | ❌ | `string` | The placement group id for which the manual recovery walk is requested. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RecoveryWalkResponse` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_GetInstanceView
**Description:** Gets the status of a VM scale set instance

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/instanceView` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetInstanceView` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_UpdateInstances
**Description:** Upgrades one or more virtual machines to the latest SKU set in the VM scale set model

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/manualupgrade` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmInstanceIDs** | body | ✅ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceRequiredIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetRollingUpgrades_StartOSUpgrade
**Description:** Starts a rolling upgrade to move all virtual machine scale set instances to the latest available Platform Image OS version

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osRollingUpgrade` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_GetOSUpgradeHistory
**Description:** Gets list of OS upgrades on a VM scale set instance

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/osUpgradeHistory` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetListOSUpgradeHistory` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_PerformMaintenance
**Description:** Perform maintenance on one or more virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/performMaintenance` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_PowerOff
**Description:** Power off (stop) one or more virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/poweroff` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **skipShutdown** | query | ❌ | `boolean` | The parameter to request non-graceful VM shutdown. True value for this flag indicates non-graceful shutdown whereas false indicates otherwise. Default value for this flag is false if not specified |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Reapply
**Description:** Reapplies the Virtual Machine Scale Set Virtual Machine Profile to the Virtual Machine Instances

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/reapply` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Redeploy
**Description:** Shuts down all the virtual machines in the virtual machine scale set, moves them to a new node, and powers them back on

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/redeploy` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Reimage
**Description:** Reimages (upgrade the operating system) one or more virtual machines in a VM scale set which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/reimage` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmScaleSetReimageInput** | body | ❌ | `object` | Parameters for Reimaging VM ScaleSet. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetReimageParameters` | Parameters for Reimaging VM ScaleSet. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ReimageAll
**Description:** Reimages all the disks ( including data disks ) in the virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/reimageall` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Restart
**Description:** Restarts one or more virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/restart` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetRollingUpgrades_Cancel
**Description:** Cancels the current virtual machine scale set rolling upgrade

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/cancel` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetRollingUpgrades_GetLatest
**Description:** Gets the status of the latest virtual machine scale set rolling upgrade

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/rollingUpgrades/latest` |
| **Tags** | RollingUpgradeStatusInfos |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RollingUpgradeStatusInfo` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ScaleOut
**Description:** Scales out one or more virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/scaleOut` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **parameters** | body | ✅ | `object` | The input object for ScaleOut API. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VMScaleSetScaleOutInput` | The input object for ScaleOut API. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_SetOrchestrationServiceState
**Description:** Changes ServiceState property for a given service

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/setOrchestrationServiceState` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **parameters** | body | ✅ | `object` | The input object for SetOrchestrationServiceState API. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `OrchestrationServiceStateInput` | The input object for SetOrchestrationServiceState API. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_ListSkus
**Description:** Gets a list of SKUs available for your VM scale set, including the minimum and maximum VM instances allowed for each SKU

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/skus` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetListSkusResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSets_Start
**Description:** Starts one or more virtual machines in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/start` |
| **Tags** | VirtualMachineScaleSets |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **vmInstanceIDs** | body | ❌ | `object` | A list of virtual machine instance IDs from the VM scale set. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMInstanceIDs` | A list of virtual machine instance IDs from the VM scale set. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_List
**Description:** Gets a list of all virtual machines in a VM scale sets

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{virtualMachineScaleSetName}/virtualMachines` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **virtualMachineScaleSetName** | path | ✅ | `string` | The name of the VirtualMachineScaleSet |
| **$filter** | query | ❌ | `string` | The filter to apply to the operation. Allowed values are 'startswith(instanceView/statuses/code, 'PowerState') eq true', 'properties/latestModelApplied eq true', 'properties/latestModelApplied eq false'. |
| **$select** | query | ❌ | `string` | The list parameters. Allowed values are 'instanceView', 'instanceView/statuses'. |
| **$expand** | query | ❌ | `string` | The expand expression to apply to the operation. Allowed values are 'instanceView'. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVMListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Get
**Description:** Gets a virtual machine from a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'InstanceView' will retrieve the instance view of the virtual machine. 'UserData' will retrieve the UserData of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVM` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Update
**Description:** Updates a virtual machine of a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **If-Match** | header | ❌ | `string` | The ETag of the transformation. Omit this value to always overwrite the current resource. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. |
| **If-None-Match** | header | ❌ | `string` | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will result in error from server as they are not supported. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update Virtual Machine Scale Sets VM operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVM` | Parameters supplied to the Update Virtual Machine Scale Sets VM operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVM` | Resource 'VirtualMachineScaleSetVM' update operation succeeded |
| **202** | `VirtualMachineScaleSetVM` | The request has been accepted for processing, but processing has not yet completed. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Delete
**Description:** Deletes a virtual machine from a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **forceDeletion** | query | ❌ | `boolean` | Optional parameter to force delete a virtual machine from a VM scale set. (Feature in Preview) |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_ApproveRollingUpgrade
**Description:** Approve upgrade on deferred rolling upgrade for OS disk on a VM scale set instance

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/approveRollingUpgrade` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_AttachDetachDataDisks
**Description:** Attach and detach data disks to/from a virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/attachDetachDataDisks` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the attach and detach data disks operation on a Virtual Machine Scale Sets VM. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `AttachDetachDataDisksRequest` | Parameters supplied to the attach and detach data disks operation on a Virtual Machine Scale Sets VM. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `StorageProfile` | Azure operation completed successfully. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Deallocate
**Description:** Deallocates a specific virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/deallocate` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMExtensions_List
**Description:** The operation to get all extensions of an instance in Virtual Machine Scaleset

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions` |
| **Tags** | VirtualMachineScaleSetVMExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVMExtensionsListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMExtensions_Get
**Description:** The operation to get the VMSS VM extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineScaleSetVMExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVMExtension` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMExtensions_CreateOrUpdate
**Description:** The operation to create or update the VMSS VM extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineScaleSetVMExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |
| **extensionParameters** | body | ✅ | `object` | Parameters supplied to the Create Virtual Machine Extension operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMExtension` | Parameters supplied to the Create Virtual Machine Extension operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVMExtension` | Resource 'VirtualMachineScaleSetVMExtension' update operation succeeded |
| **201** | `VirtualMachineScaleSetVMExtension` | Resource 'VirtualMachineScaleSetVMExtension' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMExtensions_Update
**Description:** The operation to update the VMSS VM extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineScaleSetVMExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |
| **extensionParameters** | body | ✅ | `object` | Parameters supplied to the Update Virtual Machine Extension operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMExtensionUpdate` | Parameters supplied to the Update Virtual Machine Extension operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVMExtension` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMExtensions_Delete
**Description:** The operation to delete the VMSS VM extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineScaleSetVMExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_GetInstanceView
**Description:** Gets the status of a virtual machine from a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/instanceView` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineScaleSetVMInstanceView` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_PerformMaintenance
**Description:** Performs maintenance on a virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/performMaintenance` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_PowerOff
**Description:** Power off (stop) a virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/powerOff` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **skipShutdown** | query | ❌ | `boolean` | The parameter to request non-graceful VM shutdown. True value for this flag indicates non-graceful shutdown whereas false indicates otherwise. Default value for this flag is false if not specified |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Redeploy
**Description:** Shuts down the virtual machine in the virtual machine scale set, moves it to a new node, and powers it back on

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/redeploy` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Reimage
**Description:** Reimages (upgrade the operating system) a specific virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/reimage` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **vmScaleSetVMReimageInput** | body | ❌ | `object` | Parameters for the Reimaging Virtual machine in ScaleSet. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineScaleSetVMReimageParameters` | Parameters for the Reimaging Virtual machine in ScaleSet. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_ReimageAll
**Description:** Allows you to re-image all the disks ( including data disks ) in the a VM scale set instance

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/reimageall` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Restart
**Description:** Restarts a virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/restart` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_RetrieveBootDiagnosticsData
**Description:** The operation to retrieve SAS URIs of boot diagnostic logs for a virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/retrieveBootDiagnosticsData` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **sasUriExpirationTimeInMinutes** | query | ❌ | `integer` | Expiration duration in minutes for the SAS URIs with a value between 1 to 1440 minutes. **Note:** If not specified, SAS URIs will be generated with a default expiration duration of 120 minutes. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RetrieveBootDiagnosticsDataResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_RunCommand
**Description:** Run command on a virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/runCommand` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Run command operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `RunCommandInput` | Parameters supplied to the Run command operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RunCommandResult` | Azure operation completed successfully. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMRunCommands_List
**Description:** The operation to get all run commands of an instance in Virtual Machine Scaleset

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/runCommands` |
| **Tags** | VirtualMachineScaleSetVMRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VirtualMachineScaleSet |
| **instanceId** | path | ✅ | `string` | The name of the VirtualMachineScaleSetVM |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommandsListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMRunCommands_Get
**Description:** The operation to get the VMSS VM run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineScaleSetVMRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VirtualMachineScaleSet |
| **instanceId** | path | ✅ | `string` | The name of the VirtualMachineScaleSetVM |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommand` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMRunCommands_CreateOrUpdate
**Description:** The operation to create or update the VMSS VM run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineScaleSetVMRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VirtualMachineScaleSet |
| **instanceId** | path | ✅ | `string` | The name of the VirtualMachineScaleSetVM |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |
| **runCommand** | body | ✅ | `object` | Parameters supplied to the Create Virtual Machine RunCommand operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineRunCommand` | Parameters supplied to the Create Virtual Machine RunCommand operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommand` | Resource 'VirtualMachineRunCommand' update operation succeeded |
| **201** | `VirtualMachineRunCommand` | Resource 'VirtualMachineRunCommand' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMRunCommands_Update
**Description:** The operation to update the VMSS VM run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineScaleSetVMRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VirtualMachineScaleSet |
| **instanceId** | path | ✅ | `string` | The name of the VirtualMachineScaleSetVM |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |
| **runCommand** | body | ✅ | `object` | Resource create parameters. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineRunCommandUpdate` | Resource create parameters. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommand` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMRunCommands_Delete
**Description:** The operation to delete the VMSS VM run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineScaleSetVMRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VirtualMachineScaleSet |
| **instanceId** | path | ✅ | `string` | The name of the VirtualMachineScaleSetVM |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_SimulateEviction
**Description:** The operation to simulate the eviction of spot virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/simulateEviction` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **204** | `A` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineScaleSetVMs_Start
**Description:** Starts a virtual machine in a VM scale set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmScaleSetName}/virtualMachines/{instanceId}/start` |
| **Tags** | VirtualMachineScaleSetVMS |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmScaleSetName** | path | ✅ | `string` | The name of the VM scale set. |
| **instanceId** | path | ✅ | `string` | The instance ID of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_List
**Description:** Lists all of the virtual machines in the specified resource group

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **$filter** | query | ❌ | `string` | The system query option to filter VMs returned in the response. Allowed value is 'virtualMachineScaleSet/id' eq /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachineScaleSets/{vmssName}' |
| **$expand** | query | ❌ | `string` | The expand expression to apply on operation. 'instanceView' enables fetching run time status of all Virtual Machines, this can only be specified if a valid $filter option is specified |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Get
**Description:** Retrieves information about the model view or the instance view of a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. 'InstanceView' retrieves a snapshot of the runtime properties of the virtual machine that is managed by the platform and can change outside of control plane operations. 'UserData' retrieves the UserData property as part of the VM model view that was provided by the user during the VM Create/Update operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachine` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_CreateOrUpdate
**Description:** The operation to create or update a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **If-Match** | header | ❌ | `string` | The ETag of the transformation. Omit this value to always overwrite the current resource. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. |
| **If-None-Match** | header | ❌ | `string` | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will result in error from server as they are not supported. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Create Virtual Machine operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachine` | Parameters supplied to the Create Virtual Machine operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachine` | Resource 'VirtualMachine' update operation succeeded |
| **201** | `VirtualMachine` | Resource 'VirtualMachine' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Update
**Description:** The operation to update a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **If-Match** | header | ❌ | `string` | The ETag of the transformation. Omit this value to always overwrite the current resource. Specify the last-seen ETag value to prevent accidentally overwriting concurrent changes. |
| **If-None-Match** | header | ❌ | `string` | Set to '*' to allow a new record set to be created, but to prevent updating an existing record set. Other values will result in error from server as they are not supported. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Update Virtual Machine operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineUpdate` | Parameters supplied to the Update Virtual Machine operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachine` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Delete
**Description:** The operation to delete a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **forceDeletion** | query | ❌ | `boolean` | Optional parameter to force delete virtual machines. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_AssessPatches
**Description:** Assess patches on the VM

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/assessPatches` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineAssessPatchesResult` | Azure operation completed successfully. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_AttachDetachDataDisks
**Description:** Attach and detach data disks to/from the virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/attachDetachDataDisks` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the attach and detach data disks operation on the virtual machine. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `AttachDetachDataDisksRequest` | Parameters supplied to the attach and detach data disks operation on the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `StorageProfile` | Azure operation completed successfully. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Capture
**Description:** Captures the VM by copying virtual hard disks of the VM and outputs a template that can be used to create similar VMs

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/capture` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Capture Virtual Machine operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineCaptureParameters` | Parameters supplied to the Capture Virtual Machine operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineCaptureResult` | Azure operation completed successfully. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_ConvertToManagedDisks
**Description:** Converts virtual machine disks from blob-based to managed disks

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/convertToManagedDisks` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Deallocate
**Description:** Shuts down the virtual machine and releases the compute resources

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/deallocate` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **hibernate** | query | ❌ | `boolean` | Optional parameter to hibernate a virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensions_List
**Description:** The operation to get all extensions of a Virtual Machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions` |
| **Tags** | VirtualMachineExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineExtensionsListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensions_Get
**Description:** The operation to get the extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineExtension` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensions_CreateOrUpdate
**Description:** The operation to create or update the extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |
| **extensionParameters** | body | ✅ | `object` | Parameters supplied to the Create Virtual Machine Extension operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineExtension` | Parameters supplied to the Create Virtual Machine Extension operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineExtension` | Resource 'VirtualMachineExtension' update operation succeeded |
| **201** | `VirtualMachineExtension` | Resource 'VirtualMachineExtension' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensions_Update
**Description:** The operation to update the extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |
| **extensionParameters** | body | ✅ | `object` | Parameters supplied to the Update Virtual Machine Extension operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineExtensionUpdate` | Parameters supplied to the Update Virtual Machine Extension operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineExtension` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineExtensions_Delete
**Description:** The operation to delete the extension

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/extensions/{vmExtensionName}` |
| **Tags** | VirtualMachineExtensions |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **vmExtensionName** | path | ✅ | `string` | The name of the virtual machine extension. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Generalize
**Description:** Sets the OS state of the virtual machine to generalized

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/generalize` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_InstallPatches
**Description:** Installs patches on the VM

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/installPatches` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **installPatchesInput** | body | ✅ | `object` | Input for InstallPatches as directly received by the API |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineInstallPatchesParameters` | Input for InstallPatches as directly received by the API |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineInstallPatchesResult` | Azure operation completed successfully. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_InstanceView
**Description:** Retrieves information about the run-time state of a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/instanceView` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineInstanceView` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_migrateToVMScaleSet
**Description:** Migrate a virtual machine from availability set to Flexible Virtual Machine Scale Set

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/migrateToVirtualMachineScaleSet` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **parameters** | body | ❌ | `object` | Parameters supplied to the Migrate Virtual Machine operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `MigrateVMToVirtualMachineScaleSetInput` | Parameters supplied to the Migrate Virtual Machine operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_PerformMaintenance
**Description:** The operation to perform maintenance on a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/performMaintenance` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_PowerOff
**Description:** The operation to power off (stop) a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/powerOff` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **skipShutdown** | query | ❌ | `boolean` | The parameter to request non-graceful VM shutdown. True value for this flag indicates non-graceful shutdown whereas false indicates otherwise. Default value for this flag is false if not specified |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Reapply
**Description:** The operation to reapply a virtual machine's state

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/reapply` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Redeploy
**Description:** Shuts down the virtual machine, moves it to a new node, and powers it back on

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/redeploy` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Reimage
**Description:** Reimages (upgrade the operating system) a virtual machine which don't have a ephemeral OS disk, for virtual machines who have a ephemeral OS disk the virtual machine is reset to initial state

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/reimage` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **parameters** | body | ❌ | `object` | Parameters supplied to the Reimage Virtual Machine operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineReimageParameters` | Parameters supplied to the Reimage Virtual Machine operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Restart
**Description:** The operation to restart a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/restart` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_RetrieveBootDiagnosticsData
**Description:** The operation to retrieve SAS URIs for a virtual machine's boot diagnostic logs

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/retrieveBootDiagnosticsData` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **sasUriExpirationTimeInMinutes** | query | ❌ | `integer` | Expiration duration in minutes for the SAS URIs with a value between 1 to 1440 minutes. **Note:** If not specified, SAS URIs will be generated with a default expiration duration of 120 minutes. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RetrieveBootDiagnosticsDataResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_RunCommand
**Description:** Run command on the VM

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommand` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |
| **parameters** | body | ✅ | `object` | Parameters supplied to the Run command operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `RunCommandInput` | Parameters supplied to the Run command operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `RunCommandResult` | Azure operation completed successfully. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineRunCommands_ListByVirtualMachine
**Description:** The operation to get all run commands of a Virtual Machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommands` |
| **Tags** | VirtualMachineRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the VirtualMachine |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommandsListResult` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineRunCommands_GetByVirtualMachine
**Description:** The operation to get the run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the VirtualMachine |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |
| **$expand** | query | ❌ | `string` | The expand expression to apply on the operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommand` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineRunCommands_CreateOrUpdate
**Description:** The operation to create or update the run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PUT` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the VirtualMachine |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |
| **runCommand** | body | ✅ | `object` | Parameters supplied to the Create Virtual Machine RunCommand operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineRunCommand` | Parameters supplied to the Create Virtual Machine RunCommand operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommand` | Resource 'VirtualMachineRunCommand' update operation succeeded |
| **201** | `VirtualMachineRunCommand` | Resource 'VirtualMachineRunCommand' create operation succeeded |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineRunCommands_Update
**Description:** The operation to update the run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `PATCH` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the VirtualMachine |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |
| **runCommand** | body | ✅ | `object` | Parameters supplied to the Update Virtual Machine RunCommand operation. |

#### 📦 Request Body
| Name | Required | Type/Schema | Description |
| :--- | :---: | :--- | :--- |
| (Body Content) | ✅ | `VirtualMachineRunCommandUpdate` | Parameters supplied to the Update Virtual Machine RunCommand operation. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineRunCommand` | The request has succeeded. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachineRunCommands_Delete
**Description:** The operation to delete the run command

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `DELETE` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/runCommands/{runCommandName}` |
| **Tags** | VirtualMachineRunCommands |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the VirtualMachine |
| **runCommandName** | path | ✅ | `string` | The name of the VirtualMachineRunCommand |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | Resource deleted successfully. |
| **202** | `A` | Resource deletion accepted. |
| **204** | `A` | Resource does not exist. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_SimulateEviction
**Description:** The operation to simulate the eviction of spot virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/simulateEviction` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **204** | `A` | There is no content to send for this request, but the headers may be useful. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_Start
**Description:** The operation to start a virtual machine

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `POST` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/start` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `A` | The request has succeeded. |
| **202** | `A` | Resource operation accepted. |
| **default** | `CloudError` | An unexpected error response. |

---

## 🚀 VirtualMachines_ListAvailableSizes
**Description:** Lists all available virtual machine sizes to which the specified virtual machine can be resized

#### 📌 Base Information
| Field | Details |
| :--- | :--- |
| **Method** | `GET` |
| **Endpoint** | `/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Compute/virtualMachines/{vmName}/vmSizes` |
| **Tags** | VirtualMachines |

#### 🛠️ URI Parameters
| Name | In | Required | Type | Description |
| :--- | :---: | :---: | :---: | :--- |
| ApiVersionParameter | (Ref) | - | - | 공통 정의 참조 |
| SubscriptionIdParameter | (Ref) | - | - | 공통 정의 참조 |
| ResourceGroupNameParameter | (Ref) | - | - | 공통 정의 참조 |
| **vmName** | path | ✅ | `string` | The name of the virtual machine. |

#### ✅ Responses
| Code | Schema | Description |
| :---: | :--- | :--- |
| **200** | `VirtualMachineSizeListResult` | Azure operation completed successfully. |
| **default** | `CloudError` | An unexpected error response. |

---

