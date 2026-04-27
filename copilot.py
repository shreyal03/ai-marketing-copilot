def marketing_copilot(goal):
    if goal == "increase retention":
        return {
            "audience": "inactive users",
            "channel": "email",
            "message": "We miss you! Here’s an offer just for you."
        }
    elif goal == "increase sales":
        return {
            "audience": "high-value users",
            "channel": "push notification",
            "message": "Exclusive deal just for you!"
        }
    else:
        return {
            "audience": "all users",
            "channel": "email",
            "message": "Check out our latest updates!"
        }

# Example
result = marketing_copilot("increase retention")

print("Recommended Campaign:")
for key, value in result.items():
    print(f"{key}: {value}")
