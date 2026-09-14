import db

def add_post(title, content, user_id):
    sql = """INSERT INTO posts (title, content, user_id)
            VALUES (?, ?, ?)"""
    db.execute(sql, (title, content, user_id))

def get_posts():
    sql = """SELECT * FROM posts
            ORDER BY created_at DESC"""
    return db.query(sql)