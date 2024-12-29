def mix(secret, mix_data):
    return secret ^ mix_data


def prune(secret):
    return secret % 16777216


def calculate_next(secret):
    secret = prune(mix(secret, secret * 64))
    secret = prune(mix(secret, secret // 32))
    secret = prune(mix(secret, secret * 2048))
    return secret
