def bit_stuffing(sender_data):
    stuffed_data = []
    count = 0

    for bit in sender_data:
        stuffed_data.append(bit)

        if bit == '1':
            count += 1
        else:
            count = 0

        if count == 5:
            stuffed_data.append('0')
            count = 0

    return ''.join(stuffed_data)

def bit_unstuffing(receiver_data):
    unstuffed_data = []
    i = 0
    count = 0

    while i < len(receiver_data):
        while i < len(receiver_data) and receiver_data[i] == '1':
            unstuffed_data.append(receiver_data[i])
            i += 1
            count += 1
        if i == len(receiver_data):
            break
        if count != 5:
            unstuffed_data.append(receiver_data[i])
        i += 1
        count = 0

    return ''.join(unstuffed_data)





# Stuffing
sender_data = input("Enter sender data (0s and 1s): ")
stuffed_data = bit_stuffing(sender_data)
print('------------------Bit Stuffing----------------------\n')
print("Sender Data:", sender_data)
print("Stuffed Data:", stuffed_data)

# Unstuffing
print('\n------------------Bit Unstuffing----------------------\n')
received_data = stuffed_data
unstuffed_data = bit_unstuffing(received_data)
print("Sending Data:", received_data)
print("Unstuffed Data:", unstuffed_data)
