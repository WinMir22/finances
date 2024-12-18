import aiosqlite


async def add_user(user_id, full_name, username, money):
    connect = await aiosqlite.connect('db.db')
    cursor = await connect.cursor()
    check_user = await cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    check_user = await check_user.fetchone()
    if check_user is None:
        await cursor.execute('INSERT INTO users (user_id, full_name, username, money) VALUES (?, ?, ?, ?)',
                             (user_id, full_name, username, money))
        await connect.commit()
    await cursor.close()
    await connect.close()


async def get_user_count():
    connect = await aiosqlite.connect("db.db")
    cursor = await connect.cursor()
    user_count = await cursor.execute("SELECT COUNT(*) FROM users")
    user_count = await user_count.fetchone()
    await cursor.close()
    await connect.close()
    return user_count[0]


async def get_users_money(user_id):
    connect = await aiosqlite.connect("db.db")
    cursor = await connect.cursor()
    user_money = await cursor.execute("SELECT money FROM users WHERE user_id = ?", (user_id))
    user_money = await user_money.fetchone()
    await cursor.close()
    await connect.close()
    return int(user_money[0])