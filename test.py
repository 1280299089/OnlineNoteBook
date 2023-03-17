from passlib.hash import sha256_crypt

password = "yoyo"
hash = sha256_crypt.hash("yoyo")
print(f"加密后：{hash}")

# 验证密码
result1 = sha256_crypt.verify("yoy1", hash)
print(result1)
result2 = sha256_crypt.verify("yoyo", hash)
print(result2)
