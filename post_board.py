import db

def add_post(title, content, user_id):
    sql = """INSERT INTO posts (title, content, user_id)
            VALUES (?, ?, ?)"""
    db.execute(sql, [title, content, user_id])

def get_posts():
    sql = """SELECT * FROM posts
            ORDER BY created_at DESC"""
    return db.query(sql)

def get_post(post_id):
    sql = """SELECT * FROM posts
            WHERE id = ?"""
    result = db.query(sql, [post_id])
    return result[0]

def delete_post(post_id):
    sql = """DELETE FROM posts
            WHERE id = ?"""
    db.execute(sql, [post_id])

def update_post(post_id, title, content):
    sql = """UPDATE posts
            SET title = ?, content = ?
            WHERE id = ?"""
    db.execute(sql, [title, content, post_id])

