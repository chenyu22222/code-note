from task import add_together

result = add_together.delay(10, 20)
print(result.wait())