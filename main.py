import requests


def teacher_list():
    url = "http://127.0.0.1:8000/teacher/"
    response = requests.get(url).json()
    return response


def student_list():
    url = "http://127.0.0.1:8000/student/"
    response = requests.get(url).json()
    return response


def create_student(full_name, should_give, gave, payment_types, teacher):
    url = f"http://127.0.0.1:8000/student/"
    response = requests.post(url, json={
        "full_name": full_name,
        "should_give": should_give,
        "gave": gave,
        "payment_types": payment_types,
        "teacher": teacher
    })
    return response


def plan():
    url = f"http://127.0.0.1:8000/students/plan/"
    response = requests.get(url).json()
    return response


print(plan())
