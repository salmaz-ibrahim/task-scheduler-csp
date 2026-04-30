from scheduler import solve_schedule

test_cases = [
    {
        "name": "Valid input",
        "input": "Study, Gym, Cooking",
        "expected": "success"
    },
    {
        "name": "Empty input",
        "input": "",
        "expected": "error"
    },
    {
        "name": "Duplicate tasks",
        "input": "Study, Study",
        "expected": "duplicate"
    },
    {
        "name": "Extra commas (clean input)",
        "input": "Study,,Gym",
        "expected": "success"
    },
    {
        "name": "Too many tasks",
        "input": "Study, Eat, Clean, Exercise, Work",
        "expected": "slots_error"
    }
]


def evaluate_result(result, expected):
    if expected == "success":
        return result["status"] == "success"

    elif expected == "error":
        return result["status"] == "error"

    elif expected == "duplicate":
        return (
            result["status"] == "error" and
            "Duplicate" in result["message"]
        )

    elif expected == "slots_error":
        return (
            result["status"] == "error" and
            "Not enough time slots" in result["message"]
        )

    return False


def run_tests():
    print("\n🧪 Running Scheduler Tests...\n")

    passed = 0

    for i, test in enumerate(test_cases, 1):
        result = solve_schedule(test["input"])
        is_pass = evaluate_result(result, test["expected"])

        print(f"Test {i}: {test['name']}")
        print(f"Input: {test['input']}")
        print(f"Result: {result}")

        if is_pass:
            print("✔ PASS\n")
            passed += 1
        else:
            print("❌ FAIL\n")

    print(f"Summary: {passed}/{len(test_cases)} tests passed")


if __name__ == "__main__":
    run_tests()