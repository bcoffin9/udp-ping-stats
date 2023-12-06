# UDP Pinger Lab

## Complete from Computer Networking: A Top-Down Approach 8th Edition

### How to use

1. Run the server code first and keep the terminal running.
2. Open a new terminal and run the client code.
3. You should be able to confirm on both the server and client which packets are successful
4. Verify that the output is created in the resources folder with the statistics from the test

---

## Passing Criteria

- Send 10 Ping Messages to the target server over UDP
- For each message, print the RTT (Round Trip Time)
- The ping will at most for 1 second before determining the packet lost
  - The lost packet will be reported in the output
- There will be a log printed to the console as well as an output file in the results folder
  - The output file will be tagged with a timestamp, avg response time, and the name of the target server

---

## Future Dev Ideas

- Testing coverage
