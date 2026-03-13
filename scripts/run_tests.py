import os


def run_api_tests():
    print("Running API tests...")
    os.system("pytest tests --alluredir=reports/api")

def run_performance_tests():
    print("Running Performance tests...")
    os.system(
        "locust -f performance/locustfile.py --headless -u 10 -r 2 -t 30s --host=https://jsonplaceholder.typicode.com"
    )


if __name__ == "__main__":

    run_api_tests()
    run_performance_tests()

    print("All tests executed")