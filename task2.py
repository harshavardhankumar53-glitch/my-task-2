def phishing_training():
    print("🚨 Phishing Awareness Training 🚨\n")
    print("Phishing is a cyberattack where attackers trick you into revealing sensitive information.")
    print("\n🔎 How to recognize phishing emails:")
    print("- Suspicious sender address")
    print("- Urgent or threatening language")
    print("- Links to fake websites")
    print("- Unexpected attachments")

    print("\n🧠 Example:")
    print("Email: 'Your bank account will be locked! Click here to verify.'")
    print("👉 This is a phishing attempt!")

    print("\n✅ Best Practices:")
    print("- Verify sender identity")
    print("- Don’t click unknown links")
    print("- Report suspicious emails")
    print("- Use multi-factor authentication")

    # Simple quiz
    print("\n📋 Quick Quiz:")
    answer = input("Q: An email says 'You won a lottery, click here to claim!' Is this phishing? (yes/no): ").lower()
    if answer == "yes":
        print("🎉 Correct! That’s a phishing attempt.")
    else:
        print("❌ Incorrect. That’s a phishing attempt.")

# Run training
phishing_training()
