import sys

message = "Hello, World!"

print(message)

message_utf8 = message.encode("UTF-8")
print(message_utf8)
print(sys.getsizeof(message_utf8))
print(message_utf8.decode("UTF-8"))

# message_utf16 = message.encode("UTF-16")
# print(message_utf16)
# print(sys.getsizeof(message_utf16))
# print(message_utf16.decode("UTF-16"))

# message_utf32 = message.encode("UTF-32")
# print(message_utf32)
# print(sys.getsizeof(message_utf32))
# print(message_utf32.decode("UTF-32"))
