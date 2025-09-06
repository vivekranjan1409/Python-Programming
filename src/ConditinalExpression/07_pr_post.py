post = input("Enter a post: ")

postLower = post.lower()

if("harry" in postLower):
    print("This post is talking about Harry.")
else:
    print("This post is NOT talking about Harry.")