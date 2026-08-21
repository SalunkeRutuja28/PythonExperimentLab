#String slicing
def main():
    phone = "+1 617-598-1002"
    # print(phone[0:3]) #617
    print(phone[:3]) #617
    print(phone[8:12]) #1002
    print(phone[8:]) #98-1002
    print(phone[-4:]) #1002

main()