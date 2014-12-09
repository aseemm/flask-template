from app import read_entries

result = read_entries.delay(10)

if result.ready():
    print("Task has run")
    if result.successful():
        print("Results was %s" % result.result)
    else:
        if isinstance(result.result, Exception):
            print("Task failed due to raising an exception")
            raise result.result
        else:
            print("Task failed without raising an exception")
else:
    print("Task has not yet run")
