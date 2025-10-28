def ends_with(site: str) -> bool:
    if site.endswith('com'):
        return True
    return False


print(
    ends_with('ya.com'),
    ends_with('ya.ru'),
    sep='\n',
)
