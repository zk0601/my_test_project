import redis

# r = redis.Redis(host='47.110.67.202', port=6379, password='123456')
pool = redis.ConnectionPool(host='47.110.67.202', port=6379, password='123456')
r = redis.Redis(connection_pool=pool)

# r.setex('name', 10, 'he')
#
# r.setex('name', 20, 'haha')
# print(r.get('name'))
print(r.get('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjEsInRpbWVzdGFtcCI6MTU0NzU0MzM4OX0.c9hqSmsxwx5T7wj1zgZqp40hrJqEv3XFAh3rhpntOiE'))
print(r.ttl('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOjEsInRpbWVzdGFtcCI6MTU0NzU0MzM4OX0.c9hqSmsxwx5T7wj1zgZqp40hrJqEv3XFAh3rhpntOiE'))
print(r.keys())
