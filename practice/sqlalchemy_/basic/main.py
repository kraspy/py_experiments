from database import (
    fill_database,
    get_all_users,
    get_posts,
    get_user_with_posts,
    get_users_joinedload,
    get_users_lazy,
    get_users_selectinload,
    session,
)


def main():
    with session() as s:
        fill_database(s, 5, 15)
        result = get_all_users(s)

        print(result)

        if user := get_user_with_posts(s, 1):
            print(user)
            print(user.posts)
        else:
            print('User not found')

        print(get_posts(s))

        print('=== Lazy loading ===')
        users = get_users_lazy(s)
        for user in users:
            print(user)
            for post in user.posts:
                print(post)
        print('\n')

        print('=== joinedload ===')
        users = get_users_joinedload(s)
        for user in users:
            print(user)
            for post in user.posts:
                print(post)
        print('\n')

        print('=== selectinload ===')
        users = get_users_selectinload(s)
        for user in users:
            print(user)
            for post in user.posts:
                print(post)


if __name__ == '__main__':
    main()
