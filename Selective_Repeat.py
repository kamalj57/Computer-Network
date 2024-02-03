total_packets = int(input("Enter the  number of packets: "))
window_size = int(input("Enter the Window Size: "))
print("------------------------------------------------------------\nSelective Repeat\n------------------------------------------------------------")
if total_packets < 0 or window_size <= 0:
    print("Enter valid input values")
else:
    acknowledged_packets = set()
    tt = 0

    for i in range(1, total_packets + 1, window_size):
        for k in range(i, min(i + window_size, total_packets + 1)):
            tt += 1
            print("Sending Packet:",k)
        
        ack_count = len(set(range(i, i + window_size)).intersection(acknowledged_packets))

        if ack_count < window_size:
            for k in range(i, min(i + window_size, total_packets+ 1)):
                if k % 4 == 0:
                    print("Timeout!!\nAcknowledgment for packet:", k, "not received")
                    print("Retransmitting packet:",k)
                    tt += 1

        for k in range(i, min(i + window_size, total_packets + 1)):
            if k not in acknowledged_packets:
                print("Acknowledgment for packet:", k, "received")
                acknowledged_packets.add(k)
    print("\n------------------------------------------------------------")                        
    print("Total_packets :",total_packets)
    print("Total number of packets sent :", tt)
    print("Number of packets  resented :",tt-total_packets)

