import ray

runtime_env = {"pip": ["emoji"]}


@ray.remote(runtime_env=runtime_env)
def f():
    import emoji

    return emoji.emojize("Python is :thumbs_up:")


print(ray.get(f.remote()))
