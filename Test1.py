

chat = []

n = int(input("Enter number of messages: "))
print("Enter messages in format: Name: message")

for _ in range(n):
    line = input()
    if ":" in line:
        name, msg = line.split(":", 1)
        chat.append((name.strip(), msg.strip()))
    else:
        chat.append(("Unknown", line.strip()))

while True:
    print("\n--- MENU ---")
    print("1. Total messages")
    print("2. Unique users")
    print("3. Total words")
    print("4. Average words per message")
    print("5. Longest message")
    print("6. Most active user")
    print("7. Messages by a user")
    print("8. Most frequent word by a user")
    print("9. First & last message by user")
    print("10. Check if user present")
    print("11. Repeated words")
    print("13. User with longest avg message")
    print("14. Count mentions of a user")
    print("15. Remove duplicate messages")
    print("16. Sort messages A-Z")
    print("17. Show questions")
    print("18. Reply ratio")
    print("19. Deleted messages")
    print("0. Exit")

    ch = int(input("Enter choice: "))

    if ch == 0:
        break

    elif ch == 1:
        print("Total messages =", len(chat))

    elif ch == 2:
        users = {name for name, msg in chat}
        print("Users =", users)

    elif ch == 3:
        tw = sum(len(msg.split()) for name, msg in chat)
        print("Total words =", tw)

    elif ch == 4:
        tw = sum(len(msg.split()) for name, msg in chat)
        print("Average words =", tw / len(chat))

    elif ch == 5:
        longest = max(chat, key=lambda x: len(x[1]))
        print("Longest message =", longest)

    elif ch == 6:
        count = {}
        for name, msg in chat:
            count[name] = count.get(name, 0) + 1
        print("Most active user =", max(count, key=count.get))

    elif ch == 7:
        u = input("User: ")
        print("Messages =", sum(1 for name, msg in chat if name.lower() == u.lower()))

    elif ch == 8:
        u = input("User: ")
        words = []
        for name, msg in chat:
            if name.lower() == u.lower():
                words += msg.lower().split()
        if words:
            freq = {w: words.count(w) for w in words}
            print(max(freq, key=freq.get))
        else:
            print("No words")

    elif ch == 9:
        u = input("User: ")
        msgs = [msg for name, msg in chat if name.lower() == u.lower()]
        if msgs:
            print("First =", msgs[0])
            print("Last  =", msgs[-1])
        else:
            print("No messages")

    elif ch == 10:
        u = input("User: ")
        print(any(name.lower() == u.lower() for name, msg in chat))

    elif ch == 11:
        allw = []
        for name, msg in chat:
            allw += msg.lower().split()
        rep = {w for w in allw if allw.count(w) > 1}
        print(rep)

    elif ch == 13:
        user_words = {}
        for name, msg in chat:
            user_words.setdefault(name, []).append(len(msg.split()))
        best = max(user_words, key=lambda u: sum(user_words[u]) / len(user_words[u]))
        avg = sum(user_words[best]) / len(user_words[best])
        print(best, avg)

    elif ch == 14:
        u = input("User to search: ")
        print(sum(1 for name, msg in chat if u.lower() in msg.lower().split()))

    elif ch == 15:
        seen = set()
        unique = []
        for name, msg in chat:
            full = f"{name}: {msg}"
            if full not in seen:
                unique.append(full)
                seen.add(full)
        print(unique)

    elif ch == 16:
        sorted_msgs = sorted([f"{name}: {msg}" for name, msg in chat])
        print(sorted_msgs)

    elif ch == 17:
        qs = [f"{name}: {msg}" for name, msg in chat if "?" in msg]
        print(qs)

    elif ch == 18:
        a = input("User A: ")
        b = input("User B: ")
        replies = sum(1 for name, msg in chat if name.lower() == b.lower() and a.lower() in msg.lower())
        print("Reply ratio =", replies)

    elif ch == 19:
        print(sum(1 for name, msg in chat if msg == "This message was deleted"))

    else:
        print("Invalid choice")
