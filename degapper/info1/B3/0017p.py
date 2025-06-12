def myroundup(rndup_value):
    if int(rndup_value) == rndup_value:
        return rndup_value
    else:
        return int(rndup_value + 1)