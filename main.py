import get_from_google as g


ret = g.get_data('python books',0)
for i in ret:
    print(i)

