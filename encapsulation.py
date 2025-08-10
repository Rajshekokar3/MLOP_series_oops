from oops_project import chatbook

user=chatbook()
print(user._chatbook__username)

print(user.get_name())
print(user.set_name("Agent X"))
print(user.get_name())


user1=chatbook()
print(user1.id)
chatbook.set_id(10)
user2=chatbook()
print(user2.id)