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
The device must perform certain actions that will must generate requests like POST, GET, DELETE using a specific protocol (e.g. HTTP/S). Thus, these actions can be mocked and verified on the server (test server) if the action is correct.
An example could be the function:
	`create_user(name, password)`, we can run the function in our emulated environment, For instance, we can check the presence of POST requests in the network using Wireshark, and check on our server if there is in our database the name string and the password in the right format (encoded for security reasons). We do this for all functions that the api documentation has.
	The weakness here is that we can't really test the UI part: for example, if after creating the user the application changes color, we can see a variable change but we don't really know if it is as expected graphically. However, the problem can be found with a higher level test or a beta tester if there is one.

## 2. How would you test that the API between the embedded and the mobile is working as expected without having the real physical device
Same logic here, we will emulate the API response using the mock function and check if its behavior is correct. For example, the application needs get from the API an answer. We can execute the function and parse the API answer which should be a json file. Check if the information is correct and the structure as well. Also, we can do a performance test to get the response time and check if it's acceptable. And we can do the same for all API functions by analyzing the response, positive response, different 404, 403 error messages, etc.

## For both points
> __Please note that all functions related to bluetooth communication must be mocked to obtain the same behavior as the device here.__
