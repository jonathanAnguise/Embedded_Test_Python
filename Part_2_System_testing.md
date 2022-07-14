# Part2: System Testing

```
  Physiscal
   Device       Cloud    Human
     ▲ │         ▲ │      ▲ │
     │ │         │ │      │ │
     │ │         │ │      │ │
 ┌───┼─┼─────┬─┬─┼─┼──┬─┬─┼─┼──┬─┐
 │   │ │     │ │ │ │  │ │ │ │  │ │
 │   │ ▼     │ │ │ ▼  │ │ │ ▼  │ │
 │ Bluetooth │ │ WiFi │ │ HMI  │ │
 ├───────────┘ └──────┘ └──────┘ │
 │                               │
 │             EMBEDDED          │
 │                │ ▲            │
 │                │ │            │
 ├────────────────┼─┼────────────┤
 │                │ │            │
 │                ▼ │            │
 │             FIRMWARE          │
 │                ▲ │            │
 │                │ │            │
 ├────────────────┼─┼────────────┤
 │                │ │            │
 │                  ▼            │
 │            ELECTRONICS        │
 └───────────────────────────────┘
```

## 1. How would you test that the API between the embedded and the cloud is working as expected without having a real physical device
The device must perform certain actions that generate requests like POST, GET, DELETE using a specific protocol (HTTP/S for example). So we can recreate these actions and check on the server (test server) if the action is correct. For example, let's imagine the function:
	`create_user(name, password)`, we can run the function in our emulated environment, check in the network using wireshark for example the POST request, and check on our server if there is in our database the name string and the password in the right format (encoded for security reasons). And we do for all the functions that the API documentation shows. The weakness here is that we can't really test the UI part: for example if after creating the user the application changes color, we can see a change of variable but we don't really know if it is really as expected graphically. But here the problem can be found with a higher level test or a beta tester if there is one.

## 2. How would you test that the API between the embedded and the mobile is working as expected without having the real physical device
Same logic here, we will emulate the API response using the mock function and check if the behavior is correct. For example, let's say the application needs to ask the API who the president of the United States is. We can execute the specific GET function and parse the response which should be a json file. Check if the information is correct and the structure as well. Also, we can perform a performance test to get the response in time. And we can do the same for all API functions by analyzing the response, positive response, different 404, 403 error messages, etc.

## For both points
>> __Please note that all functions related to bluetooth communication must be mocked to obtain the same behavior as the device here.__
